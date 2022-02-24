# this module return dict of files in directory "data"

import os
import json
import cv2

def list_dir_fls(folder='data', current_folder = True):
    answer = {'folder': '', 'subfolders': [], 'files': []}
    try:
        if current_folder:
            data_path = os.path.join(os.path.dirname(__file__), folder)
        else:
            data_path = folder
        answer['folder'] = data_path
        folders = [os.path.join(data_path, name) for name in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, name))]
        files = [os.path.join(data_path, name) for name in os.listdir(data_path) if os.path.isfile(os.path.join(data_path, name))]
        for fold in folders:
            answer['subfolders'].append(list_dir_fls(folder=fold, current_folder = False))
        answer['files'] = files
    except Exception as e:
        print(e)

    with open('folders_tree.json', 'w') as outfile:
        json.dump(answer, outfile)
    return(answer)

# print(list_dir_fls(folder='data/umarked'))

def rename_files(folder_path = 'data', abs=False):
    list_folders_files = list_dir_fls(folder='data/marked')
    for sub_f in list_folders_files['subfolders']:
        num = 0
        folder_path = sub_f['folder']
        folder_abs_name = sub_f['folder'].split('/')[-1]
        for file_path in sub_f['files']:
            abs_name = file_path.split('/')[-1]
            new_abs_name = f'{folder_abs_name}.{num}.tif'
            new_name = f'{folder_path}/{new_abs_name}'
            os.rename(file_path, new_name)
            num += 1


if __name__ == '__main__':
    print('PyCharm')
