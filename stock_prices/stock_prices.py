#!/usr/bin/python

import argparse

def find_max_profit(prices):
  maximum = -1000000
  for val in range(len(prices)-1):
    rightOf = prices[val+1:]
    maximumForThis = max(rightOf) - prices[val]
    if maximumForThis > maximum:
      maximum = maximumForThis
  print(maximum)
  return maximum



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))