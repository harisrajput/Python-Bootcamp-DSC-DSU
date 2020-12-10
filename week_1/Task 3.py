#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
def Lyrics(lyric):
   
    lyric= lyric.split(" ")
    for i in range(len(lyric)-1):
        print(lyric[i])
        time.sleep(1)
lyric = input()
Lyrics(lyric)   


# In[ ]:




