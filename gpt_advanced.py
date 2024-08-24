import os
import datetime

def get_file_info(directory='.', recursive=True):
    """
    Generates a list of dictionaries about files in the specified directory.
    
    Args:
        directory (str): The path to the directory to scan. Defaults to the current working directory.
        recursive (bool): If True, the function will also scan nested directories.

    Returns:
        List[dict]: A list of dictionaries, each containing information about a file.
    """
    file_info_list = []

    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            stats = os.stat(file_path)
            file_info = {
                'name': filename,
                'path': file_path,
                'size': stats.st_size,
                'creation_time': datetime.datetime.fromtimestamp(stats.st_ctime).isoformat(),
                'modification_time': datetime.datetime.fromtimestamp(stats.st_mtime).isoformat()
            }
            file_info_list.append(file_info)
        
        if not recursive:
            # If not recursive, break after scanning the top directory
            break

    return file_info_list

def main():
    directory = '.'  # Default to current working directory
    file_info_list = get_file_info(directory)
    print(file_info_list)

if __name__ == "__main__":
    main()
