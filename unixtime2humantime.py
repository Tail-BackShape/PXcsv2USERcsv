import pandas as pd
import datetime
import shutil
import os
import glob
from tqdm import tqdm


# csvを開くときの各種オプション
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.options.display.float_format = "{:.15f}".format


# conv_csvディレクトリがなければ直下に作成する
conv_dir = "./conv_csv"
if not os.path.exists(conv_dir):
    os.makedirs(conv_dir)


# conv_csvディレクトリがなければ直下に作成する
raw_dir = "./raw_csv"
if not os.path.exists(raw_dir):
    os.makedirs(raw_dir)

# /raw_csv/にある.csvのファイルを表示
file_list = glob.glob("./raw_csv/*.csv")
file_list = [x.replace("\\", "/") for x in file_list]
print("\n".join(file_list))

# 変換元csv
read_filepath = str(input("select csv file>"))


# 変換後に書き込むCSVの用意
write_filepath = "./conv_csv/conv_" + os.path.basename(read_filepath)
shutil.copyfile(read_filepath, write_filepath)

# dataflameでcsvを読み込み
df = pd.read_csv(write_filepath, header=0)


num = df.shape[0]  # timestampの数
print("\nnumber of data>", num)


# timestampの数だけ繰り返す
for i in tqdm(range(num)):

    # 行i,列timestampをvalに代入
    val = df.at[i, "timestamp"]

    # unixtimeをJSTに変換
    time2jst = datetime.datetime.fromtimestamp(val)

    # unixtimeをJSTに置換
    df.replace({"timestamp": {val: time2jst}}, inplace=True)

    i += 1


# 変換・置換後のデータを保存
df.to_csv(write_filepath)


print("Just Finished!")

print("\nInput file:\t", read_filepath)
print("Output file:\t", write_filepath)
