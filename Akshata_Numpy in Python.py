#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


#1-Dim Array 
l1=[10,20,30,40,50]
a1=np.array(l1)
print(type(l1))
print(l1)
print("--------------------------------------------------")
print(type(a1))
print(a1)


# In[3]:


#2-Dim Array

l2=[[10,20,30],[40,50,60],[70,80,90]]
a2=np.array(l2)
print(type(l2))
print(l2)
print("----------------------------------------------------")
print(type(a2))
print(a2)


# In[4]:


#Generate single random float number using numpy
a3=np.random.rand(1)
a3


# In[5]:


#Generate array of random number using numpy
a4=np.random.rand(5)
a4


# In[6]:


#Generate single random int number using numpy
a5=np.random.randint(5)
a5


# In[7]:


#Generate multiple random number using numpy
a6=np.random.randint(5,10,3)
a6


# In[8]:


#arange() is similar to range()func in python
a7=np.arange(50)
a7


# In[9]:


a8=np.arange(50,100)
a8


# In[10]:


a9=np.arange(5,51,5)
a9


# In[11]:


a10=a7.reshape(5,10)
a10


# In[12]:


#Elements Picking in 2-Dim array
#Picking First row
a10[0]


# In[13]:


#Pick single element
a10[1,6]


# In[14]:


#picking multiple rows
a10[:3]


# In[15]:


#picking multiple rows and columns
a10[:3,:5]


# In[16]:


a10[2:5,4:10]


# In[17]:


a10[:,::2]


# In[18]:


a10[::2]


# In[19]:


a2


# In[20]:


a2.diagonal()


# In[21]:


a2.min()


# In[22]:


a2.max()


# In[23]:


a2.mean()


# In[24]:


#list in array form
l3=[10,20,25,13,48,75]
a11=np.array(l3)
a11


# In[25]:


#Conditional picking 
#Create new array while consisting of element which is greater than 20 from  a11
a12=a11[a11>20]
a12

