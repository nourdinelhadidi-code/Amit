import os


def create_folders(path):
      
    if not os.path.exists(path):
        os.makedirs(path)

    for i in range(20):
        inner_path = os.path.join(path,"dir_" + str(i))
        if not os.path.exists(inner_path):
            os.makedirs(inner_path)