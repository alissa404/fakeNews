import os
import glob
import json
import pandas as pd
from configparser import ConfigParser


def config2dict(config):
    """
    a function convert config object to dictionary
    :param config: an object generated from configparser
    :return: a dictionary containing information of config object
    """
    sections_dict = {}

    # get all defaults
    defaults = config.defaults()
    temp_dict = {}
    if hasattr(defaults, 'iterkeys'):
        iterkeys = defaults.iterkeys()
    else:
        iterkeys = defaults.items()

    for key in iterkeys:
        temp_dict[key] = defaults[key]

    sections_dict['default'] = temp_dict

    # get sections and iterate over each
    sections = config.sections()

    for section in sections:
        options = config.options(section)
        temp_dict = {}
        for option in options:
            temp_dict[option] = config.get(section, option)

        sections_dict[section] = temp_dict
    return sections_dict


def max_str_in_list(l : list):
    return max(l, key=len)


def find_text(id, dataset, label):
    path = f'fakenew_dataset/{dataset}/{label}/{id}/'
    try:
        jsonfile = os.path.join(path, os.listdir(path)[0])
        with open(jsonfile) as f:
            text = json.load(f)['text']
    except:
        text = 'NaN'
    return text


def preprocessing(config: ConfigParser, flag='gossipcop_fake'):
    # will change to object later virsion
    # reading config
    INFO = config2dict(config)
    CSVPATH = INFO['Csv Path'][flag]
    DATASET, LABEL = flag.split('_')
    RESULT_DIR = INFO['Dir Path']['resultdir']

    # read csv
    df = pd.read_csv(CSVPATH).dropna()

    # parsing news media
    ser = df['news_url'].str.split('/').str[0].str.strip('wwwcom').str.split('.').apply(max_str_in_list)
    df['news_media'] = ser

    # add nes cat
    df['news_dataset'] = '政治' if DATASET == 'gissip' else '娛樂'

    # drop col # change to config
    df = df.drop(columns='tweet_ids')

    # add text
    ser = df['id'].apply(find_text, dataset=DATASET, label=LABEL)
    df['text'] = ser

    # add credibility
    df['credibility'] = INFO['Label'][LABEL]

    # save
    if not os.path.exists(RESULT_DIR):
        os.makedirs(RESULT_DIR)
    save_path = os.path.join(RESULT_DIR, 'gossipcop_fake.csv')

    df.to_csv(save_path)
    return df


def merge_dataframe():
    pass
