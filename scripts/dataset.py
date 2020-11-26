import os
import sys
import json 
import numpy as np
from FakeNewsProcesser.utils import preprocessing


def find_texts(id, tag, cat):
    datasetpath = f'fakenew_dataset/fakenewsnet_dataset_1/{cat}/{tag}/{id}/tweets'
    jsons = os.listdir(datasetpath)

    text_dict = {}
    for json_file in jsons:
        json_id = json_file.rstrip('.json')
        with open(os.path.join(datasetpath, json_file)) as f:
            text = json.load(f)['text']
            text_dict[json_id] = text
    return text_dict


def find_text(id, tag, cat):
    datasetpath = f'fakenew_dataset/fakenewsnet_dataset_1/{cat}/{tag}/{id}/tweets'
    try:
        json_file = os.listdir(datasetpath)[0]

        with open(os.path.join(datasetpath, json_file)) as f:
            text = json.load(f)['text']
    except:
        text = 'NaN'
    return text

if __name__ == '__main__':
    # config
    # PATH = 'data/origin/gossipcop_fake.csv'
    PATH = sys.argv[1]
    TAG = PATH.rstrip('.csv').split('_')[-1]
    CATEGORY = PATH.rstrip('.csv').split('/')[1].rstrip('_fake')
    # add savepath

    df = preprocessing(PATH, tag=TAG, category=CATEGORY)
