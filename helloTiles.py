# -*- coding: utf-8 -*-
# @Time: 2020/9/3 22:03
# @Author: Rollbear
# @Filename: helloTiles.py

import tiles as t
from tqdm import tqdm  # 进度条支持


def main():
    data_folder = "./data/cit-DBLP/"
    output_path = "./output"
    num_of_slices = 15

    for i in tqdm(range(15)):
        # 合成文件路径
        data_path = data_folder + f"converted_{i}.edgelist"

    # todo::算法需要edgelist中包含时间戳
    # 初始化TILES算法
    tl = t.TILES(data_path,
                 path=output_path)
    tl.execute()  # 执行算法


if __name__ == '__main__':
    main()
