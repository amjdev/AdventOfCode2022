#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 * ========================================================================
 *
 *       Filename:
 *
 *    Description:
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


def main():
    with open('input4.txt', 'r') as f:
        lines = f.readlines()
        overlaps = 0
        partial = 0

        for i in lines:
            pair = i.split(',')
            r1 = pair[0]
            r2 = pair[1]

            r1_ini = int(r1.split('-')[0])
            r1_end = int(r1.split('-')[1])

            r2_ini = int(r2.split('-')[0])
            r2_end = int(r2.split('-')[1])

            if (r1_ini <= r2_ini) and (r1_end >= r2_end):
                # Overlap r1_ini....r2_ini...r2_end...r1_end
                overlaps = overlaps + 1
            elif (r1_ini >= r2_ini) and (r1_end <= r2_end):
                # Overlap r2_ini....r1_ini...r1_end...r2_end
                overlaps = overlaps + 1
            elif (r1_ini <= r2_ini) and (r1_end >= r2_ini):
                # Overlap r1_ini....r2_ini...r1_end...r2_end
                partial = partial + 1
            elif (r2_ini <= r1_ini) and (r2_end >= r1_ini):
                # Overlap r2_ini....r1_ini...r2_end...r1_end
                partial = partial + 1

        total = overlaps + partial

        print(f"Part 1: There are {overlaps} full overlaps")
        print(f"Part 2: There are {total} total overlaps")


if __name__ == "__main__":
    main()
