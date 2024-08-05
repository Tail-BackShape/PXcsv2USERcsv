# PXcsv2USERcsv

## 概要
pixhawkのログのtimestampを日本時間にサクッと置換するやつ。  
csvヘッダーの"timestamp"列を変換するので別にpixhawkじゃなくてもいける（はず）  

## HOW TO USE

```bash
# リポジトリをクローン
git clone https://github.com/Tail-BackShape/PXcsv2USERcsv.git

# ディレクトリに移動
cd PXcsv2USERcsv

# 実行
python unixtime2humantime input.csv #任意のcsv
