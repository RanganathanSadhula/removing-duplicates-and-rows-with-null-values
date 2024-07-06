#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# Read the dataset
data = pd.read_csv("C:\\Users\\91701\\Downloads\\NASA_airfoil_noise_raw.csv")

# Get the number of rows
num_rows = data.shape[0]

# Print the number of rows
print("Number of rows in the dataset:", num_rows)


# In[4]:


import pandas as pd

# Read the dataset
data = pd.read_csv("C:\\Users\\91701\\Downloads\\NASA_airfoil_noise_raw.csv")

# Remove duplicate rows
data_no_duplicates = data.drop_duplicates()

# Get the number of rows after removing duplicates
num_rows_no_duplicates = data_no_duplicates.shape[0]

# Print the number of rows after removing duplicates
print("Number of rows after removing duplicates:", num_rows_no_duplicates)


# In[5]:


import pandas as pd

# Read the dataset
data = pd.read_csv("C:\\Users\\91701\\Downloads\\NASA_airfoil_noise_raw.csv")

# Remove duplicate rows
data_no_duplicates = data.drop_duplicates()

# Remove rows with null values
data_cleaned = data_no_duplicates.dropna()

# Get the number of rows after removing duplicates and rows with null values
num_rows_cleaned = data_cleaned.shape[0]

# Print the number of rows after removing duplicates and rows with null values
print("Number of rows after removing duplicates and rows with null values:", num_rows_cleaned)


# In[ ]:




