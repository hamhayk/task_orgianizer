from utils import create_folder, files_in_dict, sort_dict, json_string, create_json, get_size, readable_sorted_files_dict
#import utils
import os

dirname = os.path.dirname(__file__)

PATH = os.path.join(dirname, "files")

files_lst = os.listdir(PATH)

dist_json_file = "file_distribution.json"

size_json_file = "file_sizes.json"

create_json(json_string(sort_dict(files_in_dict())), dist_json_file)

get_size()

sort_dict(get_size())

create_json(json_string(readable_sorted_files_dict()), size_json_file)

create_folder()