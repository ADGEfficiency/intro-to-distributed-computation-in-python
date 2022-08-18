from pathlib import Path


Path('./data').mkdir(exist_ok=True)
months = [str(month).zfill(2) for month in range(1, 5)]
urls = [
    f"http://www.nemweb.com.au/Data_Archive/Wholesale_Electricity/MMSDM/2021/MMSDM_2021_{month}/MMSDM_Historical_Data_SQLLoader/DATA/PUBLIC_DVD_DISPATCH_UNIT_SCADA_2021{month}010000.zip"
    for month in months
]
