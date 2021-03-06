# -*- coding: utf-8 -*-
# @Time: 2020/10/20 9:11
# @Author: Rollbear
# @Filename: dblp_total.py


import tiles as t
import os
from tqdm import tqdm  # 进度条支持


def run_tiles_on_a_dataset(dataset, edgelist_name=None, obs=365, ttl=float('inf'), out="tiles_output"):
    working_dir = f"../dblp/datasets/frame_with_timestamp/{dataset}/"
    if edgelist_name is None:
        edgelist_name = sorted([path for path in os.listdir(working_dir) if path.endswith(".edgelist")])[-1]
    data_path = working_dir + edgelist_name
    if not os.path.exists(working_dir + out):
        os.mkdir(working_dir + out)
    output_path = working_dir + out

    tl = t.TILES(data_path,
                 path=output_path,
                 obs=obs,
                 ttl=ttl)

    print(f"run on {data_path}\noutput to {output_path}")
    tl.execute()  # 执行算法


if __name__ == '__main__':
    avail_types = [
        "phdthesis",
        "www",
        "book",
        "incollection",
        "article",
        "inproceedings"
    ]

    for avail_type in tqdm(avail_types):
        run_tiles_on_a_dataset(avail_type,
                               edgelist_name=f"{avail_type}_sorted.edgelist",
                               obs=365,
                               out="tiles_output_test3")
