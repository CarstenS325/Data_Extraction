import os  # Import the os module for interacting with the operating system
import datetime  # Import datetime module to handle dates and times

def get_file_info(directory):
    """
    Generates a list of dictionaries with information about files in the specified directory.

    Args:
        directory (str): The path to the directory to scan.

    Returns:
        List[dict]: A list of dictionaries containing file information.
    """
    file_info_list = []  # Initialize an empty list to hold file information dictionaries
    for filename in os.listdir(directory):    # Iterate over each filename in the specified directory
        file_path = os.path.join(directory, filename)  # Construct the full file path
        if os.path.isfile(file_path):    # Check if the path is a file (not a directory)
            stats = os.stat(file_path)  # Get the file statistics
            file_info = {               # Create a dictionary with file information
                'name': filename,  # File name
                'size': stats.st_size,  # File size in bytes
                'creation_time': datetime.datetime.fromtimestamp(stats.st_ctime).isoformat(),  # Creation time in ISO format
                'modification_time': datetime.datetime.fromtimestamp(stats.st_mtime).isoformat()  # Last modification time in ISO format
            }
            file_info_list.append(file_info)  # Add the file information dictionary to the list
    return file_info_list  # Return the list of file information dictionaries
def main():
    working_directory = os.getcwd()  # Get the current working directory
    file_info_list = get_file_info(working_directory)  # Get file information for the working directory
    print(file_info_list)  # Print the list of file information dictionaries
if __name__ == "__main__":
    main()  # Execute the main function when the script is run directly

