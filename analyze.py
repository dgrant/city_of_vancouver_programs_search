#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import os

def main():
    files = os.listdir('json')
    nums = []
    for file in files:
        num = int(os.path.splitext(file)[0].split('_')[1])
        nums.append(num)
    nums.sort()
    binwidth = 100
    plt.hist(nums, bins=np.arange(min(nums), max(nums) + binwidth, binwidth))
    plt.show()

if __name__ == '__main__':
    main()
