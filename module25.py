from datetime import date
from datetime import time
from datetime import datetime
import os

today = date.today()
date_time = datetime.now()
print("Today's date is:", today)
print("All together now", date_time)

#Display Working Directory
#method using "getcwd()" which will return current working directory
#if you want just the directory name then you can split by "/" or using
#another function called "basename" from 'os.path' module


dirpath = os.getcwd()
print("Your current working directory is: " + dirpath)
foldername = os.path.basename(dirpath)
print("The directory name is: " + foldername)

#displaying file metadata
#os.stat() function, put file name in brackets

#st_mode - protection bits
#st_ino - inode number
#st_dev - device
#st_nlink - number of hard links
#st_uid - user id of owner
#st_gid - group id of owner
#st_size - size of file, in bytes
#st_atime - time of most recent access
#st_mtime - time of most recent modification
#st_ctime - time of most recent metadata change

print(os.stat("module25.py"))
