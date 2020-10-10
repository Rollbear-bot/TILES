# -*- coding: utf-8 -*-
# @Time: 2020/9/5 10:32
# @Author: Rollbear
# @Filename: merge_edgelist.py

from tqdm import tqdm


def main():
    data_folder = "../data/converted_synthetic1/"
    output_path = "../data/converted_synthetic1/merged.edgelist"
    num_of_slice = 15

    with open(output_path, "w") as wf:
        for i in tqdm(range(num_of_slice)):
            with open(data_folder + f"converted_{i}.edgelist", "r") as rf:
                wf.writelines(rf.readlines())


if __name__ == '__main__':
    main()
