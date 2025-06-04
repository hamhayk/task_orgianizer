import os
import shutil
import json

PATH = r"C:\Users\hayk.hambardzumyan\Desktop\python\task_organizer\files"

files_lst = os.listdir(PATH)

json_f_name_count = "file_distribution.json"

def create_folder():
    for file in os.listdir(PATH):
        full_path = os.path.join(PATH, file)
        if os.path.isfile(full_path):
            f_name, f_extension = os.path.splitext(file)
            if f_extension == ".jpg":
                folder_name = "Images"
            elif f_extension == ".pdf" or f_extension == ".docx":
                folder_name = "Documents"
            elif f_extension == ".mp4":
                folder_name = "Videos"
            elif f_extension == ".txt":
                folder_name = "Text files"
            elif f_extension == ".json":
                folder_name = "Json File"
            elif f_extension == ".xml":
                folder_name = "XML File"
            else:
                None

            os.makedirs(f"{PATH}/{folder_name}", exist_ok=True)
            source = f"{PATH}/{file}"   

            destination = f"{PATH}/{folder_name}/{file}"

            shutil.move(source, destination)

def files_in_dict():

    files_dict = {}

    for file in files_lst:
        f_name, f_extension = os.path.splitext(file)
        if f_extension in files_dict:
            files_dict[f_extension]  += 1
        else:
            files_dict[f_extension] = 1
    return files_dict

def sort_dict(dct):

    sorted_files_dict = dict(sorted(dct.items(), reverse=True, key=lambda item: item[0]))

    return sorted_files_dict
    
def json_string(dict):

    json_string = json.dumps(dict, indent=len(sort_dict(files_in_dict())))  

    return json_string

def create_json(dict, f_name):
    fp = os.path.join(PATH, f_name)
    with open(fp, "w") as file:
        file.write(dict)

def readable_size(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"

def get_size():

    files_dict_by_size = {}

    for file in files_lst:
    
        file_size = os.path.getsize(f"{PATH}/{file}")

        
        if file_size in files_dict_by_size:
            files_dict_by_size[file_size].append(f"files/{file}")
        else:
            files_dict_by_size[file_size] = [f"files/{file}"]

    return files_dict_by_size

def readable_sorted_files_dict():

    r_sorted_files_dict = {}
    for size, path in get_size().items():
        read_size = readable_size(size)
        r_sorted_files_dict[read_size] = path
    
    return r_sorted_files_dict