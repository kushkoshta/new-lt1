#!/usr/bin/env python
# coding: utf-8

# In[30]:


import numpy as np
import matplotlib.pyplot as plt
city_x = np.array([100,120,85,90,110,95])
city_y = np.array([80,75,60,95,85,90])
city_z = np.array([150,140,135,160,155,170])
print(city_x)
def total_rainfall(v):
    return np.sum(v)


# In[31]:


city_y


# In[32]:


city_z


# In[33]:


print("TOTAL RAINFALL IN CITY_X",total_rainfall(city_x))
print("TOTAL RAINFALL IN CITY_Y",total_rainfall(city_y))
print("TOTAL RAINFALL IN CITY_Z",total_rainfall(city_z))


# In[34]:


def total_average(v):
    return np.mean(v)


# In[35]:


print("AVERAGE RAINFALL IN CITY_X",total_average(city_x))
print("AVERAGE RAINFALL IN CITY_Y",total_average(city_y))
print("AVERAGE RAINFALL IN CITY_Z",total_average(city_z))


# In[36]:


def total_avg_month(x,y,z):
    v = []
    for i in range(0,6):
        v.append((x[i]+y[i]+z[i])/3.0)
    return v
        


# In[37]:


a = total_avg_month(city_x,city_y,city_z)
print("AVERAGE RAINFALL IN EVERY MONTH",a)


# In[38]:


x=np.arange(1,7)
fig = plt.figure()
axes = fig.add_axes([0.2,0.2,1,1])
axes.plot(x,city_x,label='X')
axes.plot(x,city_y,label='Y')
axes.plot(x,city_z,label='Z')
plt.grid()
plt.legend(loc=[1.04,0])
plt.show()


# In[39]:


rng = []
rng.append(city_x.max()-city_x.min())
rng.append(city_x.max()-city_x.min())
rng.append(city_x.max()-city_x.min())
print("RANGE OF RAINFALL",rng)


# In[42]:


m = [1,2,3]
plt.bar(m,rng)
plt.title("RANGE OF RAINFALL")
plt.show()


# In[ ]:




