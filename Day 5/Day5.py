#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 * ========================================================================
 *
 *       Filename: Day 6
 *
 *    Description: Move packets
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
import Stack


def main():
    with open('input5.txt', 'r') as f:
        lines = f.readlines()

        start = lines[0:8]
        moves = lines[10:]

        stacks = []
        stacks2 = []
        for i in range(9):
            stacks.append(Stack.Stack())
            stacks2.append([])

        for line in reversed(start):
            clean = line.replace('\n', '').replace('[', '').replace(']', '')\
                .replace('  ', ' ')
            # print(clean)
            for i in range(9):
                if clean[i*2] != ' ':
                    stacks[i].push(clean[i*2])
                    stacks2[i].append(clean[i*2])

        # for i in range(9):
        #     print(f'____ Pila {i} ____')
        #     print(stacks2[i])

        for m in moves:
            # print(m)
            parse = m.split(' ')
            quantity = int(parse[1])
            origin = int(parse[3])-1
            destiny = int(parse[5])-1
            # print(f"Quantity {quantity}, Origin {origin}, Destiny {destiny}")

            # Part 1
            for i in range(quantity):
                stacks[destiny].push(stacks[origin].pop())

            # Part 2
            block = stacks2[origin][-quantity:]
            del stacks2[origin][-quantity:]
            stacks2[destiny].extend(block)

        # Print topmost elements of each stack
        result = ''
        for i in range(9):
            result += stacks[i].pop()
        print(f"Part 1 solution: {result}")

        # Part 2
        result2 = ''
        for i in range(9):
            result2 += str(stacks2[i][-1])
        print(f"Part 2 solution: {result2}")


if __name__ == "__main__":
    main()
