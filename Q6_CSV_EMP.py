#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
emp_id,emp_name,empsal,empdept
6) Wap to read csv file which contain following columns emp id, emp name, empsal, empdept
a) Find out the avg salary of ITdept
'''
import csv
import sys
fil_path=input('Enter file')
sal=[]
try:
    csv_fil=open(fil_path,'r')
except Exception as e:
    print(sys.exc_info())
else:
    reader=csv.DictReader(csv_fil)
    for row in reader:
        if row['empdept'] == 'IT':
            sal.append(int(row['empsal']))
    print(f'Average salary of it Dept is : {sum(sal)/len(sal)}')
    
finally:
    csv_fil.close()
    print('process over :) :)')
    

