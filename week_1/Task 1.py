#!/usr/bin/env python
# coding: utf-8

# In[11]:


def DiagonalName(name):
    s=""
    for i in range(len(name)):
        
        print(s+ name[i])
        s=s+" "
DiagonalName("Haris Rajput")        


# In[25]:


def RevDiagonalName(name):
    s=""
    for i in range(len(name)-1,-1,-1):
        
        print(s+ name[i])
        s=s+" "
RevDiagonalName("Haris") 


# In[ ]:




