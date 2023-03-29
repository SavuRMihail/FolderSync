# FolderSync
syncs the replica folder to the exact folder structure and contents of source folder

It is ran via the command line and basically does what is written above.
A few important notes:
-> It runs only in seconds so far due to testing purposes, it can be easily modified to wait for hours or minutes for each sync cycle however.
-> You run it via cmd like this: python main.py D:/source/ D:/replica/ 15

"D:/source/"  is the source directory
"D:/replica/" is the replica directory
15 is the amount you wish for it to run in seconds. For larger amounts you could just multiply by 60 for minutes and so on.
It also creates log.txt which writes has whatever was copied in there.

My implementation basically contains a timer which is the sync cycle time, a delete function which deletes everything from the replica, and then 2 functions one which makes the folder structure and one which parses recursively each folder and copies each individual file. I tested it on my machine with a folder containing 3 subfolders and a folder depth of 3.
