import matplotlib.pyplot as plt  
import seaborn as sns  
import pandas as pd  
#loading the dataset 'tips'  
df=pd.read_csv("tips.csv")  
#plotting the graph  
sns.countplot(y='sex',hue='smoker',data=df)  
plt.show()  


# two categorial thre horizontal grafh by javapoint