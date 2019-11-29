from src.cuberoot import feature
import sys


def main():
    number = (sys.argv[1])
    res = feature.cube_root(number)
    print(res)