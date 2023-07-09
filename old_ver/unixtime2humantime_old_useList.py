import pandas as pd
import datetime
import shutil
import os
import glob
from tqdm import tqdm

print("tolist.py\n")

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

# timestamp列の値をリストに格納
df_list = list(df["timestamp"])
df_check = list(df["timestamp"])


# print(df_check)

number = len(df_list)

# リストの値を変換
for j in tqdm(range(number)):
    df_list[j] = datetime.datetime.fromtimestamp(df_list[j])


for i in tqdm(range(number)):
    df.replace(df_check[i], df_list[i], inplace=True)

df.to_csv(write_filepath)

print("Just Finished!")
print("\nInput file:\t", read_filepath)
print("Output file:\t", write_filepath)

input()
