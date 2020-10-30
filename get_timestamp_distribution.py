# -*- coding: utf-8 -*-
# @Time: 2020/10/30 9:14
# @Author: Rollbear
# @Filename: get_timestamp_distribution.py
# 获取每个数据集的边时间戳分布，确保时间戳的转化正常

import matplotlib.pyplot as plt
import datetime
from tqdm import tqdm
import os


def timestamp2datetime_str(timestamp):
    if timestamp < 0:
        # 对负数时间戳要单独处理
        datetime_array = datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=timestamp)
    else:
        datetime_array = datetime.datetime.utcfromtimestamp(timestamp)
    return datetime_array.strftime("%Y-%m-%d %H:%M:%S")


def timestamp2year(timestamp):
    if timestamp < 0:
        # 对负数时间戳要单独处理
        datetime_array = datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=timestamp)
    else:
        datetime_array = datetime.datetime.utcfromtimestamp(timestamp)
    return datetime_array.strftime("%Y")


def check_timestamp(edgelist_path, fig_dump_path, show=False, print_log=False):
    with open(edgelist_path, "r") as rf:
        lines = rf.readlines()
        timestamp_lt = [float(line.rstrip().split("\t")[-1]) for line in lines]
        datetime_lt = [int(timestamp2year(line)) for line in timestamp_lt]

        datetime_dict = {key: 0 for key in range(min(datetime_lt), max(datetime_lt))}
        for line in datetime_lt:
            datetime_dict[line] = datetime_dict.get(line, 0) + 1

        x_y = [(int(key), datetime_dict[key]) for key in datetime_dict]
        x_y.sort(key=lambda item: item[0])

        plt.barh([item[0] for item in x_y], [item[1] for item in x_y])
        if show:
            plt.show()
        if print_log:
            print("\n" + "="*20)
            print(f"in {edgelist_path}:")
            for item in x_y:
                print(f"year: {item[0]}\t#sample: {item[1]}")

        plt.savefig(fig_dump_path)


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
        fig_dump_path = f"./fig/{dataset}.png"

        check_timestamp(data_path, fig_dump_path, print_log=True)
