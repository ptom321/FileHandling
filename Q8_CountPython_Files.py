#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Wap to find out count of all the python files in any specific directory and subdirectory
'''
import os.path
    
file_path=input("Please enter directory")

try:
    if os.path.exists(file_path):
        print('\n ********Total number of files in each folder********* \n')
    else:
        raise IOError('Path does not exist')
    for path,subfolders,files in os.walk(file_path):
        i=0
        for file in files:
            name,extension=os.path.splitext(os.path.join(path,file))
            if extension == '.py':
                i+=1
        print(path.split('\\')[-1],i)

except Exception as E:
    print(sys.exc_info())
finally:
    print('\nBye Bye :)')
                
                
         
        

