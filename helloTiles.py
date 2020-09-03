# -*- coding: utf-8 -*-
# @Time: 2020/9/3 22:03
# @Author: Rollbear
# @Filename: helloTiles.py

import tiles as t


def main():
    data_path = "./data/cit-DBLP/0.edgelist"
    output_path = "./output"

    # todo::算法需要edgelist中包含时间戳
    # 初始化TILES算法
    tl = t.TILES(data_path,
                 path=output_path)
    tl.execute()  # 执行算法


if __name__ == '__main__':
    main()
