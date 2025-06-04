import os
import json

PATH = r"C:\Users\hayk.hambardzumyan\Desktop\python\task_organizer\files"

files_lst = os.listdir(PATH)


json_f_name = "file_distribution.json"



files_dict = {}

for file in files_lst:
    f_name, f_extension = os.path.splitext(file)
    if f_extension in files_dict:
        files_dict[f_extension]  += 1
    else:
        files_dict[f_extension] = 1
print(files_dict)


# sorted_files_dict = dict(sorted(files_dict.items(), reverse=True, key=lambda item: item[0]))
# print(sorted_files_dict)

json_string = json.dumps(files_dict, sort_keys=True, indent=len(files_dict))  
#print(json_string)


fp = os.path.join(PATH, json_f_name)
with open(fp, "w") as file:
    file.write(json_string)