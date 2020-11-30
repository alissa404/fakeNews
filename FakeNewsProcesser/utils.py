import os
import json
import pandas as pd


def max_str_in_list(l : list):
    return max(l, key=len)


# def find_texts(id, tag, cat):
#     datasetpath = f'fakenew_dataset/{cat}/{tag}/{id}/tweets'
#     jsons = os.listdir(datasetpath)

#     text_dict = {}
#     for json_file in jsons:
#         json_id = json_file.rstrip('.json')
#         with open(os.path.join(datasetpath, json_file)) as f:
#             text = json.load(f)['text']
#             text_dict[json_id] = text
#     return text_dict


def find_text(id, dataset, label):
    datasetpath = f'fakenew_dataset/{dataset}/{label}/{id}/tweets'
    try:
        json_file = os.listdir(datasetpath)[0]

        with open(os.path.join(datasetpath, json_file)) as f:
            text = json.load(f)['text']
    except:
        text = 'NaN'
    return text


def preprocessing(path, dataset, label):
    df = pd.read_csv(path).dropna()

    # parsing news media
    ser = df['news_url'].str.split('/').str[0].str.strip('wwwcom').str.split('.').apply(max_str_in_list)
    df['news_media'] = ser

    # add nes cat
    df['news_dataset'] = '政治' if dataset == 'gissipcop' else '娛樂'

    # drop col # change to config
    df = df.drop(columns='tweet_ids')

    # add text
    ser = df['id'].apply(find_text, label=label, cat=dataset)
    df['text'] = ser

    # add credibility
    df['credibility'] = 1 if label == 'real' else 0
    return df


def merge_dataframe():
    pass
