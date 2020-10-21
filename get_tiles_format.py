# -*- coding: utf-8 -*-
# @Time: 2020/10/21 19:15
# @Author: Rollbear
# @Filename: get_tiles_format.py

import os
from tqdm import tqdm


def get_tiles_format(edgelist_path, dump_path, segregation_char, add_create_action=True):
    with open(edgelist_path, "r") as rf:
        data = [row.rstrip().split(segregation_char) for row in rf.readlines()]
        if add_create_action:
            output_str = ["+" + segregation_char + segregation_char.join(row) + "\n" for row in data]
        # write data
        with open(dump_path, "w") as wf:
            wf.writelines(output_str)


if __name__ == '__main__':
    avail_types = ["phdthesis",
                   "article",
                   "inproceedings",
                   "book",
                   "incollection",
                   "www"]

    for dataset in tqdm(avail_types):
        working_dir = f"../dblp/datasets/frame_with_timestamp/{dataset}/"
        edgelist = sorted([path for path in os.listdir(working_dir) if path.endswith(".edgelist")])[-1]
        data_path = working_dir + edgelist

        get_tiles_format(edgelist_path=data_path,
                         dump_path=working_dir + dataset + "_tiles_format.edgelist",
                         segregation_char="\t")
