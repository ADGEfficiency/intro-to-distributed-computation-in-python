from pathlib import Path
import datetime

import requests
from prefect_dask import DaskTaskRunner
import pandas as pd
import prefect

from common import urls
   
   
@prefect.task(retries=3, retry_delay_seconds=2)
def download(url):
    logger = prefect.get_run_logger()
    logger.info(f" downloading {url}")
    response = requests.get(url)
    assert response.ok
    fname = url.split('/')[-1]
    Path(f'./data/{fname}').write_bytes(response.content)
    
    
@prefect.task()
def process(url):
    fname = url.split('/')[-1]
    data = pd.read_csv(f'./data/{fname}', skiprows=1)
    data = data.groupby('SETTLEMENTDATE').agg('mean', 'std')

    
@prefect.flow(task_runner=DaskTaskRunner())
def main(urls):
    for url in urls:
        logger = prefect.get_run_logger()
        logger.info(f" downloading {url}")
        download_task = download.submit(url)
        logger.info(f" processing {url}")
        process.submit(url, wait_for=[download_task])
        

if __name__ == '__main__':
    main(urls)
