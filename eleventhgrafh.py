# importing numpy as np library module  
import numpy as np  
# Importing seaborn library in program  
import seaborn as sns  
# Importing mataplotlib library to show graph in output  
import matplotlib.pyplot as plt  
# Selecting style for boxplot with set() function  
sns.set(style="white")  
# Generate a random univariate type distribution  
ru = np.random.RandomState(10)  
d = ru.normal(size=100)  
# Plotting a simple histogram with kdeplot variation  
sns.histplot(d, kde=True, color="m")  
plot = sns.histplot(d, kde=True, color="m")  
print(plot)  
plt.show() # using show() function  


#this was a dist plot by javapoint website