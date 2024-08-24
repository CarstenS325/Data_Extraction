import os
import datetime

def get_file_info(directory='.', recursive=True):
    """
    Generates a dictionary of dictionaries about files in the specified directory, including nested directories.
    
    Args:
        directory (str): The path to the directory to scan. Defaults to the current working directory.
        recursive (bool): If True, the function will also scan nested directories.

    Returns:
        dict: A dictionary where each key is a directory and its value is another dictionary with file info and subdirectories.
    """
    def scan_directory(path):
        directory_info = {}
        for root, dirs, files in os.walk(path):
            # Process files
            for filename in files:
                file_path = os.path.join(root, filename)
                stats = os.stat(file_path)
                file_info = {
                    'size': stats.st_size,
                    'creation_time': datetime.datetime.fromtimestamp(stats.st_ctime).isoformat(),
                    'modification_time': datetime.datetime.fromtimestamp(stats.st_mtime).isoformat()
                }
                # Add file information to the dictionary
                directory_info[file_path] = file_info

            # Process subdirectories
            if recursive:
                for dirname in dirs:
                    subdirectory_path = os.path.join(root, dirname)
                    directory_info[dirname] = scan_directory(subdirectory_path)
                
                # Prevent `os.walk` from walking into subdirectories if not recursive
                dirs[:] = [] 

            break  # Stop scanning deeper in the current `os.walk` loop
        
        return directory_info

    return scan_directory(directory)

def main():
    directory = '.'  # Default to current working directory
    file_info_dict = get_file_info(directory)
    print(file_info_dict)

if __name__ == "__main__":
    main()
