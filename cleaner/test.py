import os
FOLDER='/home/backups'

os.system('df -h')

for file in os.scandir(FOLDER):
    print(file)