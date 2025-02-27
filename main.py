import logging
from dask.distributed import Client, LocalCluster
from computation import computation
from dask_yarn import YarnCluster
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def local_run():
    cluster = LocalCluster()
    client = Client(cluster)  # Connect to distributed cluster and override default

    filename = '*.part'
    encoding = "cp1252"
    input_folder = "./data/31Ottobre/"
    output_folder = "./output/"

    computation(filename, encoding, input_folder, output_folder)

def data_proc_run():
    cluster = YarnCluster()
    logger.info("Client UI available at {}".format(cluster.application_client.ui.address))
    client = Client(cluster)  # Connect to distributed cluster and override default

    filename = '*.part'
    encoding = "cp1252"
    # input_folder = "home/giuseppemento/dask_covid_istat/data/31Ottobre/"
    input_folder = os.environ.get('INPUT_FOLDER')
    # output_folder = "./output/"
    output_folder = os.environ.get('OUTPUT_FOLDER')

    computation(filename, encoding, input_folder, output_folder)

if __name__ == "__main__":
    # local_run()
    data_proc_run()