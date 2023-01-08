#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 * ========================================================================
 *
 *       Filename: Stack
 *
 *    Description:  Implementación de una pila usando una lista
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


class Stack:
    def __init__(self):
        self.stackList = []
        self.stackSize = 0

    def push(self, item):
        self.stackList.append(item)
        self.stackSize += 1

    def pop(self):
        if self.stackSize == 0:
            raise Exception("Stack is empty")
        temp = self.stackList.pop()
        self.stackSize -= 1
        return temp

    def size(self):
        return self.stackSize

    def isEmpty(self):
        return(self.stackSize == 0)


def main():
    print("Prueba de pila")
    pila = Stack()

    print("Metiendo en la pila: 3, 8, 12")
    pila.push(3)
    pila.push(8)
    pila.push(12)

    print("Vaciando pila")
    for i in range(pila.size()):
        num = pila.pop()
        print(f"Saco {num}")


if __name__ == "__main__":
    main()
