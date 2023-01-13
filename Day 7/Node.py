#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 * ========================================================================
 *
 *       Filename: Node.py
 *
 *    Description: Node of the tree for a tree of files
 *
 *        Version:  1.0
 *        Created:  01/13/20 
 *       Revision:  none
 *
 *         Author:  Antonio Molina Jiménez (AMJ), amj.com@gmail.com
 *        Company:
 *
 * ========================================================================
"""


class Node():
    iNode = 0  # Unique id for all nodes in the tree
    name = ''
    size = 0  # Directories have size=0, files size > 0
    parentId = 0  # Id of parent node. 0 for root node

    def __init__(self, iNode, name, size, parent):
        """ Create node """
        self.iNode = iNode
        self.name = name
        self.size = size
        self.parentId = parent


def main():
    n = Node(1, 'Test', 100, 0)
    print(f"Node {n.iNode}- {n.name} (size: {n.size}), parent: {n.parentId}")


if __name__ == "__main__":
    main()
