import json
import os
import re
import pandas as pd
import numpy as np
from tqdm import tqdm
from pprint import pprint
from typing import List,Dict


def get_mulit_turns(string):
    match = re.search(r'<用户与客服的对话 START>(.*?)<用户与客服的对话 END>',string,re.DOTALL)
    mutli_turns = match.group(1)
    return mutli_turns
    

def 
path = '/home/fangdong.wang/www2025/test1/test1.json'
image_folder = '/home/fangdong.wang/www2025/test1/images'
prompt_start = '你是一个电商客服专家，请根据用户与客服的多轮对话判断用户的意图分类标签'
save_path = '/home/fangdong.wang/www2025/test1/test1_intent.json'

data = []
with open(path,'r',encoding = 'utf-8') as f:
    data = json.load(f)

intent_data = []
for item in tqdm(data):
    instruction = item["instruction"]
    if prompt_start in instruction:
        if len(item["image"])>=1:
            # try:
            item["image"] = [os.path.join(image_folder,img) for img in item["image"]]
            item["id"] = f'test1_{item["id"]}'
            item["multi_turn_dialogue"] = get_mulit_turns(instruction)
            intent_data.append(item)
            # except:
            #     pprint(item)

with open(save_path,'w',encoding='utf-8') as f:
    json.dump(intent_data, f, ensure_ascii=False, indent=4)
    

