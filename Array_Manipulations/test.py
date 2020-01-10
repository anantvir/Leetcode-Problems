from PIL import Image
import random
import numpy
import math
import operator
import os
import sys

#image_path = os.path.join(os.getcwd(), sys.argv[1])
#image_name = os.path.splitext(os.path.basename(sys.argv[1]))[0]

'''Read in the image as pixel values and get its size'''
image=Image.open('D:\Courses\Fall 19\ELEG 815 Statistical Learning\HW4\Homework4Files\Image.png','r')
image = image.resize((200,200))
image = image.convert('RGB')
width, height=image.size
imagePixels=list(image.getdata())
print(imagePixels[0])
K = 5

print("Creating image by K = {}".format(K))
'''Based on the selected K values, randomly pick up K points from the image to initialize the centers'''
initial_centers = set()
for x in range(K):
    initial_centers.add(imagePixels[random.randint(0,len(imagePixels)-1)])

'''Run the K-means algorithm'''
old_centers = set()
new_centers = initial_centers
# check for convergence
while old_centers != new_centers:
    old_centers = new_centers
    clusterDict = dict([(key, []) for key in new_centers])
    # for each pixel in the picture, calculate its distance to the centers and assign it to the corresponding center(from which its distance is the nearest) to form clusters
    for eachPixelTupleIndex in range(len(imagePixels)):
        distanceDict={}
        for eachCenter in new_centers:
            pixelValues=imagePixels[eachPixelTupleIndex]
            distanceList= numpy.subtract(pixelValues,eachCenter)
            distance=0
            for eachNumber in distanceList:
                distance+=eachNumber**2
            distance= math.sqrt(distance)
            distanceDict[eachCenter]=distance
        
        bestCenter=min(distanceDict.items(), key=operator.itemgetter(1))[0]
        clusterDict[bestCenter].append(eachPixelTupleIndex)

    # calculate new centers by sample means of the pixel R,G,B values
    new_centers = set()
    for center in clusterDict:
        new_center_temp = (0,0,0)
        for pixelIndex in clusterDict[center]:
            new_center_temp = tuple(map(operator.add, new_center_temp, imagePixels[pixelIndex]))
        new_center = tuple(map(lambda x: int(x/len(clusterDict[center])), new_center_temp))
        new_centers.add(new_center)

'''Recreate and output the image'''
newIm = Image.new("RGB", (width, height))
pix = newIm.load()
for i in range(height):
    for j in range(width):
        for center in clusterDict:
            if ((i - 1) * width + j) in clusterDict[center]:
                pix[j,i] = center
newIm.save('D:\\Courses\\Fall 19\\ELEG 815 Statistical Learning\\HW4\\Homework4Files\\newImage5.png', "PNG")

print("All finished!")