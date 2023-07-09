import pandas as pd
import dask.dataframe as dd
import datetime
import shutil
import os
import glob


def unixtime2humantime(read_filepath):

    pd.set_option("display.max_rows", None)
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", None)
    pd.options.display.float_format = "{:.15f}".format

    conv_dir = "./conv_csv"
    if not os.path.exists(conv_dir):
        os.makedirs(conv_dir)

    raw_dir = "./raw_csv"
    if not os.path.exists(raw_dir):
        os.makedirs(raw_dir)

    write_filepath = "./conv_csv/conv_" + os.path.basename(read_filepath)
    shutil.copyfile(read_filepath, write_filepath)

    ddf = dd.read_csv(write_filepath)

    ddf["timestamp"] = ddf["timestamp"].apply(
        lambda ts: datetime.datetime.fromtimestamp(ts),
        meta=("timestamp", "datetime64[ns]"),
    )
    ddf = ddf.compute()

    ddf.to_csv(write_filepath, index=False)

    print("\nInput file:\t", read_filepath)
    print("Output file:\t", write_filepath)


if __name__ == "__main__":
    print("unixtime2humantime.py\n")

    file_list = glob.glob("./raw_csv/*.csv")
    file_list = [x.replace("\\", "/") for x in file_list]
    print("\n".join(file_list))
    read_filepath = str(input("select csv file>"))

    unixtime2humantime(read_filepath)

    input("Enter any key...>")
