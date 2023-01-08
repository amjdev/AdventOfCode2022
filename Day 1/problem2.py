#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 * ========================================================================
 *
 *       Filename: problem2.py
 *
 *    Description: Calories, part 2
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
        elves = []

        for line in f:
            if (line == '\n'):
                if calories > max:
                    max = calories
                elves.append(calories)
                calories = 0
            else:
                calories = calories + int(line[:-1])

        elves.sort(reverse=True)
        total = elves[0] + elves[1] + elves[2]
        print(elves)

        print(f"Top 3 calories = {elves[0]} + {elves[1]} + {elves[2]} "
              f"= {total}")


if __name__ == "__main__":
    main()
