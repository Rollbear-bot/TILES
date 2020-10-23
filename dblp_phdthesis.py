# -*- coding: utf-8 -*-
# @Time: 2020/9/28 10:42
# @Author: Rollbear
# @Filename: dblp_phdthesis.py

import tiles as t
from tqdm import tqdm  # 进度条支持


def main():
    working_dir = "../dblp/datasets/frame_with_timestamp/phdthesis/"
    data_path = working_dir + "2017.edgelist"
    output_path = working_dir + "tiles_output/"

    tl = t.TILES(data_path,
                 path=output_path,
                 obs=7)

    tl.execute()  # 执行算法


if __name__ == '__main__':
    main()
