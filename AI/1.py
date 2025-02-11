#%%
import cv2
from matplotlib import pyplot as plt

#%%
image =cv2.imread('ehsanrezaei.jpg',0)
model = cv2.CascadeClassifier('model.xml')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
#%%
face = model.detectMultiScale(image,1.1,4)
x=face[0][0]
y=face[0][1]
w=face[0][2]
h=face[0][3]
image = cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
#%%
plt.imshow(image)
# %%
