import os
import shutil
import time
import datetime
import sys
from datetime import date

# sourceDir = r'D:/source/'
# replicaDir = r'D:/replica/'


def countDown(mins, sec):
    totalS = mins * 60 + sec

    while totalS > 0:
        timer = datetime.timedelta(seconds=totalS)
        print(timer, end='\r')
        time.sleep(1)
        totalS = totalS - 1
    print('Done!')


def deleteAll(dir):
    for files in os.listdir(dir):
        path = os.path.join(dir, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)


def folderStructure(input, output):
    for dirpath, dirnames, filenames in os.walk(input):
        structure = os.path.join(output, dirpath[len(input):])
        if not os.path.isdir(structure):
            os.mkdir(structure)
        else:
            continue
            # print('Already exists!')


def recursiveFolder(sourceD, replicaD):
    for file in os.listdir(sourceD):
        sourcePath = sourceD + os.sep + file
        replicaPath = replicaD + os.sep + file
        # print(sourcePath, replicaPath)
        if os.path.isfile(sourcePath):
            # print(sourcePath)
            shutil.copyfile(sourcePath, replicaPath)
            print("Copied " + sourcePath + " to " + replicaPath + " successfully!")
            logToFile(str("\nCopied " + sourcePath + " to " + replicaPath + " successfully!\n"))
        elif os.path.isdir(sourcePath):
            recursiveFolder(sourcePath, replicaPath)


def logToFile(text):
    f = open("log.txt", "a")
    f.write(text)
    f.close()


sourceDir = str(sys.argv[1])
replicaDir = str(sys.argv[2])
inputSec = int(sys.argv[3])
mins = 0

if not os.path.exists(sourceDir):
    print("Invalid source path!")
else:
    print("Valid source path!")

if not os.path.exists(replicaDir):
    print("Invalid replica path!")
else:
    print("Valid replica path!")

while 1 != 0:
    countDown(mins, inputSec)
    deleteAll(replicaDir)
    f = open("log.txt", "a")
    today = date.today()
    f.write(str(today))
    folderStructure(sourceDir, replicaDir)
    recursiveFolder(sourceDir, replicaDir)
