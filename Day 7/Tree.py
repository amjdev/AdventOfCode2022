#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 * ========================================================================
 *
 *       Filename: Tree.py
 *
 *    Description: Tree of nodes
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
import Node

class Tree():
    maxId = 0
    nodes = []

    def __init__(self):
        """ Create tree. Root node created by default """
        self.nodes.append(new Node(self.maxId,'/',0,0))
        

    def addNode(self, name, size, parent):
        """ Add new node to tree"""
        self.maxId += 1
        self.nodes.append(new Node(self.maxId, name, size, parent))
        return self.maxId

    def print(self, idRoot):
        """ Print the tree structure """
        level = 0
        for n in nodes:
            s = '|' + '-'*level
            if n.size == 0:
               print(s + n.name)


def main():


if __name__ == "__main__":
    main()
