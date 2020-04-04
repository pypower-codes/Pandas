#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Creating a dataframe using List:

# import pandas as pd
import pandas as pd
 
# list of strings
lst = ['PyPower', 'Projects', 'Explores', 'Amazing', 
            'and', 'Cool', 'PythonProjects']
 
# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)


# In[3]:


# Python code demonstrate creating 
# DataFrame from dict narray / lists 
# By default addresses.
 
import pandas as pd
 
# intialise data of lists.
data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
 
# Create DataFrame
df = pd.DataFrame(data)
 
# Print the output.
print(df)


# In[4]:


# Import pandas package
import pandas as pd
 
# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
 
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
 
# select two columns
print(df[['Name', 'Qualification']])


# In[5]:


# importing pandas package
import pandas as pd
 
# making data frame from csv file
data = pd.read_csv("D:\\PyPower\\Pandas\\nba.csv", index_col ="Name")
 
# retrieving row by loc method
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]
 
 
print(first, "\n\n\n", second)


# In[6]:


# importing pandas module 
import pandas as pd 

# making data frame 
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv") 

# calling head() method 
# storing in new variable 
data_top = data.head() 

# display 
data_top 


# In[8]:


# Adding new column to existing DataFrame in Pandas

# Import pandas package 
import pandas as pd 

# Define a dictionary containing Students data 
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'], 
		'Height': [5.1, 6.2, 5.1, 5.2], 
		'Qualification': ['Msc', 'MA', 'Msc', 'Msc']} 

# Convert the dictionary into DataFrame 
df = pd.DataFrame(data) 

# Declare a list that is to be converted into a column 
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna'] 

# Using 'Address' as the column name 
# and equating it to the list 
df['Address'] = address 

# Observe the result 
df 


# In[9]:


# Import pandas package 
import pandas as pd 

# Define a dictionary containing Students data 
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'], 
		'Height': [5.1, 6.2, 5.1, 5.2], 
		'Qualification': ['Msc', 'MA', 'Msc', 'Msc']} 

# Convert the dictionary into DataFrame 
df = pd.DataFrame(data) 

# Using DataFrame.insert() to add a column 
df.insert(2, "Age", [21, 23, 24, 21], True) 

# Observe the result 
df 


# In[10]:


#Grouping Data

# importing pandas module 
import pandas as pd 

# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi', 
				'Gaurav', 'Anuj', 'Princi', 'Abhi'], 
		'Age':[27, 24, 22, 32, 
			33, 36, 27, 32], 
		'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj', 
				'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'], 
		'Qualification':['Msc', 'MA', 'MCA', 'Phd', 
						'B.Tech', 'B.com', 'Msc', 'MA']} 
	

# Convert the dictionary into DataFrame 
df = pd.DataFrame(data1) 

print(df) 


# In[11]:


# using groupby function 
# with one key 

df.groupby('Name') 
print(df.groupby('Name').groups) 


# In[12]:


# applying groupby() function to 
# group the data on Name value. 
gk = df.groupby('Name') 
	
# Let's print the first entries 
# in all the groups formed. 
gk.first() 


# In[13]:


#Concatenating Two DataFrames

# importing pandas module
import pandas as pd 
 
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
   
# Define a dictionary containing employee data 
data2 = {'Name':['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'], 
        'Age':[17, 14, 12, 52], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
 
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1,index=[0, 1, 2, 3])
 
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2, index=[4, 5, 6, 7])
 
print(df, "\n\n", df1) 

#Now we apply .concat function in order to concat two dataframe

# using a .concat() method
frames = [df, df1]
 
res1 = pd.concat(frames)
res1


# In[14]:


# importing pandas module
import pandas as pd 
 
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd'],
        'Mobile No': [97, 91, 58, 76]} 
   
# Define a dictionary containing employee data 
data2 = {'Name':['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'], 
        'Age':[22, 32, 12, 52], 
        'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons'],
        'Salary':[1000, 2000, 3000, 4000]} 
 
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1,index=[0, 1, 2, 3])
 
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2, index=[2, 3, 6, 7]) 
 
print(df, "\n\n", df1) 

#Now we set axes join = inner for intersection of dataframe

# applying concat with axes
# join = 'inner'
res2 = pd.concat([df, df1], axis=1, join='inner')
 
res2


# In[15]:


# importing pandas module
import pandas as pd 
  
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd'],
        'Mobile No': [97, 91, 58, 76]} 
    
# Define a dictionary containing employee data 
data2 = {'Name':['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'], 
        'Age':[22, 32, 12, 52], 
        'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons'],
        'Salary':[1000, 2000, 3000, 4000]} 
  
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1,index=[0, 1, 2, 3])
  
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2, index=[2, 3, 6, 7]) 
print(df, "\n\n", df1) 

#Now we are going to apply ignore_index as an argument.

# using ignore_index
res = pd.concat([df, df1], ignore_index=True)
 
res


# In[ ]:


from pandas import DataFrame
export_csv = df.to_csv(r"D:\\PyPower\\Pandas\\nba.csv",index = False)

