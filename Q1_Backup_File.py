#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Wap to accept a file name and directory name from user and create a backup of this file in same directory
'''
import os
import os.path
import shutil

   
path=input("Please enter directory")
file=input('Please enter file')


try:
   if os.path.exists(file_path):
       print('\n ********Taking Backup of file********* \n')
   else:
       raise IOError('Path does not exist')
   os.chdir(path)
   
   with open('bckup1.txt','w') as f:
       pass
   shutil.copy(os.path.join(path,file),os.path.join(path,'bckup1.txt'))


except Exception as E:
   print(sys.exc_info())
finally:
   print('\nBye Bye :)')

