import os
import sys
import json 
import numpy as np
from configparser import ConfigParser
from FakeNewsProcesser.utils import preprocessing


if __name__ == '__main__':
    # reading config
    config = ConfigParser()
    config.read_file(open('config.cfg'))

    # preprocessing dataset
    df = preprocessing(config, flag='gossipcop_fake')
    print(df.keys())
    print(df.head())
    print(df['news_url'])