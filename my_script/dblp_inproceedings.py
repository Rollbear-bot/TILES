# -*- coding: utf-8 -*-
# @Time: 2020/10/20 8:22
# @Author: Rollbear
# @Filename: dblp_inproceedings.py

import tiles as t
from tqdm import tqdm  # 进度条支持


def main():
    working_dir = "../dblp/datasets/frame_with_timestamp/inproceedings/"
    data_path = working_dir + "2021.edgelist"
    output_path = working_dir + "tiles_output_test2/"

    tl = t.TILES(data_path,
                 path=output_path,
                 obs=365,
                 ttl=730)

    tl.execute()  # 执行算法


if __name__ == '__main__':
    main()