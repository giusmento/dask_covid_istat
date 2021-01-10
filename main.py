import dask.dataframe as dd
import logging
from dask.distributed import Client, LocalCluster
from computation import computation
from dask_yarn import YarnCluster

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def local_run():
    cluster = LocalCluster(host="cluster-dask-m", environment="venv.tat.gz")
    client = Client(cluster)  # Connect to distributed cluster and override default

    filename = '*.part'
    encoding = "cp1252"
    input_folder = "./data/31Ottobre/"
    output_folder = "./output/"

    computation(filename, encoding, input_folder, output_folder)

def data_proc_run():
    cluster = YarnCluster(host="cluster-dask-m", environment="venv.tat.gz")
    client = Client(cluster)  # Connect to distributed cluster and override default

    filename = '*.part'
    encoding = "cp1252"
    input_folder = "/home/giuseppemento/dask_covid_istat/data/31Ottobre/"
    output_folder = "./output/"

    computation(filename, encoding, input_folder, output_folder)

if __name__ == "__main__":
    # local_run()
    data_proc_run()