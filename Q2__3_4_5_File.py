#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Wap to find out total no of lines total no of words total no of characters in file
'''
import sys
fil_path=input('Enter file')
try:
    fil=open(fil_path,'r')
    fil_rev=open(r'C:\Users\priyanka\Desktop\python test\reverse.txt','w')
except Exception as e:
    print(sys.exc_info())
else:
    words=0
    chars=0
    for line in fil:
        
        fil_rev.write(line[::-1])
        fil_rev.write('\n')
        words=words+len(line.split(' '))
        for char in line.strip().replace(' ',''):
            chars+=1
    print(f'Total number of words : {words}\nTotal number of characters is {chars}')
finally:
    fil.close()
    fil_rev.close()
    print('process over')

    

