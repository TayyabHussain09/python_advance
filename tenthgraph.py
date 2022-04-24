# Importing seaborn library in program  
import seaborn as sns  
# Importing mataplotlib library to show graph in output  
import matplotlib.pyplot as plt  
# Setting style with set() function  
sns.set(style="dark")  
# Using dataset() function to declare data type  
FMR = sns.load_dataset("fmri")  
# Plotting various responses for different\  
# Regions and events  
sns.lineplot(x="timepoint",  
             y="signal",  
             hue="region",  
             style="event",  
             data=FMR) # using lineplot() function to create line plot  
plt.show() # using show() function  



#this was the line plot by javapoint website