#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
7)Wap to accept directory name from user and remove if it is modify 30days older and if size is 100kb(use fun m10)
'''
import time
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
            file_time=os.path.getctime(os.path.join(path,file))
            if file_time < (time.time()-30*24*60*60) and file_siz == 0:
                print(f'{os.path.join(path,file)}')
                os.unlink(r'C:\Users\priyanka\Desktop\python test\file3.txt')
except Exception as E:
    print(sys.exc_info())
finally:
    print('\nBye Bye :)')
                
                
         
        
 

