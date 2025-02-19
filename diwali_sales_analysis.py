#!/usr/bin/env python
# coding: utf-8

# In[1]:


11+10


# In[2]:


print("data analytics on the go")


# In[3]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns


# In[4]:


get_ipython().system('pip install #to install any libraries')


# In[5]:


df =pd.read_excel("C:\\Users\\prami\\OneDrive\\Desktop\\EXCEL\\diwali_sales_python.xlsx")


# In[6]:


df.shape


# In[7]:


df.head(10)


# In[8]:


df.info()


# <H2> DATA CLEANING </H2>

# In[9]:


df.isnull().sum()


# In[10]:


df.drop(["Status","unnamed1"], axis=1, inplace=True)


# In[11]:


df.describe()


# In[12]:


df.info()


# In[13]:


df.isnull().sum()


# In[14]:


df.dropna(inplace= True )


# In[15]:


df.shape


# In[16]:


df.info()


# In[17]:


df.isnull().sum()


# In[18]:


df.info()


# In[19]:


df["Amount"] = df["Amount"].astype("int")


# In[20]:


df.info()


# In[21]:


df.dtypes


# In[22]:


df.columns


# In[23]:


df.rename(columns = {"Marital_Status" :"Shaadi"})


# In[24]:


#didnt save by not using inplace = true in the data file 


# In[25]:


df.describe()


# In[26]:


df[["Age","Amount"]].describe()


# In[27]:


#[[]]: to undestand the specific one when chosing the data


# <h1> DATA ANALYSIS : EXPLORATORY DATA ANALYSIS </H1>

# In[28]:


df.columns


# <h><b> GENDER </b> </h>

# In[29]:


df.dtypes


# In[30]:


ax = sns.countplot(x= "Gender", data=df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[31]:


sls_gen_base= df.groupby(["Gender"], as_index=False)["Amount"].sum().sort_values(by="Amount",ascending=False)


# In[32]:


sls_gen_base


# #Above created is an extra variable with the following values in it.

# In[33]:


sls_gen_base= df.groupby(["Gender"], as_index=False)["Amount"].sum().sort_values(by="Amount",ascending=False)
sns.barplot(x= "Gender", y="Amount", data=sls_gen_base)
for bars in ax.containers:
    ax.bar_label(bars)


# <p><b> Above Understanding our market segment to create marketing campaigns </b><p/>

# In[34]:


sns.countplot(data=df, x="Age Group", hue ="Gender")


# <P><B> As we can see the sales there are high number of females shoppers than the male when even compared in the age category </b></p>

# In[37]:


sales_age= df.groupby(["Age Group"], as_index=False)["Amount"].sum().sort_values(by="Amount",ascending=False)
sns.barplot(x= "Age Group", y="Amount", data=sales_age)


# <P><B> As we can see in the above pictures we understand the age group that spent alot in the upcoming diwali sales </b></p>
# 

# In[38]:


df.columns


# In[40]:


sales_state = df.groupby(["State"], as_index=False)["Orders"].sum().sort_values(by="Orders", ascending=False)


# In[41]:


sales_state


# In[43]:


sns.barplot(x="State", y="Orders", data=sales_state)
sns.set(rc={'figure.figsize':(20,5)})


# <P><B> The highest number of sales were gained from the Metropolitian cities , However Uttarpradesh came out to be the first state with the highest contribution </b></p>

# In[44]:


df.columns


# In[ ]:


sales_married = df.groupby(["Marital_Status"], as_index=False)["Product_Category"].sum().sort_values(by="Product_Category", ascending=False)


# In[48]:


sales_married


# In[ ]:


#it didnt work : didnt make sense either : experiment gone wrong


# In[77]:


sales_married2 = df.groupby(["Occupation"], as_index=False)["Amount"].sum().sort_values(by="Amount", ascending=False)


# In[78]:


sales_married2


# In[79]:


sns.set(rc={'figure.figsize':(20,5)})
sns.barplot( y="Amount", x="Occupation", data =sales_married2)


# In[ ]:


#And the buyers were mainly from the above categories: this data can help in the marketing area, to establish campaigns and tv ads with certain sentiment


# <h><b> PRODUCT CATEGORY </B></H>

# In[81]:


df.columns


# In[ ]:


product_sales = df.groupby(["Product_Category"], as_index=False)["Amount"].sum().sort_values(by="Amount", ascending=False).head(10)


# In[ ]:


product_sales


# In[ ]:


sns.set(rc={"figure.figsize":(20,5)})
sns.barplot(x="Product_Category",y="Amount", data= product_sales)


# In[ ]:


sns.set(rc={"figure.figsize":(20,5)})
ax = sns.countplot(data = df, x="Product_Category")

for bars in ax.containers:
    ax.bar_labels(bars)


# <h> <B> CONCLUSION </B></H>

# <h>According to Our whole Analysis we understood that majrity of our customers are from the age of 25-36 years adults, majorely employed in the IT and the health care sectors basically corporate and the other employees; However the most amount of sales are brought by the women for products like food, clothing and health care 
# 
# Thank you </h>
# 

# In[ ]:




