# -*- coding: utf-8 -*-
# @Time: 2020/10/20 11:38
# @Author: Rollbear
# @Filename: dblp_total_sys_input.py

import tiles as t
import os
import sys


def run_tiles_on_a_dataset(dataset, edgelist=None, alg="TILES"):
    working_dir = f"../dblp/datasets/frame_with_timestamp/{dataset}/"
    if edgelist is None:
        edgelist_path = sorted([path for path in os.listdir(working_dir) if path.endswith(".edgelist")])[-1]
    else:
        edgelist_path = edgelist
    data_path = working_dir + edgelist_path
    output_path = working_dir + "tiles_output/"

    if alg == "TILES":
        tl = t.TILES(data_path,
                     path=output_path,
                     obs=365)
    elif alg == "eTILES":
        tl = t.eTILES(data_path,
                      path=output_path,
                      obs=365)
    else:
        tl = t.eTILES(data_path,
                      path=output_path,
                      obs=365)

    print(f"run on {data_path}\noutput to {output_path}")
    tl.execute()  # 执行算法


if __name__ == '__main__':
    avail_type = sys.argv[1]
    if len(sys.argv) > 2:
        run_tiles_on_a_dataset(avail_type, edgelist=sys.argv[2], alg="eTILES")
    else:
        run_tiles_on_a_dataset(avail_type)
