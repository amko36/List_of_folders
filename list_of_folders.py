#   The current script generates a list of folders in a given path. The files are not listed.
 
import os

path='/www/' # should be absolute path finished by '/' for Linux or by '\\' for Windows
directory=os.listdir(path) # lists all folders and files of the directory

for i in range(len(directory)):
    # we well check if each element presented in our path is a folder or not
    # that's why we should use the absolute paths 
    abspath=path+directory[i] 
    
    if os.path.isdir(abspath): 
        print(directory[i])

