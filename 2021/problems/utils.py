from timeit import default_timer as timer
import os
# from zUtils.utils import *
from typing import List, Tuple

from colorama import init
from colorama import Fore, Back, Style
init()
os.system('cls' if os.name == 'nt' else 'clear')

outputDebug = True


def printGood(text):
    doPrint(Fore.GREEN + str(text) + Fore.RESET)


def printOK(text):
    doPrint(Fore.RESET + Style.RESET_ALL + str(text) + Fore.RESET + Style.RESET_ALL)


def printBad(text):
    doPrint(Fore.YELLOW + Style.NORMAL + str(text) + Fore.RESET + Style.RESET_ALL)


def printDisaster(text):
    doPrint(Fore.RED + Style.BRIGHT + str(text) + Fore.RESET + Style.RESET_ALL)


def printDebug(text):
    if outputDebug:
        doPrint(Style.DIM + Fore.LIGHTBLACK_EX + str(text) + Fore.RESET + Style.RESET_ALL)


def doPrint(output):
    print(output)

### Advent of Code init stuff ###


data = []


def get_data(filename):
    _data = []
    if os.path.exists(filename):
        f = open(filename, "r")
        if f.mode == 'r':
            _data = f.read().splitlines()
            f.close()
    return _data


def advent_init(filename: str, args: List[str]) -> List[str]:
    data = []

    if len(args) >= 2:
        filename = args[1]

    data = get_data(filename)
    if (data == []):
        printDisaster("NO FILE")

    return data