import matplotlib.pyplot as plt  
import seaborn as sns  
import pandas as pd  
#loading the dataset 'tips'  
df=pd.read_csv("/content/tips.csv")  
#plotting the graph  
sns.countplot(x='sex',hue='smoker',data=df)  
plt.show()   

# two categeriol countplot by javapoint