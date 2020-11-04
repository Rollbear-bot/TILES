# -*- coding: utf-8 -*-
# @Time: 2020/11/4 15:43
# @Author: Rollbear
# @Filename: sort_edgelist.py

import os
from tqdm import tqdm


def sort_edgelist_by_timestamp(edgelist_path, dump_path, segregating="\t"):
    with open(edgelist_path, "r") as rf:
        lines = rf.readlines()
        lines.sort(key=lambda line: float(str(line).rstrip().split(segregating)[2]))
        with open(dump_path, "w") as wf:
            wf.writelines(lines)


def case_online():
    avail_types = ["phdthesis",
                   "article",
                   "inproceedings",
                   "book",
                   "incollection",
                   "www"]
    for dataset in tqdm(avail_types):
        working_dir = f"../dblp/datasets/frame_with_timestamp/{dataset}/"
        edgelist_path = sorted([path for path in os.listdir(working_dir) if path.endswith(".edgelist")])[-1]
        data_path = working_dir + edgelist_path
        sort_edgelist_by_timestamp(data_path, working_dir + f"{dataset}_sorted.edgelist")


def local_test():
    # test
    path = "data/dblp_timestamp/article/2021.edgelist"
    dump = "../data/dblp_timestamp/article/2021_sorted.edgelist"
    sort_edgelist_by_timestamp(path, dump)


if __name__ == '__main__':
    case_online()
