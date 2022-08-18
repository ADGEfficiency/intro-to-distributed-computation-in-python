from pathlib import Path
import io
import zipfile

import coiled
import pandas as pd
import prefect
from prefect_dask.task_runners import DaskTaskRunner
import requests

from common import urls

from io import StringIO, BytesIO
from pathlib import Path
from typing import Dict, Union
from zipfile import ZipFile
import datetime
import json

from rich import print
import boto3
import botocore
import numpy as np
import pandas as pd
from rich import print


class S3File:
    """parent class for S3 files"""

    def __init__(self, bucket, key, profile_name=None, region="ap-southeast-2"):
        self.bucket = bucket
        self.key = key
        self.session = boto3.Session(region_name=region, profile_name=profile_name)
        self.client = self.session.client("s3")
        self.resource = self.session.resource("s3")


class S3Zip(S3File):
    def __init__(self, bucket, key, profile_name=None, region="ap-southeast-2"):
        super().__init__(bucket, key, profile_name=profile_name, region=region)

    def read(self):
        print(f" reading Zip from s3: {self.bucket, self.key}")
        s3 = self.client
        obj = s3.get_object(Bucket=self.bucket, Key=self.key)
        zip_data = obj["Body"].read()
        print(f" reading Zip from s3: {self.bucket, self.key}")
        return zip_data

    def write(self, data, **kwargs):
        s3 = self.resource
        obj = s3.Object(self.bucket, self.key)
        obj.put(Body=data)
        print(f" writing Zip to s3: {self.bucket, self.key}")


software_env = "kiwipycon-tutorial"
#  setup a docker image with these pip requirements
coiled.create_software_environment(
    name=software_env,
    pip="requirements.txt",
)

# instance = ["t3.medium", "t3.xlarge" ]
instance = ["t3.xlarge", ]
runner = DaskTaskRunner(
    # tell the DaskExecutor to run on Coiled
    cluster_class="coiled.Cluster",
    # Coiled-specific keyword arguments
    cluster_kwargs={
        "scheduler_vm_types": instance,
        "worker_vm_types": instance,
        "n_workers": 8,
        "software": software_env,
        "shutdown_on_close": True,
        "name": "prefect-executor",
    },
)


@prefect.task(retries=3)
def download(url, chunk_size=128):
    logger = prefect.get_run_logger()
    logger.info(f" downloading {url}")
    response = requests.get(url)
    assert response.ok
    fi = S3Zip("kiwipycon-tutorial-2022", url.split('/')[-1]).write(response.content)
    return response


@prefect.task()
def process(url):
    logger = prefect.get_run_logger()
    logger.info(f" processing {url}")
    zip_fi = zipfile.ZipFile(
        io.BytesIO(S3Zip("kiwipycon-tutorial-2022", url.split('/')[-1]).read())
    )
    fname = zip_fi.namelist()[0]
    data = pd.read_csv(zip_fi.open(fname), skiprows=1)
    data = data.groupby("SETTLEMENTDATE").agg("mean", "std")


@prefect.flow(task_runner=runner)
def main(urls):
    for url in urls:
        response = download.submit(url)
        process.submit(url, wait_for=[response])


if __name__ == "__main__":
    main(urls)
