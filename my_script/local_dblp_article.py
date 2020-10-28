# -*- coding: utf-8 -*-
# @Time: 2020/10/27 0:04
# @Author: Rollbear
# @Filename: local_dblp_article.py

import tiles as t
from tqdm import tqdm  # 进度条支持


def main():
    working_dir = "../data/dblp_timestamp/article/"
    data_path = working_dir + "2021.edgelist"
    output_path = working_dir + "tiles_output/"

    tl = t.TILES(data_path,
                 path=output_path,
                 obs=7)

    tl.execute()  # 执行算法


if __name__ == '__main__':
    main()
