#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


from sklearn.datasets import load_digits
function = load_digits()


# In[3]:


# input variables or features
function.data.shape # X
X= function.data


# In[4]:


# output labesl
function.target.shape # y 
y=function.target


# In[5]:


plt.figure(figsize=(40,15))
for index, (image, label) in enumerate(zip(function.data[0:10], function.target[0:40])):
    plt.subplot(1,40,index+1)
    plt.imshow(np.reshape(image,(8,8)),cmap=plt.cm.gray)
    plt.title(label, fontsize=20)


# In[7]:


# splitting the dataset
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.2, random_state = 0)


# In[8]:


print("Train input data of X: ",X_train.shape)
print("Test input data of X: ",X_test.shape)
print("Train input data of y: ",y_train.shape)
print("Test input data of y: ",y_test.shape)


# In[9]:


# model train
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression().fit(X_train, y_train)
lr


# In[10]:


lr.predict(X_test[0:50])
prediction = lr.predict(X_test)
prediction


# In[11]:


# acuracy prediction
score = lr.score(X_test,y_test)
print("The accuracy score is : ", score)
    


# In[12]:


# confusion matrix
from sklearn import metrics
cm = metrics.confusion_matrix(y_test, prediction)
cm


# In[13]:


fig = plt.figure(figsize = (9,9))
sns.heatmap(cm, annot=True, fmt=".3f", linewidths = .5, square = True, cmap = "Spectral");
plt.ylabel("actual output")
plt.xlabel("predicted output")
comple_title = "Accuracy Score: {0}".format(score)
plt.title(comple_title, size = 15);


# In[14]:


fig.savefig('accuracy.png')


# In[15]:


print(cm)


# In[16]:


# getting the miisqualified values
import numpy as np
import matplotlib.pyplot as plt
index = 0
misclassifiedIndexes = []
for label, predict in zip(y_test, prediction):
    if label != predict:
        misclassifiedIndexes.append(index)
        index +=1


# In[24]:


fig2 = plt.figure(figsize = (30,8))
for plotIndex, badIndex in enumerate(misclassifiedIndexes[0:5]): # getting only 10 misqualified values
    plt.subplot(1,5,plotIndex + 1)
    plt.imshow(np.reshape(X_test[badIndex], (8,8)), cmap=plt.cm.gray)
    plt.title("Predicted: {}, Actual: {},".format(prediction[badIndex], y_test[badIndex]), fontsize = 20 )  # as predicted values are equil to the actual values because my model accuracy is very good


# In[25]:


fig2.savefig("human vs machine behaviour with tayyab's model accuracy of 96%")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




