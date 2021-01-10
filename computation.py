import dask.dataframe as dd
import logging

logger = logging.getLogger(__name__)

def computation(filename:str, encoding:str, input_folder:str, output_dolfer:str):
    logger.info("Load CSV file {}{} with encoding {}".format(input_folder, filename, encoding))
    df = dd.read_csv( input_folder + filename, encoding=encoding)

    logger.info("Filter out all unavailable values".format(filename, encoding))
    df = df[df["T_20"] != "n.d."]
    logger.info("cast columns".format(filename, encoding))
    df["T_20"] = df["T_20"].astype(int)
    df["T_19"] = df["T_19"].astype(int)
    df["T_18"] = df["T_18"].astype(int)
    df["T_17"] = df["T_17"].astype(int)

    logger.info("Calculate last 3 yrs mean".format(filename, encoding))
    df["T19_T18_T17_mean"] = (df["T_19"] + df["T_18"] + df["T_17"]) / 3

    logger.info("Calculate delta with 2020".format(filename, encoding))
    df["delta"] = df["T_20"] - df["T19_T18_T17_mean"]

    logger.info("Start processing".format(filename, encoding))

    # prepare dataset for cities
    df_city = df.groupby("NOME_COMUNE").agg({"delta": "sum"}).reset_index().set_index("delta").map_partitions(
        lambda x: x.sort_index(ascending=False))
    df_city.compute()
    logger.info("Process city completed".format(filename, encoding))

    # prepare dataset for region
    df_region = df.groupby("NOME_REGIONE").agg({"delta": "sum"}).reset_index().set_index("delta").map_partitions(
        lambda x: x.sort_index(ascending=False))
    df_region.compute()
    logger.info("Process region completed".format(filename, encoding))

    del df
    logger.info("Save dataframe")
    df_city.to_csv(output_dolfer)
    del df_city
    df_region.to_csv(output_dolfer)
    del df_region
    logger.info("Completed")

    return True
