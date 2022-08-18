from coiled import Cluster
import dask
from dask.distributed import Client


if __name__ == '__main__':
# create a remote Dask cluster with Coiled
    cluster = Cluster(software="coiled/default-py39")

# interact with Coiled using the Dask distributed client
    client = Client(cluster)

# link to Dask Dashboard
    print("Dask Dashboard:", client.dashboard_link)

# generate random timeseries of data
    df = dask.datasets.timeseries("2000", "2005", partition_freq="2w").persist()

# perform a groupby with an aggregation
    output = df.groupby("name").aggregate({"x": "sum", "y": "max"}).compute()
    print(output)

# Close the cluster
    cluster.close()

# Close the client
    client.close()
