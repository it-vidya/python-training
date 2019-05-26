import os
stat =os.stat('first.py')
print(stat)
print(stat.st_atime)
print(stat.st_mtime)
print(stat.st_ctime)
print(stat.st_size)
