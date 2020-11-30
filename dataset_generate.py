import os
import sys
import json 
import numpy as np
from configparser import ConfigParser
from FakeNewsProcesser.utils import preprocessing


if __name__ == '__main__':
    # reading config
    config = ConfigParser()
    # PATH = 'data/origin/gossipcop_fake.csv'
    PATH = sys.argv[1]
    TAG = PATH.rstrip('.csv').split('_')[-1]
    CATEGORY = PATH.rstrip('.csv').split('/')[-1].rstrip('_fake')
    # add savepath

    df = preprocessing(PATH, tag=TAG, category=CATEGORY)
    df.to_csv('./testout.csv')
