#!/usr/bin/env python
# coding: utf-8

# In[23]:


# A variable is a name given to a memory location. It is the basic unit of storage in a program.


# In[3]:





# In[2]:


#Rules for declaring the variables in python:


# In[ ]:





# In[ ]:


Rule 1 : No name spaces while declaring the variable name


# In[4]:


First name = 'Ahmed'
print(First name)


# In[ ]:


#Instead of spaces underscore should be used


# In[5]:


First_name = 'Shiva'
print(First_name)


# 

# In[ ]:


Rule 2 : A variable name should not start with a number


# In[6]:


1name = "Ram"
print(1name)


# In[7]:


name1 = "Ram"
print(name1)


# In[ ]:





# In[ ]:


Rule 3 : A variable shoud not contain any special characters


# In[8]:


name@ = "priya"
print(name@)


# In[ ]:





# In[ ]:


Introduction to data types in python:
    1. Mutable datatypes -----> which we can edit or alter (flexible ones)
    2. Immutable datatypes----> which we cannot able to edit or alter(fixed)


# In[ ]:





# In[ ]:


Introduction to string datatype :
    
overview ; String is a series of characters enclosed in quotes.

classification : it is classified as immutable datatype
    
get_ipython().set_next_input('how to define a string');get_ipython().run_line_magic('pinfo', 'string')

two possible approaches : 
    1. single quotes
    2. double quotes
    


# In[9]:


name1 = 'Aravind'
print(name1)


# In[10]:


name2 = "Adithya"
print(name2)


# In[ ]:





# In[ ]:


introduction to string methods:
    
methods are builtin programs that are available to use in python.


# In[ ]:


type----> it will be validating the datatypes...


# In[11]:


type("name")


# In[2]:


type("5.5")


# In[ ]:





# In[16]:


full_name = "abdul gaffar"
print(full_name)


# In[14]:


print(full_name.title())


# In[15]:


# title is used to print the first letter as capital


# In[ ]:





# In[17]:


# if we want to convert the full name in capitals use ".upper()"


# In[18]:


name = "abdul gaffar"
print(name.upper())


# In[19]:


# if we want to convert the full name in small letters use ".lower()"


# In[21]:


name = "ABDUL GAFFAR"
print(name.lower())


# In[ ]:





# In[ ]:


Introduction to f strings:


# In[7]:


first_name = "nikhil"
last_name = "kumar"
fullname = f"{first_name}{last_name}"
print(fullname)


# In[ ]:


#req : i want to have a full name


# In[9]:


print(fullname .title())


# In[12]:


# Adding white spaces to strings :


# In[13]:


print("Favourite_programming_language:pythoncc++javaswift")


# In[14]:



print("Favourite_programming_language:\npython\nc\nc++\njava\nswift")


# In[15]:


print("Favourite_programming_language:\n\tpython\n\tc\n\tc++\n\tjava\n\tswift")


# In[ ]:


# removing whitespaces from strings


# In[16]:


x=  "Python"
print(x)


# In[3]:


y = "  Python"
print(y)


# In[18]:


z = "Python  "
print(z)


# In[20]:


y.lstrip()


# In[21]:


z.rstrip()


# In[22]:


x.rstrip()


# In[ ]:





# In[3]:


# Introduction to list datatype :


# In[9]:


#overview : A list is a collection of items maintained in a particular order
classification: It is classified as mutable datatype(flexible)
How do you define a list...?   []


# In[ ]:





# In[12]:


students = ['kumar','naveen','keerthi','ayub','imran','joseph']


# In[13]:


print(students)


# In[14]:


type(students)


# In[15]:


# How to acess from the above element list...?


# In[16]:


# req : i want to get the kumar output from the students list?


# In[ ]:





# In[18]:


Introduction to indexing : .....>0,1,2,3,4.....


# In[19]:


print(students[0])


# In[21]:


Note : By using the concept of indexing we can acess the elements from the list


# In[22]:


print(students[2])


# In[ ]:





# In[ ]:


1. how to add new elements to the list
2. how to modify the elements in the list
3. how to delete the elements in the list


# In[ ]:





# In[ ]:


1. how to add new elements to the list


# In[ ]:





# In[ ]:


# req: i want to add nikhil to the list


# In[23]:


students.append('nikhil')


# In[24]:


print(students)


# In[ ]:


# req: i want to add deepa in the list


# In[25]:


students.append('deepa')
print(students)


# In[ ]:


# req: to add ayesha to the 2nd index


# In[28]:


students.insert(2,'ayesha')
print(students)


# In[30]:


print(students[2])


# In[ ]:





# In[ ]:


2. how to modify the elements in the list


# In[ ]:


# req: i wan to replace naveen with kalyan


# In[31]:


students[1] = 'kalyan'
print(students)


# In[ ]:





# In[ ]:


3. how to delete the elements in the list


# In[ ]:


# req: i want to delete keerthi name from the list


# In[32]:


del students[3]
print(students)


# In[ ]:





# In[2]:


Organizing the list data types


# In[ ]:





# In[6]:


cars = ['seltos','bmw','audi','suzuki','verna','benz']
print(cars)


# In[7]:





# In[ ]:


# req : i want to organize the list in capital order....A-Z.....?


# In[ ]:


# two approaches
1. temporary approach----> changes made will be reversed.
2. permanent approach----> changes will be permanently applied.


# In[ ]:





# In[8]:


print(sorted(cars)) # temp approach


# In[ ]:


# b,b----> e,m


# In[ ]:





# In[10]:


cars.sort() # permanent apprroach


# In[11]:


print(cars)


# In[ ]:





# In[ ]:


# how to count the no of elements that are present in the list


# In[14]:


len(cars)


# In[15]:


print(cars)


# In[ ]:


# how to print the list in reverse order.


# In[21]:


cars.reverse()


# In[23]:


print(cars)


# In[ ]:





# In[ ]:


Introduction to slicing of strings


# In[ ]:





# In[27]:


students = ['yogesh','prudhvi','deepa','pallavi','asof','javed','kumar','naveen']
print(students)


# In[28]:


# general syntax of slicing :


# In[ ]:


[starvalue:stopvalue:stepcount]


# In[ ]:


Note : Stop value is always exclusive ---->  last number it wont be considered


# In[ ]:


# req : i want to get yogesh and prudhivi in


# In[29]:


print(students[0:1]) # we have to add +1


# In[30]:


print(students[0:3])


# In[50]:


#


# In[51]:


#


# In[ ]:


S=”PYTHON”X,Y=5,2print(“The quotient is”, x/y,  x//y, S, sep=”$”,end=” “)S=”IS EASY”print(“PYTHON”,S)


# In[14]:


S=”PYTHON”X,Y=5,2print(“The quotient is”, x/y,  x//y, S, sep=”$”,end=” “)S=”IS EASY”print(“PYTHON”,S)


# In[48]:


#


# In[49]:


#


# In[ ]:





# In[ ]:





# In[ ]:





# In[47]:


#


# In[46]:


#


# In[45]:


#


# In[ ]:




