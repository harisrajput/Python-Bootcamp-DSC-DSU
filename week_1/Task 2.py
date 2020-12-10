#!/usr/bin/env python
# coding: utf-8

# In[ ]:


StudentRecord=[]
avg=0
for i in range(5):
    global StudentRecord
    roll_num=input("Enter Student Roll#: ")
    name=input("Enter Name: ")
    age=input("Enter Age: ")
    marks=input("Enter Marks out of 100: ")
    StudentRecord.append({"roll_num":roll_num,"name":name,"age":age,"marks": marks})
print("**roll_num** | **name** | **age** | **marks**")
for i in range(len(StudentRecord)):
    global avg
    print(StudentRecord[i].get("roll_num"),"        |",StudentRecord[i].get("name"),StudentRecord[i].get("age"),StudentRecord[i].get("marks"))
    avg=avg+int(StudentRecord[i].get("marks"))
avg=avg/5    
print(avg)    


# # 

# In[ ]:





# In[ ]:





