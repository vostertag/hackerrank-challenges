#!/bin/python3

import sys

def maxiumumToys(prices, k):
    prices = sorted(prices)
    total = 0
    for i in range(len(prices)):
        if(total + prices[i] > k):
            return i
        else:
            total += prices[i]
    return len(prices)

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    prices = list(map(int, input().strip().split(' ')))
    result = maxiumumToys(prices, k)
    print(result)
