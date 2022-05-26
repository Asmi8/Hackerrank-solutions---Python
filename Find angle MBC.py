#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math


# In[ ]:


cat = list(map(int,[input() for x in range(2)]))
inverse_tan = math.atan(cat[0]/cat[1]) 
print(round(math.degrees(inverse_tan)), chr(176), sep='' )

