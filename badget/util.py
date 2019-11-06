import json
import os
import pathlib
import re

time_format = '%Y-%m-%d %H:%M:%S'

def get_stem(filename):
     return pathlib.Path(filename).stem

def get_json_filenames_in_dir(path):
    return [f for f in os.listdir(path) if re.match(r'^.*\.json', f)]

def for_each_json_file_in_dir(path, func):

    filenames = get_json_filenames_in_dir(path)
    
    for filename in filenames:
        with open(os.path.join(path, filename), 'r') as f:
            o = json.load(f)
            func(filename, o)