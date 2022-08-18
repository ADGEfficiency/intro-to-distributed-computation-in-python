from pathlib import Path

import numpy as np
import pandas as pd
import requests

from common import urls


def download(url):
    response = requests.get(url)
    assert response.ok
    fname = url.split('/')[-1]
    Path(f'./data/{fname}').write_bytes(response.content)
    
    
def process(url):
    fname = url.split('/')[-1]
    data = pd.read_csv(f'./data/{fname}', skiprows=1)
    data = data.groupby('SETTLEMENTDATE').agg('mean', 'std')
   

def main(urls):
    for url in urls:
        download(url)
        process(url)


if __name__ == '__main__':
    main(urls)
