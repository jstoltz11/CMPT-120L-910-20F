import argparse
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

parser = argparse.ArgumentParser()

parser.add_argument('-n', type=int, help='This number will be used in a function that sums the integers from 0 to the input.')

args = parser.parse_args()

logging.info('You have entered ' + str(args.n) + '.')

total = sum(range(args.n + 1))

logging.info('Your total is ' + str(total) + '.')