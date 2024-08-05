import pandas as pd
import dask.dataframe as dd
import datetime
import shutil
import os
import sys


def unixtime2humantime(read_filepath):
    # Pandasの表示オプションを設定
    pd.set_option("display.max_rows", None)
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", None)
    pd.options.display.float_format = "{:.15f}".format

    # 書き込み用のファイルパスを設定
    write_filepath = "conv_" + os.path.basename(read_filepath)
    shutil.copyfile(read_filepath, write_filepath)

    # Dask DataFrameを読み込む
    ddf = dd.read_csv(write_filepath)

    # timestamp列をフォーマット変換
    ddf["timestamp"] = ddf["timestamp"].apply(
        lambda ts: datetime.datetime.fromtimestamp(ts).strftime('%Y/%m/%d %H:%M:%S.%f')[:-3],
        meta=("timestamp", "object"),
    )
    ddf = ddf.compute()

    # 結果をCSVファイルに保存
    ddf.to_csv(write_filepath, index=False)

    # 結果を表示
    print("\nInput file:\t", read_filepath)
    print("Output file:\t", write_filepath)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python unixtime2humantime.py <input_csv_file>")
    else:
        read_filepath = sys.argv[1]
        print("unixtime2humantime.py\n")
        unixtime2humantime(read_filepath)
