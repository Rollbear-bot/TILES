# -*- coding: utf-8 -*-
# @Time: 2020/9/4 8:06
# @Author: Rollbear
# @Filename: data_converter.py
# 将空格分割的数据改为Tab分割的数据，并加上时间戳

import time


def main():
    data_path = "../data/cit-DBLP/0.edgelist"
    output_path = "../data/cit-DBLP/converted_0.edgelist"

    lines = []
    with open(data_path, "r") as rf:
        with open(output_path, "w") as wf:
            for line in rf:
                # 使用tab分割数据，并加上时间戳
                lines.append("\t".join(line.rstrip().split(" ")) +
                             f"\t{time.time()}\n")
            # 写入输出文件
            wf.writelines(lines)


if __name__ == '__main__':
    main()
