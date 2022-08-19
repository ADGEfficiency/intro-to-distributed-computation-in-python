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


software_env = "kiwipycon-tutorial"
#  setup a docker image with these pip requirements
coiled.create_software_environment(
    name=software_env,
    pip="requirements-coiled.txt",
)

instance = ["t3.medium", "t3.xlarge" ]
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
    return response


@prefect.task()
def process(url, response):
    logger = prefect.get_run_logger()
    logger.info(f" processing {url}")
    zip_fi = zipfile.ZipFile(
        io.BytesIO(response.content)
    )
    fname = zip_fi.namelist()[0]
    data = pd.read_csv(zip_fi.open(fname), skiprows=1)
    data = data.groupby("SETTLEMENTDATE").agg("mean", "std")


@prefect.flow(task_runner=runner)
def main(urls):
    for url in urls:
        response = download.submit(url)
        process.submit(url, response)


if __name__ == "__main__":
    main(urls)
