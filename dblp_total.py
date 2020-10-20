# -*- coding: utf-8 -*-
# @Time: 2020/10/20 9:11
# @Author: Rollbear
# @Filename: dblp_total.py


import tiles as t
import os
from tqdm import tqdm  # 进度条支持


def run_tiles_on_a_dataset(dataset):
    working_dir = f"../dblp/datasets/frame_with_timestamp/{dataset}/"
    edgelist_path = sorted([path for path in os.listdir(working_dir) if path.endswith(".edgelist")])[-1]
    data_path = working_dir + edgelist_path
    output_path = working_dir + "tiles_output/"

    tl = t.TILES(data_path,
                 path=output_path,
                 obs=365)

    tl.execute()  # 执行算法


if __name__ == '__main__':
    avail_types = ["phdthesis",
                   "article",
                   "inproceedings",
                   "book",
                   "incollection",
                   "www"]
    for t in tqdm(avail_types):
        run_tiles_on_a_dataset(t)
