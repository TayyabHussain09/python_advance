#steps involved in data visualization
#import libraries is step 1
import seaborn as sns
import matplotlib.pyplot as plt
# setting a theme is step two
sns.set_theme(style="ticks", color_codes=True)
#import data set is third step you can also import your own data
kashti = sns.load_dataset("titanic")
print(kashti)
#plot basic graph is fourth step
p = sns.countplot(x="sex", data=kashti,)
plt.show()
#plot basic graph with two variable (count plot) is fifth step
p = sns.countplot(x="sex", data=kashti, hue="class")
plt.show()
#plot basic graph with two variable (count plot) with title
# is sixth step
p = sns.countplot(x="sex", data=kashti, hue="class")
p.set_title("my personal titanic plot")
plt.show()
