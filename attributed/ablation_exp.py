# -*- coding: utf-8 -*-
# @Time: 2020/12/13 15:43
# @Author: Rollbear
# @Filename: ablation_exp.py

from tiles.alg.TILES import TILES
from tiles.alg.attributed_TILES import AttributedTILES, NodeAttrHandler


def main():
    # basic_model = TILES()

    handler = NodeAttrHandler(node_attr_filename="../data/AIDS/AIDS.node_attrs",
                              alpha=1,
                              beta=0.1)
    attr_model = AttributedTILES(obs=5000,
                                 ttl=10000,
                                 filename="../data/AIDS/AIDS.edges",
                                 path="../output/AIDS_tiles_output",
                                 segregate_char=",",
                                 auto_timestamp=True,
                                 node_attr_handler=handler)

    attr_model.execute()


if __name__ == '__main__':
    main()
