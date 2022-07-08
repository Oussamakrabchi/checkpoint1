#!/usr/bin/env python
# coding: utf-8

# In[15]:


#exo 1 :
firstname = input("what is your first name? ")
lastname = input("what is your last name? ")
print(lastname +" "+ firstname)


# In[68]:


#exo 2 :
n = int(input("type an integer "))
temp = str(n) #temp is a string value of n
n1=temp+temp #n1 = nn
n2=temp+temp+temp #n2 = nnn
result = n +int(n1)+int(n2)
print("The computed value is : " ,result)


# In[32]:


#exo 3 :
n = int(input("type a number "))
if (n % 2) == 0 :
    print(n, "is an even number")
else :
    print(n, "is an odd number")


# In[38]:


#exo 4 :
for i in range(2000,3200) :
    if (i % 7) == 0 and (i % 5)!= 0 :
        print(i , end =" ")


# In[62]:


#exo 5 :
import math
n = int(input("Enter a number: "))
if n > 0 :
    print("The factorial of ", n, " is : ")
    print(math.factorial(n))
else :
    print("the factorial of negative value is undefined")


# In[59]:


#exo 6 :
string = input("type something ")
for i in range(0,len(string)) :
    if (i % 2) == 0 :
        print(string[i], end=" ")


# In[72]:


#exo 7 :
price = int(input("what is the price ? ")) #price must be a positive number
if price > 0 :
    if price >= 500 :
        newprice = price - price * (50/100)
        print("new price after the discount is ",newprice)
    elif price < 200 :
        newprice = price - price * (10/100)
        print("new price after the discount is ",newprice)
    elif price >=200 and price < 500:
        newprice = price - price * (30/100)
        print("new price after the discount is ",newprice)
else :
    print("price value must be a positive number")


# In[ ]:




