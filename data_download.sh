#!/bin/bash

cd  event_data

mkdir -p Video/TimeRFT
mkdir -p Video/VideoEspresso

tree Video

echo -n "请输入您的HuggingFace token: "
read -s hf_token
echo

if [ -z "$hf_token" ]; then
    echo "错误：未输入token！"
    exit 1
fi

echo "开始下载TimeRFT数据集..."
huggingface-cli download \
    --token "$hf_token" \
    --resume-download \
    --local-dir-use-symlinks True \
    --repo-type dataset \
    Boshenxx/TimeR1-Dataset \
    --local-dir Video/TimeRFT

if [ $? -eq 0 ]; then
    echo "TimeRFT数据集下载完成！"
else
    echo "TimeRFT数据集下载失败！"
    exit 1
fi

echo "开始下载VideoEspresso数据集..."
huggingface-cli download \
    --token "$hf_token" \
    --resume-download \
    --local-dir-use-symlinks True \
    --repo-type dataset \
    hshjerry0315/VideoEspresso_train_video \
    --local-dir Video/VideoEspresso

if [ $? -eq 0 ]; then
    echo "VideoEspresso数据集下载完成！"
else
    echo "VideoEspresso数据集下载失败！"
    exit 1
fi

echo "所有操作完成！"