# -*- coding: utf-8 -*-
# @Time: 2020/10/16 11:01
# @Author: Rollbear
# @Filename: test_tiles_on_dblp.py

import unittest
import tiles as t


class TestOnDBLP(unittest.TestCase):
    def test_dblp_phdthesis(self):
        data_path = "../../data/dblp_timestamp/phdthesis/2017.edgelist"
        output_path = "../../data/dblp_timestamp/phdthesis/"

        tl = t.TILES(data_path,
                     path=output_path)
        tl.execute()  # 执行算法


if __name__ == '__main__':
    unittest.main()
