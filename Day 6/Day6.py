#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 * ========================================================================
 *
 *       Filename: Day 6
 *
 *    Description: Signal detection
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


def find(line, distinct):
    for i in range(len(line)-distinct):
        string = str(line[i:i+distinct])
        # print(string)

        found = False

        for j in range(distinct-1):
            for k in range(j+1, distinct):
                if string[j] == string[k]:
                    found = True
                    break
        if not(found):
            return(i+distinct)


def main():
    with open('input6.txt', 'r') as f:
        lines = f.readlines()

        for line in lines:
            r1 = find(line, 4)
            print(f"Part 1 {r1}")

            r2 = find(line, 14)
            print(f"Part 2 {r2}")


if __name__ == "__main__":
    main()
