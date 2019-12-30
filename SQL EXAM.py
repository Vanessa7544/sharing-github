#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


# In[24]:


# Step1-load the dataset
data = pd.read_csv(r"C:\Users\vanes\Downloads\naep.csv")


# In[25]:


data


# In[168]:


# Step1-Write a query that allows you to inspect the schema of the naep table.
get_ipython().system('pip install sqlalchemy')
get_ipython().system('pip install psycopg2')
get_ipython().system('pip install psycopg2-binary')
postgres_user = 'dsbc_student'
postrgres_pw = '7*.8G9QH21'
postgres_host = '142.93.121.174'
postgres_port = '5432'
postgres_db = 'department_of_education'
from sqlalchemy import create_engine
engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(postgres_user, postrgres_pw, postgres_host, postgres_port, postgres_db ))
sql = '''
SELECT* 
FROM naep;
'''
stats = engine.execute(sql)
engine.dispose()
rows = stats.fetchall()
print(rows)


# In[163]:


# Step2-Write a query that returns the first 50 records of the naep table.
sql = '''
SELECT* FROM naep
LIMIT 50;
'''
stats = engine.execute(sql)
engine.dispose()
rows = stats.fetchall()
print(rows)


# In[164]:


# Step3-Write a query that returns summary statistics for avg_math_4_score by state.
# Make sure to sort the results alphabetically by state name.
sql = '''
SELECT *
FROM naep
ORDER  BY avg_math_4_score DESC ;  
'''
stats = engine.execute(sql)
engine.dispose()
rows = stats.fetchall()
print(rows)


# In[159]:


# Step 3
sql = '''
SELECT 
 ROUND (AVG(avg_math_4_score), 2 ) avg_math_4_score
FROM naep;  
'''
stats = engine.execute(sql)
engine.dispose()
rows = stats.fetchall()
print(rows)


# In[111]:


# Step 3
sql = '''
SELECT MAX(avg_math_4_score)
FROM naep;  
'''
stats = engine.execute(sql)
engine.dispose()
rows = stats.fetchall()
print(rows)


# In[112]:


# Step 3
sql = '''
SELECT MIN(avg_math_4_score)
FROM naep;  
'''
stats = engine.execute(sql)
engine.dispose()
rows = stats.fetchall()
print(rows)


# In[114]:


# Step4-Write a query that alters the previous query so that it returns only the summary statistics for 
# avg_math_4_score by state with differences in max and min values that are greater than 30.
sql = '''
SELECT MAX(avg_math_4_score)-MIN(avg_math_4_score)difference
FROM naep;  
'''
stats = engine.execute(sql)
engine.dispose()
rows = stats.fetchall()
print(rows)


# In[121]:


# Step5-Write a query that returns a field called bottom_10_states that lists the states in the bottom 10 for 
# avg_math_4_score in the year 2000.
sql = '''
SELECT *
FROM naep
ORDER BY avg_math_4_score > 187.135 
AND year > 2000
limit 10;
'''
stats = engine.execute(sql)
engine.dispose()
rows = stats.fetchall()
print(rows)


# In[143]:


# Step6-Write a query that calculates the average avg_math_4_score rounded to the nearest 2 decimal places 
# over all states in the year 2000.
sql = '''
SELECT 
ROUND (AVG(avg_math_4_score), 2 ) avg_math_4_score
FROM naep
where year > 2000;
'''
stats = engine.execute(sql)
engine.dispose()
rows = stats.fetchall()
print(rows)


# In[122]:


# Step7-Write a query that returns a field called below_average_states_y2000 that lists all states with an 
# avg_math_4_score less than the average over all states in the year 2000.
sql = '''
SELECT *
FROM naep
where avg_math_4_score < 238.92
AND year < 2000;
'''
stats = engine.execute(sql)
engine.dispose()
rows = stats.fetchall()
print(rows)


# In[123]:


# Step8-Write a query that returns a field called scores_missing_y2000 that lists any states with missing values 
# in the avg_math_4_score column of the naep data table for the year 2000.
sql = '''
SELECT *
FROM naep
where avg_math_4_score IS NULL
AND YEAR = 2000;
'''
stats = engine.execute(sql)
engine.dispose()
rows = stats.fetchall()
print(rows)


# In[161]:


#Step9-Write a query that returns for the year 2000 the state, avg_math_4_score, and total_expenditure from the naep table 
#left outer joined with the finance table, using id as the key and ordered by total_expenditure greatest to least. Be sure to round avg_math_4_score to the nearest 2 decimal places, and then filter out NULL avg_math_4_scores in order to see any correlation more clearly.
sql = '''
SELECT naep.state, ROUND(avg_math_4_score,2) AS avg_math_4_score, total_expenditure, naep.year
FROM naep LEFT OUTER JOIN finance 
ON naep.id = finance.id
WHERE naep.year = 2000 and avg_math_4_score is NOT NULL;
'''
stats = engine.execute(sql)
engine.dispose()
rows = stats.fetchall()
print(rows)

