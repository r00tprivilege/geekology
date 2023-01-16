#Directory Organizer

import argparse
import os

def path():
    parse = argparse.ArgumentParser(
        add_help=True, description="Organization by type")
    parse.add_argument('directory_path', type=str, default='./',
                       help="The absolute path to the directory")
    return parse.parse_args().directory_path

#Modify this part for organizing more formats
docs = ['.log', '.txt', '.doc', '.docx', '.md', '.pdf', '.wps']
pix = ['.png', '.jpg', 'jpeg', '.bmp']
music = ['.mp3', '.wav']
compressed = ['.zip', '.rar', '.tar', '.gz', '.bz2', '.xz']
video = ['.3gp', '.mov', '.mp4', '.mkv', '.srt', '.avi']
web = ['.html', .'.css', '.js']
source = ['.py', '.c', '.cpp', '.java',]


directories = [path() + '/Compressed', path() + '/Documents',
               path() + '/Pictures', path() + '/Music', path() + '/Video', path() + '/Web', path() + '/Source-codes',]

print("This organize your files to different directories according to their type!!")
print("Are you sure you want to continue? (y/n)")
theFlag = input('>>>')
if theFlag.lower() == 'y':
    try:
        for d in directories:
            os.mkdir(d)
    except FileExistsError:
        pass

    for files in os.listdir(path()):
        dot = (files.rfind('.'))
        if dot is not 0 and dot is not -1:
            if files[dot:].lower() in music:
                os.rename(path() + '/' + files, path() + '/Music/' + files)
            if files[dot:].lower() in pix:
                os.rename(path() + '/' + files, path() + '/Pictures/' + files)
            if files[dot:].lower() in docs:
                os.rename(path() + '/' + files, path() + '/Documents/' + files)
            if files[dot:].lower() in compressed:
                os.rename(path() + '/' + files, path() +
                          '/Compressed/' + files)
            if files[dot:].lower() in video:
                os.rename(path() + '/' + files, path() + '/Video/' + files)
            if files[dot:].lower() in web:
                os.rename(path() + '/' + files, path() + '/Web/' + files)
            if files[dot:].lower() in source:
                os.rename(path() + '/' + files, path() + '/Source-codes/' + files)    

    for d in directories:
        if os.listdir(d) is None:
            os.removedirs(d)
else:
    print("Finishing")
    os.sys.exit(0)
