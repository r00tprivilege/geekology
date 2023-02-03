import zipfile
import sys
import os


# compressor
def zip_file(f_path):
    compress_file = zipfile.ZipFile(f_path + '.zip', 'w')
    compress_file.write(path, compress_type=zipfile.ZIP_DEFLATED)
    compress_file.close()


# Declare: return all file paths of the particular directory
def retrieve_f_paths(dir_name):
    # paths variable
    f_paths = []

    # Read all directory, subdirectories and file lists
    for root, directories, files in os.walk(dir_name):
        for fName in files:
            # Create the full file path by using os module.
            f_path = os.path.join(root, fName)
            f_paths.append(f_path)

    # return all paths
    return f_paths


def zip_dir(dir_path, f_paths):
    # write files and folders to a zipfile
    compress_dir = zipfile.ZipFile(dir_path + '.zip', 'w')
    with compress_dir:
        # write each file separately
        for file in f_paths:
            compress_dir.write(file)


if __name__ == "__main__":
    path = sys.argv[1]

    if os.path.isdir(path):
        files_path = retrieve_f_paths(path)
        # print the list of files to be zipped
        print('The following list of files will be zipped:')
        for file_name in files_path:
            print(file_name)
        zip_dir(path, files_path)
    elif os.path.isfile(path):
        print('The %s will be zipped:' % path)
        zip_file(path)
    else:
        print('a special file(socket,FIFO,device file), please input file or dir')
