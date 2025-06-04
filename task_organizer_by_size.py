import os
import json

PATH = r"C:\Users\hayk.hambardzumyan\Desktop\python\task_organizer\files"

files_lst = os.listdir(PATH)


json_f_name = "file_sizes.json"

def readable_size(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"

files_dict = {}


for file in files_lst:
    
    file_size = os.path.getsize(f"files/{file}")

    
    if file_size in files_dict:
        files_dict[file_size].append(f"files/{file}")
    else:
        files_dict[file_size] = [f"files/{file}"]

sorted_files_dict = dict(sorted(files_dict.items(), reverse=True, key=lambda item: item[0]))
 
r_sorted_files_dict = {}
for size, path in sorted_files_dict.items():
    read_size = readable_size(size)
    r_sorted_files_dict[read_size] = path

json_string = json.dumps(r_sorted_files_dict, indent=4)  

fp = os.path.join(PATH, json_f_name)
with open(fp, "w") as file:
    file.write(json_string)

