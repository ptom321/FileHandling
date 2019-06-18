#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Wap to accept directory name from user and remove all the empty files
'''
import os
import sys
import os.path


file_path=input("Please enter directory")

try:
    if os.path.exists(file_path):
        print('\n ********Deleting below files********* \n')
    else:
        raise IOError('Path does not exist')
    for path,subfolders,files in os.walk(file_path):
         for file in files:
            file_siz=os.path.getsize(os.path.join(path,file))
            if file_siz == 0:
                print(file)
                os.unlink(os.path.join(path,file))
except Exception as E:
    print(sys.exc_info())
finally:
    print('\nBye Bye :)')
                

