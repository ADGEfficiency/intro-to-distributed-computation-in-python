import asyncio
from pathlib import Path
import datetime

from prefect_dask import DaskTaskRunner
import httpx
import pandas as pd
import prefect

from common import urls
   
   
@prefect.task(retries=3, retry_delay_seconds=2)
async def download(url):
    logger = prefect.get_run_logger()
    logger.info(f" downloading {url}")
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    assert response.status_code == httpx.codes.ok, url
    fname = url.split('/')[-1]
    Path(f'./data/{fname}').write_bytes(response.content)
    
    
@prefect.task()
async def process(url):
    fname = url.split('/')[-1]
    data = pd.read_csv(f'./data/{fname}', skiprows=1)
    data = data.groupby('SETTLEMENTDATE').agg('mean', 'std')

    
@prefect.flow(task_runner=DaskTaskRunner())
async def main(urls):
    for url in urls:
        logger = prefect.get_run_logger()
        logger.info(f" downloading {url}")
        download_task = await download.submit(url)
        logger.info(f" processing {url}")
        process.submit(url, wait_for=[download_task])
        

if __name__ == '__main__':
    asyncio.run(main(urls))