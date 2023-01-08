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
    points = {
        'A X': 0 + 3,
        'A Y': 3 + 1,
        'A Z': 6 + 2,

        'B X': 0 + 1,
        'B Y': 3 + 2,
        'B Z': 6 + 3,

        'C X': 0 + 2,
        'C Y': 3 + 3,
        'C Z': 6 + 1

    }

    with open('input2.txt') as f:
        total = 0

        for line in f:
            total = total + points[line[:-1]]

        print(f"Total points: {total}")


if __name__ == "__main__":
    main()
