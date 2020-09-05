# -*- coding: utf-8 -*-
# @Time: 2020/9/5 9:25
# @Author: Rollbear
# @Filename: synthetic_data_converter.py

import time
import os
from tqdm import tqdm


def main():
    data_folder = "../data/synthetic3/"
    output_folder = "../data/converted_synthetic3/"
    num_of_slice = 15

    # 处理每个时间片
    for i in tqdm(range(num_of_slice)):
        lines = []
        file_path = data_folder + f"{i}.edgelist"
        with open(file_path, "r") as rf:
            with open(output_folder + f"converted_{i}.edgelist", "w") as wf:
                for line in rf:
                    # 使用tab分割数据，并加上时间戳
                    lines.append("\t".join(line.rstrip().split(" ")) +
                                 f"\t{time.time()}\n")
                # 写入输出文件
                wf.writelines(lines)


if __name__ == '__main__':
    main()
