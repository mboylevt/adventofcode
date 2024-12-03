import requests
import sys

day = sys.argv[1]
cookies = {'session': '53616c7465645f5f24babda2c3a36bb4353cfb9764611b96faf8028d35ab6e5a5a2b988b63a173de087642f8aecca63bb3b3136dbdbdcbd2d4cbf6b2abaca5d7'}
r = requests.get('https://adventofcode.com/2024/day/{}/input'.format(day), cookies=cookies)
with open('2024/input/{}.txt'.format(day), '+w') as out:
    out.write(r.text)
