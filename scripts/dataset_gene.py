import os 
import sys
import numpy as np
import pandas as pd
import json


class FileConnector(object):
    def __init__(self, root):
        self.root = root

    def _file_structure_parser(self):
        for root, _, fnames in os.walk(self.root):
            for fname in fnames:
                print(fnames)


if __name__ == '__main__':
    root_path = 'fakenewsnet_dataset_1\\gossipcop\\fake'
    fileconnector = FileConnector(root_path)

    gossipcop_fake = {}

    data_ids = os.listdir(root_path)
    for data_id in data_ids:
        {'data_id' : data_id}
        
        with open(os.path.join(root_path, data_id, os.listdir(os.path.join(root_path, data_id))[0])) as json_file:
            news_contents = json.load(json_file)
            print(news_contents.keys())
            assert 6==5

    # for id in ids:
    #     data_id = id
    #     print(os.listdir(os.path.join(root_path, data_id)))
    #     with open(os.path.join(root_path, data_id, r"news contents.json")) as json_file:
    #         news_contents = json.loads(json_file)
    #     print(news_contents)
    #     assert 6==5