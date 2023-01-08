#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 * ========================================================================
 *
 *       Filename: Day 3
 *
 *    Description: Priorities
 *
 *        Version:  1.0
 *        Created:  01/04/20 18:28:09
 *       Revision:  none
 *
 *         Author:  Antonio Molina Jiménez (AMJ), amj.com@gmail.com
 *        Company:
 *
 * ========================================================================
"""


def priority(c):
    value = ord(c)
    if value < 97:
        return value - 64 + 26
    else:
        return value - 96


def main():
    with open('input3.txt') as f:
        lines = f.readlines()
        # Quitar los saltos de línea
        clean = [lc[:-1] for lc in lines]
        list1 = [l1[0:int(len(l1)/2)] for l1 in clean]
        list2 = [l2[int(len(l2)/2):] for l2 in clean]
        # listCommon = []
        totalPriority = 0
        totalPriorityG = 0

        for i in range(len(clean)):
            common = ''.join(sorted(set.intersection(set(list1[i]),
                                                     set(list2[i]))))
            if (i % 3) == 0:
                commonGroup = ''.join(sorted(set.intersection(
                    set(clean[i]), set(clean[i+1]), set(clean[i+2]))))
                totalPriorityG = totalPriorityG + priority(commonGroup)

            # listCommon.append(common)
            print(clean[i], list1[i], list2[i], common, priority(common))
            totalPriority = totalPriority + priority(common)

        print(f"Total priority = {totalPriority}")
        print(f"Total priority Group = {totalPriorityG}")


if __name__ == "__main__":
    main()
