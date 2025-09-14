#!/bin/bash
# 遍历当前目录下所有的 zip 文件并解压
for file in *.zip; do
    if [ -f "$file" ]; then
        echo "正在解压: $file"
        unzip -o "$file" -d "${file%.zip}"
    fi
done
