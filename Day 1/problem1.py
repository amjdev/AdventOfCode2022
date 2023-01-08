#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 * ========================================================================
 *
 *       Filename: problem1.py
 *
 *    Description: Calories, part 1
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
    with open('input.txt') as f:
        max = 0
        calories = 0

        for line in f:
            if (line == '\n'):
                if calories > max:
                    max = calories
                calories = 0
            else:
                calories = calories + int(line[:-1])

        print(f"Max calories = {max}")


if __name__ == "__main__":
    main()
