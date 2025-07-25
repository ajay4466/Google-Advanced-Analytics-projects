#!/usr/bin/env python
# coding: utf-8

# # Activity: Structure your data 

# ## Introduction
# 
# In this activity, you will practice structuring, an **exploratory data analysis (EDA)** step that helps data science projects move forward. During EDA, when working with data that contains aspects of date and time, "datetime" transformations are integral to better understanding the data. As a data professional, you will encounter datetime transformations quite often as you determine how to format your data to suit the problems you want to solve or the questions you want to answer. This activity gives you an opportunity to apply these skills and prepare you for future EDA, where you will need to determine how best to structure your data.
# 
# In this activity, you are a member of an analytics team that provides insights to an investing firm. To help them decide which companies to invest in next, the firm wants insights into **unicorn companies**–companies that are valued at over one billion dollars.  
# 
# You will work with a dataset about unicorn companies, discovering characteristics of the data, structuring the data in ways that will help you draw meaningful insights, and using visualizations to analyze the data. Ultimately, you will draw conclusions about what significant trends or patterns you find in the dataset. This will develop your skills in EDA and your knowledge of functions that allow you to structure data.
# 
# 
# 
# 

# ## Step 1: Imports 

# ### Import relevant libraries and modules
# 
# Import the relevant Python libraries and modules that you will need to use. In this activity, you will use `pandas`, `numpy`, `seaborn`, and `matplotlib.pyplot`.

# In[4]:


# Import the relevant Python libraries and modules needed in this lab.

### YOUR CODE HERE ###
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# ### Load the dataset into a DataFrame
# 
# The dataset provided is in the form of a csv file named `Unicorn_Companies.csv` and contains a subset of data on unicorn companies. As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.

# In[5]:


# RUN THIS CELL TO IMPORT YOUR DATA.

### YOUR CODE HERE ###
companies = pd.read_csv("Unicorn_Companies.csv")


# ## Step 2: Data exploration
# 

# ### Display the first 10 rows of the data
# 
# In this section, you will discover what the dataset entails and answer questions to guide your exploration and analysis of the data. This is an important step in EDA. 
# 
# To begin, display the first 10 rows of the data to get an understanding of how the dataset is structured. 

# In[6]:


# Display the first 10 rows of the data.

### YOUR CODE HERE ###
companies.head()


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to [the content about exploratory data analysis in Python](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/lecture/kfl9b/find-stories-using-the-six-exploratory-data-analysis-practices).
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Use the function in the `pandas` library that allows you to get a specific number of rows from the top of a DataFrame.
#  
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
#   Call the `head()` function from the `pandas` library and pass in the number of rows you want from the top of the DataFrame.
# 
# </details>

# ### Identify the number of rows and columns
# 
# Identify the number of rows and columns in the dataset. This will help you get a sense of how much data you are working with.

# In[7]:


# Identify the number of rows and columns in the dataset.

### YOUR CODE HERE ###

companies.shape


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to [the content about exploratory data analysis in Python](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/lecture/kfl9b/find-stories-using-the-six-exploratory-data-analysis-practices).
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Use the property that DataFrames in `pandas` have to display the number of rows and the number of columns as a tuple.
#  
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# The `shape` property that DataFrames have can help.
# 
# </details>

# **Question:** How many rows and columns are in the dataset? How many unicorn companies are there? How many aspects are shown for each company?
# 

#  1074 rows and 10 columns it means there a total of 1074 unicorn company and each companies 10 aspects are shown including the name of the unicorn company

# ### Check for duplicates in the data

# In[8]:


# Check for duplicates.

### YOUR CODE HERE ###
companies.drop_duplicates()
companies.shape


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to [the content about exploratory data analysis in Python](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/lecture/kfl9b/find-stories-using-the-six-exploratory-data-analysis-practices).
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Use the function in `pandas` that can be called on a DataFrame to return the same DataFrame but with duplicates removed.
# 
# Use property that DataFrames in `pandas` have that to display the number of rows and columns as a tuple.
#  
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Call the `drop_duplicates()` function on `companies`, followed by calling the `shape` property. 
# 
# Compare the shape that is returned from this to the original shape of `companies`, which you identified previously. 
# 
# </details>

# **Question:** Based on the preceding output, are there any duplicates in the dataset?
# 

# There are no duplicates in the dataset

# ### Display the data types of the columns 
# 
# Knowing the data types of the columns is helpful because it indicates what types of analysis and aggregation can be done, how a column can be transformed to suit specific tasks, and so on. Display the data types of the columns. 

# In[9]:


# Display the data types of the columns.

### YOUR CODE HERE ###

companies.dtypes


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to [the content about exploratory data analysis in Python](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/lecture/kfl9b/find-stories-using-the-six-exploratory-data-analysis-practices).
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Use the property that DataFrames in `pandas` have to display the data types of the columns in the specified DataFrame.
#  
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# The `dtypes` property that DataFrames have can help.
# 
# </details>

# **Question:** What do you notice about the data types of the columns in the dataset?
# 

# only year founded has a dtype of integer rest all have dtype of object.

# **Question:** How would you sort this dataset in order to get insights about when the companies were founded? Then, how would you arrange the data from companies that were founded the earliest to companies that were founded the latest?
# 

# i'll use sort method on year founded column and set ascending to TRUE

# ### Sort the data
# 
# In this section, you will continue your exploratory data analysis by structuring the data. This is an important step in EDA, as it allows you to glean valuable and interesting insights about the data afterwards.
# 
# To begin, sort the data so that you can get insights about when the companies were founded. Consider whether it would make sense to sort in ascending or descending order based on what you would like to find.

# In[10]:


# Sort `companies` and display the first 10 rows of the resulting DataFrame.

### YOUR CODE HERE ###
df = companies.sort_values('Year Founded')

df.head(10)


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to [the content about exploratory data analysis in Python](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/lecture/kfl9b/find-stories-using-the-six-exploratory-data-analysis-practices).
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Use the function in `pandas` that allows you to sort a DataFrame along a specific column.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Use the `sort_values()` function, specifying the `by` parameter as the name of the column that you want to sort by and the `ascending` parameter as needed. Note that by default, `ascending` is set to `True`. If you want to sort in descending order, specify the `ascending` parameter as `False`.
# 
# </details>

# **Question:** What do you observe from the sorting that you performed?
# 

# the oldest comapny was founded in year 1919 and after that another company which became unicorn came in 1979 after 1990 almost every year we can see a unicorn company in that year

# **Question:** Which library would you use to get the count of each distinct value in the `Year Founded` column? 
# 

# Pandas library

# ### Determine the number of companies founded each year
# 
# Find out how many companies in this dataset were founded each year. Make sure to display each unique `Year Founded` that occurs in the dataset, and for each year, a number that represents how many companies were founded then.

# In[11]:


# Display each unique year that occurs in the dataset
# along with the number of companies that were founded in each unique year.

### YOUR CODE HERE ###
df.value_counts('Year Founded')


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to [the content about exploratory data analysis in Python](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/lecture/kfl9b/find-stories-using-the-six-exploratory-data-analysis-practices).
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Use the function in `pandas` that allows you to get the count for each distinct value in a specific column.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Use the `value_counts()` function on the `Year Founded` column. 
# 
# </details>

# **Question:** What do you observe from the counts of the unique `Year Founded` values in the dataset?
# 

# Year 2015 had the most unicorns followed by year 2016

# **Question:** What kind of graph represents the counts of samples based on a particular feature?
# 

# [Write your response here. Double-click (or enter) to edit.]

# Plot a histogram of the `Year Founded` feature.

# In[12]:


# Plot a histogram of the Year Founded feature.
### YOUR CODE HERE ###

sns.histplot(data=companies, x='Year Founded')
plt.title('Year Founded histogram');


# **Question:** If you want to compare when one company joined unicorn status to when another company joined, how would you transform the `Date Joined` column to gain that insight? To answer this question, notice the data types.
# 

# i will first convert the data joined column into standard format using the date and time format and then calculate the difference

# ### Convert the `Date Joined` column to datetime
# 
# Convert the `Date Joined` column to datetime. This will split each value into year, month, and date components, allowing you to later gain insights about when a company gained unicorn status with respect to each component.

# In[13]:


# Convert the `Date Joined` column to datetime.
# Update the column with the converted values.

### YOUR CODE HERE ###
df['Date Joined'] = pd.to_datetime(df['Date Joined'])



# Display the data types of the columns in `companies`
# to confirm that the update actually took place.

### YOUR CODE HERE ###
df.dtypes


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to [the content about datetime transformations in Python](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/supplement/ZcM4z/reference-guide-datetime-manipulation).
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Use the function in `pandas` that allows you to convert an object to datetime format.
# 
# Use the property that DataFrames have that can be used to display the data types of the columns.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Use the `to_datetime()` function on the `Date Joined` column.
# 
# Make sure to update the column by reassigning to the result of the function call mentioned previously.
# 
# Use the `dtypes` property to get the data types of the columns in `companies`.
# 
# </details>

# **Question:** How would you obtain the names of the months when companies gained unicorn status?
# 

# i can use inbuilt functions dt.month_name() to do this

# ### Create a `Month Joined` column
# 
# Obtain the names of the months when companies gained unicorn status, and use the result to create a `Month Joined` column. 

# In[14]:


# Obtain the names of the months when companies gained unicorn status.
# Use the result to create a `Month Joined` column.

### YOUR CODE HERE ###
df['Month Joined'] = df['Date Joined'].dt.month_name()




# Display the first few rows of `companies`
# to confirm that the new column did get added.

### YOUR CODE HERE ###
df.head()


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to [the content about extracting components from datetime objects in Python](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/lecture/Vh13u/use-structuring-methods-to-establish-order-in-your-dataset).
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Use the function in the `pandas` library that contains datetime strings in order to extract the month names.
# 
# Use the function in the `pandas` library that allows you to display the first few rows of a DataFrame.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Use the `dt.month_name()` function on the `Date Joined` column.
# 
# Use a pair of square brackets to create a new column. Make sure to specify the name of the new column inside the brackets and assign the column to the result of calling the function mentioned previously.
# 
# Use the `head()` function to display the first few rows of a DataFrame.
# 
# </details>

# **Question:** Using the 'Date Joined' column, how would you determine how many years it took for companies to reach unicorn status?
# 

# by finding the difference with year founded 

# ### Create a `Years To Join` column
# 
# Determine how many years it took for companies to reach unicorn status, and use the result to create a `Years To Join` column. Adding this to the dataset can help you answer questions you may have about this aspect of the companies.

# In[15]:


# Determine how many years it took for companies to reach unicorn status.
# Use the result to create a `Years To Join` column.

### YOUR CODE HERE ###
df['Year Unicorn'] = df['Date Joined'].dt.year

df['Years To Join'] = df['Year Unicorn'] - df['Year Founded']


# Display the first few rows of `companies`
# to confirm that the new column did get added.
### YOUR CODE HERE ###
df.head()


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to [the content about extracting components from datetime objects in Python](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/lecture/Vh13u/use-structuring-methods-to-establish-order-in-your-dataset).
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Use the property in the `pandas` library that contains datetime strings in order to extract the year components.
# 
# Use the function in the `pandas` library that allows you to display the first few rows of a DataFrame.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Use the `dt.year` property on the `Date Joined` column to obtain the years that companies became unicorns.
# 
# Obtain the arithmetic difference elementwise between two series in `pandas` by using the subtraction operator.  
# 
# Use a pair of square brackets to create a new column. Make sure to specify the name of the new column inside the brackets and assign the column to the result of calling the function mentioned previously.
# 
# Use the `head()` function can to display the first few rows of a DataFrame.
# 
# </details>

# **Question:** Which year would you like to gain more insight on with respect when companies attained unicorn status, and why?
# 

# i would choose year 2021 as it had the most unicorn companies

# ### Gain more insight on a specific year
# 
# To gain more insight on the year of that interests you, filter the dataset by that year and save the resulting subset into a new variable. 

# In[16]:


# Filter dataset by a year of your interest (in terms of when companies reached unicorn status).
# Save the resulting subset in a new variable. 

### YOUR CODE HERE ###

df.value_counts('Year Unicorn')

df_2021 = df[df['Year Unicorn'] == 2021]

# Display the first few rows of the subset to confirm that it was created.

### YOUR CODE HERE ###
df_2021.head()


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to [the content about structuring data in Python](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/lecture/Vh13u/use-structuring-methods-to-establish-order-in-your-dataset).
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Use the property in the `pandas` library that contains datetime strings in order to extract the year components.
# 
# Use square brackets to filter a DataFrame in order get a subset of the data. Make sure to specify an appropriate condition inside those brackets. The condition should convey which year you want to filter by. The rows that meet the condition are the rows that will be selected.
# 
# Use the function in the `pandas` library that allows you to display the first few rows of a DataFrame.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Use the `dt.year` property on the `Date Joined` column to obtain the years that companies became unicorns.
# 
# Make sure to create a new variable and assign it to the subset. 
# 
# Use the `head()` function to display the first few rows of a DataFrame.
# 
# </details>

# **Question:** Using a time interval, how could you observe trends in the companies that became unicorns in one year?
# 

# Using time interval i can see how many years it took for a company to become a unicorn.

# ### Observe trends over time
# 
# Implement the structuring approach that you have identified to observe trends over time in the companies that became unicorns for the year that interests you.

# In[17]:


# After identifying the time interval that interests you, proceed with the following:
# Step 1. Take the subset that you defined for the year of interest. 
#         Insert a column that contains the time interval that each data point belongs to, as needed.
# Step 2. Group by the time interval.
#         Aggregate by counting companies that joined per interval of that year.
#         Save the resulting DataFrame in a new variable.


# After identifying the time interval that interests you, proceed with the following:
# Step 1. Take the subset that you defined for the year of interest. 
#         Insert a column that contains the time interval that each data point belongs to, as needed.
# Step 2. Group by the time interval.
#         Aggregate by counting companies that joined per interval of that year.
#         Save the resulting DataFrame in a new variable.

### YOUR CODE HERE ###

# Insert a `Week Joined` column into `companies_2021.`
df_2021.insert(3, "Week Joined", df_2021["Date Joined"].dt.strftime('%Y-W%V'), True)

# Group `companies_2021` by `Week Joined`. 
# Aggregate by counting companies that joined per week of 2021.
# Save the resulting DataFrame in a new variable.
companies_by_week_2021 = df_2021.groupby(by="Week Joined")["Company"].count().reset_index().rename(columns={"Company":"Company Count"})

# Display the first few rows of the new DataFrame to confirm that it was created.

### YOUR CODE HERE ###

companies_by_week_2021.head()


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to [the content about structuring data in Python](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/lecture/Vh13u/use-structuring-methods-to-establish-order-in-your-dataset).
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# To obtain the data in a specific periodic datetime format, call a function in the `pandas` library on a series that contains datetime strings.   
# 
# Keep in mind that currently, the `Valuation` column is of data type `object` and contains `$` and `B` to indicate that each amount is in billions of dollars.
# 
# Call functions in the `pandas` library to achieve the following tasks:
#   - Apply a function to each value in the series.
#   - Cast each value in the series to a specified data type.
# 
# Use a pair of square brackets to access a particular column from the result of grouping a DataFrame. 
# 
# Use these functions in the `pandas` library to achieve the following tasks:
# - Concatenate two DataFrames together
# - Drop columns that you do not need from a DataFrame
# - Group a DataFrame by a specific column
# - Compute the average value for each group
# - Reset the index so that the column that you grouped on also appears as a column after the grouping (instead of remaining an index) 
# - Rename columns in a DataFrame
# - Display the first few rows of a DataFrame
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Use `dt.strftime('%Y-W%V')` on the `Date Joined` column to obtain the weeks that companies became unicorns.
# 
# Use these functions in `pandas` to acheive the following tasks:
# - `groupby()` to group a DataFrame by a specific column
# - `count()` to count the number of rows that belong to each group
# - `reset_index()` to reset the index so that the column that you grouped on also appears as a column after the grouping (instead of remaining an index) 
# - `rename()` to rename the columns in a DataFrame
# - `head()` to display the first few rows of a DataFrame
# 
# </details>

# **Question:** How would you structure the data to observe trends in the average valuation of companies from 2020 to 2021?  

# [Write your response here. Double-click (or enter) to edit.]

# ### Compare trends over time
# 
# Implement the structuring approach that you have identified in order to compare trends over time in the average valuation of companies that became unicorns in the year you selected above and in another year of your choice. Keep in mind the data type of the `Valuation` column and what the values in that column contain currently.

# In[18]:


# After identifying the additional year and time interval of interest, proceed with the following:
# Step 1. Filter by the additional year to create a subset that consists of companies that joined in that year.
# Step 2. Concatenate that new subset with the subset that you defined previously.
# Step 3. As needed, add a column that contains the time interval that each data point belongs to, 
#         in the concatenated DataFrame.
# Step 4. Transform the `Valuation` column as needed.
# Step 5. Group by the time interval.
#         Aggregate by computing average valuation of companies that joined per interval of the corresponding year.
#         Save the resulting DataFrame in a new variable.

### YOUR CODE HERE ###
companies["Date Joined"] = pd.to_datetime(companies["Date Joined"], errors='coerce')

# Filter by the additional year to create a subset that consists of companies that joined in that year.
companies_2020 = companies[companies["Date Joined"].dt.year == 2020]

# Concatenate the new subset with the subset that you defined previously.
companies_2020_2021 = pd.concat([companies_2020, df_2021.drop(columns="Week Joined")])

# Add `Quarter Joined` column to `companies_2021`.

companies_2020_2021["Quarter Joined"] = companies_2020_2021["Date Joined"].dt.to_period('Q').dt.strftime('%Y-Q%q')

# Convert the `Valuation` column to numeric by removing `$` and `B` and casting each value to data type `float`.
companies_2020_2021["Valuation"] =  companies_2020_2021["Valuation"].str.strip("$B").astype(float)

# Group `companies_2020_2021` by `Quarter Joined`, 
# Aggregate by computing average `Funding` of companies that joined per quarter of each year.
# Save the resulting DataFrame in a new variable.
companies_by_quarter_2020_2021 = companies_2020_2021.groupby(by="Quarter Joined")["Valuation"].mean().reset_index().rename(columns={"Valuation":"Average Valuation"})

# Display the first few rows of the new DataFrame to confirm that it was created.

### YOUR CODE HERE ###

companies_by_quarter_2020_2021.head()


# 
# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to [the content about manipulating data in Python](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/lecture/0GjvK/date-string-manipulations-with-python).
# 
# </details>
# 

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# To obtain the data in a specific periodic datetime format, call a function in the `pandas` library on a series that contains datetime strings.   
# 
# Keep in mind that currently, the `Valuation` column is of data type `object` and contains `$` and `B` to indicate that each amount is in billions of dollars.
# 
# Call functions in the `pandas` library on a series to acheive the following tasks:
#   - Apply a function to each value in the series.
#   - Cast each value in the series to a specified data type.
# 
# Use a pair of square brackets to access a particular column from the result of grouping a DataFrame. 
# 
# These functions in the `pandas` library can help achieve the following tasks:
# - Concatenate two DataFrames together
# - Drop columns that you do not need from a DataFrame
# - Group a DataFrame by a specific column
# - Compute the average value for each group
# - Reset the index so that the column that you grouped on also appears as a column after the grouping (instead of remaining an index) 
# - Rename columns in a DataFrame
# - Display the first few rows of a DataFrame
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Use `.dt.to_period('Q').dt.strftime('%Y-Q%q')` on the `Date Joined` column to obtain the quarters during which companies became unicorns.
# 
# Convert the `Valuation` column to numeric by removing `$` and `B` and casting each value to data type `float`.
# 
# Use the following functions in `pandas` to acheive the following tasks:
# - `concat` to concatenate two DataFrames together (note: this function takes in a list of DataFrames and returns a DataFrame that contains all rows from both inputs)
# - `drop()` to drop columns that you do not need from a DataFrame
# - `groupby()` to group a DataFrame by a specific column
# - `mean()` to compute the average value for each group
# - `reset_index()` to reset the index so that the column that you grouped on also appears as a column after the grouping (instead of remaining an index) 
# - `rename()` to rename the columns in a DataFrame
# - `head()` to display the first few rows of a DataFrame
# 
# </details>

# ## Step 3: Time-to-unicorn visualization
# 
# ### Visualize the time it took companies to become unicorns
# 
# Using the `companies` dataset, create a box plot to visualize the distribution of how long it took companies to become unicorns, with respect to the month they joined. 

# In[19]:


# Define a list that contains months in chronological order.

### YOUR CODE HERE ###
months = ['january' , 'february' , 'march' , 'april' , 'may' , 'june' , 'july' , 'august' , 'september' , 'october',
         'november','december']

# Print out the list to confirm it is correct.
months
### YOUR CODE HERE ###


            


# In[20]:




# Convert 'Date Joined' to datetime
df['Date Joined'] = pd.to_datetime(df['Date Joined'], errors='coerce')

# Create 'Month Joined' column
df['Month Joined'] = df['Date Joined'].dt.strftime('%B')

# Define correct order
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']

# Plot
sns.boxplot(x=df['Month Joined'], 
            y=df['Years To Join'], 
            order=months, 
            showfliers=False)

plt.title('Distribution of years to become unicorn with respect to month joined')
plt.xticks(rotation=45, ha='right')
plt.show()


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to [the content about creating a box plot](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/lecture/Pf6KW/eda-structuring-with-python).
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Use the function in the `seaborn` library that allows you to create a box plot.
# 
# Use the functions in the `matplotlib.pyplot` module that allow you to acheive the following tasks:
# - set the title of a plot
# - rotate labels on the x-axis of a plot
# - display a plot
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Use the `boxplot()` function from `seaborn` to create a box plot, passing in the parameters `x`, `y`, `order`, and `showfliers`. To keep outliers from appearing on the box plot, set `showfliers` to `False`.
# 
# Use following functions to achieve the following tasks:
# - `plt.title()` to set the title of a plot
# - `plt.xticks()` to rotate labels on the x-axis of a plot
# - pass in the parameters `rotation=45, horizontalalignment='right'`to rotate the labels by 45 degrees and align the labels to the right
# - `plt.show()` to display a plot
# 
# </details>

# **Question:** In the preceding box plot, what do you observe about the median value for `Years To Join` for each month?
# 

# In the preceding box plot, the median value for Years To Join is different for each month. Also, the median Years To Join is lower for the months of September and October. This could indicate that companies that reached unicorn status in early fall took less time to reach $1 billion valuation. This is because the number of companies is relatively close/consistent for each month. If that were not the case, it would be misleading to compare the median values from the box plots between months.

# ## Step 4: Results and evaluation
# 

# ### Visualize the time it took companies to reach unicorn status
# 
# In this section, you will evaluate the result of structuring the data, making observations, and gaining further insights about the data. 
# 
# Using the `companies` dataset, create a bar plot to visualize the average number of years it took companies to reach unicorn status with respect to when they were founded. 

# In[21]:


# Set the size of the plot.

### YOUR CODE HERE ###

plt.figure(figsize=(10,6))

# Create bar plot to visualize the average number of years it took companies to reach unicorn status 
# with respect to when they were founded.
# Plot data from the `companies` DataFrame.

### YOUR CODE HERE ###

sns.barplot(x = df['Year Founded'], y= df['Years To Join'])


# Set title

### YOUR CODE HERE ###

plt.title("Bar plot of years to join with respect to year founded")


# Set x-axis label

### YOUR CODE HERE ###

plt.xlabel("Year founded")


# Set y-axis label

### YOUR CODE HERE ###

plt.ylabel("Years to join unicorn status")


# Rotate the labels on the x-axis as a way to avoid overlap in the positions of the text.  

### YOUR CODE HERE ###

plt.xticks(rotation=45, horizontalalignment='right')

# Display the plot.

### YOUR CODE HERE ###

plt.show()


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to [the content about creating a bar plot](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/lecture/0GjvK/date-string-manipulations-with-python).
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Use the function in the `seaborn` library that allows you to create a bar plot where the height of each bar is the average value for the corresponding category, by default.
# 
# Use the functions in the `matplotlib.pyplot` module that allow you to set the size, title, x-axis label, and y-axis label of plots. In that module, there are also functions for rotating the labels on the x-axis and displaying the plot. 
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Use the `barplot()` function from `seaborn`, passing in the parameters `x`, `y`, and `ci`. To keep confidence interval lines from appearing on the bar plot,  set `ci` to `False`.
# 
# Use `plt.figure()`, passing in the `figsize` parameter to set the size of a plot.
# 
# Use `plt.title()`, `plt.xlabel()`, `plt.ylabel()` to set the title, x-axis label, and y-axis label, respectively. 
# 
# Use `plt.xticks()` to rotate labels on the x-axis of a plot. Paass in the parameters `rotation=45, horizontalalignment='right'` to rotate the labels by 45 degrees and align the labels to the right.
# 
# Use `plt.show()` to display a plot.
# 
# </details>

# **Question:** What trends do you notice in the data? Specifically, consider companies that were founded later on. How long did it take those companies to reach unicorn status?
# 

# With going forward in time the no. of years it takes to reach unicorn status is definately coming down

# ### Visualize the number of companies that joined per interval 
# 
# Using the subset of companies joined in the year of interest, grouped by the time interval of your choice, create a bar plot to visualize the number of companies that joined per interval for that year. 

# In[22]:


# Set the size of the plot.

### YOUR CODE HERE ###

plt.figure(figsize = (20, 5))

# Create bar plot to visualize number of companies that joined per interval for the year of interest.

### YOUR CODE HERE ###

plt.bar(x=companies_by_week_2021['Week Joined'],height=companies_by_week_2021['Company Count'])
plt.plot()

# Set the x-axis label.

### YOUR CODE HERE ###

plt.xlabel("Week number")

# Set the y-axis label.

### YOUR CODE HERE ###

plt.ylabel("Number of companies")

# Set the title.

### YOUR CODE HERE ###

plt.title("Number of companies that became unicorns per week in 2021")

# Rotate the labels on the x-axis as a way to avoid overlap in the positions of the text.  

### YOUR CODE HERE ###

plt.xticks(rotation = 45, horizontalalignment='right', fontsize=8)

# Display the plot.

### YOUR CODE HERE ###

plt.show()


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to [the content about creating a bar plot](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/lecture/0GjvK/date-string-manipulations-with-python).
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Use the function in the `seaborn` library that allows you to create a bar plot where the height of each bar is the average value for the corresponding category, by default.
# 
# Use the functions in the `matplotlib.pyplot` module that allow you to set the size, title, x-axis label, and y-axis label of plots. In that module, there are also functions for rotating the labels on the x-axis and displaying the plot. 
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Use the `barplot()` function from `seaborn`, passing in the parameters `x`, `y`, and `ci`. To keep confidence interval lines from appearing on the bar plot,  set `ci` to `False`.
# 
# Use `plt.figure()`, passing in the `figsize` parameter to set the size of a plot.
# 
# Use `plt.title()`, `plt.xlabel()`, `plt.ylabel()` to set the title, x-axis label, and y-axis label, respectively. 
# 
# Use `plt.xticks()` to rotate labels on the x-axis of a plot. Paass in the parameters `rotation=45, horizontalalignment='right'` to rotate the labels by 45 degrees and align the labels to the right.
# 
# Use `plt.show()` to display a plot.
# 
# </details>

# **Question:** What do you observe from the bar plot of the number of companies that joined per interval for the year of 2021? When did the highest number of companies reach $1 billion valuation?
# 
#   

# 2021 week 37

# ### Visualize the average valuation over the quarters
# 
# Using the subset of companies that joined in the years of interest, create a grouped bar plot to visualize the average valuation over the quarters, with two bars for each time interval. There will be two bars for each time interval. This allows you to compare quarterly values between the two years.

# In[24]:


# Using slicing, extract the year component and the time interval that you specified, 
# and save them by adding two new columns into the subset. 

### YOUR CODE HERE ###

companies_by_quarter_2020_2021['Quarter Number'] = companies_by_quarter_2020_2021['Quarter Joined'].str[-2:]
companies_by_quarter_2020_2021['Year Joined'] = companies_by_quarter_2020_2021['Quarter Joined'].str[:4]

# Set the size of the plot.

### YOUR CODE HERE ###

plt.figure(figsize = (10, 5))

# Create a grouped bar plot.

### YOUR CODE HERE ###

sns.barplot(x=companies_by_quarter_2020_2021['Quarter Number'],
            y=companies_by_quarter_2020_2021['Average Valuation'],
            hue=companies_by_quarter_2020_2021['Year Joined'])
plt.plot()

# Set the x-axis label.

### YOUR CODE HERE ###

plt.xlabel("Quarter number")

# Set the y-axis label.

### YOUR CODE HERE ###

plt.ylabel("Average valuation (billions of dollars)")

# Set the title.

### YOUR CODE HERE ###

plt.title("Average valuation of companies that became unicorns per quarter in 2020 vs. 2021")

# Display the plot.

### YOUR CODE HERE ###

plt.show()


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Refer to [the content about creating a grouped bar plot](https://www.coursera.org/learn/go-beyond-the-numbers-translate-data-into-insight/lecture/Pf6KW/eda-structuring-with-python).
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Use the function in the `seaborn` library that allows you to create a grouped bar plot, specifying the category and height for each bar, as well as the hue.
# 
# Use the functions in the `matplotlib.pyplot` module that allow you to set the size, title, x-axis label, and y-axis label of plots. In that module, there is also a function for displaying the plot. 
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Use the `plt.bar()` to create the bar plot, passing in the parameters `x`, `y`, and `hue`. For the task at hand, set `hue` to the column that contains year joined. 
# 
# Use `plt.figure()`, passing in the `figsize` parameter to set the size of a plot.
# 
# Use `plt.title()`, `plt.xlabel()`, `plt.ylabel()` to set the title, x-axis label, and y-axis label, respectively. 
# 
# Use `plt.show()` to display a plot.
# 
# </details>

# **Question:** What do you observe from the preceding grouped bar plot?
# 
#   

# year 2020 had most unicorn companies quarterly as compared to year 2021
# year 2021 quarter 1 had highest average valuation compared to the later period of that year

# **Question:** Is there any bias in the data that could potentially inform your analysis?
# 

# maybe location can be included which cities are seen 

# **Question:** What potential next steps could you take with your EDA?

# analyze data based on cities and same industry

# **Question:** Are there any unanswered questions you have about the data? If yes, what are they?
# 

# How many rounds of funding did each company require and when did this funding take place?
# Have any of these unicorn companies acquired other companies along the way? If so, which companies acquired other companies, which companies did they acquire, and when did the acquisitions take place?

# ## Considerations

# **What are some key takeaways that you learned from this lab?**

# i learned strucuting data is crucial also the datetime format is very necessary

# **What findings would you share with others?**

# we had 1074 companies data
# year 2015 had most succesfull unicorn 
# September and October month had taken on average less time to reach unicorn status
# 

# **What recommendations would you share with stakeholders based on these findings?**

# According to data analysis that was conducted on a dataset of 1074 unicorn companies, companies that joined in the months of September and October tended to take less time to become unicorns.
# Another finding was that many of the unicorn companies that were founded in 2021 were founded in the United States and belong to "Fintech", "E-commerce & direct-to-consumer", and "Internet software & services" industries. So if the stakeholders want to invest in companies founded in 2021, it would be a good idea to consider companies that belong to these industries, as they may be strong candidates for becoming unicorns.
# It was also discovered that the average valuation of companies that joined in 2021 is highest in the first quarter of the year, and the average valuation of companies that joined in 2020 is the third quarter of the year. When considering companies that newly join in the future, it would be worth closely looking at companies that join in the first and third quarters of the year.
# The data can be analyzed further to gather more insights that are specific to the interests of the investing firm and the stakeholders.

# **References**
# 
# Bhat, M.A. (2022, March).[*Unicorn Companies*](https://www.kaggle.com/datasets/mysarahmadbhat/unicorn-companies). 
# 
# 

# **Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged.

# In[ ]:



