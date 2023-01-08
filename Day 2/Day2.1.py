#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 * ========================================================================
 *
 *       Filename: Day2.1.py
 *
 *    Description: Paper, Scissors, Rock
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
        'A X': 1 + 3,
        'A Y': 2 + 6,
        'A Z': 3 + 0,

        'B X': 1 + 0,
        'B Y': 2 + 3,
        'B Z': 3 + 6,

        'C X': 1 + 6,
        'C Y': 2 + 0,
        'C Z': 3 + 3

    }

    with open('input2.txt') as f:
        total = 0

        for line in f:
            total = total + points[line[:-1]]

        print(f"Total points: {total}")


if __name__ == "__main__":
    main()
