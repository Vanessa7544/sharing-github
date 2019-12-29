#!/usr/bin/env python
# coding: utf-8

# In[23]:


# import libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


# In[24]:


# load the dataset
data = pd.read_csv(r"C:\Users\vanes\Downloads\naep.csv")


# In[25]:


data


# ![Naep-50.png](attachment:Naep-50.png)

# In[26]:


# load the dataset
data = pd.read_csv(r"C:\Users\vanes\Downloads\naep-50.csv")


# In[27]:


data


# ![3.jpg](attachment:3.jpg)

# <font size=2> Here shows the state is by order
# </font> 

# ![Count.jpg](attachment:Count.jpg)

# In[ ]:


counts = [row['count'] for row in rows]

print ('The total number of math 4 is' = (counts))


# <font size=2> Here shows the total numberof math4 which is 561
# </font> 

# ![Average.png](attachment:Average.png)

# In[ ]:


average = [row['Average'] for row in rows] 

print ('The Average number of math 4 is' = (average))


# <font size=2> Here shows the average numberof math4 which is 234.80
# </font> 

# ![Max.png](attachment:Max.png)

# In[ ]:


max = [row['max'] for row in rows] 

print ('The max number of math 4 is' = (max))


# <font size=2> Here shows the highest score of math4 which is 253.421
# </font> 

# ![Min.png](attachment:Min.png)

# In[ ]:


min = [row['max'] for row in rows] 

print ('The max number of math 4 is' = (min))


# <font size=2> Here shows the lowest score of math4 which is 187.135</font> 
# 

# In[6]:


# Import the SQL ALchemy engine
from sqlalchemy import create_engine


# ![difference.png](attachment:difference.png)

# In[ ]:


difference = [row['difference'] for row in rows] 

print ('The difference number of math 4 is' = (difference))


# <font size=2> Here shows the lowest score of math4 which is 66.286</font> 

# ![5.png](attachment:5.png)

# In[ ]:


bottom_10_states = [row['bottom_10_states'] for row in rows] 

print ('The bottom_10_states are' = (bottom_10_states))


# <font size=2> The bottom_10_states are 'COLORADO','COLUMBIA','ARIZONA','CALIFORNIA','CONNECTICUT','DELAWARE','ALABAMA','ALASKA','ARKANSAS','FLORIDA'</font> 

# ![6.jpg](attachment:6.jpg)

# <font size=2> Here shows the average avg_math_4_score rounded to the nearest 2 decimal places over all states in the year 2000 which is 238.92.</font> 

# ![7.png](attachment:7.png)

# In[ ]:


below_average_states_y2000 = [row['below_average_states_y2000'] for row in rows] 

print ('below_average_states_y2000' = (below_average_states_y2000))


# <font size=2> Here shows below_average_states_y2000 that lists all states with an avg_math_4_score less than the average over all states in the year 2000.</font> 

# ![8.png](attachment:8.png)

# In[ ]:


scores_missing_y2000 = [row['scores_missing_y2000'] for row in rows] 

print ('scores_missing_y2000' = (scores_missing_y2000))


# <font size=2> Here shows below_average_states_y2000 that lists all states with an avg_math_4_score less than the average over all states in the year 2000. Total are 10 items in 2000.</font> 
