import os 

def file_info():
    file_info_list = []
    for filename in os.listdir('.'):
        file_path = os.path.join('.', filename)
        if os.path.isfile(file_path):
            stats = os.stat(file_path)
            file_info = {
                'name': filename, 
                'size': stats.st_size,
            }
            file_info_list.append(file_info)
file_info()


# print(file_info)