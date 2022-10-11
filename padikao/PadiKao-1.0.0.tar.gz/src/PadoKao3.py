print ("""

from PIL import Image
from matplotlib import pyplot as plt
from mtcnn.mtcnn import MTCNN
import cv2
import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense
from tensorflow.keras.applications import imagenet_utils
from tensorflow.keras.preprocessing import image
import h5py
import random
import warnings
warnings.filterwarnings("ignore")






########################################################################################################################################################################
#10_Face_Recognition_Facenet_Siamese.ipynb

from tensorflow.keras.models import load_model
​
model = load_model('facenet_keras.h5')# load the model
​
print(model.inputs)
print(model.outputs)
#Dataset
# https://drive.google.com/file/d/1IuRDCbCDKES1d3VnXZGmX3NqRCcHqw7H/view?usp=sharing
​
#https://drive.google.com/drive/folders/1PffV5nGK3-yga3OkgIzKX38ZmOvo3Q_X?usp=sharing
#!pip install mtcnn
from PIL import Image
from matplotlib import pyplot as plt
from PIL import Image
from matplotlib import pyplot as plt
# load image from file
image = plt.imread('group_img.jpg')
plt.imshow(image)
from mtcnn.mtcnn import MTCNN
from mtcnn.mtcnn import MTCNN
detector = MTCNN()
# detect faces in the image
results = detector.detect_faces(image)
len(results)
results #hounding boxes for each face and position of eyes, nose and mouth
#extract only face regions
faces=[]
for i in range(len(results)):
    # extract the bounding box from the first face
    x1, y1, width, height = results[i]['box']
    # bug fix
    x1, y1 = abs(x1), abs(y1)
    x2, y2 = x1 + width, y1 + height
​
    # extract the face
    face = image[y1:y2, x1:x2]
​
    # resize pixels to the model size
    image1 = Image.fromarray(face)
    image1 = image1.resize((160, 160))
    face_array = np.array(image1)
    faces.append(face_array)
len(faces)
for i in faces:
    plt.imshow(i)
    plt.show()
results
detector = MTCNN()
​
from os import listdir
folder = 'Database_photo/'
i = 1
face_ref=[]
# enumerate files
for filename in listdir(folder):
​
    path = folder + filename
    image = plt.imread(path)
    #print(image.shape)
#     plt.imshow(image)
#     plt.show()
    results = detector.detect_faces(image)
    # extract the bounding box from the first face
    x1, y1, width, height = results[0]['box']
    x1, y1 = abs(x1), abs(y1)
    x2, y2 = x1 + width, y1 + height
    # extract the face
    face = image[y1:y2, x1:x2]
    # resize pixels to the model size
    image1 = Image.fromarray(face)
    image1 = image1.resize((160,160))
    face_array = np.array(image1)
    face_ref.append(face_array)
    #print(i, face_array.shape)
    # plot
    plt.subplot(2, 6, i)
    plt.axis('off')
    plt.imshow(face)
    i += 1
plt.show()
​
emb_ref=[]
for i in range(len(face_ref)):
    face_pn=face_ref[i].astype('float32')
    # standardize pixel values across channels (global)
    mean, std = face_pn.mean(), face_pn.std()
    face_pn = (face_pn - mean) / std
​
    face_pn = np.expand_dims(face_pn, axis=0)
​
    y_pn = model.predict(face_pn)
    # get embedding
    embedding_ref = y_pn[0]
    emb_ref.append(embedding_ref)
len(emb_ref)
i=1 #give the index of any player
plt.imshow(faces[i]) # Anchor/original face in the group image
face_anch=faces[i].astype('float32')
# standardize pixel values across channels (global)
mean, std = face_anch.mean(), face_anch.std()
face_anch = (face_anch - mean) / std
​
face_anch = np.expand_dims(face_anch, axis=0)
​
y_anch = model.predict(face_anch)
# get embedding
emb_anch = y_anch[0]
#Compare the embedding of anchor image with reference image
res1=[]
for i in range(len(emb_ref)):
    res1.append(np.sqrt(np.sum((emb_ref[i]-emb_anch)**2)))
res1
np.argmin(res1)
plt.imshow(face_ref[np.argmin(res1)])

########################################################################################################################################################################
#1_TensorFlow Basics_In_Class_Session1_Solution-1.ipynb
Deep Learning Session 1: In-Class 1
1. Creation of Tensors
2. Slicing of Tensors
3. Operations on Tensors
4. Activation Functions
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
# Import required Libraries 
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
1. Create a random tensor with 4 rows and 3 columns. Output random values should fit in a normal distribution
tensor1=tf.random.normal([4,3])
tensor1
2. Access the second row of the above matrix and print its value alone
row2=tensor1[1,:]
print(row2.numpy())
3. Assign the first value (first row, first column) and last value(last row, last column) to zero
tensor11=tf.Variable(tensor1)
tensor11[0,0].assign(0)
tensor11[3,2].assign(0)
4. Replace all the values of third row to zero
tensor11[2,:].assign([0,0,0])
5. Create two tensor constants and perform addition and multiplication
t1=tf.constant(3)
t2=tf.constant(4)
print(t1+t2)
print(t1*t2)
6. Create two tensors [3,2] and [4,6]. Compute the Euclidean distance distance between the two tensor points.
tv1=tf.Variable([3.,2])
tv2=tf.Variable([4.,6])
tf.sqrt(tf.reduce_sum(tf.math.square(tv1-tv2)))
7. Create 2 random matrices of size [3,3] and [3,3] with minimum value 1 and maximum value 10 and perform element wise multiplication and Matrix Multiplications
m1=tf.Variable(np.random.randint(1,11,[3,3]))
m2=tf.Variable(np.random.randint(1,11,[3,3]))
print(m1*m2)
print(m1@m2)
8. Compute the product of determinant of above two matrices
m1=tf.cast(m1,tf.float32)
d1=tf.linalg.det(m1)
m2=tf.cast(m2,tf.float32)
d2=tf.linalg.det(m2)
d1*d2
9. Create a float tensor and cast it into integer
t1=tf.Variable([2.,3,4])
print(t1.dtype)
t2=tf.cast(t1,tf.int8)
print(t2.dtype)
10. Plot the Sigmoidal activation function using the equation. keep the x value between -10 to 10
x=np.linspace(-10,10,50)
y=1/(1+np.exp(-x))
plt.plot(x,y)
11. Plot the Relu activation function using the equation. keep the x value between -10 to 10
x=np.linspace(-10,10,50)
y=np.zeros((1,len(x)))
y=y[0]
for i in range(len(x)):
    if x[i]<0:
        y[i]=0
    else:
        y[i]=x[i]
plt.plot(x,y)
12. Plot the Tanh activation function using the equation. keep the x value between -10 to 10
x=np.linspace(-10,10,50)
y=(np.exp(x)-np.exp(-x))/(np.exp(-x)+np.exp(x))
plt.plot(x,y)
13. Perform the following equation using tensors y = x^4+x^2+6, where x = [1,2,4,2,8,10]
x=tf.Variable([1,2,4,2,8,10])
tf.pow(x,4)+tf.pow(x,2)+6
14. Consider the regression data below:
inp=tf.constant([[18,1.5,1.5],[21,3,1.2],[29,7,2.5],[29,11,1.5],[17,1,1.5], [22,2,2.5],[31,12,1.5],[30,8,2.5]])

out=tf.constant([[5],[6],[9],[13],[4.8],[5.5],[13.2],[10.5]])

Compute the model coefficents using adam optimizer ? Use the loss function as Sum of squared error

inp=tf.constant([[18,1.5,1.5],[21,3,1.2],[29,7,2.5],[29,11,1.5],[17,1,1.5], [22,2,2.5],[31,12,1.5],[30,8,2.5]])
​
out=tf.constant([[5],[6],[9],[13],[4.8],[5.5],[13.2],[10.5]])
# Randomly assume
w=tf.Variable([1.,1.,1.])
def mod1(inputs,weight):
    return tf.tensordot(inputs,weight,1)
loss1=lambda: tf.reduce_mean((tf.pow((mod1(inp,w)-tf.transpose(out)),2)))
opti=tf.optimizers.Adam(learning_rate=0.1)
for i in range(100):
    opti.minimize(loss1,var_list=[w])
print(tf.tensordot(inp[0],w,1)) #predicted by optimized weights
print(out[0]) #actual
15. Perform the following equation
new_weight = alpha *Error + previous_weight
Assign the initial value of new_weight=0
Randomly create 100 values for error. Update the new_weight for every value of error
err=tf.random.normal([100])
​
alpha=tf.constant(0.05) 
w=tf.Variable(0.)
ws=[]
​
for i in range(err.numpy().shape[0]): 
    w=alpha*err.numpy()[i] + w
    ws.append(w)
plt.plot(ws)
​


########################################################################################################################################################################
#1_TensorFlowBasics_DL_Session1_Faculty_Notebook-v2-2.ipynb


Deep Learning Session 1 - TensorFlow Basics
import tensorflow as tf
import numpy as np
import pandas as pd
How to create the TENSORS of type constant and variable
t1=tf.constant(3)
t1
# to get only the value
t1.numpy()
# to get the rank of a scalar tensor
tf.rank(t1)
print(tf.rank(t1))
# creating a 1D tensor
t2=tf.constant([3,2,5,8])
t2
# to get the rank of a 1D tensor
print(t2.numpy())
print(tf.rank(t2))
​
# creating a 2D tensor
t3=tf.constant([[1,3,4],[3,2,5],[3,5,7]])
t3
# to get the rank of a 2D tensor
print(t3.numpy())
print(tf.rank(t3))
# creating a 3D tensor
t4=tf.constant([[[1,3,4],[3,2,5],[3,5,7]],[[0,1,4],[6,2,2],[3,5,7]],[[0,3,9],[3,2,5],[3,5,7]]])
t4
# to get the rank of a 3D tensor
print(tf.rank(t4))
tf.size(t4)
# creating a variable tensor with name 'var1' and type float
tv1=tf.Variable(2,dtype=tf.float32,name='var1')
tv1
# casting the float tensor to int
tf.cast(tv1,tf.int32)
Accessing elements in a tensor
tv2=tf.Variable([2,4,6,3,8])
tv2
# get the 1st element
tv2[0]
# get the first 3 elements
tv2[:3]
# create a tensor of shape [4,3] and random values
tv3=tf.random.normal([4,3])
tv3
# converting the tensor to variable tensor to allow us to perform operations on it.
tv4=tf.Variable(tv3)
tv4
# change 1st element value to 0
tv4[0,0].assign(0)
# change values of 1st row to 1
tv4[0,:].assign([1,1,1])
# create a [3,3] matriz containing 1
tf.ones([3,3])
# create a [4,4] matriz containing 0
tf.zeros([4,4])
# reshape operations
tv4
tf.reshape(tv4,[6,2])
# selecting elements of tensor based on some condition
tv3=tf.random.normal([4,3])
tv3
tv3<0 #condition
# way 1
tv3[tv3<0]
# way 2
tf.where(tv3<0)
Arithmetic operations on tensors
a=tf.Variable([2.,3,1])
b=tf.Variable([3.,4,1])
print((a+b)) # Addition
print(a*b) # Element wise Multiplication
print(a/b) # Division
print(a%b) # Modulus
# Dot product along axis 1
tf.tensordot(a,b,1)
# Dot product along axis 0
tf.tensordot(a,b,0)
# way 2 of adding 2 tensors
tf.add(a,b)
print(tf.pow(a,2)) # power
print(tf.sqrt(a)) # square root
print(tf.exp(a,0.5)) # exponential
print(tf.math.log(a)) # log
Matrix Multiplication

m1=tf.Variable(np.random.randint(1,5,[4,4]))
m2=tf.Variable(np.random.randint(1,5,[4,4]))
m1.numpy(),m2.numpy()
m1*m2 # Element wise Multiplication
tf.matmul(m1,m2) # Matrix Multiplication
# to find determinant of m1
​
m1=tf.cast(m1,tf.float32)
tf.linalg.det(m1)
# to find eigen values of m1
tf.linalg.eigvals(m1)
# to find transpose of m1
tf.transpose(m1)
# concatinating 2 tensors
m2=tf.cast(m2,tf.float32)
tf.concat([m1,m2],1)
Perform the following equation
upd_avg=alphaRaw_data + (1-alpha)previous_upd_avg
raw_data=tf.random.normal([100])
#raw_data.numpy()
alpha=tf.constant(0.05)
upd_avg=tf.Variable(0.)
res=[]
for i in range(raw_data.numpy().shape[0]):
    upd_avg=alpha*raw_data.numpy()[i]+ (1-alpha)*upd_avg
    res.append(upd_avg.numpy())
from matplotlib import pyplot as plt
plt.plot(res)
Optimizing the Coefficients for miminum loss in Tensorflow
# Consider the input matrix 
inp=tf.constant([[23,0.5,1],[26,2,1],[34,6,2],[34,10,1],[22,0,1],
                 [27,1,2],[36,11,1],[35,7,2]])
inp.numpy()
out=tf.constant([[2],[3],[6],[10],[1.8],[2.5],[10.2],[7.5]]) # output/ target - regression
w=tf.Variable([1.,1.,1.])  # random assumption of initial weight
tf.tensordot(inp,w,1)  # mulitplying the inputs with weights
def mod1(inputs,weight):
    return tf.tensordot(inputs,weight,1)
# define the abosule error as loss function
loss=lambda: tf.reduce_sum((abs(mod1(inp,w)-tf.transpose(out)))) 
opti=tf.optimizers.Adam(learning_rate=0.1) # Use adam optmizer (Gradient descent variant to find coeff)
for i in range(100):
    opti.minimize(loss,var_list=[w])    # Run the optmizer for minimizing the loss
    #print(w.numpy())
w # updated weight
# predicted output for updated/optmized weight
print(tf.tensordot(inp[0],w,1))
print(out[0]) #actual output


########################################################################################################################################################################
#1_TensorFlowBasics_TakeHome_Solutions_S1.ipynb
. Create a random tensor with 10 rows and 10 columns. Output random values should between range 1 and 10
a = tf.random.stateless_uniform([10,10], seed=(3,3), minval=1, maxval=10, dtype=tf.int32)
print(a)
2. Assign the first value (first row, first column) and last value(last row, last column) to ZERO
a = tf.Variable(a)
a[0,0].assign(0)
a[-1,-1].assign(0)
b = a.read_value()
print(b)
3. Create two tensor constants and perfrom subtraction and division
a = tf.constant(2)
b = tf.constant(3)
​
print("a + b :" , a.numpy() - b.numpy())
print("Addition with constants: ", a-b)
print("Addition with constants: ", tf.subtract(a, b))
print("a * b :" , a.numpy() / b.numpy())
print("Multiplication with constants: ", a/b)
print("Multiplication with constants: ", tf.divide(a, b))
​
4. Create 2 random matrices of size [4,4] and [4,4] with minimum value -10 and maximum value 10 and perform multiplication
#matrix multiple vs broad cast matrix
matrix1 = tf.random.stateless_uniform([4,4], seed=(3,3), minval=-10, maxval=10, dtype=tf.int32)
​
# Create another Constant that produces a 2x1 matrix.
matrix2 = tf.random.stateless_uniform([4,4], seed=(3,3), minval=-10, maxval=10, dtype=tf.int32)
​
# Create a Matmul op that takes 'matrix1' and 'matrix2' as inputs.
# The returned value, 'product', represents the result of the matrix
# multiplication.
product = tf.matmul(matrix1, matrix2)
print("Multiplication with matrixes:", product)
​
# broadcast matrix in Multiplication
​
print("broadcast matrix in Multiplication:", matrix1 * matrix2)
5. Create a float tensor and cast it into integer
#cast operations
a = tf.convert_to_tensor(2.)
b = tf.cast(a, tf.int32)
print(a, b)
##Variable manipulation

Variables are manipulated via the tf.Variable class. A tf.Variable represents a tensor whose value can be changed by running ops on it.Specific ops allow you to read and modify the values of this tensor.

6. Create a tensorflow variable with a name_scope and assign a value 100 to it
with tf.name_scope("my"):
    variable = tf.Variable(100)
print("tensor:", variable)
print("value:", variable.numpy())
7. Square your variable value
variable = variable * variable
print("value:", variable.numpy())
8. Increment your variable using assign_add() function
## To use the value of a tf.Variable in a TensorFlow graph, simply treat it like a normal tf.Tensor
variable = tf.Variable(2)
variable.assign_add(1)
print("value:", variable.numpy())
##Gradient Tape

tf.GradientTape is an API for automatic differentiation - computing the gradient of a computation with respect to its input variables. Tensorflow "records" all operations executed inside the context of a tf.GradientTape onto a "tape" ref: https://www.tensorflow.org/api_docs/python/tf/GradientTape

9. Calculate the first derivative for the function y = 3*(x^3) + 4(x^2), where x = 2
#First derivative
x = tf.constant(2.0)
with tf.GradientTape() as g:
  g.watch(x)
  y = (3*(x**3)) + (4*(x**2))
dy_dx = g.gradient(y, x)
print(dy_dx)
​
Calculate the second derivative for the function y = (1/12)(x*4), where x = 2.5
#second derivative
x = tf.constant(2.5)
with tf.GradientTape() as g:
  g.watch(x)
  with tf.GradientTape() as gg:
    gg.watch(x)
    y = (1/12)*(x**4)
  dy_dx = gg.gradient(y, x)     
d2y_dx2 = g.gradient(dy_dx, x)  
print(d2y_dx2)



########################################################################################################################################################################
#2_CIFAR-10_Inclass_Session2_Solution.ipynb


CIFAR-10 Dataset
CIFAR-10 is an established computer-vision dataset used for object recognition. It is a subset of the 80 million tiny images dataset and consists of 60,000 32x32 color images containing one of 10 object classes, with 6000 images per class. It was collected by Alex Krizhevsky, Vinod Nair, and Geoffrey Hinton.

In fact, even Tensorflow and Keras allow us to import and download the MNIST dataset directly from their API.

labels = [‘airplane’, ‘automobile’, ‘bird’, ‘cat’, ‘deer’, ‘dog’, ‘frog’, ‘horse’, ‘ship’, ‘truck’]

Import tensorflow and check it's version

import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt
Let's load CIFAR dataset

from tensorflow.keras.datasets import cifar10
​
# the data, shuffled and split between train and test sets
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
​
1. Print shape of the data and understand howmany images of different class exist in this datset
print(X_train.shape)
#There are 50000 images are there in total in this train datset. Each image is 32x32x3 in size
print(X_test.shape)
#There are 10000 images are there in total in this train datset. Each image is 32x32x3 in size
np.unique(y_train) 
# 10 differnt classes. The labels are:
# [‘airplane’, ‘automobile’, ‘bird’, ‘cat’, ‘deer’, ‘dog’, ‘frog’, ‘horse’, ‘ship’, ‘truck’]
2. Visualize some images using matplotlib
plt.imshow(X_train[600,:,:,:])
print(y_train[600]) # Label 0 : Aeroplane
3. Convert the RGB Image to Grayscale(For easier computation)
Hint: tf.image.rgb_to_grayscale(X_train)

The above code will give the result as tensor, take only the numpy part from it and procced.

x_train=tf.image.rgb_to_grayscale(X_train).numpy()
x_test=tf.image.rgb_to_grayscale(X_test).numpy()
x_train.shape
4. Normalize the data so that data is in range 0-1
x_train=x_train/255.
x_test=x_test/255.
5. Reshape train and test images into one dimensional vector
xtrain=x_train.reshape(50000,32*32)
xtest=x_test.reshape(10000,32*32)
xtrain.shape
6. Print shape of data and number of images
print(xtrain.shape)
print('The number of images :',xtrain.shape[0])
7. One-hot encode the class vector
Hint: from tensorflow.keras.utils import to_categorical

from tensorflow.keras.utils import to_categorical
ytrain = to_categorical(y_train, num_classes=10)
ytest = to_categorical(y_test, num_classes=10)
​
print("Shape of y_train:", ytrain.shape)
print("One value of y_train:", ytrain[0])
DNN
08. Construct the Deep Neural Network of following architecture
    input_neurons x 64 x 32 x 32 x output_neurons
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
​
img_classifier=Sequential() 
​
img_classifier.add(Dense(units=64,activation='relu',input_dim=1024))
​
img_classifier.add(Dense(units=32,activation='relu'))
​
img_classifier.add(Dense(units=32,activation='relu'))
​
img_classifier.add(Dense(units=10,activation='softmax'))
​
09. Compile and fit the model
let's compile our model
loss: "categorical_crossentropy"
metrics: "accuracy"
optimizer: "sgd"
then next step will be to fit model
give train data - training features and labels
batch size: 32
epochs: 50
give validation data - testing features and labels
img_classifier.compile(optimizer='sgd',loss='categorical_crossentropy',metrics=['accuracy'])
img_classifier.fit(xtrain,ytrain,batch_size=32,epochs=50,validation_data=(xtest, ytest))
10. Calculate Final loss and accuracy on test data
img_classifier.evaluate(xtest, ytest)


########################################################################################################################################################################
#2_MNIST_HyperParameter-Optimization_Inclass_S2_tuning_Solution.ipynb

MNIST neural network - Hyperparameter Optimization using Tensorflow
MNIST Dataset
The MNIST database contains 60,000 training images and 10,000 testing images taken from American Census Bureau employees and American high school students. The MNIST dataset is one of the most common datasets used for image classification and accessible from many different sources. In fact, even Tensorflow and Keras allow us to import and download the MNIST dataset directly from their API.

1. Load Fashion MNIST dataset
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.datasets import fashion_mnist
​
# the data, shuffled and split between train and test sets
(X_train, y_train), (X_val, y_val) = fashion_mnist.load_data()
X_train and X_test contain greyscale RGB codes (from 0 to 255) while y_train and y_test contains labels from 0 to 9 which represents which number they actually are.

2. Visualize one image using matplotlib and print the shape of the train and test data
import matplotlib.pyplot as plt
%matplotlib inline
print("Label: {}".format(y_train[9000]))
plt.imshow(X_train[9000], cmap='gray')
print(X_train.shape)
print(y_train.shape)
print(X_val.shape)
print(y_val.shape)
3. Reshape the features to train the Deep Neural Network
X_train = X_train.reshape(60000, 784)
print(X_train.shape)
X_val = X_val.reshape(10000, 784)
print(X_val.shape)
4. Normalize features
Normalize features from 0-255 to 0-1
print(X_train.max())
print(X_train.min())
​
X_train = X_train / 255.0
X_val = X_val / 255.0
​
print(X_train.max())
print(X_train.min())
​
5. One-hot encode the class vector
import tensorflow as tf
print(y_train[10])
y_train = tf.keras.utils.to_categorical(y_train, num_classes=10)
y_val = tf.keras.utils.to_categorical(y_val, num_classes=10)
print(y_train[10])
6. Display some images and print their labels
import numpy as np
​
# visualizing the first 10 images in the dataset and their labels
%matplotlib inline
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 1))
for i in range(10):
    plt.subplot(1, 10, i+1)
    plt.imshow(X_train[i].reshape(28, 28), cmap="gray")
    plt.axis('off')
    print('label for each of the below image: %s' % (np.argmax(y_train[0:10][i])))
plt.show()
​
7. Write a function to train the Deep Neural Network with two hidden layers. The function should recieve a arguments iterations, learning rate and regularization penalty from the user. The choice of number of hidden layer neurons is yours. Use the SGD optimzer and use the momentum value as 0.9
Written in a function - to run it multiple times
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import regularizers, optimizers
​
def train_and_test_loop(iterations, lr, Lambda, verb=True):
​
    ## hyperparameters
    iterations = iterations
    learning_rate = lr
    hidden_nodes = 256
    output_nodes = 10
        
    model = Sequential()
    model.add(Dense(hidden_nodes, input_shape=(784,), activation='relu'))
    model.add(Dense(hidden_nodes, activation='relu'))
    model.add(Dense(output_nodes, activation='softmax', kernel_regularizer=regularizers.l2(Lambda)))
    
    sgd = optimizers.SGD(lr=learning_rate, decay=1e-6, momentum=0.9)
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
    
    # Fit the model
    model.fit(X_train, y_train, epochs=iterations, batch_size=1000, verbose= 1)
    
    [loss,score_train]=model.evaluate(X_train,y_train)
    [loss,score_test]=model.evaluate(X_val,y_val)
    
    return score_train,score_test
8. Creating another function to train DNN model with the following modification
Instead of accuracy at each epoch below code gives the consolidate accuracy
Model should print both train and test accuracy
def train_and_test_loop1(iterations, lr, Lambda, verb=True):
​
    ## hyperparameters
    iterations = iterations
    learning_rate = lr
    hidden_nodes = 256
    output_nodes = 10
​
    model = Sequential()
    model.add(Dense(hidden_nodes, input_shape=(784,), activation='relu'))
    model.add(Dense(hidden_nodes, activation='relu'))
    model.add(Dense(output_nodes, activation='softmax', kernel_regularizer=regularizers.l2(Lambda)))
    
    sgd = optimizers.SGD(lr=learning_rate, decay=1e-6, momentum=0.9)
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
    
    # Fit the model
    model.fit(X_train, y_train, epochs=iterations, batch_size=1000, verbose= 1)
    #score = model.evaluate(X_train, y_train, verbose=0)
    [loss,score_train]=model.evaluate(X_train,y_train)
    [loss,score_test]=model.evaluate(X_val,y_val)
    
    return score_train,score_test
9. Train the model with no regularization and choose some very very small value of lamda and comment about the model performance.
Double Check that the loss is reasonable
Disable the regularization (Lambda = 0)
lr = 0.00001
Lambda = 0
train_and_test_loop(10, lr, Lambda)
Loss is not changing in consecutive iteration. It may becasue of vanishing gradient
10. Incease the learning factor to some two digit number and comemnt about the model peformance. Kepp regularization factor as 0.
lr = 20
Lambda = 0
train_and_test_loop1(10, lr, Lambda)
Loss is increasing. It may due to exploding gradient. Increasing alpha to big value also one reason for exploding
11. Explore the model for the alpha between 0.1 to 1 and comment about best alpha model performace
lr=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
for i in lr:
    score=train_and_test_loop1(10,i,0)
    print('epocs:',10,'train_accuracy:',score[0],'test_accuracy:',score[1],'alpha:', i)
When alpha=0.1, the model is peforming well, but slightly the overfitting is there, which can be reduced by regularizing the model
12. Choose the best value of learning factor from the above step and use some small value of regularization (lamda) and comment about the model performace.
train_and_test_loop1(10,0.1,0.005)
# Overfitting is reducing, but the model training performance also reducing slightly
13. Try a (larger) regularization say 50. Comment about the model performance?
lr=0.1
Lambda = 50
train_and_test_loop1(20, lr, Lambda)
Loss id becoming too high (nan) as more penalty is added to the loss function
14. Find the best combination of learning rate and regularization lambda. Explore learning rate between 0.1 to 1 and lamda beteween 0.001 to 0.01
#lr=[0.0001,0.001,0.01,0.1,1,10,20,50]
#lam=[0.0001,0.001,0.01,0.1,1,10,20,50]
lr=np.linspace(0.1,1,10)
lam=np.linspace(0.001,0.01,10)
for i,j in zip(lr,lam):
    score=train_and_test_loop1(5,i,j)
    print('epocs:',10,'train_accuracy:',score[0],'test_accuracy:',score[1],'alpha:', i,'Regularization:',j)
15. Tune the model with kerasclassifier and GridsearchCV
def tune_model(learning_rate,activation, lamda,initializer,num_unit):
    model = Sequential()
    model.add(Dense(num_unit, kernel_initializer=initializer,activation=activation, input_dim=784))
    #model.add(Dropout(dropout_rate))
    model.add(Dense(num_unit, kernel_initializer=initializer,activation=activation))
    #model.add(Dropout(dropout_rate)) 
    model.add(Dense(10, activation='softmax',kernel_regularizer=regularizers.l2(lamda)))
    sgd = optimizers.SGD(lr=learning_rate)
    model.compile(loss='categorical_crossentropy',optimizer=sgd,metrics=['accuracy'])
    return model
batch_size = [20, 50, 100][:1]
epochs = [1, 20, 50][:1]
initializer = ['lecun_uniform', 'normal', 'he_normal', 'he_uniform'][:1]
learning_rate = [0.1, 0.001, 0.02][:1]
lamda = [0.001, 0.005, 0.01][:1]
num_unit = [256, 128][:1]
activation = ['relu', 'tanh', 'sigmoid', 'hard_sigmoid', 'linear'][:1]
parameters = dict(batch_size = batch_size,
                  epochs = epochs,
                  learning_rate=learning_rate,
                  lamda = lamda,
                  num_unit = num_unit,
                  initializer = initializer,
                  activation = activation)
model =tf.keras.wrappers.scikit_learn.KerasClassifier(build_fn=tune_model, verbose=0)
from sklearn.model_selection import GridSearchCV
models = GridSearchCV(estimator = model, param_grid=parameters, n_jobs=1)
best_model = models.fit(X_train, y_train)
print('Best model :',best_model.best_params_)
​


########################################################################################################################################################################
#2_NN_scratch_Faculty_Session2_Notebook_NN_scratch-2.ipynb

MNIST neural network - Hyperparameter Optimization using Tensorflow
MNIST Dataset
The MNIST database contains 60,000 training images and 10,000 testing images taken from American Census Bureau employees and American high school students. The MNIST dataset is one of the most common datasets used for image classification and accessible from many different sources. In fact, even Tensorflow and Keras allow us to import and download the MNIST dataset directly from their API.

1. Load Fashion MNIST dataset
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.datasets import fashion_mnist
​
# the data, shuffled and split between train and test sets
(X_train, y_train), (X_val, y_val) = fashion_mnist.load_data()
X_train and X_test contain greyscale RGB codes (from 0 to 255) while y_train and y_test contains labels from 0 to 9 which represents which number they actually are.

2. Visualize one image using matplotlib and print the shape of the train and test data
import matplotlib.pyplot as plt
%matplotlib inline
print("Label: {}".format(y_train[9000]))
plt.imshow(X_train[9000], cmap='gray')
print(X_train.shape)
print(y_train.shape)
print(X_val.shape)
print(y_val.shape)
3. Reshape the features to train the Deep Neural Network
X_train = X_train.reshape(60000, 784)
print(X_train.shape)
X_val = X_val.reshape(10000, 784)
print(X_val.shape)
4. Normalize features
Normalize features from 0-255 to 0-1
print(X_train.max())
print(X_train.min())
​
X_train = X_train / 255.0
X_val = X_val / 255.0
​
print(X_train.max())
print(X_train.min())
​
5. One-hot encode the class vector
import tensorflow as tf
print(y_train[10])
y_train = tf.keras.utils.to_categorical(y_train, num_classes=10)
y_val = tf.keras.utils.to_categorical(y_val, num_classes=10)
print(y_train[10])
6. Display some images and print their labels
import numpy as np
​
# visualizing the first 10 images in the dataset and their labels
%matplotlib inline
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 1))
for i in range(10):
    plt.subplot(1, 10, i+1)
    plt.imshow(X_train[i].reshape(28, 28), cmap="gray")
    plt.axis('off')
    print('label for each of the below image: %s' % (np.argmax(y_train[0:10][i])))
plt.show()
​
7. Write a function to train the Deep Neural Network with two hidden layers. The function should recieve a arguments iterations, learning rate and regularization penalty from the user. The choice of number of hidden layer neurons is yours. Use the SGD optimzer and use the momentum value as 0.9
Written in a function - to run it multiple times
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import regularizers, optimizers
​
def train_and_test_loop(iterations, lr, Lambda, verb=True):
​
    ## hyperparameters
    iterations = iterations
    learning_rate = lr
    hidden_nodes = 256
    output_nodes = 10
        
    model = Sequential()
    model.add(Dense(hidden_nodes, input_shape=(784,), activation='relu'))
    model.add(Dense(hidden_nodes, activation='relu'))
    model.add(Dense(output_nodes, activation='softmax', kernel_regularizer=regularizers.l2(Lambda)))
    
    sgd = optimizers.SGD(lr=learning_rate, decay=1e-6, momentum=0.9)
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
    
    # Fit the model
    model.fit(X_train, y_train, epochs=iterations, batch_size=1000, verbose= 1)
    
    [loss,score_train]=model.evaluate(X_train,y_train)
    [loss,score_test]=model.evaluate(X_val,y_val)
    
    return score_train,score_test
8. Creating another function to train DNN model with the following modification
Instead of accuracy at each epoch below code gives the consolidate accuracy
Model should print both train and test accuracy
def train_and_test_loop1(iterations, lr, Lambda, verb=True):
​
    ## hyperparameters
    iterations = iterations
    learning_rate = lr
    hidden_nodes = 256
    output_nodes = 10
​
    model = Sequential()
    model.add(Dense(hidden_nodes, input_shape=(784,), activation='relu'))
    model.add(Dense(hidden_nodes, activation='relu'))
    model.add(Dense(output_nodes, activation='softmax', kernel_regularizer=regularizers.l2(Lambda)))
    
    sgd = optimizers.SGD(lr=learning_rate, decay=1e-6, momentum=0.9)
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
    
    # Fit the model
    model.fit(X_train, y_train, epochs=iterations, batch_size=1000, verbose= 1)
    #score = model.evaluate(X_train, y_train, verbose=0)
    [loss,score_train]=model.evaluate(X_train,y_train)
    [loss,score_test]=model.evaluate(X_val,y_val)
    
    return score_train,score_test
9. Train the model with no regularization and choose some very very small value of lamda and comment about the model performance.
Double Check that the loss is reasonable
Disable the regularization (Lambda = 0)
lr = 0.00001
Lambda = 0
train_and_test_loop(10, lr, Lambda)
Loss is not changing in consecutive iteration. It may becasue of vanishing gradient
10. Incease the learning factor to some two digit number and comemnt about the model peformance. Kepp regularization factor as 0.
lr = 20
Lambda = 0
train_and_test_loop1(10, lr, Lambda)
Loss is increasing. It may due to exploding gradient. Increasing alpha to big value also one reason for exploding
11. Explore the model for the alpha between 0.1 to 1 and comment about best alpha model performace
lr=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
for i in lr:
    score=train_and_test_loop1(10,i,0)
    print('epocs:',10,'train_accuracy:',score[0],'test_accuracy:',score[1],'alpha:', i)
When alpha=0.1, the model is peforming well, but slightly the overfitting is there, which can be reduced by regularizing the model
12. Choose the best value of learning factor from the above step and use some small value of regularization (lamda) and comment about the model performace.
train_and_test_loop1(10,0.1,0.005)
# Overfitting is reducing, but the model training performance also reducing slightly
13. Try a (larger) regularization say 50. Comment about the model performance?
lr=0.1
Lambda = 50
train_and_test_loop1(20, lr, Lambda)
Loss id becoming too high (nan) as more penalty is added to the loss function
14. Find the best combination of learning rate and regularization lambda. Explore learning rate between 0.1 to 1 and lamda beteween 0.001 to 0.01
#lr=[0.0001,0.001,0.01,0.1,1,10,20,50]
#lam=[0.0001,0.001,0.01,0.1,1,10,20,50]
lr=np.linspace(0.1,1,10)
lam=np.linspace(0.001,0.01,10)
for i,j in zip(lr,lam):
    score=train_and_test_loop1(5,i,j)
    print('epocs:',10,'train_accuracy:',score[0],'test_accuracy:',score[1],'alpha:', i,'Regularization:',j)
15. Tune the model with kerasclassifier and GridsearchCV
def tune_model(learning_rate,activation, lamda,initializer,num_unit):
    model = Sequential()
    model.add(Dense(num_unit, kernel_initializer=initializer,activation=activation, input_dim=784))
    #model.add(Dropout(dropout_rate))
    model.add(Dense(num_unit, kernel_initializer=initializer,activation=activation))
    #model.add(Dropout(dropout_rate)) 
    model.add(Dense(10, activation='softmax',kernel_regularizer=regularizers.l2(lamda)))
    sgd = optimizers.SGD(lr=learning_rate)
    model.compile(loss='categorical_crossentropy',optimizer=sgd,metrics=['accuracy'])
    return model
batch_size = [20, 50, 100][:1]
epochs = [1, 20, 50][:1]
initializer = ['lecun_uniform', 'normal', 'he_normal', 'he_uniform'][:1]
learning_rate = [0.1, 0.001, 0.02][:1]
lamda = [0.001, 0.005, 0.01][:1]
num_unit = [256, 128][:1]
activation = ['relu', 'tanh', 'sigmoid', 'hard_sigmoid', 'linear'][:1]
parameters = dict(batch_size = batch_size,
                  epochs = epochs,
                  learning_rate=learning_rate,
                  lamda = lamda,
                  num_unit = num_unit,
                  initializer = initializer,
                  activation = activation)
model =tf.keras.wrappers.scikit_learn.KerasClassifier(build_fn=tune_model, verbose=0)
from sklearn.model_selection import GridSearchCV
models = GridSearchCV(estimator = model, param_grid=parameters, n_jobs=1)
best_model = models.fit(X_train, y_train)
print('Best model :',best_model.best_params_)
​

########################################################################################################################################################################
#3_MNIST_HyperParameter_Faculty_Notebook_Session3_Hyper_Parameters_DNN-1.ipynb


MNIST Dataset
The MNIST database contains 60,000 training images and 10,000 testing images taken from American Census Bureau employees and American high school students. The MNIST dataset is one of the most common datasets used for image classification and accessible from many different sources. In fact, even Tensorflow and Keras allow us to import and download the MNIST dataset directly from their API.

import tensorflow as tf
import numpy as np
#Load the MNIST digit datset
from tensorflow.keras.datasets import mnist
(xtrain,ytrain),(xtest,ytest)=mnist.load_data()
xtrain.shape # there are 60000 images of each 28 rows and 28 columns
xtest.shape
from matplotlib import pyplot as plt
plt.imshow(xtrain[0,:,:])
ytrain[0] # The output label for the image shown above
x_train=xtrain.reshape(60000,28*28) # reshaping images as one dimensional
x_test=xtest.reshape(10000,28*28)
x_train=x_train/255. # scaling the images
x_test=x_test/255.
y_train=tf.keras.utils.to_categorical(ytrain,num_classes=10) # Encoding the target levels
y_test=tf.keras.utils.to_categorical(ytest,num_classes=10) 
y_train[0]
ytrain[0]
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras import regularizers, optimizers
#Create the function to define a DNN model with dynamic iteration, learning_rate, 
#regularization penalty# neurons in the hidden layer for tuning
def train_and_test_model(itr,lr,lamda):
    
    iterations=itr
    learning_rate=lr
    hidden_nodes=256
    output_nodes=10
    
    model=Sequential()
    model.add(Dense(units=hidden_nodes,activation='relu',input_dim=784))
    model.add(Dense(units=hidden_nodes,activation='relu'))
    model.add(Dense(units=output_nodes,activation='softmax',kernel_regularizer=regularizers.l2(lamda)))
    
    sgd=optimizers.SGD(lr=learning_rate)
    model.compile(loss='categorical_crossentropy',optimizer=sgd,metrics=['accuracy'])
    
    model.fit(x_train,y_train,epochs=iterations,batch_size=1000,verbose=0)
    [loss,score_train]=model.evaluate(x_train,y_train)
    [loss,score_test]=model.evaluate(x_test,y_test)
    
    return score_train,score_test  # returning both train and test scores
lr=0.00001 # Choose very small value of learning rate
lamda=0
train_and_test_model(10,lr,lamda) # Leading to vanishing gradiant problem
# loss is not changing in each iteration much and model accuracy is poor. 
#To understand it run with verbose =1 in the above function
lr=0.001 # Increasing the learning_rate to 0.001 improving the performance slightly
lamda=0 # no regularization
train_and_test_model(10,lr,lamda)
lr=0.1# Increasing the learning_rate to 0.1 improving the performance above 90 percent
lamda=0
train_and_test_model(10,lr,lamda)
lr=1 # learning rate of 1 giving very good results for this datset [It may not be same for all the data]
lamda=0
train_and_test_model(10,lr,lamda)
lr=50   # Increasing the lr to 50 leading to Exploding Gradient. Loss going out of control
lamda=0
train_and_test_model(10,lr,lamda)
lr=0.0000001  # Vanishing Gradient
lamda=0
train_and_test_model(10,lr,lamda)
lr=1 
lamda=0.02 # Introduce small regularization, regularization will reduce overfitting, but bias error may slightly increase
train_and_test_model(10,lr,lamda) # Less overfitting
lr=1 
lamda=1 
train_and_test_model(10,lr,lamda) # Underfitting, penalty(lamda) of 1, reducing the performance greatly
#Coarse tuning - Explore the model for wide span of learning rate and lamda(regularization penalty)
lr=[0.0001,0.001,0.01,0.1,1,10,20,50]
lam=[0.0001,0.001,0.01,0.1,1,10,20,50]
for i,j in zip(lr,lam):
    score=train_and_test_model(10,i,j)
    print('epocs:',10,'train_accuracy:',score[0],'test_accuracy:',score[1],'alpha:', i,'Regularization:',j)
#Another random way of doing coarse tuning
import math
for k in range(1,10):
    lr = math.pow(10, np.random.uniform(-7.0, 3.0))
    Lambda = math.pow(10, np.random.uniform(-7,-2))
    best_acc = train_and_test_model(10, lr, Lambda)
    print('k:',k,'epocs:',100,'accuracy:',best_acc,'alpha:', lr,'Regularization:',Lambda)
​
import math
math.pow(10,np.random.uniform(-7.0, 3.0))
#Create the function to define a DNN model with dynamic learning_rate, regularization penalty
         # neurons in the hidden layer,activation function and weight intitialization for tuning
def tune_model(learning_rate,activation, lamda,initializer,num_unit):
    model = Sequential()
    model.add(Dense(num_unit, kernel_initializer=initializer,activation=activation, input_dim=784))
    #model.add(Dropout(dropout_rate))
    model.add(Dense(num_unit, kernel_initializer=initializer,activation=activation))
    #model.add(Dropout(dropout_rate)) 
    model.add(Dense(10, activation='softmax',kernel_regularizer=regularizers.l2(lamda)))
    sgd = optimizers.SGD(lr=learning_rate)
    model.compile(loss='categorical_crossentropy',optimizer=sgd,metrics=['accuracy'])
    return model
#he_normal 
#std = sqrt(2/fan_in)
#fan_in= number of neurons in the hiddenlayer
#Define hyper parameters values
batch_size = [20, 50, 100][:1]
epochs = [1, 20, 50][:1]
initializer = ['lecun_uniform', 'normal', 'he_normal', 'he_uniform'][:1]
learning_rate = [0.1, 0.001, 0.02][:1]
lamda = [0.001, 0.005, 0.01][:1]
num_unit = [256, 128][:1]
activation = ['relu', 'tanh', 'sigmoid', 'hard_sigmoid', 'linear'][:1]
#create dictionary with hyper parameters
parameters = dict(batch_size = batch_size,
                  epochs = epochs,
                  learning_rate=learning_rate,
                  lamda = lamda,
                  num_unit = num_unit,
                  initializer = initializer,
                  activation = activation)
parameters
# Make this keras model compatible to sklearn to apply gridsearchCV
model =tf.keras.wrappers.scikit_learn.KerasClassifier(build_fn=tune_model, verbose=0)
from sklearn.model_selection import GridSearchCV
models = GridSearchCV(estimator = model, param_grid=parameters, n_jobs=1)
best_model = models.fit(x_train, y_train)
print('Best model :',best_model.best_params_)
import pandas as pd
pd.DataFrame(best_model.cv_results_)
# Run for all the combinations and take the best results interms of both bias and variance error


########################################################################################################################################################################
#3_MNIST_Hyperparameter_Inclass_S3_Solution.ipynb
MNIST Dataset
The MNIST database contains 60,000 training images and 10,000 testing images taken from American Census Bureau employees and American high school students. The MNIST dataset is one of the most common datasets used for image classification and accessible from many different sources. In fact, even Tensorflow and Keras allow us to import and download the MNIST dataset directly from their API.

1. Load Fashion MNIST dataset
from tensorflow.keras.datasets import fashion_mnist
​
# the data, shuffled and split between train and test sets
(X_train, y_train), (X_val, y_val) = fashion_mnist.load_data()
X_train and X_test contain greyscale RGB codes (from 0 to 255) while y_train and y_test contains labels from 0 to 9 which represents which number they actually are.

2. Visualize one image using matplotlib and print the shape of the train and test data
import matplotlib.pyplot as plt
%matplotlib inline
print("Label: {}".format(y_train[9000]))
plt.imshow(X_train[9000], cmap='gray')
print(X_train.shape)
print(y_train.shape)
print(X_val.shape)
print(y_val.shape)
3. Reshape the features to train the Deep Neural Network
X_train = X_train.reshape(60000, 784)
print(X_train.shape)
X_val = X_val.reshape(10000, 784)
print(X_val.shape)
4. Normalize features
Normalize features from 0-255 to 0-1
print(X_train.max())
print(X_train.min())
​
X_train = X_train / 255.0
X_val = X_val / 255.0
​
print(X_train.max())
print(X_train.min())
​
5. One-hot encode the class vector
import tensorflow as tf
print(y_train[10])
y_train = tf.keras.utils.to_categorical(y_train, num_classes=10)
y_val = tf.keras.utils.to_categorical(y_val, num_classes=10)
print(y_train[10])
6. Display some images and print their labels
import numpy as np
​
# visualizing the first 10 images in the dataset and their labels
%matplotlib inline
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 1))
for i in range(10):
    plt.subplot(1, 10, i+1)
    plt.imshow(X_train[i].reshape(28, 28), cmap="gray")
    plt.axis('off')
    print('label for each of the below image: %s' % (np.argmax(y_train[0:10][i])))
plt.show()
​
7. Write a function to train the Deep Neural Network with two hidden layers. The function should recieve a arguments iterations, learning rate and regularization penalty from the user. The choice of number of hidden layer neurons is yours. Use the SGD optimzer and use the momentum value as 0.9
Written in a function - to run it multiple times
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import regularizers, optimizers
​
def train_and_test_loop(iterations, lr, Lambda, verb=True):
​
    ## hyperparameters
    iterations = iterations
    learning_rate = lr
    hidden_nodes = 256
    output_nodes = 10
        
    model = Sequential()
    model.add(Dense(hidden_nodes, input_shape=(784,), activation='relu'))
    model.add(Dense(hidden_nodes, activation='relu'))
    model.add(Dense(output_nodes, activation='softmax', kernel_regularizer=regularizers.l2(Lambda)))
    
    sgd = optimizers.SGD(lr=learning_rate, decay=1e-6, momentum=0.9)
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
    
    # Fit the model
    model.fit(X_train, y_train, epochs=iterations, batch_size=1000, verbose= 1)
    
    [loss,score_train]=model.evaluate(X_train,y_train)
    [loss,score_test]=model.evaluate(X_val,y_val)
    
    return score_train,score_test
8. Creating another function to train DNN model with the following modification
Instead of accuracy at each epoch below code gives the consolidate accuracy
Model should print both train and test accuracy
def train_and_test_loop1(iterations, lr, Lambda, verb=True):
​
    ## hyperparameters
    iterations = iterations
    learning_rate = lr
    hidden_nodes = 256
    output_nodes = 10
​
    model = Sequential()
    model.add(Dense(hidden_nodes, input_shape=(784,), activation='relu'))
    model.add(Dense(hidden_nodes, activation='relu'))
    model.add(Dense(output_nodes, activation='softmax', kernel_regularizer=regularizers.l2(Lambda)))
    
    sgd = optimizers.SGD(lr=learning_rate, decay=1e-6, momentum=0.9)
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
    
    # Fit the model
    model.fit(X_train, y_train, epochs=iterations, batch_size=1000, verbose= 1)
    #score = model.evaluate(X_train, y_train, verbose=0)
    [loss,score_train]=model.evaluate(X_train,y_train)
    [loss,score_test]=model.evaluate(X_val,y_val)
    
    return score_train,score_test
9. Train the model with no regularization and choose some very very small value of lamda and comment about the model performance.
Double Check that the loss is reasonable
Disable the regularization (Lambda = 0)
lr = 0.00001
Lambda = 0
train_and_test_loop(10, lr, Lambda)
Loss is not changing in consecutive iteration. It may becasue of vanishing gradient
10. Incease the learning factor to some two digit number and comemnt about the model peformance. Kepp regularization factor as 0.
lr = 20
Lambda = 0
train_and_test_loop1(10, lr, Lambda)
Loss is increasing. It may due to exploding gradient. Increasing alpha to big value also one reason for exploding
11. Explore the model for the alpha between 0.1 to 1 and comment about best alpha model performace
lr=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
for i in lr:
    score=train_and_test_loop1(10,i,0)
    print('epocs:',10,'train_accuracy:',score[0],'test_accuracy:',score[1],'alpha:', i)
When alpha=0.1, the model is peforming well, but slightly the overfitting is there, which can be reduced by regularizing the model
12. Choose the best value of learning factor from the above step and use some small value of regularization (lamda) and comment about the model performace.
train_and_test_loop1(10,0.1,0.005)
# Overfitting is reducing, but the model training performance also reducing slightly
13. Try a (larger) regularization say 50. Comment about the model performance?
lr=0.1
Lambda = 50
train_and_test_loop1(20, lr, Lambda)
Loss id becoming too high (nan) as more penalty is added to the loss function
14. Find the best combination of learning rate and regularization lambda. Explore learning rate between 0.1 to 1 and lamda beteween 0.001 to 0.01
#lr=[0.0001,0.001,0.01,0.1,1,10,20,50]
#lam=[0.0001,0.001,0.01,0.1,1,10,20,50]
lr=np.linspace(0.1,1,10)
lam=np.linspace(0.001,0.01,10)
for i,j in zip(lr,lam):
    score=train_and_test_loop1(5,i,j)
    print('epocs:',10,'train_accuracy:',score[0],'test_accuracy:',score[1],'alpha:', i,'Regularization:',j)
15. Tune the model with kerasclassifier and GridsearchCV
def tune_model(learning_rate,activation, lamda,initializer,num_unit):
    model = Sequential()
    model.add(Dense(num_unit, kernel_initializer=initializer,activation=activation, input_dim=784))
    #model.add(Dropout(dropout_rate))
    model.add(Dense(num_unit, kernel_initializer=initializer,activation=activation))
    #model.add(Dropout(dropout_rate)) 
    model.add(Dense(10, activation='softmax',kernel_regularizer=regularizers.l2(lamda)))
    sgd = optimizers.SGD(lr=learning_rate)
    model.compile(loss='categorical_crossentropy',optimizer=sgd,metrics=['accuracy'])
    return model
batch_size = [20, 50, 100][:1]
epochs = [1, 20, 50][:1]
initializer = ['lecun_uniform', 'normal', 'he_normal', 'he_uniform'][:1]
learning_rate = [0.1, 0.001, 0.02][:1]
lamda = [0.001, 0.005, 0.01][:1]
num_unit = [256, 128][:1]
activation = ['relu', 'tanh', 'sigmoid', 'hard_sigmoid', 'linear'][:1]
parameters = dict(batch_size = batch_size,
                  epochs = epochs,
                  learning_rate=learning_rate,
                  lamda = lamda,
                  num_unit = num_unit,
                  initializer = initializer,
                  activation = activation)
model =tf.keras.wrappers.scikit_learn.KerasClassifier(build_fn=tune_model, verbose=0)
from sklearn.model_selection import GridSearchCV
models = GridSearchCV(estimator = model, param_grid=parameters, n_jobs=1)
best_model = models.fit(X_train, y_train)
print('Best model :',best_model.best_params_)
​



########################################################################################################################################################################
#3_MNIST_Takehome_S3_solution.ipynb

Fashion-MNIST Dataset
Fashion-MNIST is a dataset of Zalando's article images—consisting of a training set of 60,000 examples and a test set of 10,000 examples. Each example is a 28x28 grayscale image, associated with a label from 10 classes. Zalando intends Fashion-MNIST to serve as a direct drop-in replacement for the original MNIST dataset for benchmarking machine learning algorithms. It shares the same image size and structure of training and testing splits.

Firstly, let's select TensorFlow version 2.x in colab

1. Import Tensorflow library and random number generator, also write code to ignore thw warnings
%tensorflow_version 2.x
import tensorflow
tensorflow.__version__
import random
random.seed(0)

# Ignore the warnings
import warnings
warnings.filterwarnings("ignore")
# Initialize the random number generator
import random
random.seed(0)
​
# Ignore the warnings
import warnings
warnings.filterwarnings("ignore")
2. Let's load Fashion MNIST dataset
from tensorflow.keras.datasets import fashion_mnist
​
# the data, shuffled and split between train and test sets
(X_train, y_train), (X_val, y_val) = fashion_mnist.load_data()
X_train and X_test contain greyscale RGB codes (from 0 to 255) while y_train and y_test contains labels from 0 to 9 which represents which number they actually are.

3. Visualize one image using matplotlib
import matplotlib.pyplot as plt
%matplotlib inline
print("Label: {}".format(y_train[9000]))
plt.imshow(X_train[9000], cmap='gray')
Print shape of the data
print(X_train.shape)
print(y_train.shape)
print(X_val.shape)
print(y_val.shape)
4. Reshape features
reshape() method gives a new shape to an array without changing its data
You can read more about it here https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html
X_train = X_train.reshape(60000, 784)
print(X_train.shape)
X_val = X_val.reshape(10000, 784)
print(X_val.shape)
5. Normalize features
Normalize features from 0-255 to 0-1
print(X_train.max())
print(X_train.min())
​
X_train = X_train / 255.0
X_val = X_val / 255.0
​
print(X_train.max())
print(X_train.min())
​
6. One-hot encode the class vector
convert class vectors (integers) to binary class matrix
convert X_train and X_val
number of classes: 10
print(y_train[10])
y_train = tensorflow.keras.utils.to_categorical(y_train, num_classes=10)
y_val = tensorflow.keras.utils.to_categorical(y_val, num_classes=10)
print(y_train[10])
7. Print some images and their labels
import numpy as np
​
# visualizing the first 10 images in the dataset and their labels
%matplotlib inline
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 1))
for i in range(10):
    plt.subplot(1, 10, i+1)
    plt.imshow(X_train[i].reshape(28, 28), cmap="gray")
    plt.axis('off')
    print('label for each of the below image: %s' % (np.argmax(y_train[0:10][i])))
plt.show()
​
8. Creating model 1 with input shape 784, 256 hidden nodes in layer1 and an output layer, activation - relu, kernel_regularizer = lambda
Written in a function - to run it multiple times
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import regularizers, optimizers
​
def train_and_test_loop(iterations, lr, Lambda, verb=True):
​
    ## hyperparameters
    iterations = iterations
    learning_rate = lr
    hidden_nodes = 256
    output_nodes = 10
        
    model = Sequential()
    model.add(Dense(hidden_nodes, input_shape=(784,), activation='relu'))
    model.add(Dense(hidden_nodes, activation='relu'))
    model.add(Dense(output_nodes, activation='softmax', kernel_regularizer=regularizers.l2(Lambda)))
    
    sgd = optimizers.SGD(lr=learning_rate, decay=1e-6, momentum=0.9)
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
    
    # Fit the model
    model.fit(X_train, y_train, epochs=iterations, batch_size=1000, verbose= 1)
9. Creating model 2
Same model as above
Instead of accuracy at each epoch below code gives the consolidate accuracy
Notice: The model.evaluate line at the last is the only difference from model 1
def train_and_test_loop1(iterations, lr, Lambda, verb=True):
​
    ## hyperparameters
    iterations = iterations
    learning_rate = lr
    hidden_nodes = 256
    output_nodes = 10
​
    model = Sequential()
    model.add(Dense(hidden_nodes, input_shape=(784,), activation='relu'))
    model.add(Dense(hidden_nodes, activation='relu'))
    model.add(Dense(output_nodes, activation='softmax', kernel_regularizer=regularizers.l2(Lambda)))
    
    sgd = optimizers.SGD(lr=learning_rate, decay=1e-6, momentum=0.9)
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
    
    # Fit the model
    model.fit(X_train, y_train, epochs=iterations, batch_size=1000, verbose= 1)
    score = model.evaluate(X_train, y_train, verbose=0)
    
    return score
10. Next steps
Double Check that the loss is reasonable
Disable the regularization (Lambda = 0)
lr = 0.00001
Lambda = 0
train_and_test_loop(1, lr, Lambda)
Question
Is the loss range correct? What about accuracy, does it make sense for an untrained network
Answer
Absolutely! There are 10 output classes and the model is correctly predicting 1 up on 10 times (1/10 = 0.1% approx) as it is untrained.
11. Now, lets crank up the Lambda(Regularization)and check what it does to our loss function.
lr = 0.00001
Lambda = 1e3
train_and_test_loop(1, lr, Lambda)
loss went up. Good! (Another sanity check)

12. Now, lets overfit to a small subset of our dataset, in this case 20 images, to ensure our model architecture is good
X_train_subset = X_train[0:20]
y_train_subset = y_train[0:20]
X_train = X_train_subset
y_train = y_train_subset
X_train.shape
y_train.shape
Tip: Make sure that you can overfit very small portion of the training data
So, set a small learning rate and turn regularization off

In the code below:

Take the first 20 examples from MNIST
turn off regularization(reg=0.0)
use simple vanilla 'sgd'
Lets try and run for 500 iterations as the data set is very small

lr = 0.001
Lambda = 0
train_and_test_loop(500, lr, Lambda)
Very small loss, train accuracy going to 100, nice! We are successful in overfitting. The model architecture looks fine. Lets go for fine tuning it.
Loading the original dataset again
Import dataset
This dataset can be imported
High level API Keras has some datasets available
mnist.load_data() returns two tuples (x_train, y_train), (x_test, y_test):
x_train, x_val: uint8 array of grayscale image data with shape (num_samples, 28, 28)
y_train, y_val: uint8 array of digit labels (integers in range 0-9) with shape (num_samples,).
(X_train, y_train), (X_val, y_val) = tensorflow.keras.datasets.fashion_mnist.load_data()
Reshape features
reshape() method gives a new shape to an array without changing its data
You can read more about it here https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html
X_train = X_train.reshape(60000, 784)
print(X_train.shape)
X_val = X_val.reshape(10000, 784)
print(X_val.shape)
Normalize features
Normalize features from 0-255 to 0-1
X_train = X_train / 255.0
X_val = X_val / 255.0
One-hot encode the class vector
convert class vectors (integers) to binary class matrix
convert X_train and X_val
number of classes: 10
y_train = tensorflow.keras.utils.to_categorical(y_train, num_classes=10)
y_val = tensorflow.keras.utils.to_categorical(y_val, num_classes=10)
13. Start with small regularization and find learning rate that makes the loss go down.
we start with Lambda(small regularization) = 1e-7
we start with a small learning rate = 1e-7
lr = 1e-7
Lambda = 1e-7
train_and_test_loop(20, lr, Lambda)
Loss barely changing. Learning rate is probably too low.
14. Okay now lets try a (larger) learning rate 1e6. What could possibly go wrong?
Learning rate lr = 1e8
Regularization lambda = 1e-7
lr = 1e8
Lambda = 1e-7
train_and_test_loop(20, lr, Lambda)
Loss exploding. Learning rate is too high.
Cost is very high. Always means high learning rate
15. Lets try to train now with a value of learning rate between 1e-7 and 1e8
learning rate = 1e4
regularization remains the small, lambda = 1e-7
lr = 1e4
Lambda = 1e-7
train_and_test_loop(20, lr, Lambda)
Still too high learning rate. Loss is not decreasing. The rough range of learning rate we should be cross validating is somewhere between [1e3 to 1e-7]
Hyperparameter Optimization
Cross validation Strategy
Do coarse -> fine cross-validation in stages

First stage: only a few epochs to get rough idea of what params work

Second stage: longer running time, finer search

… (repeat as necessary)

Tip for detecting explosions in the solver:
If the cost is ever > 3 * original cost, break out early
16. Run coarse search for 10 times with different lr and Lambda values each with 100 epochs.
import math
for k in range(1,10):
    lr = math.pow(10, np.random.uniform(-7.0, 3.0))
    Lambda = math.pow(10, np.random.uniform(-7,-2))
    best_acc = train_and_test_loop1(100, lr, Lambda, False)
    print("Try {0}/{1}: Best_val_acc: {2}, lr: {3}, Lambda: {4}\n".format(k, 100, best_acc, lr, Lambda))
17. Now run finer search
import math
for k in range(1,5):
    lr = math.pow(10, np.random.uniform(-4.0, -1.0))
    Lambda = math.pow(10, np.random.uniform(-4,-2))
    best_acc = train_and_test_loop1(100, lr, Lambda, False)
    print("Try {0}/{1}: Best_val_acc: {2}, lr: {3}, Lambda: {4}\n".format(k, 100, best_acc, lr, Lambda))
alt text### Running deep with lr=0.02 and Lambda=1e-4

lr = 2e-2
Lambda = 1e-4
train_and_test_loop1(100, lr, Lambda)

########################################################################################################################################################################
#4_ImageProcessing_Session4_Faculty_Notebook_ImageProcessing-1.ipynb

import cv2
import pandas as pd import numpy as np import matplotlib.pyplot as plt

# Dataset link
#https://drive.google.com/drive/folders/1L3xiKJAe5XgobQGV-CFShJoss8h1NakC?usp=sharing
​
# This script was deleveped on google colab. Some minor changes required to execute the same in local machine.
cv2.__version__
# For working in colab, we need to mount the google drive, so that we can access any data file from the drive
from google.colab import drive
drive.mount('/content/drive')
#loading the file from content drive location
img=cv2.imread('/content/drive/MyDrive/open_cv_images/cameraman.png')
img.shape
from google.colab.patches import cv2_imshow
​
#cv2.imshow('screen1',img)
#cv.waitKey(0)
#cv2.destroyAllWindows()
​
# the above three lines is for displaying an image in local machine using open cv
cv2_imshow(img)
img=img[:,:,0]
img.shape
img.dtype
# Increase the brightness of the image
img1=img.astype('float')
img2=img1+100
img2[img2>255]=255
img1[0,0],img2[0,0]
res_img=np.hstack((img1,img2))
cv2_imshow(res_img)
# Increase the brightness of the image
img1=img.astype('float')
img2=0.5*img1+100
img2[img2>255]=255
res_img=np.hstack((img1,img2))
cv2_imshow(res_img)
imgn=img1/255 # scaled
img_log=np.log(imgn)
#cv2_imshow(img_log)
#res_img=np.hstack((img1,img2,img_log))
plt.imshow(img_log,cmap='gray')
img3=255-img1
cv2_imshow(img3)
# Histogram Equilization
# Histogram Specification
# Adaptive Histogram equilization
fruit=cv2.imread('/content/drive/MyDrive/open_cv_images/low_contrast_fruit_basket.jpg',0)
fruit.shape
fruit.min(),fruit.max()
cv2_imshow(fruit)
​
img_eq=cv2.equalizeHist(fruit)
res=np.hstack((fruit,img_eq))
cv2_imshow(res)
plt.hist(img_eq.ravel(),256,[0,256])
plt.show()
lung=cv2.imread('/content/drive/MyDrive/open_cv_images/noisy_lung.jpg',0)
cv2_imshow(lung)
mask=np.ones((3,3),dtype='float')/9
filt=cv2.filter2D(lung,-1,mask)
cv2_imshow(filt)
lung1=cv2.imread('/content/drive/MyDrive/open_cv_images/3_nod.jpg',0)
cv2_imshow(lung1)
mask=np.matrix('-1 -1 -1;-1 8 -1;-1 -1 -1')
filt=cv2.filter2D(lung1,-1,mask)
cv2_imshow(filt)
img=cv2.imread('/content/drive/MyDrive/open_cv_images/mri_tumor1.jpg',0)
cv2_imshow(img)
plt.hist(img.ravel(),256,[0,256])
plt.show()
img=cv2.imread('/content/drive/MyDrive/open_cv_images/mri_tumor1.jpg',0)
img[img>140]=255
img[img<=140]=0
cv2_imshow(img)
#Morphological Operations
#Dilation, Erosion, clear border, skeltenization, thickining, thinning, areaopen, closing
se1=cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
mask=cv2.morphologyEx(img,cv2.MORPH_OPEN,se1)
cv2_imshow(mask)
# feature Extraction
# Shape feat, Texture feat, color feat
# Area of RoI = Number of pixels forming that RoI
ar=(mask!=0).sum()
ar
# Max Height and Max Width
# count the number of non zero pixels in each column in the image and pick the max count.
max_h=(mask!=0).sum(axis=0).max()
max_w=(mask!=0).sum(axis=1).max()
max_h,max_w
#eccentricity
ecc=max_h/max_w
ecc
# Permieter
m=np.matrix('-1 -1 -1;-1 8 -1;-1 -1 -1')
edge=cv2.filter2D(mask,-1,m)
cv2_imshow(edge)
peri=(edge!=0).sum()
peri
#centroid
mom=cv2.moments(mask)
x_cent=np.round(mom['m10']/mom['m00'])
y_cent=np.round(mom['m01']/mom['m00'])
print(x_cent,y_cent)
contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cnt=contours[0]
cnt_ar=cv2.contourArea(cnt)
cnt_ar
hull=cv2.convexHull(cnt)
hull_ar=cv2.contourArea(hull)
hull_ar
(x,y),rad=cv2.minEnclosingCircle(cnt)
rad
# Texture features
#mean, var, std, skew, 
img=cv2.imread('/content/drive/MyDrive/open_cv_images/mri_tumor1.jpg',0)
mask=mask/255
tum=img*mask
cv2_imshow(tum)
me=np.mean(tum[tum!=0])
me
sd=np.std(tum[tum!=0])
sd
import scipy.stats as stats
sk=stats.skew(tum[tum!=0])
sk
feat=np.array([ar,max_h,max_w,ecc,peri,x_cent,y_cent,cnt_ar,hull_ar,rad,me,sd,sk])
feat=pd.DataFrame(feat)
feat
#Say if u have 1000 images, u can calculate these 13 features for each image and can generate the dataset of size 1000x13
# frame the output coolum for each image with the help of radiologist report
# With this build any ML model to predict the cancerous nature of tumor

########################################################################################################################################################################
#4_MNIST_Model_S4_TakeHome_Solution_fashionMNIST_Final.ipynb

Fashion MNIST Dataset
Fashion-MNIST is a dataset of Zalando's article images consisting of a training set of 60,000 examples and a test set of 10,000 examples.

The classes are 'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'

Each example is a 28x28 grayscale image, associated with a label from 10 classes.The Fashion-MNIST dataset is one of the most common datasets used for image classification and accessible from many different sources. In fact, even Tensorflow and Keras allow us to import and download the Fashion-MNIST dataset directly from their API.

Firstly, let's select TensorFlow version 2.x in colab

1 . Install & Import the required packages
%tensorflow_version 2.x
import tensorflow
tensorflow.__version__
pip install keras_sequential_ascii
import os
import time
import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.constraints import maxnorm
from keras.optimizers import SGD
from keras.layers import Activation
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.normalization import BatchNormalization
from keras.utils import np_utils
from keras_sequential_ascii import sequential_model_to_ascii_printout
from keras import backend as K
#if K.backend()=='tensorflow':
#    K.set_image_dim_ordering("th")
​
# Import Tensorflow with multiprocessing for use 16 cores on plon.io
import tensorflow as tf
import multiprocessing as mp
​
# Initialize the random number generator
import random
random.seed(0)
​
# Ignore the warnings
import warnings
warnings.filterwarnings("ignore")
2 . Load the dataset & perform exploratory analysis on the dataset
2 .a. Import the Fashion MNIST dataset
Let's load MNIST dataset

fashion_mnist = keras.datasets.fashion_mnist
​
# the data, shuffled and split between train and test sets
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
2 .b. Print out the datashape of train & test
Print shape of the data
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)
2 .c. Visualize a particular image
X_train and X_test contain greyscale RGB codes (from 0 to 255) while y_train and y_test contains labels from 0 to 9 which represents which number they actually are.

Let's visualize some numbers using matplotlib

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
import matplotlib.pyplot as plt
%matplotlib inline
print("Label: {}".format(class_names [y_train[8000]]))
plt.imshow(X_train[8000], cmap='gray')
2 .d. Visualize a portion of the dataset
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(X_train[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[y_train[i]])
plt.show()
2 .e. Process the train & test data
Reshape train and test sets into compatible shapes
Sequential model in tensorflow.keras expects data to be in the format (n_e, n_h, n_w, n_c)
n_e= number of examples, n_h = height, n_w = width, n_c = number of channels
do not reshape labels
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)
Normalize data
we must normalize our data as it is always required in neural network models
we can achieve this by dividing the RGB codes with 255 (which is the maximum RGB code minus the minimum RGB code)
normalize X_train and X_test
make sure that the values are float so that we can get decimal points after division
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
​
X_train /= 255
X_test /= 255
Print shape of data and number of images
print shape of X_train
print number of images in X_train
print number of images in X_test
print("X_train shape:", X_train.shape)
print("Images in X_train:", X_train.shape[0])
print("Images in X_test:", X_test.shape[0])
print("Max value in X_train:", X_train.max())
print("Min value in X_train:", X_train.min())
​
One-hot encode the class vector
convert class vectors (integers) to binary class matrix
convert y_train and y_test
number of classes: 10
we are doing this to use categorical_crossentropy as loss
from tensorflow.keras.utils import to_categorical
​
y_train_s = to_categorical(y_train, num_classes=10)
y_test_s = to_categorical(y_test, num_classes=10)
​
print("Shape of y_train:", y_train_s.shape)
print("One value of y_train:", y_train_s[0])
3 . Build a classification model for the dataset
3 .a.Prepare a basic CNN (4 Layer) model
Initialize a sequential model again
define a sequential model
add 2 convolutional layers
no of filters: 32
kernel size: 3x3
activation: "relu"
input shape: (28, 28, 1) for first layer
flatten the data
add Flatten later
flatten layers flatten 2D arrays to 1D array before building the fully connected layers
add 2 dense layers
number of neurons in first layer: 128
number of neurons in last layer: number of classes
activation function in first layer: relu
activation function in last layer: softmax
we may experiment with any number of neurons for the first Dense layer; however, the final Dense layer must have neurons equal to the number of output classes
from tensorflow.keras.layers import Conv2D
​
model = Sequential()
model.add(Conv2D(filters=32, kernel_size=3, activation="relu", input_shape=(28, 28, 1)))
model.add(Conv2D(filters=32, kernel_size=3, activation="relu"))
model.add(Flatten())
model.add(Dense(128, activation="relu"))
model.add(Dense(10, activation="softmax"))
Compile and fit the model
let's compile our model
loss: "categorical_crossentropy"
metrics: "accuracy"
optimizer: "adam"
then next step will be to fit model
give train data - training features and labels
batch size: 32
epochs: 10
give validation data - testing features and labels
3 .b. Fit the model in the data
# Compile the model
model.compile(loss="categorical_crossentropy", metrics=["accuracy"], optimizer="adam")
​
# Fit the model
model.fit( x=X_train, y=y_train_s, batch_size=32, epochs=10, validation_split = 0.3)
4 . Evaluate the model
4 .a. Visualize the performance (Accuracy & Loss for both training & validation datda) of the model
Final loss and accuracy
model.evaluate(X_test, y_test_s)
5 .Prepare Model 2
5 .a. Develope the base model
Vanilla CNN + Pooling + Dropout
Initialize a sequential model again
define a sequential model
add 2 convolutional layers
no of filters: 32
kernel size: 3x3
activation: "relu"
input shape: (28, 28, 1) for first layer
add a max pooling layer of size 2x2
add a dropout layer
dropout layers fight with the overfitting by disregarding some of the neurons while training
use dropout rate 0.2
flatten the data
add Flatten later
flatten layers flatten 2D arrays to 1D array before building the fully connected layers
add 2 dense layers
number of neurons in first layer: 128
number of neurons in last layer: number of classes
activation function in first layer: relu
activation function in last layer: softmax
we may experiment with any number of neurons for the first Dense layer; however, the final Dense layer must have neurons equal to the number of output classes
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dropout, MaxPooling2D
​
# Initialize the model
model = Sequential()
​
# Add a Convolutional Layer with 32 filters of size 3X3 and activation function as 'relu' 
model.add(Conv2D(filters=32, kernel_size=3, activation="relu", input_shape=(28, 28, 1)))
​
# Add a Convolutional Layer with 32 filters of size 3X3 and activation function as 'relu' 
model.add(Conv2D(filters=32, kernel_size=3, activation="relu"))
​
# Add a MaxPooling Layer of size 2X2 
model.add(MaxPooling2D(pool_size=(2, 2)))
​
# Apply Dropout with 0.2 probability 
model.add(Dropout(rate=0.2))
​
# Flatten the layer
model.add(Flatten())
​
# Add Fully Connected Layer with 128 units and activation function as 'relu'
model.add(Dense(128, activation="relu"))
​
#Add Fully Connected Layer with 10 units and activation function as 'softmax'
model.add(Dense(10, activation="softmax"))
Compile and fit the model
let's compile our model
loss: "categorical_crossentropy"
metrics: "accuracy"
optimizer: "adam"
Use EarlyStopping
then next step will be to fit model
give train data - training features and labels
batch size: 32
epochs: 10
give validation data - testing features and labels
5 .b. Fit the model in the data
# Compile the model
model.compile(loss="categorical_crossentropy", metrics=["accuracy"], optimizer="adam")
​
# Use earlystopping
callback = tensorflow.keras.callbacks.EarlyStopping(monitor='val_accuracy', patience=2, min_delta=0.01)
​
# Fit the model
model.fit(x=X_train, y=y_train_s, batch_size=32, epochs=10, validation_data=(X_test, y_test_s), callbacks=[callback])
6 . Evaluate the modeluate the model 2
6 .a. Visualize the performance (Accuracy & Loss for both training & validation datda) of the model
Final loss and accuracy
model.evaluate(X_test, y_test_s)
6 .b. Visualize the model prediction
Let's visualize results using matplotlib

import matplotlib.pyplot as plt
%matplotlib inline
plt.imshow(X_test[200].reshape(28, 28), cmap='gray')
y_pred = model.predict(X_test[200].reshape(1, 28, 28, 1))
print("Predicted label:", class_names[y_pred.argmax()])
print("Softmax Outputs:", y_pred)
print(y_pred.sum())
7 .Store the Weights
# save weights to file
model.save_weights("fashion_MNIST_weights.h5")


########################################################################################################################################################################
#4_TransfromImage_Inclass-Session4-Solutions.ipynb

1. Load the image statue.jpg and print its shape and comemnt about its spatial and graylevel resolution
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
​
img=cv2.imread('statue.png',0)
print(img.shape)
print(img.max())
​
# Spatial resolution is 288 x 384 
# graylevel resolution is 8 bit, because to represent 252 levels 8 bit is required (2^8 = 256)
2. Darken the Image loaded in the first step
img1=img-50
img1[img1<0]=0
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.imshow('img1',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
3. Apply exponential and log transform on the image with differnt constants
imgg=img/255.
c=-1.2
img2=np.exp(c*imgg)
img3=np.log(1+imgg)
cv2.imshow('img',img2)
cv2.waitKey(0)
cv2.imshow('img1',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
4. Plot the histogram of the statue image and comment about the contrast nature of the image
plt.hist(img.ravel(),256,[0,256])
plt.show()
#### 5. Apply Histogram equlization and adaptive histogram eqilization to imporve the contrast of the image
equ=cv2.equalizeHist(img)
​
clahe = cv2.createCLAHE(clipLimit=10.0, tileGridSize=(4,4))
cl1 = clahe.apply(img)
​
res = np.hstack((img,equ,cl1)) 
cv2.imshow("adaptive histogram",res)
cv2.waitKey(0)
cv2.destroyAllWindows()
6. Load your passport image and visualize each color plane along with its histogram
img=cv2.imread('ballons.bmp')
imgb=img[:,:,0]
imgg=img[:,:,1]
imgr=img[:,:,2]
​
img1=img.copy()
img1[:,:,0]=imgb
img1[:,:,1]=0
img1[:,:,2]=0
cv2.imshow('blue_plane',img1)
cv2.waitKey(0)
​
img2=img.copy()
img2[:,:,0]=0
img2[:,:,1]=imgg
img2[:,:,2]=0
cv2.imshow('green_plane',img2)
cv2.waitKey(0)
​
img3=img.copy()
img3[:,:,0]=0
img3[:,:,1]=0
img3[:,:,2]=imgr
cv2.imshow('red_plane',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
7. Load the image 'leena.png'. Reduce the noise present in the image.
img=cv2.imread('leena.png',0)
kernel=np.ones((7,7),dtype="float")/49
filt = cv2.filter2D(img,-1,kernel)
​
plt.subplot(121),plt.imshow(img,'gray'),plt.title('Original')
​
plt.subplot(122),plt.imshow(filt,'gray'),plt.title('Averaging')
8. Load the image 'opencv.png' and extract only the edges from the images.
img=cv2.imread('opencv.png')
img=cv2.resize(img,(200,200))
grayim = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
​
kernel=np.matrix('-1 -1 -1; -1 8 -1; -1 -1 -1')
dst = cv2.filter2D(grayim,-1,kernel)
dst1=25*dst
cv2.imshow('original',img)
cv2.waitKey(0)
cv2.imshow('edges',dst1)
cv2.waitKey(0)
cv2.destroyAllWindows()
9. Segment only the elephant from the elephant.jpg image
a=cv2.imread('cheetha.jpg',0)
b = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
b=cv2.resize(a,(400,400))
c=b.copy()
c[(b>130)]=0
c[(b<=130)]=255
cv2.imshow('img',c)
cv2.waitKey(0)
cv2.destroyAllWindows()
10. Apply required morphological processing to clean the segmented image
se1 = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))
mask = cv2.morphologyEx(c, cv2.MORPH_OPEN, se1)
plt.imshow(mask,'gray')
11. Compute the area of the segmented Cheetha image. (If required crop the unwanted part)
mask1=mask[100:350,:] # to remove non cheeta part
plt.imshow(mask1,cmap='gray')
# area of the cheetha mask
ar=(mask1!=0).sum()
ar
12. Compute the height and width of the Cheetha
max_h=(mask1!=0).sum(axis=0).max()
print('Height',max_h)
​
max_w=(mask1!=0).sum(axis=1).max()
print('Width',max_w)
13 Compute the eccencity ratio of the cheetha
ecc=max_h/max_w
ecc
14 Compute the average diameter of the cheetha image (average of number of pixels in each row)
avg_dia=(mask1!=0).sum(axis=1).mean()
print('Average_dia',avg_dia)
15 Compute the Position of Cheetha in the image
m = cv2.moments(mask1)
 
x = np.round(m['m10']/m['m00'])
y = np.round(m['m01']/m['m00'])
print(x,y)
​
16 Frame the feature vector for Cheeta
cheetha1 = np.array([ar,max_h,max_w,ecc,avg_dia,x,y])
cheetha1
​


########################################################################################################################################################################
#5_CNN_Faculty_Notebook2_Session5_CNN_callback-1.ipynb

Import the tensorflow librabry and Load the MNIST dataset
import tensorflow as tf from tensorflow.keras.datasets import mnist (xtrain,ytrain),(xtest,ytest)=mnist.load_data()

#Scale the data
x_train=xtrain/255.
x_test=xtest/255.
#Visualize few samples
import matplotlib.pyplot as plt
plt.imshow(x_train[18,:,:],cmap='gray')
xtrain.shape
# CNN required data to be in the 4D
# first dimension is number of images
# second dimension is number of rows in the image
# Third dimension is number of columns in the image
# Fourth dimension is number of planes in the image( 1 for grayscale, 3 for color)
import numpy as np
xtrain1=np.expand_dims(x_train,3) 
xtest1=np.expand_dims(x_test,3)
xtrain1.shape
#Encode the target column
ytrain=tf.keras.utils.to_categorical(ytrain,num_classes=10)
ytest=tf.keras.utils.to_categorical(ytest,num_classes=10)
ytrain[0]
# import the libraries required for CNN
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense
#Define the architecture of CNN
classifier=Sequential()
​
classifier.add(Conv2D(16,(3,3),input_shape=(28,28,1),activation ='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))
​
classifier.add(Conv2D(32,(3,3),activation ='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))
​
classifier.add(Flatten())
​
classifier.add(Dense(units=64,activation='relu'))
classifier.add(Dense(units=10,activation='softmax'))
​
# compilation statergy for the model
classifier.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
# apply earlystopping callback to stop the iteration if there is no improvement in model performace 
                               #for few consecutive iteration defined by 'patience'
# apply model checkpoint callback to save the weights corresponds to the best iteration
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
​
keras_callback=[EarlyStopping(monitor='val_loss',patience=3,mode='min',min_delta=0.001),
               ModelCheckpoint('./Check_Point',monitor='val_loss',save_best_only=True)]
# fit (Train) the model with callbacks
classifier.fit(x=xtrain1,y=ytrain,batch_size=32,epochs=10,validation_split=0.2,callbacks=keras_callback)
# Save the weights, this weight we are going to use in out next experiment on Transfer Learning
classifier.save('my_digit_model.h5')

########################################################################################################################################################################
#5_CNN_Faculty_Notebook_Session5_CNN-1.ipynb

Convolution Neural Network (CNN)
#Dataset link:
#https://drive.google.com/drive/folders/1ESsfpI6sYTtHoUv8ihI0AJSOVgij6xfq?usp=sharing
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense
# Importing the libraries for the layers of CNN
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense
# Importing the library for image handling/preprocessing
from tensorflow.keras.preprocessing import image
# Image Augumentation
# create few more images by stretching, zooming, shrinking, rotating, flipping the available images
#This will make the model to learn very generically about the data
from tensorflow.keras.preprocessing.image import ImageDataGenerator
train_datagen=ImageDataGenerator(rescale=1/255.,
        rotation_range=45,     #Random rotation between 0 and 45
        width_shift_range=0.2,   #% shift
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='reflect')
test_datagen=ImageDataGenerator(rescale=1/255.) # We dont experiment the test data generally
# only scaling is enough for test data
# Laod the images from the train and test folders by resizing it for 128x128
#Image augumentaion defined above will be performed for each batch of images 
# class mode is "categorical" for multiclass problem ("binary" for binomial problem) 
training_set=train_datagen.flow_from_directory('C:/Users/Senthil/Desktop/DEEP_LEARNING/flower_photos/Training',
                                              target_size=(128,128),
                                              batch_size=128,
                                              class_mode='categorical')
​
# Total of 2736 images corresponds to 5 differnt classses are loaded in to this notebook 
                                                   #from the training folder (harddrive)
test_set=test_datagen.flow_from_directory('C:/Users/Senthil/Desktop/DEEP_LEARNING/flower_photos/Testing',
                                              target_size=(128,128),
                                              batch_size=128,
                                              class_mode='categorical')
​
# Total of 934 images corresponds to 5 differnt classses are loaded in to this notebook 
                                                   #from the testing folder (harddrive)
classifier = Sequential() # Sequentialy we are going to add the layers in this network
​
#Define the convolution layer with 16 kernals each of size 3x3
# This layer will accept the images of size 128x128x3
# Activation function for this layer is ReLU
classifier.add(Conv2D(16, (3, 3), input_shape = (128, 128, 3), activation = 'relu'))
​
#Maxpool layer generally defined at the end of each convolution layer. 
#Poolsize of 2x2 will bring down the feature map(convolution layer output) size by half
classifier.add(MaxPooling2D(pool_size = (2, 2)))
​
# Define the second convolution and maxpool layer
classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
​
#Third Convolution and Maxpool Layer
classifier.add(Conv2D(64, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
​
# Flatten the feature map produced by the last convolution layer as single vector
classifier.add(Flatten())
​
#Add the hidden layers
classifier.add(Dense(units = 128,activation = 'relu'))
​
# Output layer should have 5 neurons as this data is having 5 classes of flowers
#"Softmax" activation function is preferred for Multiclass problem 
classifier.add(Dense(units = 5, activation = 'softmax'))
#compile the CNN model with 'adam' optimizer to minimize the loss (cross entropy)
classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
# Fit(Train) the model using trainset of data
# How many time the weight needs to be updated in one iteratin will be decided by steps_per_epoch
# How many iteration for which the training need to be happen will be decided by 'epochs'
classifier.fit_generator(training_set,
                         steps_per_epoch =2736//128,
                         epochs = 3,
                         validation_data = test_set,
                         validation_steps = 934//128)
#Libraries for loading image and visualising the output of each layer
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt
from visualize_layer import visualize_layer
import warnings
warnings.filterwarnings('ignore')
img_path='C:\\Users\\Senthil\\Desktop\\DEEP_LEARNING\\flower_photos\\Training\\daisy\\21652746_cc379e0eea_m.jpg'
visualize_layer(img_path,classifier) # Function to visualize the output of each layer
# The first layer of CNN (i.e first convolution layer)
classifier.layers[0]
# output of the first layer
classifier.layers[0].output
#input of the CNN model
classifier.input
#Visuale the first layer output only (16 feature maps)
viz_model = tf.keras.models.Model(inputs = classifier.input, outputs = classifier.layers[0].output)
img = load_img(img_path, target_size=(128, 128))
x  = img_to_array(img)  
x=np.expand_dims(x,0)
x /= 255.0
feature_maps = viz_model.predict(x)
for i in range(0,feature_maps.shape[-1]):
    plt.imshow(feature_maps[:,:,:,i][0])
    plt.show()
classifier.summary()

########################################################################################################################################################################
#5_EDA_S5_TakeHome_Solution_Fashion_ImgNet_final.ipynb

Classification of a subset Image net data Transfer Learning from pre-trained Fashion MNIST CNN
ImageNet is an image database organized according to the WordNet hierarchy (currently only the nouns), in which each node of the hierarchy is depicted by hundreds and thousands of images. Currently we have an average of over five hundred images per node. We hope ImageNet will become a useful resource for researchers, educators, students and all of you who share our passion for pictures.

A subset of data on 'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot' have been collected from Imagenet.

The train and validation subsets can be combined to make a larger training set.

Note : -

For the sake of simplcity we have changed the format of the data and stored the data in a .npy format file.Which has the X_train , y_train ,X_test & y_test in a dictionary format.

1 .Load the dataset and Import the packages
Firstly, let's select TensorFlow version 2.x in colab

%tensorflow_version 2.x
import tensorflow
tensorflow.__version__
# Initialize the random number generator
import random
random.seed(0)
​
# Ignore the warnings
import warnings
warnings.filterwarnings("ignore")
As we are using google colab, we need to mount the google drive to load the data file

from google.colab import drive
drive.mount('/content/drive/')
Add path to the folder where your dataset is present

project_path = '/content/drive/MyDrive/My_DL/S5/TakeHome/'
Let's load the dataset now

import numpy as np
​
# Open the file as readonly
data = np.load(project_path + 'Img-Net_10.npy',allow_pickle='TRUE').item()
​
# Load the training, test and validation set
X_train = data['X_train']
y_train = data['y_train']
X_test = data['X_test']
y_test = data['y_test']
​
2 . Perform exploratory analysis on the dataset
2 .a. Print out the datashape of train & test
# Declare variables
​
batch_size = 32 # 32 examples in a mini-batch, smaller batch size means more updates in one epoch
num_classes = 10 #
epochs = 200 # repeat 200 times
data_augmentation = True
​
print('X_train shape : ',X_train.shape)
print('y_train shape : ',len(y_train))
print('X_test shape : ',X_test.shape)
print('y_test shape : ',len(y_test))
​
# Here are the classes in the dataset, as well as 10 random images from each
​
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
​
2 .b. Visualize a particular image
import matplotlib.pyplot as plt
plt.figure(figsize = (2,2))
%matplotlib inline
print("Label: {}".format(y_train[150]))
plt.imshow(X_train[150], cmap='gray')
# Print figure with 10 random images from each
​
fig = plt.figure(figsize=(5,5))
for i in range(num_classes):
  ax = fig.add_subplot(2, 5, 1 + i, xticks=[], yticks=[])
  img_num = np.random.randint(X_train.shape[0])
  ax.imshow(X_train[img_num], cmap='gray')
  ax.set(xlabel=y_train[img_num])
 
plt.show()
2 .c. Visualize a portion of the dataset
3 . Process the dataset
3 .a. Print the shape of training and testing data
print("X_train shape:", X_train.shape)
print("y_train shape:", len(y_train))
print("X_test shape:", X_test.shape)
print("y_test shape:", len(y_test))
code = {'T-shirt/top' : 0, 'Trouser': 1, 'Pullover': 2, 'Dress': 3, 'Coat': 4,
               'Sandal': 5, 'Shirt': 6, 'Sneaker': 7, 'Bag': 8, 'Ankle boot': 9}
import pandas as pd
​
y_train_label = y_train
y_train = list(pd.Series(y_train).replace(code))
y_train = np.array(y_train)
​
y_test_label = y_test
y_test = list(pd.Series(y_test).replace(code))
y_test = np.array(y_test)
​
print("Shape of y_train:", y_train.shape)
print("One value of y_train:", y_train[0])
3 .b. Let's check out the dataset
%matplotlib inline
import matplotlib.pyplot as plt
​
columns = 10
rows = 10
​
fig=plt.figure(figsize=(8, 8))
​
for i in range(1, columns*rows + 1):
    img = X_test[i]
    fig.add_subplot(rows, columns, i)
    print (y_test_label[i], end=' ')
    if i % columns == 0:
      print ("")
    plt.imshow(img, cmap='gray')
​
plt.show()
3 .c. Resize all the train and test inputs to 28X28, to match with MNIST CNN model's input size
3 .c.i. Preproccess the data
# Importing OpenCV module for the resizing function
import cv2
import numpy as np
​
# Create a resized dataset for training and testing inputs with corresponding size
# Here we are resizing it to 28X28 (same input size as MNIST)
X_train_resized = np.zeros((X_train.shape[0], 28, 28))
for i in range(X_train.shape[0]):
  #using cv2.resize to resize each train example to 28X28 size using Cubic interpolation
  X_train_resized[i,:,:] = cv2.resize(X_train[i], dsize=(28, 28), interpolation=cv2.INTER_CUBIC)
​
X_test_resized = np.zeros((X_test.shape[0], 28, 28))
for i in range(X_test.shape[0]):
  #using cv2.resize to resize each test example to 28X28 size using Cubic interpolation
  X_test_resized[i,:,:] = cv2.resize(X_test[i], dsize=(28, 28), interpolation=cv2.INTER_CUBIC)
  
# We don't need the original dataset anynmore so we can clear up memory consumed by original dataset
del(X_train, X_test)
3 .c.ii. Reshape train and test sets into compatible shapes
Sequential model in tensorflow.keras expects data to be in the format (n_e, n_h, n_w, n_c)
n_e= number of examples, n_h = height, n_w = width, n_c = number of channels
do not reshape labels
X_train = X_train_resized.reshape(X_train_resized.shape[0], 28, 28,1)
X_test = X_test_resized.reshape(X_test_resized.shape[0], 28, 28,1)
We can delete X_train_resized and X_test_resized variables as we are going to use X_train and X_test variables going further

del(X_train_resized, X_test_resized)
3 .c.iii. Normalize data
we must normalize our data as it is always required in neural network models
we can achieve this by dividing the RGB codes with 255 (which is the maximum RGB code minus the minimum RGB code)
normalize X_train and X_test
make sure that the values are float so that we can get decimal points after division
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
​
X_train /= 255
X_test /= 255
2 .c.iv. Print shape of data and number of images
print shape of X_train
print number of images in X_train
print number of images in X_test
print("X_train shape:", X_train.shape)
print("Images in X_train:", X_train.shape[0])
print("Images in X_test:", X_test.shape[0])
3 .c.vi. One-hot encode the class vector
convert class vectors (integers) to binary class matrix
convert y_train and y_test
number of classes: 10
we are doing this to use categorical_crossentropy as loss
from tensorflow.keras.utils import to_categorical
​
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)
​
print("Shape of y_train:", y_train.shape)
print("One value of y_train:", y_train[0])
Let's see one example after one-hot encoding

3 .d. Visualize an iage from the data
print("Label: ", y_train_label[100])
plt.imshow(X_train[100].reshape(28,28), cmap='gray')
4 . Build a classification model for the dataset
4 .a. Vanilla CNN + Pooling + Dropout
Initialize a sequential model again
define a sequential model
add 2 convolutional layers
no of filters: 32
kernel size: 3x3
activation: "relu"
input shape: (28, 28, 1) for first layer
add a max pooling layer of size 2x2
add a dropout layer
dropout layers fight with the overfitting by disregarding some of the neurons while training
use dropout rate 0.2
flatten the data
add Flatten later
flatten layers flatten 2D arrays to 1D array before building the fully connected layers
add 2 dense layers
number of neurons in first layer: 128
number of neurons in last layer: number of classes
activation function in first layer: relu
activation function in last layer: softmax
we may experiment with any number of neurons for the first Dense layer; however, the final Dense layer must have neurons equal to the number of output classes
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dropout, MaxPooling2D
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
​
# Initialize the model
model = Sequential()
​
# Add a Convolutional Layer with 32 filters of size 3X3 and activation function as 'relu' 
model.add(Conv2D(filters=32, kernel_size=3, activation="relu", input_shape=(28, 28, 1)))
​
# Add a Convolutional Layer with 32 filters of size 3X3 and activation function as 'relu' 
model.add(Conv2D(filters=32, kernel_size=3, activation="relu"))
​
# Add a MaxPooling Layer of size 2X2 
model.add(MaxPooling2D(pool_size=(2, 2)))
​
# Apply Dropout with 0.2 probability 
model.add(Dropout(rate=0.2))
​
# Flatten the layer
model.add(Flatten())
​
# Add Fully Connected Layer with 128 units and activation function as 'relu'
model.add(Dense(128, activation="relu"))
​
#Add Fully Connected Layer with 10 units and activation function as 'softmax'
model.add(Dense(10, activation="softmax"))
4 .b. Make only dense layers trainable
freeze the initial convolutional layer weights and train only the dense (FC) layers
set trainalble = False for all layers other than Dense layers
for layers in model.layers:
    if('dense' not in layers.name):
        layers.trainable = False
    if('dense' in layers.name):
        print(layers.name + ' is trained')
4 .c. Load pre-trained weights from Fashion MNIST CNN model
load the file named fashion_MNIST_weights.h5
model.load_weights(project_path + 'fashion_MNIST_weights.h5')
4 .d. Compile the model
loss: "categorical_crossentropy"
metrics: "accuracy"
optimizer: "adam"
# Compile the model
model.compile(loss="categorical_crossentropy", metrics=["accuracy"], optimizer="adam")
5 . Evaluate this model
model.evaluate(X_test, y_test)
6 . Training the CNN
6 .a. Fit the model to the CINIC-10 dataset
Use early stopping
fit the model
give train data - training features and labels
batch size: 32
epochs: 10
give validation data - testing features and labels
# Use earlystopping
callback = tensorflow.keras.callbacks.EarlyStopping(monitor='val_accuracy', patience=2, min_delta=0.01)
​
# Fit the model
model.fit(x=X_train, y=y_train, batch_size=32, epochs=15, validation_data=(X_test, y_test), callbacks=[callback])
7 . Evaluate this model
7 .a. Final loss and accuracy
model.evaluate(X_test, y_test)
7 .b. Visualizing some predictions
plt.figure(figsize=(2,2))
plt.imshow(X_test[3].reshape(28,28), cmap='gray')
plt.show()
print("Preiction for above image: ", class_names[np.argmax(model.predict(X_test[3].reshape(1,28,28,1)))])
​
​
plt.figure(figsize=(2,2))
plt.imshow(X_test[50].reshape(28,28), cmap='gray')
plt.show()
print("Preiction for above image: ", class_names[np.argmax(model.predict(X_test[50].reshape(1,28,28,1)))])
​
​
plt.figure(figsize=(2,2))
plt.imshow(X_test[700].reshape(28,28), cmap='gray')
plt.show()
print("Preiction for above image: ", class_names[np.argmax(model.predict(X_test[700].reshape(1,28,28,1)))])
​
​
plt.figure(figsize=(2,2))
plt.imshow(X_test[590].reshape(28,28), cmap='gray')
plt.show()
print("Preiction for above image: ", class_names[np.argmax(model.predict(X_test[590].reshape(1,28,28,1)))])
​
​
plt.figure(figsize=(2,2))
plt.imshow(X_test[800].reshape(28,28), cmap='gray')
plt.show()
print("Preiction for above image: ", class_names[np.argmax(model.predict(X_test[800].reshape(1,28,28,1)))])
8 . Saving the CNN
Save the trained weights and model in h5 files
! pwd
%cd /content/drive/MyDrive/My_DL/S5/TakeHome/
! pwd
#Set the path where you want to store the model and weights 
model.save('cnn_ImgNet.h5')
model.save_weights('cnn_ImgNet_weights.h5')

########################################################################################################################################################################
#6_Sangakara_S6_TakeHome_Solution_Player_Final-1.ipynb

1 . 700 annotations of Kumar Sangakkara's face dataset
1 .a. Context
Recently I have been working on some object localization problems using Convolutional Nets and I wanted to try train the model on a new dataset other than the very common COCO or PASCAL VOC datasets. While pondering on what object to compile a small dataset around, I thought of pushing the challenge a bit more to see if the same model can be trained to localize faces. Having this in mind I wanted a dataset of a person's face annotations.

As you may know with Deep Learning models, the more data you have the more accuracy you reach. So considering the challenge to detect a face I wanted a considerable number of images of the same face that the model should be trained on.

Hence, I needed many pictures of the same person. So the person had to be famous so I could easily find many pictures. So being in Sri Lanka where else to look other than our Cricket stars. So I chose the living legend in Sri Lankan Cricket, Kumar Sangakkara.

1 .b. Content
I downloaded around 1000 images from google images and after manual cleaning ended up with 704, which are contained here. I manually annotated all the pictures using a python script to generate the xml files. (Yeah, I couldn't find a better thing to do in that 2 hours.) Now here is the dataset for anyone to make use of.

1 .c. Inspiration
So as I mentioned in the above description, my goal with this dataset was to see if an object localization model can be used to detect a face of a person. Even though I have the pipeline, I couldn't still thoroughly test its performance using a GPU. So anyone whose interested can use this dataset to test those results. Also if these annotations can be useful for any other application, feel free to use it and share it. Have fun!

1 .d. Link to dataset:
https://www.kaggle.com/mirantha/sangaface/

1 .e. Note:
For the simplicity of the data, we have convered the .xml format to .csv fomat.In the data set we have images.zip (where we have images as .png files) , train.csv (where we have path, image_height, image_width, x_min, y_min, x_max, y_max ) and validation.csv (where we have path, image_height, image_width, x_min, y_min, x_max, y_max )

2 .Load the dataset and Import the packages
2 .a. Import the packages
Firstly, let's select TensorFlow version 2.x in colab

%tensorflow_version 2.x
import tensorflow
tensorflow.__version__
# Initialize the random number generator
import random
random.seed(0)
​
# Ignore the warnings
import warnings
warnings.filterwarnings("ignore")
2 .b. Load the dataset
As we are using google colab, we need to mount the google drive to load the data file

from google.colab import drive
drive.mount('')
Add path to the folder where your dataset files are

project_path = 'D:/'
Let's load the dataset now

images_zip_path = project_path + "images.zip"
​
from zipfile import ZipFile
​
with ZipFile(images_zip_path, 'r') as z:
  z.extractall()
DATASET_FOLDER = "./images/"
TRAIN_CSV = project_path + "train.csv"
VALIDATION_CSV = project_path + "validation.csv"
2 .c. Get training data
import numpy as np
import csv
​
IMAGE_SIZE = 128 # Image sizes can vary (128, 160, 192, 224). MobileNetV2 can also take 96
​
with open(TRAIN_CSV, "r") as f:
  
  y_train = np.zeros((sum(1 for line in f), 4))
  X_train = []
  f.seek(0)
  data = csv.reader(f, delimiter=',')
  for index, row in enumerate(data):
    for i, r in enumerate(row[1:7]):
      if r != '':
        row[i+1] = int(r)
      else :
        row[i+1] = 0
    path, image_height, image_width, x0, y0, x1, y1 = row       # Read image, its dimensions, BBox coords
    path = "./"  + path.split('/')[-3] + "/" + path.split('/')[-2] + "/" + path.split('/')[-1]
    y_train[index, 0] = x0 * IMAGE_SIZE / image_width                 # Normalize bounding box by image size
    y_train[index, 1] = y0 * IMAGE_SIZE / image_height                # Normalize bounding box by image size
    y_train[index, 2] = (x1 - x0) * IMAGE_SIZE / image_width          # Normalize bounding box by image size
    y_train[index, 3] = (y1 - y0) * IMAGE_SIZE / image_height         # Normalize bounding box by image size
​
    X_train.append(path)                                              # All training images in this list
X_train[:5]
2 .d. Let's check how does the data look like
Fetching coordinates details

import cv2
# Pick a random image to check how it looks
filename = X_train[0]
unscaled = cv2.imread(filename)
region = y_train[0]
image_height, image_width, _ = unscaled.shape
x0 = int(region[0] * image_width / IMAGE_SIZE) # Scale the BBox
y0 = int(region[1] * image_height / IMAGE_SIZE)
​
x1 = int((region[0] + region[2]) * image_width / IMAGE_SIZE)
y1 = int((region[1] + region[3]) * image_height / IMAGE_SIZE)
2 .e. Visualize a particular image
Now, let's plot the image and the bounding box on top of it

import matplotlib.pyplot as plt
import matplotlib.patches as patches
​
# Create figure and axes
fig,ax = plt.subplots(1)
​
# Display the image
ax.imshow(unscaled)
​
# Create a Rectangle patch
rect = patches.Rectangle((x0, y0), x1 - x0, y1 - y0, linewidth=2, edgecolor='r', facecolor='none')
​
# Add the patch to the Axes
ax.add_patch(rect)
​
plt.show()
3 . Process the dataset
3 .a. Back to data preparation
from PIL import Image
from tensorflow.keras.applications.mobilenet import preprocess_input
​
for i, f in enumerate(X_train):
  img = Image.open(f) # Read image
  img = img.resize((IMAGE_SIZE, IMAGE_SIZE)) # Resize image
  img = img.convert('RGB')
​
  X_train[i] = preprocess_input(np.array(img, dtype=np.float32)) # Convert to float32 array
  img.close()
X_train = np.array(X_train)
X_train.shape
y_train
y_train.shape
3 .b. Data preperation for validation data
with open(VALIDATION_CSV, "r") as f:
  
  y_val = np.zeros((sum(1 for line in f), 4))
  X_val = []
  f.seek(0)
  data = csv.reader(f, delimiter=',')
  for index, row in enumerate(data):
    for i, r in enumerate(row[1:7]):
      if r != '':
        row[i+1] = int(r)
      else :
        row[i+1] = 0
    path, image_height, image_width, x0, y0, x1, y1 = row     # Read image, its dimensions, BBox coords
    path = "./" + path.split('/')[-3] + "/" + path.split('/')[-2] + "/" + path.split('/')[-1]
    y_val[index, 0] = x0 * IMAGE_SIZE / image_width                 # Normalize bounding box by image size
    y_val[index, 1] = y0 * IMAGE_SIZE / image_height                # Normalize bounding box by image size
    y_val[index, 2] = (x1 - x0) * IMAGE_SIZE / image_width          # Normalize bounding box by image size
    y_val[index, 3] = (y1 - y0) * IMAGE_SIZE / image_height         # Normalize bounding box by image size
​
    X_val.append(path)                                                # All training images in this list
X_val[:5]
for i, f in enumerate(X_val):
  img = Image.open(f) # Read image
  img = img.resize((IMAGE_SIZE, IMAGE_SIZE)) # Resize image
  img = img.convert('RGB')
​
  X_val[i] = preprocess_input(np.array(img, dtype=np.float32)) # Convert to float32 array
  img.close()
X_val = np.array(X_val)
X_val.shape
y_val
y_val.shape
4 . Build an Object Localizing model for the dataset
4 .a. Create the model
from tensorflow.keras.applications.mobilenet import MobileNet
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Conv2D, Reshape
​
ALPHA = 1.0 # Width hyper parameter for MobileNet (0.25, 0.5, 0.75, 1.0). Higher width means more accurate but slower
​
def create_model(trainable=True):
    model = MobileNet(input_shape=(IMAGE_SIZE, IMAGE_SIZE, 3), include_top=False, alpha=ALPHA) # Load pre-trained mobilenet
    # Do not include classification (top) layer
​
    # to freeze layers, except the new top layer, of course, which will be added below
    for layer in model.layers:
        layer.trainable = trainable
​
    # Add new top layer which is a conv layer of the same size as the previous layer so that only 4 coords of BBox can be output
    x0 = model.layers[-1].output
    x1 = Conv2D(4, kernel_size=4, name="coords")(x0)
    # In the line above kernel size should be 3 for img size 96, 4 for img size 128, 5 for img size 160 etc.
    x2 = Reshape((4,))(x1) # These are the 4 predicted coordinates of one BBox
​
    return Model(inputs=model.input, outputs=x2)
5 . Evaluate this model
5 .a. Define evaluation metric
def IOU(y_true, y_pred):
    intersections = 0
    unions = 0
    # set the types so we are sure what type we are using
​
    gt = y_true
    pred = y_pred
    # Compute interection of predicted (pred) and ground truth (gt) bounding boxes
    diff_width = np.minimum(gt[:,0] + gt[:,2], pred[:,0] + pred[:,2]) - np.maximum(gt[:,0], pred[:,0])
    diff_height = np.minimum(gt[:,1] + gt[:,3], pred[:,1] + pred[:,3]) - np.maximum(gt[:,1], pred[:,1])
    intersection = diff_width * diff_height
​
    # Compute union
    area_gt = gt[:,2] * gt[:,3]
    area_pred = pred[:,2] * pred[:,3]
    union = area_gt + area_pred - intersection
​
    # Compute intersection and union over multiple boxes
    for j, _ in enumerate(union):
      if union[j] > 0 and intersection[j] > 0 and union[j] >= intersection[j]:
        intersections += intersection[j]
        unions += union[j]
​
    # Compute IOU. Use epsilon to prevent division by zero
    iou = np.round(intersections / (unions + tensorflow.keras.backend.epsilon()), 4)
    # This must match the type used in py_func
    iou = iou.astype(np.float32)
    return iou
def IoU(y_true, y_pred):
    iou = tensorflow.py_function(IOU, [y_true, y_pred], Tout=tensorflow.float32)
    return iou
5 .b. Initialize the model and print summary
model = create_model(False) # Arg is False, if you want to freeze lower layers for fast training (but low accuracy)
model.summary() # Print summary
5 .c. Compile the model
loss: "mean_squared_error"
metrics: IoU
optimizer: "adam"
# Compile the model
model.compile(loss="mean_squared_error", optimizer="adam", metrics=[IoU]) # Regression loss is MSE
6 . Train model 2
6 .a. Training the model
Fit the model to the dataset

Use early stopping
fit the model
give train data - training features and labels
batch size: 32
epochs: 10
give validation data - testing features and labels
# Use earlystopping
import tensorflow 
callback = tensorflow.keras.callbacks.EarlyStopping(monitor='val_IoU', patience=5, min_delta=0.01)
​
# Fit the model
model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10, batch_size=32, callbacks=[callback])
7 . Evaluate this model
7 .a. Final loss and accuracy
model.evaluate(X_val, y_val)
7 .b. Model evaluation on Validation data
7 .b.i. Test the model on an image from validation data
# Pick a test image, run model, show image, and show predicted bounding box overlaid on the image
filename = './Image/validation/000022.png'
​
unscaled = cv2.imread(filename) # Original image for display
image_height, image_width, _ = unscaled.shape
image = cv2.resize(unscaled, (IMAGE_SIZE, IMAGE_SIZE)) # Rescaled image to run the network
feat_scaled = preprocess_input(np.array(image, dtype=np.float32))
print ("Size of original input: ", image.shape)
print("-------------------------------")
print("Size of scaled input: ", feat_scaled.shape)
region = model.predict(x=np.array([feat_scaled]))[0] # Predict the BBox
7 .b.ii. Fetching coordinates details from predicted result
x0 = int(region[0] * image_width / IMAGE_SIZE) # Scale the BBox
y0 = int(region[1] * image_height / IMAGE_SIZE)
​
x1 = int((region[0] + region[2]) * image_width / IMAGE_SIZE)
y1 = int((region[1] + region[3]) * image_height / IMAGE_SIZE)
7 .b.iii. Now, let's plot the image and the bounding box on top of it
# Create figure and axes
fig,ax = plt.subplots(1)
​
# Display the image
ax.imshow(unscaled)
​
# Create a Rectangle patch
rect = patches.Rectangle((x0, y0), x1 - x0, y1 - y0, linewidth=2, edgecolor='r', facecolor='none')
​
# Add the patch to the Axes
ax.add_patch(rect)
​
plt.show()
7 .c. Model evaluation on 2nd Validation data
7 .c.i. Test the model on second image from validation data
# Pick a test image, run model, show image, and show predicted bounding box overlaid on the image
filename = './Image/validation/000007.png'
​
unscaled = cv2.imread(filename) # Original image for display
image_height, image_width, _ = unscaled.shape
image = cv2.resize(unscaled, (IMAGE_SIZE, IMAGE_SIZE)) # Rescaled image to run the network
feat_scaled = preprocess_input(np.array(image, dtype=np.float32))
region = model.predict(x=np.array([feat_scaled]))[0] # Predict the BBox
7 .c.ii. Fetching coordinates details
x0 = int(region[0] * image_width / IMAGE_SIZE) # Scale the BBox
y0 = int(region[1] * image_height / IMAGE_SIZE)
​
x1 = int((region[0] + region[2]) * image_width / IMAGE_SIZE)
y1 = int((region[1] + region[3]) * image_height / IMAGE_SIZE)
7 .c.iii. Now, let's plot the second image and the bounding box on top of it
# Create figure and axes
fig,ax = plt.subplots(1)
​
# Display the image
ax.imshow(unscaled)
​
# Create a Rectangle patch
rect = patches.Rectangle((x0, y0), x1 - x0, y1 - y0, linewidth=2, edgecolor='r', facecolor='none')
​
# Add the patch to the Axes
ax.add_patch(rect)
​
plt.show()
​

########################################################################################################################################################################
#6_SVHN_TransferLearning_Faculty_Notebook_Session6_Transfer_Learning_workout1-1.ipynb

Classification of SVHN using Transfer Learning from pre-trained MNIST CNN
The Street View House Numbers (SVHN) Dataset
SVHN is a real-world image dataset for developing machine learning and object recognition algorithms with minimal requirement on data preprocessing and formatting. It can be seen as similar in flavor to MNIST (e.g., the images are of small cropped digits), but incorporates an order of magnitude more labeled data (over 600,000 digit images) and comes from a significantly harder, real world problem (recognizing digits and numbers in natural scene images). SVHN is obtained from house numbers in Google Street View images.

10 classes, 1 for each digit. Digit '1' has label 1, '9' has label 9 and '0' has label 0.

73257 digits for training, 26032 digits for testing, and 531131 additional, somewhat less difficult samples, to use as extra training data

Comes in two formats:

Original images with character level bounding boxes.
MNIST-like 32-by-32 images centered around a single character (many of the images do contain some distractors at the sides).
The dataset that we will be using in this notebook contains 42000 training samples and 18000 testing samples

Dataset link : https://www.kaggle.com/sasha18/street-view-house-nos-h5-file

#import tensorflow
import tensorflow as tf
import h5py
#The SVHN dataset is provided in the form of h5. We can extract the data as train and test
                                                                #using the following script. 
import h5py
​
data=h5py.File('SVHN_single_grey1.h5','r')
​
X_train=data['X_train'][:]
y_train=data['y_train'][:]
​
X_test=data['X_test'][:]
y_test=data['y_test'][:]
​
data.close()
#scaling the data
x_train=X_train/255.
x_test=X_test/255.
x_train.shape
import matplotlib.pyplot as plt
plt.imshow(x_train[20,:,:],cmap='gray')
y_train[20]
​
# Resize the images as 28x28 
#(MNIST dataset size is 28x28, as we are using the MNIST model weight, 
                                                     #we need to resize these images as 28x28 )
import cv2
import numpy as np
X_train_resize=np.zeros((42000,28,28))
​
for i in range(42000):
    X_train_resize[i,:,:]=cv2.resize(x_train[i],dsize=(28,28))
​
X_test_resize=np.zeros((18000,28,28))
for i in range(18000):
    X_test_resize[i,:,:]=cv2.resize(x_test[i],dsize=(28,28))
X_train_resize.shape
#Reshape the train and test datasets to make them 4-D
xtrain1=X_train_resize.reshape(42000,28,28,1) # u can also use np.expand_dim
xtest1=X_test_resize.reshape(18000,28,28,1)
#Encoding the target variable
from tensorflow.keras.utils import to_categorical
ytrain=to_categorical(y_train,num_classes=10)
ytest=to_categorical(y_test,num_classes=10)
ytrain[0]
# Import the libraries required for CNN
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense,Dropout
# The CNN model architecture must be same as the one we have builded for MNIST dataset,
# because our idea is to apply the weights trained for MNIST dataset to apply here on SVHN data model
classifier1=Sequential()
​
classifier1.add(Conv2D(16,(3,3),input_shape=(28,28,1),activation ='relu'))
classifier1.add(MaxPooling2D(pool_size=(2,2)))
​
classifier1.add(Conv2D(32,(3,3),activation ='relu'))
classifier1.add(MaxPooling2D(pool_size=(2,2)))
​
classifier1.add(Flatten())
​
classifier1.add(Dense(units=64,activation='relu'))
classifier1.add(Dense(units=10,activation='softmax'))
​
#Apply the MNIST data model weight on the above CNN architecture
classifier1.load_weights('my_digit_model.h5')
# Compilation statergy
classifier1.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
# Evaluating the "SVHN digit" test data on the model with the "MNIST digit" weights
classifier1.evaluate(xtest1,ytest)
#This model producing the accuracy of around 22 percent only as the two dataset are differnt (eventhough both contains digit)
# To improve the performance of this model, we need to re-train some section of the weights 
# with respect to SVHN dataset.
​
#One approach is keep the weights of the convolution layer as it is, but re-train the weights of the 
#dense layers (hidden and output layer)
# This is know as Transfer Learning through feature extraction
classifier1.layers #accessing the layers
#Accessing the layer name
for layer in classifier1.layers:
    print(layer.name)
# Trainability nature of each layer.
#by default all layer weights are trainable
for layer in classifier1.layers:
    print(layer.trainable)
#freeze the convolution layer and train only the dense layer
for layer in classifier1.layers:
    if ('dense' not in layer.name):
        layer.trainable=False
    if('dense' in layer.name):
        layer.trainable=True
for layer in classifier1.layers:
    print(layer.name,layer.trainable)
# False indicating that these layers can't be trainable (i.e the weights are freezed)
classifier1.summary()
# Non trainable parameters = convolution layer parameters = 160 +4640 =4800
# Training the model. In this step only the weights of dense layers will be updated
# convolution layer weights remain same(same as MNIST model weights)
classifier1.fit(xtrain1,ytrain,batch_size=32,epochs=10,validation_data=(xtest1,ytest))
# Model performance improved drastically
# The approach is along with tuning dense layer weights, we can also retrain few last convolution layers
#This is know as Transfer Learning through Fine Tuning
for layer in classifier1.layers:
    print(layer.name,layer.trainable)
classifier1.layers[2].trainable=True
classifier1.layers[3].trainable=True
classifier1.layers[4].trainable=True
print("After unfreezing last convolution layer")
for layer in classifier1.layers:
    print(layer.name,layer.trainable)
# Train the model. In this step along with all the dense layers, last convolution layer 
                                                           #weights also will be updated
classifier1.fit(xtrain1,ytrain,batch_size=32,epochs=10,validation_data=(xtest1,ytest))
# Reduce overfitting - Include dropout layer
classifier1=Sequential()
​
classifier1.add(Conv2D(16,(3,3),input_shape=(28,28,1),activation ='relu'))
classifier1.add(MaxPooling2D(pool_size=(2,2)))
​
classifier1.add(Conv2D(32,(3,3),activation ='relu'))
classifier1.add(MaxPooling2D(pool_size=(2,2)))
classifier1.add(Dropout(0.2))
​
classifier1.add(Flatten())
​
classifier1.add(Dense(units=64,activation='relu'))
classifier1.add(Dropout(0.2))
classifier1.add(Dense(units=10,activation='softmax'))
for layer in classifier1.layers:
    print(layer.name,layer.trainable)
classifier1.load_weights('my_digit_model.h5')
for layer in classifier1.layers:
    if ('dense' not in layer.name):
        layer.trainable=False
    if('dense' in layer.name):
        layer.trainable=True
classifier1.layers[2].trainable=True
classifier1.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
classifier1.fit(xtrain1,ytrain,batch_size=32,epochs=5,validation_data=(xtest1,ytest))
#including dropout layer reducing the overfitting 

########################################################################################################################################################################
#6_TransferLearning_Faculty_Notebook_Session6_Transfer_Learning_workout2-1.ipynb

Load the libraries required for the CNN
from tensorflow.keras.models import Sequential from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense,Dropout import tensorflow as tf

#Load the libraries required for image handling/preprocessing
from tensorflow.keras.applications import imagenet_utils
from tensorflow.keras.preprocessing import image
#Load the mobilenet model along with weights
mobile_net=tf.keras.applications.MobileNet()
#load one sample image to predict its class
#resize the image to 224, 224 because by default mobilenet can handle the image of this size only
img=image.load_img('elephant.jpg',target_size=(224,224))
img
type(img)
#convert the image into numpy array
img_ar=image.img_to_array(img)
img_ar.shape
# Make the image 4 dimensional (1,224,224,3)
import numpy as np
img_ar1=np.expand_dims(img_ar,axis=0)
#Mobilenet has been trained on the imagenet dataset after performing some preprocessing on these images
#It is necessary to do the same preprocessing on our image now prior to send this into mobilenet model
​
img_pre=tf.keras.applications.mobilenet.preprocess_input(img_ar1)
img_pre.min() # the data range is now becoming between -1 to +1
pred=mobile_net.predict(img_pre) # Predict the class of the sample image
pred.shape 
#The shape of the'pred' is 1000, because it giving us the probability value corresponds to 1000 classes
​
pred[0].shape
pred[0].max() # Maximum probabilty 
pred[0].argmax() # Position of the class which have the maximum probability
imagenet_utils.decode_predictions(pred)
#using decode_prediction function, we can get the class name and id informations for the top5 max probabity
# The sample image is predicted as tusker with 63 percent confidence
# We have already builded the flower prediction model in our previous session by 
  #developing CNN from scratch. Now we are going to build the flower prediction model through 
  # Transfer Learning approaches
#Transfer Learning  through Feature Extraction 
base_model=tf.keras.applications.MobileNet(input_shape=(128,128,3)) 
# Loading the mobilenet weights for the input image size of 128,128
#mobilenet can support the following input size [128, 160, 192, 224]
base_model.summary()
base_model=tf.keras.applications.MobileNet(input_shape=(128,128,3),include_top=False)
#include_top = False will remove the dense layers. In otherwords it will keep the model only till
# the convolution layers
#In the above summary report "global average pooling layer" is flattening the last convolution layer output.
# all these layers from global average pooling is not there if we do include_top=False
base_model.summary()
base_model.trainable=False # Freezing all the convolution layer weights
base_model.summary() 
# As base model is now only having convolution layer and we have freezed all the convolution layer 
  # weights. So the trainable parameters becomes '0'
​
#Adding customized hidden layers and output layer with the mobilenet base model 
transfer_model=Sequential([base_model,
                            Flatten(),
                           Dropout(0.2),
                          Dense(512,activation='relu'),
                           Dropout(0.2),
                          Dense(64,activation='relu'),
                           Dropout(0.2),
                          Dense(5,activation='softmax')])
transfer_model.summary()
# After adding this , the trainable parameters are increasing, these are the parameters of hidden and output layers
#Image augumentation
from tensorflow.keras.preprocessing.image import ImageDataGenerator
train_datagen=ImageDataGenerator(rescale=1/255.,
                                rotation_range=45,
                                width_shift_range=0.2,
                                height_shift_range=0.2,
                                shear_range=0.2,
                                zoom_range=0.2,
                                horizontal_flip=True,
                                fill_mode='reflect')
test_datagen=ImageDataGenerator(rescale=1/255.)
#Loading the flower dataset for training and testing
training_set=train_datagen.flow_from_directory('C:\\Users\\Senthil\\Desktop\\DEEP_LEARNING\\flower_photos\\Training',
                                              target_size=(128,128),
                                              batch_size=128,
                                              class_mode='categorical')
test_set=test_datagen.flow_from_directory('C:\\Users\\Senthil\\Desktop\\DEEP_LEARNING\\flower_photos\\Testing',
                                              target_size=(128,128),
                                              batch_size=128,
                                              class_mode='categorical')
transfer_model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
#Fit(Training) the model. In this step the weights for the top layers (hidden and output)
# are computed
transfer_model.fit(training_set,
              steps_per_epoch=2736/128,
              epochs=5,
              validation_data=test_set,
              validation_steps=934/128)
# Testing the model with single image
test_img=image.load_img('C:\\Users\\Senthil\\Desktop\\DEEP_LEARNING\\flower_photos\\example\\4.jpg',
                       target_size=(128,128))
test_img1=image.img_to_array(test_img)
test_img1=test_img1/255.
test_img2=np.expand_dims(test_img1,axis=0)
​
ypred=transfer_model.predict(test_img2)
print(training_set.class_indices)
​
print('The test image class is :',ypred.argmax())
test_img
# Transfer Learning with Fine tuning
base_model=tf.keras.applications.MobileNet(input_shape=(128,128,3),include_top=False)
base_model.summary()
#Printing last few convolution layer name
for layer in base_model.layers[71:]:
    print(layer.name)
# first 70 layers weights are Freezed. From 70 to last convolution layer weights are let to be unfreezed
for layer in base_model.layers[:70]:
    layer.trainable=False
# for layer in base_model.layers[:70]:
#     print(layer.name)
# for layer in base_model.layers:
#     print(layer.name,layer.trainable)
# Adding the customized hidden and output layer with the partially freezed based model
transfer_fine_model=Sequential([base_model,
                              Flatten(),
                              Dropout(0.2),
                              Dense(512,activation='relu'),
                              Dropout(0.2),
                              Dense(64,activation='relu'),
                              Dropout(0.2),
                              Dense(5,activation='softmax')])
from tensorflow.keras.optimizers import Adam
ada=Adam(learning_rate=0.0001) 
# use less learning factor when tuning the convolution layer weights of pretrained networks
transfer_fine_model.compile(optimizer=ada,loss='categorical_crossentropy',metrics=['accuracy'])
#Fit(Training) the model. In this step the weights for the top layers (hidden and output)
# are computed along with that the weights of unfreezed convolution layers (from 70 to last conv layer)
# laso re-trained (tuned)
transfer_fine_model.fit(training_set,
              steps_per_epoch=2736/128,
              epochs=5,
              validation_data=test_set,
              validation_steps=934/128)
# We can see the slight increase in the model performance afetr fine tuning the convolution layer

########################################################################################################################################################################
#7_BoundingBox_Faculty_Notebook_Session_7_Object_localization-1.ipynb

The Oxford-IIIT Pet Dataset
Omkar M Parkhi, Andrea Vedaldi, Andrew Zisserman and C. V. Jawahar have created a 37 category pet dataset with roughly 200 images for each class. The images have a large variations in scale, pose and lighting. All images have an associated ground truth annotation of breed, head ROI, and pixel level trimap segmentation.

Link to dataset: http://www.robots.ox.ac.uk/~vgg/data/pets/

https://drive.google.com/file/d/1uyjsKeXHv0-NBhHEBfAmqe9JLhi3bJ30/view?usp=sharing

https://drive.google.com/file/d/1kbmzEWJIFcHw7HMmokj6D7DT5M2aMzNv/view?usp=sharing

import tensorflow 
import numpy as np
import matplotlib.pyplot as plt
Load the dataset
DATASET_FOLDER = "./images/" #unzip the downloaded images and keep it under the folder 'images'
TRAIN_CSV = "train-2.csv"
VALIDATION_CSV = "validation-3.csv"
import pandas as pd
d1=pd.read_csv(TRAIN_CSV,header=None)
d1.head(2)
#This file contain the image name and the object bounding box informations for all the train images
len(d1)
#Extracting only image names
X_train=[]
for i in range(len(d1)):
    X_train.append("./" + d1[0][i].split('/')[-2] + "/" + 
                   d1[0][i].split('/')[-1])
X_train[:5]
​
ytrain=pd.DataFrame()
#Scale the bounding box with respect to the image size of 128x128
ytrain['x0']=d1[3]*128/d1[2]
ytrain['y0']=d1[4]*128/d1[1]
ytrain['x1']=(d1[5]-d1[3])*128/d1[2]
ytrain['y1']=(d1[6]-d1[4])*128/d1[1]
#ytrain.head(5)
y_train=np.array(ytrain)
y_train[:5] # scaled bounding box values
Let's check how does the data look like
import cv2
filename = X_train[97]
img = cv2.imread(filename)
plt.imshow(img)
x0=d1.iloc[97,3]
y0=d1.iloc[97,4]
x1=d1.iloc[97,5]
y1=d1.iloc[97,6]
#original bounding box co-ordinate
x0,y0,x1,y1
### code to rescale the scaled bounding boxes
### we may not required here as already we have the original BB
# import cv2
# # Pick a random image to check how it looks
# filename = X_train[97]
# unscaled = cv2.imread(filename)
# region = y_train[97]
# image_height, image_width, _ = unscaled.shape
# x0 = int(region[0] * image_width / IMAGE_SIZE) # Scale the BBox
# y0 = int(region[1] * image_height / IMAGE_SIZE)
​
# x1 = int((region[0] + region[2]) * image_width / IMAGE_SIZE)
# y1 = int((region[1] + region[3]) * image_height / IMAGE_SIZE)
​
import matplotlib.patches as patches
​
# Create figure and axes
fig,ax = plt.subplots(1)
​
# Display the image
ax.imshow(img)
​
# Create a Rectangle patch
rect = patches.Rectangle((x0, y0), x1 - x0, y1 - y0, linewidth=2, 
                         edgecolor='r', facecolor='none')
​
# Add the patch to the Axes
ax.add_patch(rect)
​
plt.show()
​
# All the bounding boxes are framed for face region of dog or cat
Read all the images and resize it to 128x128
Pre-process it with respect to Mobilenet model
from PIL import Image
from tensorflow.keras.applications.mobilenet import preprocess_input
​
for i, f in enumerate(X_train):
  img = Image.open(f) # Read image
  img = img.resize((128, 128)) # Resize image
  img = img.convert('RGB')
​
  X_train[i] = preprocess_input(np.array(img, dtype=np.float32)) # Convert to float32 array
  img.close()
X_train[0].shape
X_train = np.array(X_train)
X_train.shape # 3006 images of each 128x128x3 size present in the train dataset
y_train.shape
#Perform the same things with validation data
d1=pd.read_csv(VALIDATION_CSV,header=None)
d1.head(2)
X_val=[]
for i in range(len(d1)):
    X_val.append("./" + d1[0][i].split('/')[-2] + "/" + 
                   d1[0][i].split('/')[-1])
yval=pd.DataFrame()
yval['x0']=d1[3]*128/d1[2]
yval['y0']=d1[4]*128/d1[1]
yval['x1']=(d1[5]-d1[3])*128/d1[2]
yval['y1']=(d1[6]-d1[4])*128/d1[1]
y_val=np.array(yval)
y_val
X_val[:5]
for i, f in enumerate(X_val):
  img = Image.open(f) # Read image
  img = img.resize((128, 128)) # Resize image
  img = img.convert('RGB')
​
  X_val[i] = preprocess_input(np.array(img, dtype=np.float32)) # Convert to float32 array
  img.close()
X_val = np.array(X_val)
X_val.shape # 680 images of each 128x128x3 size present in the validation dataset
y_val.shape
Define evaluation metric
Accuracy is not a good measure for object detection. The overlapping area between actual and predicted bounding boxes can be used as a measure to evaluate the quality of object detection/localization. Intersection over Union (IoU) can be used as a metric.

from IOU import IOU
def IOU(y_true, y_pred):
    intersections = 0
    unions = 0
    # set the types so we are sure what type we are using
​
    gt = y_true
    pred = y_pred
    # Compute interection of predicted (pred) and ground truth (gt) bounding boxes
    diff_width = np.minimum(gt[:,0] + gt[:,2], pred[:,0] + pred[:,2]) - np.maximum(gt[:,0], pred[:,0])
    diff_height = np.minimum(gt[:,1] + gt[:,3], pred[:,1] + pred[:,3]) - np.maximum(gt[:,1], pred[:,1])
    intersection = diff_width * diff_height
​
    # Compute union
    area_gt = gt[:,2] * gt[:,3]
    area_pred = pred[:,2] * pred[:,3]
    union = area_gt + area_pred - intersection
​
    # Compute intersection and union over multiple boxes
    for j, _ in enumerate(union):
      if union[j] > 0 and intersection[j] > 0 and union[j] >= intersection[j]:
        intersections += intersection[j]
        unions += union[j]
​
    # Compute IOU. Use epsilon to prevent division by zero
    iou = np.round(intersections / (unions + tensorflow.keras.backend.epsilon()), 4)
    # This must match the type used in py_func
    iou = iou.astype(np.float32)
    return iou
def IoU(y_true, y_pred):
    iou = tensorflow.py_function(IOU, [y_true, y_pred], 
                                 Tout=tensorflow.float32)
    return iou
IMAGE_SIZE=128
from tensorflow.keras.applications.mobilenet import MobileNet
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Conv2D, Reshape
​
ALPHA = 1.0 # Width hyper parameter for MobileNet (0.25, 0.5, 0.75, 1.0). 
#Higher width means more accurate but slower
​
def create_model(trainable=True):
    model = MobileNet(input_shape=(IMAGE_SIZE, IMAGE_SIZE, 3), 
                      include_top=False, alpha=ALPHA) 
    # Load pre-trained mobilenet
    # Do not include classification (top) layer
​
    # to freeze layers, except the new top layer, of course, which will be added below
    for layer in model.layers:
        layer.trainable = trainable
​
    # Add new top layer which is a conv layer of the same size as the previous ]
         #layer so that only 4 coords of BBox can be output
    den1 = model.layers[-1].output
    den2 = Conv2D(4, kernel_size=4, name="coords")(den1)
    # In the line above kernel size should be 3 for img size 96, 4 for 
    #img size 128, 5 for img size 160 etc.
    den3 = Reshape((4,))(den2) # These are the 4 predicted coordinates of one BBox
​
    return Model(inputs=model.input, outputs=den3)
Initialize the model and print summary
​
model = create_model(False) # Arg is False, if you want to freeze lower layers for fast training (but low accuracy)
model.summary() # Print summary
Compile the model
loss: "mean_squared_error"
metrics: IoU
optimizer: "adam"
# Compile the model
model.compile(loss="mean_squared_error", optimizer="adam", metrics=[IoU,'accuracy']) # Regression loss is MSE
Training the model
Fit the model to the dataset

Use early stopping
fit the model
give train data - training features and labels
batch size: 32
epochs: 10
give validation data - testing features and labels
# Use earlystopping
callback = tensorflow.keras.callbacks.EarlyStopping(monitor='accuracy', patience=5, min_delta=0.01)
​
# Fit the model
model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=2, batch_size=32, callbacks=[callback])
Final loss and accuracy
model.evaluate(X_val, y_val)
Test the model on an image from test data
# Pick a test image, run model, show image, and show predicted bounding box overlaid on the image
filename = './images/shiba_inu_163.jpg'
​
unscaled = cv2.imread(filename) # Original image for display
image_height, image_width, _ = unscaled.shape
image = cv2.resize(unscaled, (128, 128)) # Rescaled image to run the network
feat_scaled = preprocess_input(np.array(image, dtype=np.float32))
print ("Size of original input: ", image.shape)
print("-------------------------------")
print("Size of scaled input: ", feat_scaled.shape)
region = model.predict(x=np.array([feat_scaled]))[0] # Predict the BBox
region
Fetching coordinates details

x0 = int(region[0] * image_width / IMAGE_SIZE) # Scale the BBox
y0 = int(region[1] * image_height / IMAGE_SIZE)
​
x1 = int((region[0] + region[2]) * image_width / IMAGE_SIZE)
y1 = int((region[1] + region[3]) * image_height / IMAGE_SIZE)
Now, let's plot the image and the bounding box on top of it

# Create figure and axes
fig,ax = plt.subplots(1)
​
# Display the image
ax.imshow(unscaled)
​
# Create a Rectangle patch
rect = patches.Rectangle((x0, y0), x1 - x0, y1 - y0, linewidth=2, edgecolor='r', facecolor='none')
​
# Add the patch to the Axes
ax.add_patch(rect)
​
plt.show()
# Pick a test image, run model, show image, and show predicted bounding box overlaid on the image
filename = './images/Abyssinian_14.jpg'
​
unscaled = cv2.imread(filename) # Original image for display
image_height, image_width, _ = unscaled.shape
image = cv2.resize(unscaled, (IMAGE_SIZE, IMAGE_SIZE)) # Rescaled image to run the network
feat_scaled = preprocess_input(np.array(image, dtype=np.float32))
region = model.predict(x=np.array([feat_scaled]))[0] # Predict the BBox
Fetching coordinates details

x0 = int(region[0] * image_width / IMAGE_SIZE) # Scale the BBox
y0 = int(region[1] * image_height / IMAGE_SIZE)
​
x1 = int((region[0] + region[2]) * image_width / IMAGE_SIZE)
y1 = int((region[1] + region[3]) * image_height / IMAGE_SIZE)
Now, let's plot the image and the bounding box on top of it

# Create figure and axes
fig,ax = plt.subplots(1)
​
# Display the image
ax.imshow(unscaled)
​
# Create a Rectangle patch
rect = patches.Rectangle((x0, y0), x1 - x0, y1 - y0, linewidth=2, edgecolor='r', facecolor='none')
​
# Add the patch to the Axes
ax.add_patch(rect)
​
plt.show()
​


########################################################################################################################################################################
#7_UNE_Covid_Model_S7_TakeHome_Solutions.ipynb

Package version
tensorflow==2.4.1rc3
numpy==1.18.2
matplotlib==3.2.1
google==2.0.3
segmentation_models==1.0.1
U - Net
Problem:
Covid-19 is likely to remain an important differential diagnosis for the foreseeable future in anyone presenting to hospital with a flu-like illness, lymphopenia on full blood count, and/or a change in normal sense of smell (anosmia) or taste.12

Most people with covid-19 infection develop chest/ling infection; however, chest radiography of people who are seriously ill with respiratory symptoms when they present to hospital can help to identify those with covid-19 infection.

WHO offers advice to non-radiologists on how to look for changes on chest radiograph that may be suggestive of covid-19 pneumonia, as prompt review and report from an onsite or remote radiologist.

The recommendations are based on a combination of emerging evidence, current guidelines, and clinical experience.

So the radiographic image of the patient lung as well as the non-radiographic image of the patient's lung has been captured.

A radiographic image is produced from imaging the reflection coming from infection boundaries. The radiographic image shows the boundaries between different effected and non-effected cells.

Data
The data is a set of images chosen for various patients chosen at random . The images are 256 x 256 pixels and each pixel is classified as either effected cell or non-effected cell. In addition to the radiographic images, the depth of the infection is provided for each image. The goal of the competition is to segment regions that contain infection.

Aim:
Implement U-Net neural model architecture in keras to solve this problem.

In this, you are asked to segment infected cells in the lung.Given a set of radiographic images that are 256 x 256 pixels each and each pixel we need to classify as either infected or non-infected. Our goal is to segment regions that contain infection.

Broad Steps:
Download the dataset
Upload to Drive
Import from drive to colab
Load the images and create training data.
Build U-net Model
Train your model.
Check the validation accuracy and plot sample.
import tensorflow
tensorflow.__version__
# Mount drive
from google.colab import drive
drive.mount('/content/drive/')
Extract data
#For simplicity we have added the required code here.
from zipfile import ZipFile
​
with ZipFile('/content/drive/MyDrive/My_DL/S7 - Semantics + Unet/New-TakeHome/train.zip', 'r') as zf:
  zf.extractall()
The train file have both images and masks with the same names_ids.
Get the list of names of images and masks and name the list imagelist and masklist.
Hint - Use os.listdir() funtions.

import os
imagelist = os.listdir('train/images')
masklist = os.listdir('train/masks')
#Test your list names by printing some of the names as given below.
print(imagelist[-1])
print(masklist[-1])
print(imagelist[5])
print(masklist[5])
Read and test your images and respective masks.
Hint -

import matplotlib.pyplot as plt

import cv2

plt.imshow(cv2.imread('path of image'))

plt.imshow(cv2.imread('path of mask'))

import  matplotlib.pyplot as plt
import cv2
​
plt.imshow(cv2.imread('train/images/{}'.format(imagelist[10])))
plt.imshow(cv2.imread('train/masks/{}'.format(masklist[10])))
Create your training data.
Hints -

image_path = os.path.join('path of your image directory' +n )

mask_path = os.path.join('path of your mask directory'+n )

import numpy as np
​
im_height, im_width = 256 , 256
​
# Get and resize train images and masks
def get_data(train=True):
    #ids = next(os.walk("train/images"))[2]
    X = np.zeros((len(imagelist), im_height, im_width, 1), dtype=np.float32)
    y = np.zeros((len(masklist), im_height, im_width, 1), dtype=np.float32)
    for n in imagelist:
        k = imagelist.index(n)
        image_path = os.path.join('train/images/' +n )
        mask_path = os.path.join('train/masks/' +n )
        
        # Load images
        img = cv2.imread(image_path, 0)
        resized_img = cv2.resize(img, (256, 256), interpolation = cv2.INTER_AREA)
        
​
        # Load masks
        if train:
            mask = cv2.imread(mask_path, 0)
            resized_mask = cv2.resize(mask, (256, 256), interpolation = cv2.INTER_AREA)
            resized_mask = np.reshape(resized_mask, (256,256,1))
            
           
​
        # Save images
        X[k, ..., 0] = resized_img.squeeze() / 255
        if train:
            y[k] = resized_mask/255
    print('Done!')
    if train:
        return X, y
    else:
        return X
    
X, y = get_data(train=True)
# Split train and valid
from sklearn.model_selection import train_test_split
​
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.15, random_state=0)
## Test your data whether it looks fine - Random check
import random 
# Check if training data looks all right
ix = random.randint(0, len(X_train))
has_mask = y_train[ix].max() > 0
​
fig, ax = plt.subplots(1, 2, figsize=(10, 10))
​
ax[0].imshow(X_train[ix, ..., 0], cmap='seismic', interpolation='bilinear')
if has_mask:
    ax[0].contour(y_train[ix].squeeze(), colors='k', levels=[0.5])
ax[0].set_title('Radiographic')
​
ax[1].imshow(y_train[ix].squeeze(), interpolation='bilinear', cmap='gray')
ax[1].set_title('Virus');
Define loss and dice_coeff function.
def dice_coefficient(y_true, y_pred):
    numerator = 2 * tensorflow.reduce_sum(y_true * y_pred)
    denominator = tensorflow.reduce_sum(y_true + y_pred)
​
    return numerator / (denominator + tensorflow.keras.backend.epsilon())
​
def loss(y_true, y_pred):
    return tensorflow.keras.backend.binary_crossentropy(y_true, y_pred) - tensorflow.math.log(dice_coefficient(y_true, y_pred) + tensorflow.keras.backend.epsilon())
Build and compile UNet Model for your data.
Hint - You can install and use segmentation models from this github repository.

Install segmentation models
!pip install git+https://github.com/qubvel/segmentation_models

!pip install git+https://github.com/qubvel/segmentation_models
from keras.utils import generic_utils
from segmentation_models import Unet
​
model = Unet(backbone_name='resnet34', encoder_weights=None, input_shape=(None, None, 1))
model.compile(optimizer='Adam', loss=loss, metrics=[dice_coefficient])
model.summary()
from segmentation_models import get_preprocessing
​
BACKBONE = 'resnet34'
preprocess_input = get_preprocessing(BACKBONE)
X_train = preprocess_input(X_train)
X_valid = preprocess_input(X_valid)
Fit your model using model.fit function.
Hint - As it might take long time to run. Run it for only 1 or 2 epochs.

model.fit(
    x=X_train,
    y=y_train,
    batch_size=16,   
    epochs=1,
    validation_data=(X_valid, y_valid)
    )
Predict on val set using model.predict funtion and store in preds_val variable.
preds_val = model.predict(X_valid, verbose=1)
#Get the threshold predictions to look at refined results.
preds_val_t = (preds_val > 0.5).astype(np.uint8)
#Plot a sample
def plot_sample(X, y, preds, binary_preds, ix=None):
    if ix is None:
        ix = random.randint(0, len(X))
​
    has_mask = y[ix].max() > 0
​
    fig, ax = plt.subplots(1, 4, figsize=(20, 10))
    ax[0].imshow(X[ix, ..., 0], cmap='seismic')
    if has_mask:
        ax[0].contour(y[ix].squeeze(), colors='k', levels=[0.5])
    ax[0].set_title('Radiographic')
​
    ax[1].imshow(y[ix].squeeze())
    ax[1].set_title('Virus')
​
    ax[2].imshow(preds[ix].squeeze(), vmin=0, vmax=1)
    if has_mask:
        ax[2].contour(y[ix].squeeze(), colors='k', levels=[0.5])
    ax[2].set_title('Virus Predicted')
    
    ax[3].imshow(binary_preds[ix].squeeze(), vmin=0, vmax=1)
    if has_mask:
        ax[3].contour(y[ix].squeeze(), colors='k', levels=[0.5])
    ax[3].set_title('Virus Predicted binary');
# Check if valid data looks all right
plot_sample(X_valid, y_valid, preds_val, preds_val_t, ix=2)
If you are getting good results- Congratulations. If you are not, try to explore what might be the reason.

​

########################################################################################################################################################################
#8_BrainTumor_Segmentation_Inclass8_Question_Solution_upd.ipynb

Brain Tumour Segmentation using Unet
Worldwide, incidences of brain tumours increases every year. Brain tumours are classified as benign (noncancerous tumours) and malignant (cancerous).Subclasses of brain tumours are primary and secondary tumours. Primary tumours start in the brain or Central Nervous Systems (CNS) whereas the secondary tumours spread from other body parts into the brain. Depends on the degree of abnormality of brain tissue, the tumours are type casted into four (1 to 4) grading levels. Tumours with 1 and 2 are low grades which are less dangerous. 3&4 grade tumours are high-grade tumours which are highly susceptible to cancer. Primary tumours have several types amongst 36.1 % all primary tumours are referred as meningioma that found near the top and outer curve of the brain. Meningioma is slowly growing noncancerous tumours that cause seizures and visual problems. Glioma is abnormal growth in glial cells presents around the neurons in the brain. Pituitary tumours grow in pituitary glands that affect body functions. Meningioma are iso-dense dura-based masses developed at the meninges of the three layers of protecting tissue of the brain and spinal cord, whose diagnosis depends on its anatomical location, shape and appearance of cells. Pituitary tumours are abnormal mass growth in cells around the surface of the pituitary gland that located at the base of skull.

For this work we have provided you the Meningioma tumor images along with its masks.

Build a Unet based segmentation model to segment the tumor region.

Dataset link: https://drive.google.com/drive/folders/11rbveSfeTsTMwHsXyPzLGTN5SDfhWcR9?usp=sharing

from google.colab import drive
drive.mount('/content/drive')
Import the required libraries
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from PIL import Image
from tensorflow.keras.utils import normalize
Load the images and masks in one folder and properly resize to same size (If required)
project_path  = '/content/drive/MyDrive/My_DL/Session 8/'
images_zip_path = project_path + "images_brain_tum-20211013T051807Z-001.zip"
​
from zipfile import ZipFile
​
with ZipFile(images_zip_path, 'r') as z:
  z.extractall()
images_zip_path = project_path + "masks_brain_tum-20211013T051808Z-001.zip"
​
from zipfile import ZipFile
​
with ZipFile(images_zip_path, 'r') as z:
  z.extractall()
#image_dir='C:\\Users\\Senthil\\Desktop\\Unet_dataset\\images_brain_tum\\'
​
image_dir= '/content/images_brain_tum/'
​
#mask_dir='C:\\Users\\Senthil\\Desktop\\Unet_dataset\\masks_brain_tum\\'
mask_dir='/content/masks_brain_tum/'
SIZE=128
​
img_dataset=[]
mask_dataset=[]
​
images=os.listdir(image_dir)
​
for i,image_name in enumerate(images):
    if (image_name.split('.')[1]=='jpg'):
        image=cv2.imread(image_dir+image_name,0)
        image=Image.fromarray(image)
        image=image.resize((SIZE,SIZE))
        img_dataset.append(np.array(image))
        #img_dataset.append(image)
        
        
masks=os.listdir(mask_dir)
​
for i,image_name in enumerate(masks):
    if (image_name.split('.')[1]=='jpg'):
        image=cv2.imread(mask_dir+image_name,0)
        image=cv2.resize(image,(SIZE,SIZE))
        (thresh, bwimage) = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY) # make sure mask is binary image
        #bwimage=Image.fromarray(bwimage)
        #mask_dataset.append(np.array(bwimage))
        mask_dataset.append(bwimage)
​
img_dataset=np.array(img_dataset)
img_dataset=normalize(img_dataset)
img_dataset=np.expand_dims(img_dataset,3)
​
mask_dataset=np.array(mask_dataset)
mask_dataset=mask_dataset/255.
mask_dataset=np.expand_dims(mask_dataset,3)
​
print(img_dataset.shape)
​
print(mask_dataset.shape)
np.unique(mask_dataset[0,:,:,0]) # make sure mask is having only 0 and 1 for binary class
Display some of the images along with its mask and make sure the position of mask matches with original image tumor position
r1=np.random.randint(1,705,size=(1,2))
r1[0][0],r1[0][1]
r1=np.random.randint(1,705,size=(1,2))
plt.figure(figsize=(10,6))
plt.subplot(2,2,1)
plt.imshow(img_dataset[r1[0][0],:,:,:].reshape(128,128),cmap='gray')
plt.subplot(2,2,2)
plt.imshow(mask_dataset[r1[0][0],:,:,:].reshape(128,128),cmap='gray')
plt.subplot(2,2,3)
plt.imshow(img_dataset[r1[0][1],:,:,:].reshape(128,128),cmap='gray')
plt.subplot(2,2,4)
plt.imshow(mask_dataset[r1[0][1],:,:,:].reshape(128,128),cmap='gray')
Write the function for Unet model. Properly define the ENCODER and DECODER section
# u-net model 
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Flatten, Conv2D, MaxPooling2D, UpSampling2D, concatenate, Conv2DTranspose, BatchNormalization, Dropout, Lambda
#from tensorflow.keras import backend as K
from tensorflow.keras import backend as K
​
​
def simple_unet_model_with_jacard(IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS):
#Build the model
    inputs = Input((IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS))
    s = inputs
​
    #Contraction path
    c1 = Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(s)
    #c1 = Dropout(0.1)(c1)
    c1 = Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c1)
    p1 = MaxPooling2D((2, 2))(c1)
    
    c2 = Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(p1)
    #c2 = Dropout(0.1)(c2)
    c2 = Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c2)
    p2 = MaxPooling2D((2, 2))(c2)
     
    c3 = Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(p2)
    #c3 = Dropout(0.2)(c3)
    c3 = Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c3)
    p3 = MaxPooling2D((2, 2))(c3)
     
    c4 = Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(p3)
    #c4 = Dropout(0.2)(c4)
    c4 = Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c4)
    p4 = MaxPooling2D(pool_size=(2, 2))(c4)
     
    c5 = Conv2D(256, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(p4)
    #c5 = Dropout(0.3)(c5)
    c5 = Conv2D(256, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c5)
    
    #Expansive path 
    u6 = Conv2DTranspose(128, (2, 2), strides=(2, 2), padding='same')(c5)
    u6 = concatenate([u6, c4])
    c6 = Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u6)
    #c6 = Dropout(0.2)(c6)
    c6 = Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c6)
     
    u7 = Conv2DTranspose(64, (2, 2), strides=(2, 2), padding='same')(c6)
    u7 = concatenate([u7, c3])
    c7 = Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u7)
    #c7 = Dropout(0.2)(c7)
    c7 = Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c7)
     
    u8 = Conv2DTranspose(32, (2, 2), strides=(2, 2), padding='same')(c7)
    u8 = concatenate([u8, c2])
    c8 = Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u8)
    #c8 = Dropout(0.1)(c8)
    c8 = Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c8)
     
    u9 = Conv2DTranspose(16, (2, 2), strides=(2, 2), padding='same')(c8)
    u9 = concatenate([u9, c1], axis=3)
    c9 = Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u9)
    #c9 = Dropout(0.1)(c9)
    c9 = Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c9)
     
    outputs = Conv2D(1, (1, 1), activation='sigmoid')(c9)
     
    model = Model(inputs=[inputs], outputs=[outputs])
    #model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.compile(optimizer = 'adam', loss = [jacard_coef_loss], metrics = [jacard_coef])
​
    model.summary()
    
    return model
 
Define the Loss function and metric using Jecard coeff or dice coeff
​
def jacard_coef(y_true, y_pred):
    y_true_f = K.flatten(y_true)
    y_pred_f = K.flatten(y_pred)
    intersection = K.sum(y_true_f * y_pred_f)
    return (intersection + 1.0) / (K.sum(y_true_f) + K.sum(y_pred_f) - intersection + 1.0)
​
def jacard_coef_loss(y_true, y_pred):
    return -jacard_coef(y_true, y_pred)  # -1 ultiplied as we want to minimize this value as loss function
​
​
Split the data into train and test. Call the Unet model and metric/loss functions defined in previous questions and compile and fit the model
%tensorflow_version 2.x
import tensorflow as tf
print("Tensorflow version " + tf.__version__)
​
try:
  tpu = tf.distribute.cluster_resolver.TPUClusterResolver()  # TPU detection
  print('Running on TPU ', tpu.cluster_spec().as_dict()['worker'])
except ValueError:
  raise BaseException('ERROR: Not connected to a TPU runtime; please see the previous cell in this notebook for instructions!')
​
tf.config.experimental_connect_to_cluster(tpu)
tf.tpu.experimental.initialize_tpu_system(tpu)
tpu_strategy = tf.distribute.experimental.TPUStrategy(tpu)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(img_dataset,mask_dataset,test_size=0.15,random_state=0)
​
​
IMG_HEIGHT=img_dataset.shape[1]
IMG_WIDTH=img_dataset.shape[2]
IMG_CHANNELS=img_dataset.shape[3]
​
model=simple_unet_model_with_jacard(IMG_HEIGHT,IMG_WIDTH,IMG_CHANNELS)
​
model.fit(x_train,y_train,batch_size=64,verbose=1,epochs=5,
          validation_data=(x_test,y_test),shuffle=False)
​
Run with more iteration on Google colab for better result. As this segmentation process is tedius it will take lot iteration for convergence
Evaluate the model performance on the test data and predict the segmented output for random test image. Plot the original image, original mask and predicted mask.
​
loss,jac_coef=model.evaluate(x_test,y_test)
​
n1=np.random.randint(0,len(x_test))
test_img=x_test[n1]
mask_test_img=y_test[n1]
test_img1=np.expand_dims(test_img,0)
pred_img=model.predict(test_img1)
pred_img1=(pred_img[0,:,:,0]>0.5).astype(np.uint8)
​
plt.figure(figsize=(16,8))
plt.subplot(131)
plt.title('Original')
plt.imshow(test_img[:,:,0],cmap='gray')
​
plt.subplot(132)
plt.title('Mask Original')
plt.imshow(mask_test_img[:,:,0],cmap='gray')
​
plt.subplot(133)
plt.title('Segmented Image')
plt.imshow(pred_img1,cmap='gray')
​
​
Use some pretrained segmentation model from segmentation_model package to acheive the brain tumor segmentation task.
!pip install segmentation_models
import segmentation_models as sm
​
BACKBONE = 'resnet34'
preprocess_input = sm.get_preprocessing(BACKBONE)
​
X_train_prepr = preprocess_input(x_train)
X_test_prepr = preprocess_input(x_test)
​
np.unique(y_train)
model_resnet_backbone = sm.Unet(BACKBONE, input_shape=(128,128,1), encoder_weights=None, classes=1, activation='sigmoid')
def jacard_coef(y_true, y_pred):
    y_true_f = K.flatten(y_true)
    y_pred_f = K.flatten(y_pred)
    intersection = K.sum(y_true_f * y_pred_f)
    return (intersection + 1.0) / (K.sum(y_true_f) + K.sum(y_pred_f) - intersection + 1.0)
​
metrics=['accuracy', jacard_coef]
model_resnet_backbone.compile(optimizer='adam', loss='binary_crossentropy', metrics=metrics)
print(model_resnet_backbone.summary())
history2=model_resnet_backbone.fit(X_train_prepr, 
          y_train,
          batch_size=64, 
          epochs=150,
          validation_data=(X_test_prepr, y_test))
loss = model_resnet_backbone.evaluate(X_test_prepr, y_test)[0]
jac_coef = model_resnet_backbone.evaluate(X_test_prepr, y_test)[1]
​
​
n1=np.random.randint(0,len(x_test))
test_img=X_test_prepr[n1]
mask_test_img=y_test[n1]
test_img1=np.expand_dims(test_img,0)
pred_img=model_resnet_backbone.predict(test_img1)
pred_img1=(pred_img[0,:,:,0]>0.5).astype(np.uint8)
​
plt.figure(figsize=(16,8))
plt.subplot(131)
plt.title('Original')
plt.imshow(test_img[:,:,0],cmap='gray')
​
plt.subplot(132)
plt.title('Mask Original')
plt.imshow(mask_test_img[:,:,0],cmap='gray')
​
plt.subplot(133)
plt.title('Segmented Image')
plt.imshow(pred_img1,cmap='gray')

########################################################################################################################################################################
#8_RCNN_Faculty_Notebook_Session8_RCNN_approach-1.ipynb

Import required libraries
import tensorflow as tf from tensorflow.keras.applications import MobileNet from tensorflow.keras.applications.mobilenet import preprocess_input from tensorflow.keras.preprocessing.image import img_to_array from tensorflow.keras.applications import imagenet_utils import imutils from imutils.object_detection import non_max_suppression import time import cv2 import numpy as np from sliding_window import sliding_window # this is user defined function from image_pyramid import image_pyramid # this is user defined function

WIDTH = 600 # resize the images to the size of 600x600
PYR_SCALE = 1.5 # To creating the multiple scaled version of image
WIN_STEP = 16 # Sliding Window step size 
ROI_SIZE = (250,250) # Region of interest (Sub image block) size
INPUT_SIZE = (224, 224) # input image size (We are using mobilenet architecture)
visualize=0 # control parameter for visualizing images
min_conf=0.9 # class probability threshold for the object predicted in each RoI
# Define the pretrained model - Mobilenet
model = MobileNet(weights="imagenet", include_top=True)
orig = cv2.imread('hummingbird.jpg')
orig = imutils.resize(orig, width=WIDTH)
(H, W) = orig.shape[:2]
pyramid = image_pyramid(orig, scale=PYR_SCALE, minSize=ROI_SIZE)
rois = []
locs = []
​
start = time.time()
# loop over the image pyramid
for image in pyramid:
    # determine the scale factor between the *original* image
    # dimensions and the *current* layer of the pyramid
    scale = W / float(image.shape[1])
​
    # for each layer of the image pyramid, loop over the sliding
    # window locations
    for (x, y, roiOrig) in sliding_window(image, WIN_STEP, ROI_SIZE):
        # scale the (x, y)-coordinates of the ROI with respect to the
        # *original* image dimensions
        x = int(x * scale)
        y = int(y * scale)
        w = int(ROI_SIZE[0] * scale)
        h = int(ROI_SIZE[1] * scale)
​
        # take the ROI and pre-process it so we can later classify
        # the region using Keras/TensorFlow
        roi = cv2.resize(roiOrig, INPUT_SIZE)
        roi = img_to_array(roi)
        roi = preprocess_input(roi)
​
        # update our list of ROIs and associated coordinates
        rois.append(roi)
        locs.append((x, y, x + w, y + h))
​
        # check to see if we are visualizing each of the sliding
        # windows in the image pyramid
        if visualize > 0:
            # clone the original image and then draw a bounding box
            # surrounding the current region
            clone = orig.copy()
            cv2.rectangle(clone, (x, y), (x + w, y + h),(0, 255, 0), 2)
​
            # show the visualization and current ROI
            cv2.imshow("Visualization", clone)
            cv2.imshow("ROI", roiOrig)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
end = time.time()
print("looping over pyramid/windows took {:.5f} seconds".format(end - start))
​
​
rois = np.array(rois, dtype="float32") 
rois.shape #Total of 132 regions of each size 224x224x3 
# Predicting the class of each ROI using the mobilenet model
print("classifying ROIs...")
start = time.time()
preds = model.predict(rois)
end = time.time()
print("classifying ROIs took {:.5f} seconds".format(end - start))
preds.shape # Probability of each ROI towards 1000 classes (Mobilenet trained for 1000 classes)
preds = imagenet_utils.decode_predictions(preds, top=1) # top probability prediction
#preds
#create a dictionary with key name as predicted class name (predicted with more than 0.9 confidence)
#keyvalues are its corresponding bounding boxes and probability
labels = {}
for (i, p) in enumerate(preds):
    im_id,obj,prob=p[0]
    if prob>0.9:
        bb=locs[i]
        L=labels.get(obj,[])
        L.append((bb, prob))
        labels[obj] = L
labels
labels.keys()
boxes1=[]
lab=[]
for label in labels.keys():
    # clone the original image so that we can draw on it
    print("showing results for '{}'".format(label))
    clone = orig.copy()
​
    # loop over all bounding boxes for the current label
    for (box, prob) in labels[label]:
        # draw the bounding box on the image
        (startX, startY, endX, endY) = box
        cv2.rectangle(clone, (startX, startY), (endX, endY),(0, 255, 0), 2)
​
    # show the results *before* applying non-maxima suppression, then
    # clone the image again so we can display the results *after*
    # applying non-maxima suppression
    cv2.imshow("Before", clone)
    cv2.waitKey(0)
    clone = orig.copy()
​
    # extract the bounding boxes and associated prediction
    # probabilities, then apply non-maxima suppression
    boxes = np.array([p[0] for p in labels[label]])
    proba = np.array([p[1] for p in labels[label]])
    boxes = non_max_suppression(boxes, proba)
    boxes1.append(boxes)
    lab.append(label)
    # loop over all bounding boxes that were kept after applying
    # non-maxima suppression
    for (startX, startY, endX, endY) in boxes:
        # draw the bounding box and label on the image
        cv2.rectangle(clone, (startX, startY), (endX, endY),(0, 255, 0), 2)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.putText(clone, label, (startX, y),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)
​
    # show the output after apply non-maxima suppression
    cv2.imshow("After", clone)
    cv2.waitKey(0);
    cv2.destroyAllWindows()
len(boxes1),lab # After non max supression, at last two objects are present in the image
clone = orig.copy()
for i in range(len(boxes1)):
    bb=boxes1[i][0]
    cv2.rectangle(clone, (bb[0], bb[1]), (bb[2], bb[3]),(0, 255, 0), 2)
    y = bb[1] - 10 if bb[1] - 10 > 10 else bb[1] + 10
    cv2.putText(clone, lab[i], (bb[0], y),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 2)
    cv2.imshow("Final Objects", clone)
    cv2.waitKey(0);cv2.destroyAllWindows()
from matplotlib import pyplot as plt
plt.imshow(cv2.cvtColor(clone, cv2.COLOR_BGR2RGB))
plt.show()
In the above result, humming bird is correctly detected, but the flower is wrongly detected as jelly fish (ofcourse its look like jelly fish). This is because mobilenet is not trained for this type of flower. Retrain the part of mobilenet weights (Transfer Learning) using some images of these type of flowers can make this model to predict the flower object correctly.

########################################################################################################################################################################
#8_YOLO_Faculty_Notebook_Session8_YOLO_Custom_Object_Detection-1.ipynb
YOLO CUSTOM OBJECT DETECTION
chrome extension for image download https://chrome.google.com/webstore/detail/image-downloader-imageye/agionbommeaifngbhincahgmoflcikhm?hl=en Download the required custom class images in bulk and keep it one folder say "yolo_data_annot"

LabelImg https://tzutalin.github.io/labelImg/

Rename the image files in "yolo_data_annot" using the following jupyter notenook https://drive.google.com/file/d/1Mc3N1jBWuzb5etXBfx_qJrUwuspHmHd-/view?usp=sharing

Mark the Bounding box and label the object using LabelImg software It will generate one .txt file for each image and one common class name txt file(classes.txt)

Open google colab. Change the factory setting to GPU and mount it

from google.colab import drive
drive.mount('/content/drive')
Create a folder in google drive as "yolo_model". Under this move the image folder "yolo_data_annot" (Now it consist of images and txt files)

Create a another folder under "yolo_model" as darknet and clone the files from the below link !git clone 'https://github.com/AlexeyAB/darknet' '/content/drive/MyDrive/yolo_model/darknet'

Go in to the darknet folder using cd command %cd /content/drive/MyDrive/yolo_model/darknet

Go to the google drive darknet folder. You can see one file now as makefile. Download it and open. Set CPU, CUDNN and OPENCV as 1

Remove the old 'makefile' and copy the updated one in the darknet folder

execute !make in google colab

Copy the files creating-files-data-and-name.py and creating-train-and-test-txt-files.py into image folder "yolo_data_annot" https://drive.google.com/file/d/1LgF9QGf8jcrRY3iDvQjJLcJBNI83YzQI/view?usp=sharing https://drive.google.com/file/d/14_XoOuzDbssc0Ttu5zkOdaFnJ_GlGgOa/view?usp=sharing

Under "yolo_data_annot" folder, we have one files classes.txt. Open this file and save as 'classes.names'. Choose saveas type as 'all'

Go into main yolo_model folder %cd /content/drive/MyDrive/yolo_model

Execute the following files from colab !python yolo_data_annot/creating-files-data-and-name.py !python yolo_data_annot/creating-train-and-test-txt-files.py Three new txt files will be generated under the yolo_data_annot folder which contains label, train and test file info

Go to google drive folder 'yolo_model' and create one new folder custom_weight

Download the yolo weights https://drive.google.com/file/d/1CyhiP6jQ51fZGKf26ehWaXSfdZWCghBX/view?usp=sharing and copy this under the custom_weight folder in google drive

Go to darknet folder-->cfg --> download yolov3.cfg

Edit this yolov3.cfg file for the following changes

Comment the "Testing" batch_size and subdivisions
Play with the Training batch_size and subdivisions. You can give bigger number for huge data (Generally you can also give 64 for batch and 16 for subdiv)(I have given 4 and 2 as my dataset have only 11 images)
Change the maxbatches value as (number of classes2000). In my case 22000=4000
Change the steps with around 20 percent devation with maxbatches. Here 3800 to 4200
There are three yolo layers in this config file.
Change the classes to 2 (for my case) in all the three yolo layers
Change the number of filters in the convolution layer just above the yolo layer, using the formula (number of class+5)*3
Change the filter size at three places(above three yolo layers)
Save the file as yolov3_custom.cfg and upload this in darknet/cfg
Create a folder with name 'backup' under yolo_model folder to save the trained weights

Train the model using the below syntax !darknet/darknet detector train yolo_data_annot/labelled_data.data darknet/cfg/yolov3_custom.cfg custom_weight/darknet53.conv.74 -dont_show

Save the configuation and weight file in local machine and test it for any image using the script given below https://drive.google.com/file/d/1NdeHdIFY_V6Ty8paf4IPTaBDW1af1DQ-/view?usp=sharing

# The above execution steps are given in the .ipynb file "yolo_training.ipynb"
# The testing script is provided in the file "yolo_1.ipynb"
# All the small annoted dataset, and other weight files executed in class is available here:
# https://drive.google.com/drive/folders/1N7x1sAF3RE4vKrwpBgLKllu4hxTq3LMz?usp=sharing


########################################################################################################################################################################
#9_BrainTumourSegmentation_Inclass8_Question-Solution.ipynb

Brain Tumour Segmentation using Unet
Worldwide, incidences of brain tumours increases every year. Brain tumours are classified as benign (noncancerous tumours) and malignant (cancerous).Subclasses of brain tumours are primary and secondary tumours. Primary tumours start in the brain or Central Nervous Systems (CNS) whereas the secondary tumours spread from other body parts into the brain. Depends on the degree of abnormality of brain tissue, the tumours are type casted into four (1 to 4) grading levels. Tumours with 1 and 2 are low grades which are less dangerous. 3&4 grade tumours are high-grade tumours which are highly susceptible to cancer. Primary tumours have several types amongst 36.1 % all primary tumours are referred as meningioma that found near the top and outer curve of the brain. Meningioma is slowly growing noncancerous tumours that cause seizures and visual problems. Glioma is abnormal growth in glial cells presents around the neurons in the brain. Pituitary tumours grow in pituitary glands that affect body functions. Meningioma are iso-dense dura-based masses developed at the meninges of the three layers of protecting tissue of the brain and spinal cord, whose diagnosis depends on its anatomical location, shape and appearance of cells. Pituitary tumours are abnormal mass growth in cells around the surface of the pituitary gland that located at the base of skull.

For this work we have provided you the Meningioma tumor images along with its masks.

Build a Unet based segmentation model to segment the tumor region.

Dataset link: https://drive.google.com/drive/folders/11rbveSfeTsTMwHsXyPzLGTN5SDfhWcR9?usp=sharing

Import the required libraries
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from PIL import Image
from tensorflow.keras.utils import normalize
Load the images and masks in one folder and properly resize to same size (If required)
image_dir='C:\\Users\\Senthil\\Desktop\\Unet_dataset\\images_brain_tum\\'
​
mask_dir='C:\\Users\\Senthil\\Desktop\\Unet_dataset\\masks_brain_tum\\'
​
SIZE=128
​
img_dataset=[]
mask_dataset=[]
​
images=os.listdir(image_dir)
​
for i,image_name in enumerate(images):
    if (image_name.split('.')[1]=='jpg'):
        image=cv2.imread(image_dir+image_name,0)
        image=Image.fromarray(image)
        image=image.resize((SIZE,SIZE))
        img_dataset.append(np.array(image))
        #img_dataset.append(image)
        
        
masks=os.listdir(mask_dir)
​
for i,image_name in enumerate(masks):
    if (image_name.split('.')[1]=='jpg'):
        image=cv2.imread(mask_dir+image_name,0)
        image=cv2.resize(image,(SIZE,SIZE))
        (thresh, bwimage) = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY) # make sure mask is binary image
        #bwimage=Image.fromarray(bwimage)
        #mask_dataset.append(np.array(bwimage))
        mask_dataset.append(bwimage)
​
img_dataset=np.array(img_dataset)
img_dataset=normalize(img_dataset)
img_dataset=np.expand_dims(img_dataset,3)
​
mask_dataset=np.array(mask_dataset)
mask_dataset=mask_dataset/255.
mask_dataset=np.expand_dims(mask_dataset,3)
​
print(img_dataset.shape)
​
print(mask_dataset.shape)
np.unique(mask_dataset[0,:,:,0]) # make sure mask is having only 0 and 1 for binary class
Display some of the images along with its mask and make sure the position of mask matches with original image tumor position
r1=np.random.randint(1,705,size=(1,2))
r1[0][0],r1[0][1]
r1=np.random.randint(1,705,size=(1,2))
plt.figure(figsize=(10,6))
plt.subplot(2,2,1)
plt.imshow(img_dataset[r1[0][0],:,:,:],cmap='gray')
plt.subplot(2,2,2)
plt.imshow(mask_dataset[r1[0][0],:,:,:],cmap='gray')
plt.subplot(2,2,3)
plt.imshow(img_dataset[r1[0][1],:,:,:],cmap='gray')
plt.subplot(2,2,4)
plt.imshow(mask_dataset[r1[0][1],:,:,:],cmap='gray')
Write the function for Unet model. Properly define the ENCODER and DECODER section
# u-net model 
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Flatten, Conv2D, MaxPooling2D, UpSampling2D, concatenate, Conv2DTranspose, BatchNormalization, Dropout, Lambda
#from tensorflow.keras import backend as K
from tensorflow.keras import backend as K
​
​
def simple_unet_model_with_jacard(IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS):
#Build the model
    inputs = Input((IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS))
    s = inputs
​
    #Contraction path
    c1 = Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(s)
    #c1 = Dropout(0.1)(c1)
    c1 = Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c1)
    p1 = MaxPooling2D((2, 2))(c1)
    
    c2 = Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(p1)
    #c2 = Dropout(0.1)(c2)
    c2 = Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c2)
    p2 = MaxPooling2D((2, 2))(c2)
     
    c3 = Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(p2)
    #c3 = Dropout(0.2)(c3)
    c3 = Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c3)
    p3 = MaxPooling2D((2, 2))(c3)
     
    c4 = Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(p3)
    #c4 = Dropout(0.2)(c4)
    c4 = Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c4)
    p4 = MaxPooling2D(pool_size=(2, 2))(c4)
     
    c5 = Conv2D(256, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(p4)
    #c5 = Dropout(0.3)(c5)
    c5 = Conv2D(256, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c5)
    
    #Expansive path 
    u6 = Conv2DTranspose(128, (2, 2), strides=(2, 2), padding='same')(c5)
    u6 = concatenate([u6, c4])
    c6 = Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u6)
    #c6 = Dropout(0.2)(c6)
    c6 = Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c6)
     
    u7 = Conv2DTranspose(64, (2, 2), strides=(2, 2), padding='same')(c6)
    u7 = concatenate([u7, c3])
    c7 = Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u7)
    #c7 = Dropout(0.2)(c7)
    c7 = Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c7)
     
    u8 = Conv2DTranspose(32, (2, 2), strides=(2, 2), padding='same')(c7)
    u8 = concatenate([u8, c2])
    c8 = Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u8)
    #c8 = Dropout(0.1)(c8)
    c8 = Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c8)
     
    u9 = Conv2DTranspose(16, (2, 2), strides=(2, 2), padding='same')(c8)
    u9 = concatenate([u9, c1], axis=3)
    c9 = Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u9)
    #c9 = Dropout(0.1)(c9)
    c9 = Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c9)
     
    outputs = Conv2D(1, (1, 1), activation='sigmoid')(c9)
     
    model = Model(inputs=[inputs], outputs=[outputs])
    #model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.compile(optimizer = 'adam', loss = [jacard_coef_loss], metrics = [jacard_coef])
​
    model.summary()
    
    return model
 
Define the Loss function and metric using Jecard coeff or dice coeff
​
def jacard_coef(y_true, y_pred):
    y_true_f = K.flatten(y_true)
    y_pred_f = K.flatten(y_pred)
    intersection = K.sum(y_true_f * y_pred_f)
    return (intersection + 1.0) / (K.sum(y_true_f) + K.sum(y_pred_f) - intersection + 1.0)
​
def jacard_coef_loss(y_true, y_pred):
    return -jacard_coef(y_true, y_pred)  # -1 ultiplied as we want to minimize this value as loss function
​
​
Split the data into train and test. Call the Unet model and metric/loss functions defined in previous questions and compile and fit the model
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(img_dataset,mask_dataset,test_size=0.15,random_state=0)
​
​
IMG_HEIGHT=img_dataset.shape[1]
IMG_WIDTH=img_dataset.shape[2]
IMG_CHANNELS=img_dataset.shape[3]
​
model=simple_unet_model_with_jacard(IMG_HEIGHT,IMG_WIDTH,IMG_CHANNELS)
​
model.fit(x_train,y_train,batch_size=64,verbose=1,epochs=1,
          validation_data=(x_test,y_test),shuffle=False)
​
Run with more iteration on Google colab for better result. As this segmentation process is tedius it will take lot iteration for convergence
Evaluate the model performance on the test data and predict the segmented output for random test image. Plot the original image, original mask and predicted mask.
​
loss,jac_coef=model.evaluate(x_test,y_test)
​
n1=np.random.randint(0,len(x_test))
test_img=x_test[n1]
mask_test_img=y_test[n1]
test_img1=np.expand_dims(test_img,0)
pred_img=model.predict(test_img1)
pred_img1=(pred_img[0,:,:,0]>0.5).astype(np.uint8)
​
plt.figure(figsize=(16,8))
plt.subplot(131)
plt.title('Original')
plt.imshow(test_img[:,:,0],cmap='gray')
​
plt.subplot(132)
plt.title('Mask Original')
plt.imshow(mask_test_img[:,:,0],cmap='gray')
​
plt.subplot(133)
plt.title('Segmented Image')
plt.imshow(pred_img1,cmap='gray')
​
​
Use some pretrained segmentation model from segmentation_model package to acheive the brain tumor segmentation task.
import segmentation_models as sm
​
BACKBONE = 'resnet34'
preprocess_input = sm.get_preprocessing(BACKBONE)
​
X_train_prepr = preprocess_input(x_train)
X_test_prepr = preprocess_input(x_test)
​
np.unique(y_train)
model_resnet_backbone = sm.Unet(BACKBONE, input_shape=(128,128,1), encoder_weights=None, classes=1, activation='sigmoid')
def jacard_coef(y_true, y_pred):
    y_true_f = K.flatten(y_true)
    y_pred_f = K.flatten(y_pred)
    intersection = K.sum(y_true_f * y_pred_f)
    return (intersection + 1.0) / (K.sum(y_true_f) + K.sum(y_pred_f) - intersection + 1.0)
​
metrics=['accuracy', jacard_coef]
model_resnet_backbone.compile(optimizer='adam', loss='binary_crossentropy', metrics=metrics)
print(model_resnet_backbone.summary())
history2=model_resnet_backbone.fit(X_train_prepr, 
          y_train,
          batch_size=64, 
          epochs=1,
          validation_data=(X_test_prepr, y_test))

########################################################################################################################################################################
#Classification - Hyper parameter tuning - MNIST.ipynb

MNIST neural network - Hyperparameter Optimization using Tensorflow
MNIST Dataset
The MNIST database contains 60,000 training images and 10,000 testing images taken from American Census Bureau employees and American high school students. The MNIST dataset is one of the most common datasets used for image classification and accessible from many different sources. In fact, even Tensorflow and Keras allow us to import and download the MNIST dataset directly from their API.

Firstly, let's select TensorFlow version 2.x in colab

%tensorflow_version 2.x
import tensorflow
tensorflow.__version__
# Initialize the random number generator
import random
random.seed(0)
​
# Ignore the warnings
import warnings
warnings.filterwarnings("ignore")
Let's load MNIST dataset

from tensorflow.keras.datasets import mnist
​
# the data, shuffled and split between train and test sets
(X_train, y_train), (X_val, y_val) = mnist.load_data()
X_train and X_test contain greyscale RGB codes (from 0 to 255) while y_train and y_test contains labels from 0 to 9 which represents which number they actually are.

Let's visualize some numbers using matplotlib

import matplotlib.pyplot as plt
%matplotlib inline
print("Label: {}".format(y_train[9000]))
plt.imshow(X_train[9000], cmap='gray')
Print shape of the data
print(X_train.shape)
print(y_train.shape)
print(X_val.shape)
print(y_val.shape)
Reshape features
reshape() method gives a new shape to an array without changing its data
You can read more about it here https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html
X_train = X_train.reshape(60000, 784)
print(X_train.shape)
X_val = X_val.reshape(10000, 784)
print(X_val.shape)
Normalize features
Normalize features from 0-255 to 0-1
print(X_train.max())
print(X_train.min())
​
X_train = X_train / 255.0
X_val = X_val / 255.0
​
print(X_train.max())
print(X_train.min())
​
One-hot encode the class vector
convert class vectors (integers) to binary class matrix
convert X_train and X_val
number of classes: 10
print(y_train[10])
y_train = tensorflow.keras.utils.to_categorical(y_train, num_classes=10)
y_val = tensorflow.keras.utils.to_categorical(y_val, num_classes=10)
print(y_train[10])
Let's see some other images and their labels
import numpy as np
​
# visualizing the first 10 images in the dataset and their labels
%matplotlib inline
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 1))
for i in range(10):
    plt.subplot(1, 10, i+1)
    plt.imshow(X_train[i].reshape(28, 28), cmap="gray")
    plt.axis('off')
    print('label for each of the below image: %s' % (np.argmax(y_train[0:10][i])))
plt.show()
​
Creating model 1
Written in a function - to run it multiple times
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import regularizers, optimizers
​
def train_and_test_loop(iterations, lr, Lambda, verb=True):
​
    ## hyperparameters
    iterations = iterations
    learning_rate = lr
    hidden_nodes = 256
    output_nodes = 10
        
    model = Sequential()
    model.add(Dense(hidden_nodes, input_shape=(784,), activation='relu'))
    model.add(Dense(hidden_nodes, activation='relu'))
    model.add(Dense(output_nodes, activation='softmax', kernel_regularizer=regularizers.l2(Lambda)))
    
    sgd = optimizers.SGD(lr=learning_rate, decay=1e-6, momentum=0.9)
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
    
    # Fit the model
    model.fit(X_train, y_train, epochs=iterations, batch_size=1000, verbose= 1)
Creating model 2
Same model as above
Instead of accuracy at each epoch below code gives the consolidate accuracy
Notice: The model.evaluate line at the last is the only difference from model 1
def train_and_test_loop1(iterations, lr, Lambda, verb=True):
​
    ## hyperparameters
    iterations = iterations
    learning_rate = lr
    hidden_nodes = 256
    output_nodes = 10
​
    model = Sequential()
    model.add(Dense(hidden_nodes, input_shape=(784,), activation='relu'))
    model.add(Dense(hidden_nodes, activation='relu'))
    model.add(Dense(output_nodes, activation='softmax', kernel_regularizer=regularizers.l2(Lambda)))
    
    sgd = optimizers.SGD(lr=learning_rate, decay=1e-6, momentum=0.9)
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
    
    # Fit the model
    model.fit(X_train, y_train, epochs=iterations, batch_size=1000, verbose= 1)
    score = model.evaluate(X_train, y_train, verbose=0)
    
    return score
Next steps
Double Check that the loss is reasonable
Disable the regularization (Lambda = 0)
lr = 0.00001
Lambda = 0
train_and_test_loop(1, lr, Lambda)
Question
Is the loss range correct? What about accuracy, does it make sense for an untrained network
Answer
Absolutely! There are 10 output classes and the model is correctly predicting 1 up on 10 times (1/10 = 0.1% approx) as it is untrained.
Now, lets crank up the Lambda(Regularization)and check what it does to our loss function.
lr = 0.00001
Lambda = 1e3
train_and_test_loop(1, lr, Lambda)
loss went up. Good! (Another sanity check)

Now, lets overfit to a small subset of our dataset, in this case 20 images, to ensure our model architecture is good
X_train_subset = X_train[0:20]
y_train_subset = y_train[0:20]
X_train = X_train_subset
y_train = y_train_subset
X_train.shape
y_train.shape
Tip: Make sure that you can overfit very small portion of the training data
So, set a small learning rate and turn regularization off

In the code below:

Take the first 20 examples from MNIST
turn off regularization(reg=0.0)
use simple vanilla 'sgd'
Lets try and run for 500 iterations as the data set is very small

lr = 0.001
Lambda = 0
train_and_test_loop(500, lr, Lambda)
Very small loss, train accuracy going to 100, nice! We are successful in overfitting. The model architecture looks fine. Lets go for fine tuning it.
Loading the original dataset again
Import dataset
This dataset can be imported
High level API Keras has some datasets available
mnist.load_data() returns two tuples (x_train, y_train), (x_test, y_test):
x_train, x_val: uint8 array of grayscale image data with shape (num_samples, 28, 28)
y_train, y_val: uint8 array of digit labels (integers in range 0-9) with shape (num_samples,).
(X_train, y_train), (X_val, y_val) = tensorflow.keras.datasets.mnist.load_data()
Reshape features
reshape() method gives a new shape to an array without changing its data
You can read more about it here https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html
X_train = X_train.reshape(60000, 784)
print(X_train.shape)
X_val = X_val.reshape(10000, 784)
print(X_val.shape)
Normalize features
Normalize features from 0-255 to 0-1
X_train = X_train / 255.0
X_val = X_val / 255.0
One-hot encode the class vector
convert class vectors (integers) to binary class matrix
convert X_train and X_val
number of classes: 10
y_train = tensorflow.keras.utils.to_categorical(y_train, num_classes=10)
y_val = tensorflow.keras.utils.to_categorical(y_val, num_classes=10)
Start with small regularization and find learning rate that makes the loss go down.
we start with Lambda(small regularization) = 1e-7
we start with a small learning rate = 1e-7
lr = 1e-7
Lambda = 1e-7
train_and_test_loop(20, lr, Lambda)
Loss barely changing. Learning rate is probably too low.
Okay now lets try a (larger) learning rate 1e6. What could possibly go wrong?
Learning rate lr = 1e8
Regularization lambda = 1e-7
lr = 1e8
Lambda = 1e-7
train_and_test_loop(20, lr, Lambda)
Loss exploding. Learning rate is too high.
Cost is very high. Always means high learning rate
Lets try to train now with a value of learning rate between 1e-7 and 1e8
learning rate = 1e4
regularization remains the small, lambda = 1e-7
lr = 1e4
Lambda = 1e-7
train_and_test_loop(20, lr, Lambda)
Still too high learning rate. Loss is not decreasing. The rough range of learning rate we should be cross validating is somewhere between [1e3 to 1e-7]
Hyperparameter Optimization
Cross validation Strategy
Do coarse -> fine cross-validation in stages

First stage: only a few epochs to get rough idea of what params work

Second stage: longer running time, finer search

… (repeat as necessary)

Tip for detecting explosions in the solver:
If the cost is ever > 3 * original cost, break out early
For example: Run coarse search for 10 times with different lr and Lambda values each with 100 epochs.
import math
for k in range(1,10):
    lr = math.pow(10, np.random.uniform(-7.0, 3.0))
    Lambda = math.pow(10, np.random.uniform(-7,-2))
    best_acc = train_and_test_loop1(100, lr, Lambda, False)
    print("Try {0}/{1}: Best_val_acc: {2}, lr: {3}, Lambda: {4}\n".format(k, 100, best_acc, lr, Lambda))
As you can see from above, Case 2, 3 and 7 yields good accuracy. It is better to focus on those values for learning rate and Lambda
Now run finer search
import math
for k in range(1,5):
    lr = math.pow(10, np.random.uniform(-4.0, -1.0))
    Lambda = math.pow(10, np.random.uniform(-4,-2))
    best_acc = train_and_test_loop1(100, lr, Lambda, False)
    print("Try {0}/{1}: Best_val_acc: {2}, lr: {3}, Lambda: {4}\n".format(k, 100, best_acc, lr, Lambda))
alt text### Running deep with lr=0.02 and Lambda=1e-4

lr = 2e-2
Lambda = 1e-4
train_and_test_loop1(100, lr, Lambda)

########################################################################################################################################################################
#Classification_MNIST.ipynb

MNIST Dataset
The MNIST database contains 60,000 training images and 10,000 testing images taken from American Census Bureau employees and American high school students. The MNIST dataset is one of the most common datasets used for image classification and accessible from many different sources. In fact, even Tensorflow and Keras allow us to import and download the MNIST dataset directly from their API.

Firstly, let's select TensorFlow version 2.x in colab

%tensorflow_version 2.x
import tensorflow
tensorflow.__version__
# Initialize the random number generator
import random
random.seed(0)
​
# Ignore the warnings
import warnings
warnings.filterwarnings("ignore")
Let's load MNIST dataset

from tensorflow.keras.datasets import mnist
​
# the data, shuffled and split between train and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train and X_test contain greyscale RGB codes (from 0 to 255) while y_train and y_test contains labels from 0 to 9 which represents which number they actually are.

Let's visualize some numbers using matplotlib

import matplotlib.pyplot as plt
%matplotlib inline
print("Label: {}".format(y_train[8000]))
plt.imshow(X_train[8000], cmap='gray')
Print shape of the data
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)
Reshape train and test sets into compatible shapes
Sequential model in tensorflow.keras expects data to be in the format (n_e, n_h, n_w, n_c)
n_e= number of examples, n_h = height, n_w = width, n_c = number of channels
do not reshape labels
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)
Normalize data
we must normalize our data as it is always required in neural network models
we can achieve this by dividing the RGB codes with 255 (which is the maximum RGB code minus the minimum RGB code)
normalize X_train and X_test
make sure that the values are float so that we can get decimal points after division
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
​
X_train /= 255
X_test /= 255
Print shape of data and number of images
print shape of X_train
print number of images in X_train
print number of images in X_test
print("X_train shape:", X_train.shape)
print("Images in X_train:", X_train.shape[0])
print("Images in X_test:", X_test.shape[0])
print("Max value in X_train:", X_train.max())
print("Min value in X_train:", X_train.min())
​
One-hot encode the class vector
convert class vectors (integers) to binary class matrix
convert y_train and y_test
number of classes: 10
we are doing this to use categorical_crossentropy as loss
from tensorflow.keras.utils import to_categorical
​
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)
​
print("Shape of y_train:", y_train.shape)
print("One value of y_train:", y_train[0])
DNN
Initialize a sequential model
let's a sequential model
flatten the data
add Flatten later
flatten layers flatten 2D arrays to 1D array before building the fully connected layers
add 2 dense layers
number of neurons in first layer: 128
number of neurons in last layer: number of classes
activation function in first layer: relu
activation function in last layer: softmax
we may experiment with any number of neurons for the first Dense layer; however, the final Dense layer must have neurons equal to the number of output classes
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
​
model = Sequential()
model.add(Flatten())
model.add(Dense(128, activation="relu"))
model.add(Dense(10, activation="softmax"))
Compile and fit the model
let's compile our model
loss: "categorical_crossentropy"
metrics: "accuracy"
optimizer: "sgd"
then next step will be to fit model
give train data - training features and labels
batch size: 32
epochs: 10
give validation data - testing features and labels
# Compile the model
model.compile(loss="categorical_crossentropy", metrics=["accuracy"], optimizer="sgd")
​
# Fit the model
model.fit(x=X_train, y=y_train, batch_size=32, epochs=10, validation_data=(X_test, y_test))
Final loss and accuracy
model.evaluate(X_test, y_test)

########################################################################################################################################################################
#Deep Learning_un proctored-Question.ipynb

PART B 10 MARKS- ANSWERS FOR ALL THE QUESTIONS
Question 1: (10 Marks)
Draw the Relu activation function and leaky relu activation function using python code. The input value ranges are [-15 to 15] and a=0.05 (3 marks)
Compare these two activation function (1 marks)
Write the python code for the neural network architecture with given inputs and compute the output value for the network (6 marks)
Input layer with 5 neurons (x1, x2, x3, x4, x5)

One hidden layer with three neurons (h1, h2, h3)

Output layer to predict the binary class

The first stage trained weights are w11=w12=w13=1,w21=w22=w23=-1, w31=w32=w33=2, w41=w42=w43=-2 , w51=w52=w53= -1

The second stage trained weights are v11 = v21 = v31= 2

Relu activation function is used for Hidden layers and sigmoidal is used for output layer

Find the probability value of the output neuron for the Input x1= 1, x2 = 2, x3=3, x4=4 ,x5 = 5

#Draw the Relu activation function and leaky relu activation function using python code. The input value ranges are [-15 to 15] 
​
# Relu Activation
​
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf; 
​
x=np.linspace(-15,15,100)
y=np.zeros((1,len(x)))
y=y[0]
for i in range(len(x)):
    if x[i]<0:
        y[i]=0
    else:
        y[i]=x[i]
plt.plot(x,y)
plt.title('ReLU Activation Function')
plt.grid()
plt.show()
def leaky_ReLU(x):
    data = [max(0.05*value,value) for value in x]
    return np.array(data, dtype=float)
​
x_data = np.linspace(-15,15,100)
y_data = leaky_ReLU(x_data)
​
plt.plot( x_data, y_data)
plt.title('Leaky ReLU Activation Function')
plt.grid()
plt.show()
​
Compare Relu and Leaky Relu activation function (Answer Here)

#2. Compare these two activation function (1 marks)
plt.plot( x, y,x_data, y_data)
plt.title('ReLU Activation Function & leaky ReLU Activation Function')
plt.legend(['ReLU','leaky_ReLU'])
plt.grid()
plt.show()
#3
Write the python code for the neural network architecture with given inputs and compute the output value for the network 
Input layer with 5 neurons (x1, x2, x3, x4, x5)
One hidden layer with three neurons (h1, h2, h3)
Output layer to predict the binary class
The first stage trained weights are w11=w12=w13=1,w21=w22=w23=-1, w31=w32=w33=2, w41=w42=w43=-2 , w51=w52=w53= -1
The second stage trained weights are v11 = v21 = v31= 2
Relu activation function is used for Hidden layers and sigmoidal is used for output layer
Find the probability value of the output neuron for the Input x1= 1, x2 = 2, x3=3, x4=4 ,x5 = 5
x=np.array(([1],[2],[3],[4],[5]))
y=np.array(([0],[1],[1],[0],[0]))
​
x_b=np.concatenate((np.zeros((5,4), dtype=int), x), axis=1)
inp_size=5
hid_size=3
out_size=1
w1=np.array(([1,1,1],[-1,-1,-1],[2,2,2],[-2,-2,-2],[-1,-1,-1]))
w1
w2=np.array(([2],[2],[2]))
w2
def sigmoid(z):
    sig=1/(1+np.exp(-z))
    return sig
​
def forward(x):
    z1=np.dot(x,w1)
    y1=sigmoid(z1)
    z2=np.dot(y1,w2)
    out=sigmoid(z2)
    print('out_shape=', out.shape)
    print('y1_shape=', y1.shape)
    return out,y1
​
def backward(x,y,w1,w2,y1,out):
    out_err=y-out
    out_delta=out_err*(out*(1-out))
    y1_err=np.dot(out_delta,w2.T)
    y1_delta=y1_err*(y1*(1-y1))
    w2=w2.astype(float)
    w1=w2.astype(float)
    w2+=np.dot(y1.T,out_delta)  # consider alpha=1  
    A=np.dot(x.T,y1_delta).T
    B=A[:,-1]
    A=np.dot(x.T,y1_delta)
    w1+=B
    return w1,w2
​
def train(x,y):
    [out,y1]=forward(x)
    backward(x,y,w1,w2,y1,out)
    return w1,w2,out
​
def predict(tes):
    [out,y1]=forward(tes)
    pred=out
    return pred
​
loss=np.zeros([1000,1],dtype=float)
for i in range(1000):
    [w1,w2,out]=train(x_b,y)
    loss[i]=np.mean(np.square(y-out))  
plt.plot(loss)
tes=np.array(([1,0,0],[1,0,1],[1,1,0],[1,1,1]))
pred=predict(tes)
print(pred)
from sklearn.linear_model import LogisticRegression
logit=LogisticRegression()
logit.fit(x,y)
ypred=logit.predict(x)
ypred


########################################################################################################################################################################
#GA_DL_Solution_binary_classification_Nonproctored_17th_May_2021.ipynb

from google.colab import drive
drive.mount('/content/drive')

from numpy.random import seed
from pandas import read_csv, DataFrame
from sklearn.preprocessing import minmax_scale
from keras.optimizers import SGD
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Flatten,Dense,Dropout,Activation
from keras.layers.normalization import BatchNormalization
import numpy as np
import pandas as pd
import sys
import tensorflow as tf
from keras import * 
import keras 
print( keras.__version__)
from keras import backend as K
K.set_image_data_format('channels_last')
##K.set_image_dim_ordering('tf')
from sklearn.metrics import log_loss
from sklearn.metrics import accuracy_score
from keras.metrics import binary_accuracy
from keras.metrics import categorical_accuracy
​
keras.backend.backend()
##keras.backend.image_dim_ordering()
#demo for planes
img_width, img_height = 200, 200
​
​
train_data_dir      = '/content/drive/My Drive/DL-Assessment/re_data/Train/'
validation_data_dir = '/content/drive/My Drive/DL-Assessment/re_data/Valid/'
​
batch_size = 2
​
​
import time
start = time.time()
​
if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)
    
    
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=input_shape)) #(3,227, 227)
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
​
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
​
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
​
# the model so far outputs 3D feature maps (height, width, features)
​
model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))
# COMPILE
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
​
end = time.time()
print(end - start)
from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)
​
#batch_size = 10
# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator(rescale=1. / 255)
​
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')
​
validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')
import time
start = time.time()
​
model.fit_generator(train_generator,
                        steps_per_epoch=100,
                        epochs=100,
                        validation_data=validation_generator)
​
end = time.time()
print(end - start)
from skimage.io import imread
from skimage.transform import resize
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.imagenet_utils import decode_predictions
import matplotlib.pyplot as plt
​
import cv2
import numpy as np
​
import time
start = time.time()
​
#img = imread('/content/drive/My Drive/28th_April_2021_GA_DL_GL/GL-Dataset/AD_GL_Test/0-Sq.png')
​
 #make sure that path_to_file contains the path to the image you want to predict on. 
img = imread('/content/drive/My Drive/DL-Assessment/20210505-175328-151032.jpg')
img = resize(img,(200,200))
#img = load_img(img, target_size=(227, 227))
#print('PIL image size',img.size)
plt.imshow(img)
plt.show()
​
test_img = cv2.imread('/content/drive/My Drive/DL-Assessment/20210505-175328-151032.jpg')
test_img = test_img.reshape(1,200,200,3)
​
Y = model.predict(test_img)[0]
print(Y)
​
#val = np.argmax(Y)
if(Y >= 0.5):
    print("Wolf")
else:
    print("Dog")
​
end = time.time()
print(end - start)
from skimage.io import imread
from skimage.transform import resize
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.imagenet_utils import decode_predictions
import matplotlib.pyplot as plt

import cv2
import numpy as np

import time
start = time.time()

#img = imread('/content/drive/My Drive/28th_April_2021_GA_DL_GL/GL-Dataset/AD_GL_Test/0-Sq.png')

 #make sure that path_to_file contains the path to the image you want to predict on. 
img = imread('/content/drive/My Drive/DL-Assessment/20210505-175427-427576.jpg')
img = resize(img,(200,200))
#img = load_img(img, target_size=(227, 227))
#print('PIL image size',img.size)
plt.imshow(img)
plt.show()

test_img = cv2.imread('/content/drive/My Drive/DL-Assessment/20210505-175427-427576.jpg')
test_img = test_img.reshape(1,200,200,3)

Y = model.predict(test_img)[0]
print(Y)

#val = np.argmax(Y)
if(Y >= 0.5):
    print("Wolf")
else:
    print("Dog")

end = time.time()
print(end - start)
from skimage.io import imread
from skimage.transform import resize
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.imagenet_utils import decode_predictions
import matplotlib.pyplot as plt
​
import cv2
import numpy as np
​
import time
start = time.time()
​
#img = imread('/content/drive/My Drive/28th_April_2021_GA_DL_GL/GL-Dataset/AD_GL_Test/0-Sq.png')
​
 #make sure that path_to_file contains the path to the image you want to predict on. 
img = imread('/content/drive/My Drive/DL-Assessment/20210505-175427-427576.jpg')
img = resize(img,(200,200))
#img = load_img(img, target_size=(227, 227))
#print('PIL image size',img.size)
plt.imshow(img)
plt.show()
​
test_img = cv2.imread('/content/drive/My Drive/DL-Assessment/20210505-175427-427576.jpg')
test_img = test_img.reshape(1,200,200,3)
​
Y = model.predict(test_img)[0]
print(Y)
​
#val = np.argmax(Y)
if(Y >= 0.5):
    print("Wolf")

########################################################################################################################################################################
#Hands-On Demo-MNIST_Python_Neural_Network_Final.ipynb

MNIST neural network from scratch
Fully Connected Layer (Linear Layer)
import numpy as np 
​
class Linear():
    def __init__(self, in_size, out_size):
        self.W = np.random.randn(in_size, out_size) * 0.01
        self.b = np.zeros((1, out_size))
        self.params = [self.W, self.b]
        self.gradW = None
        self.gradB = None
        self.gradInput = None        
​
    def forward(self, X):
        self.X = X
        self.output = np.dot(X, self.W) + self.b
        return self.output
​
    def backward(self, nextgrad):
        self.gradW = np.dot(self.X.T, nextgrad)
        self.gradB = np.sum(nextgrad, axis=0)
        self.gradInput = np.dot(nextgrad, self.W.T)
        return self.gradInput, [self.gradW, self.gradB]
Rectified Linear Activation Layer (ReLU)
class ReLU():
    def __init__(self):
        self.params = []
        self.gradInput = None
​
    def forward(self, X):
        self.output = np.maximum(X, 0)
        return self.output
​
    def backward(self, nextgrad):
        self.gradInput = nextgrad.copy()
        self.gradInput[self.output <=0] = 0
        return self.gradInput, []
Defining the softmax function
def softmax(x):
    exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
    return exp_x / np.sum(exp_x, axis=1, keepdims=True)
Defining the Cross Entropy Loss
class CrossEntropy:
    def forward(self, X, y):
        self.m = y.shape[0]
        self.p = softmax(X)
        cross_entropy = -np.log(self.p[range(self.m), y])
        # loss = cross_entropy[0] / self.m         # please note this line was in the video however the correct line is the below one
        loss = np.sum(cross_entropy) / self.m      # which involves taking a sum across the losses for all the examples in the batch
        return loss
    
    def backward(self, X, y):
        y_idx = y.argmax()        
        grad = softmax(X)
        grad[range(self.m), y] -= 1
        grad /= self.m
        return grad
Loading the MNIST dataset
from keras.datasets import mnist
from keras.utils import np_utils
​
​
(train_features, train_targets), (test_features, test_targets) = mnist.load_data()
​
​
train_features = train_features.reshape(60000, 784)
print(train_features.shape)
test_features = test_features.reshape(10000, 784)
print(test_features.shape)
​
​
# # normalize inputs from 0-255 to 0-1
train_features = train_features / 255.0
test_features = test_features / 255.0
​
print(train_targets.shape)
print(test_targets.shape)
​
X_train = train_features
y_train = train_targets
​
X_val = test_features
y_val = test_targets
​
# visualizing the first 10 images in the dataset and their labels
%matplotlib inline
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 1))
for i in range(10):
    plt.subplot(1, 10, i+1)
    plt.imshow(X_train[i].reshape(28, 28), cmap="gray")
    plt.axis('off')
plt.show()
print('label for each of the above image: %s' % (y_train[0:10]))
Here, we define the container NN class that enables the forward prop and backward propagation of the entire network. Note, how this class enables us to add layers of different types and also correctly pass gradients using the chain rule.
class NN():
    def __init__(self, lossfunc=CrossEntropy()):
        self.params = []
        self.layers = []
        self.loss_func = lossfunc
        self.grads = []
        
    def add_layer(self, layer):
        self.layers.append(layer)
        self.params.append(layer.params)
​
    def forward(self, X):
        for layer in self.layers:
            X = layer.forward(X)
        return X
    
    def backward(self, nextgrad):
        self.clear_grad_param()
        for layer in reversed(self.layers):
            nextgrad, grad = layer.backward(nextgrad)
            self.grads.append(grad)
        return self.grads
    
    def train_step(self, X, y):
        out = self.forward(X)
        loss = self.loss_func.forward(out,y)
        nextgrad = self.loss_func.backward(out,y)
        grads = self.backward(nextgrad)
        return loss, grads
    
    def predict(self, X):
        X = self.forward(X)
        return np.argmax(X, axis=1)
    
    def predict_scores(self, X):
        X = self.forward(X)
        return X
    
    def clear_grad_param(self):
        self.grads = []
Defining the update function (SGD with momentum)
def update_params(velocity, params, grads, learning_rate=0.01, mu=0.9):
    for v, p, g, in zip(velocity, params, reversed(grads)):
        for i in range(len(g)):
            v[i] = mu * v[i] + learning_rate * g[i]
            p[i] -= v[i]
Defining a function which gives us the minibatches (both the datapoint and the corresponding label)
# get minibatches
def minibatch(X, y, minibatch_size):
    n = X.shape[0]
    minibatches = []
    permutation = np.random.permutation(X.shape[0])
    X = X[permutation]
    y = y[permutation]
    
    for i in range(0, n , minibatch_size):
        X_batch = X[i:i + minibatch_size, :]
        y_batch = y[i:i + minibatch_size, ]
        minibatches.append((X_batch, y_batch))
        
    return minibatches
The traning loop
def train(net, X_train, y_train, minibatch_size, epoch, learning_rate, mu=0.9, X_val=None, y_val=None):
    val_loss_epoch = []
    minibatches = minibatch(X_train, y_train, minibatch_size)
    minibatches_val = minibatch(X_val, y_val, minibatch_size)
​
    
    for i in range(epoch):
        loss_batch = []
        val_loss_batch = []
        velocity = []
        for param_layer in net.params:
            p = [np.zeros_like(param) for param in list(param_layer)]
            velocity.append(p)
            
        # iterate over mini batches
        for X_mini, y_mini in minibatches:
            loss, grads = net.train_step(X_mini, y_mini)
            loss_batch.append(loss)
            update_params(velocity, net.params, grads, learning_rate=learning_rate, mu=mu)
​
        for X_mini_val, y_mini_val in minibatches_val:
            val_loss, _ = net.train_step(X_mini, y_mini)
            val_loss_batch.append(val_loss)
        
        # accuracy of model at end of epoch after all mini batch updates
        m_train = X_train.shape[0]
        m_val = X_val.shape[0]
        y_train_pred = np.array([], dtype="int64")
        y_val_pred = np.array([], dtype="int64")
        y_train1 = []
        y_vall = []
        for i in range(0, m_train, minibatch_size):
            X_tr = X_train[i:i + minibatch_size, : ]
            y_tr = y_train[i:i + minibatch_size,]
            y_train1 = np.append(y_train1, y_tr)
            y_train_pred = np.append(y_train_pred, net.predict(X_tr))
​
        for i in range(0, m_val, minibatch_size):
            X_va = X_val[i:i + minibatch_size, : ]
            y_va = y_val[i:i + minibatch_size,]
            y_vall = np.append(y_vall, y_va)
            y_val_pred = np.append(y_val_pred, net.predict(X_va))
            
        train_acc = check_accuracy(y_train1, y_train_pred)
        val_acc = check_accuracy(y_vall, y_val_pred)
​
        mean_train_loss = sum(loss_batch) / float(len(loss_batch))
        mean_val_loss = sum(val_loss_batch) / float(len(val_loss_batch))
        
        val_loss_epoch.append(mean_val_loss)
        print("Loss = {0} | Training Accuracy = {1} | Val Loss = {2} | Val Accuracy = {3}".format(mean_train_loss, train_acc, mean_val_loss, val_acc))
    return net
Checking the accuracy of the model
def check_accuracy(y_true, y_pred):
    return np.mean(y_pred == y_true)
Invoking all that we have created until now
from random import shuffle
​
## input size
input_dim = X_train.shape[1]
​
## hyperparameters
iterations = 10
learning_rate = 0.1
hidden_nodes = 32
output_nodes = 10
​
## define neural net
nn = NN()
nn.add_layer(Linear(input_dim, hidden_nodes))
nn.add_layer(ReLU())
nn.add_layer(Linear(hidden_nodes, output_nodes))
​
nn = train(nn, X_train , y_train, minibatch_size=200, epoch=10, \
           learning_rate=learning_rate, X_val=X_val, y_val=y_val)
fprop a single image and showing its prediction
plt.imshow(X_val[0].reshape(28,28), cmap='gray')
# Predict Scores for each class
prediction = nn.predict_scores(X_val[0])[0]
print ("Scores")
print (prediction)
np.argmax(prediction)
predict_class = nn.predict(X_val[0])[0]
predict_class
# Original class
y_val[0]

########################################################################################################################################################################
#In_Class_Session1-1.ipynb

Deep Learning Session 1: In-Class 1
1. Creation of Tensors
2. Slicing of Tensors
3. Operations on Tensors
4. Activation Functions
import numpy as np
import pandas as pd
import sklearn
import tensorflow as tf
import matplotlib.pyplot as plt
pip install tensorflow
1. Create a random tensor with 4 rows and 3 columns. Output random values should form a normal distribution
t = tf.Variable(tf.random.normal((4,3)))
t
2. Access the second row of the above matrix and print its value alone
t[1]
3. Assign the first value (first row, first column) and last value(last row, last column) to zero
val = [0,0]
ind = [[0, 0], [3,2]]
​
by_ind = tf.tensor_scatter_nd_update(t, [ind], [val])
by_ind
4. Replace all the values of third row to zero
ind = [[2,0],[2,1],[2,2]]
​
by_ind = tf.tensor_scatter_nd_update(t, [ind], [[0 for i in range(3)]])
by_ind
5. Create two tensor constants and perform addition and multiplication
a=tf.constant([4])
b=tf.constant([3])
print(a+b)
print(a*b)
6. Create two tensors [3,2] and [4,6]. Compute the equilidean distance between the two tensor points
a=tf.constant([3,2])
b=tf.constant([4,6])
​
Euch_distance = np.sqrt(tf.add_n((a-b)**2).numpy())
Euch_distance
​
7. Create 2 random matrices of size [3,3] and [3,3] with minimum value 1 and maximum value 10 and perform element wise multiplication and Matrix Multiplications
a = tf.random.uniform(
    shape =[3,3],
    minval=1,
    maxval=10,
    dtype=tf.dtypes.float32,
    seed=10
)
b = tf.random.uniform(
    shape =[3,3],
    minval=1,
    maxval=10,
    dtype=tf.dtypes.float32,
    seed=5
)
​
print("a :", a)
print("b :", b)
print("Element wise : ", a*b)
print("Matrix : ", tf.matmul(a,b))
8. Compute the product of determinant of above two matrices
tf.linalg.det(a*b) * tf.linalg.det( tf.matmul(a,b))
9. Create a float tensor and cast it into integer
float_tensor = tf.constant([2.0, 3.0, 4.0])
float_tensor
tf.cast(float_tensor, tf.int16, name=None)
10. Plot the Sigmoidal activation function using the equation. keep the x value between -10 to 10
import matplotlib.pyplot as plt
​
x = tf.constant(range(-10,10,1), dtype = tf.float32)
y = tf.keras.activations.sigmoid(x).numpy()
​
plt.plot(x,y)
​
11. Plot the Relu activation function using the equation. keep the x value between -10 to 10
x = tf.constant(range(-10,10,1), dtype = tf.float32)
y = tf.keras.activations.relu(x).numpy()
​
plt.plot(x,y)
​
12. Plot the Tanh activation function using the equation. keep the x value between -10 to 10
x = tf.constant(range(-10,10,1), dtype = tf.float32)
y = tf.keras.activations.tanh(x).numpy()
​
plt.plot(x,y)
​
13. Perform the following equation using tensors y = x^4+x^2+6, where x = [1,2,4,2,8,10]
x = tf.constant([1,2,4,2,8,10])
y = x**4 + x**2 +6
print(y)
14. Consider the regression data below:
inp=tf.constant([[18,1.5,1.5],[21,3,1.2],[29,7,2.5],[29,11,1.5],[17,1,1.5], [22,2,2.5],[31,12,1.5],[30,8,2.5]])

out=tf.constant([[5],[6],[9],[13],[4.8],[5.5],[13.2],[10.5]])

Compute the model coefficents using adam optimizer ? Use the loss function as Sum of squared error

inp=tf.constant([[18,1.5,1.5],[21,3,1.2],[29,7,2.5],[29,11,1.5],[17,1,1.5], [22,2,2.5],[31,12,1.5],[30,8,2.5]])
​
out=tf.constant([[5],[6],[9],[13],[4.8],[5.5],[13.2],[10.5]])
reg_model= tf.keras.experimental.LinearModel()
reg_model.compile(optimizer='adam', loss='mse')
reg_model.fit(inp, out, epochs=100)
print("coeffocients: \n\n",reg_model.get_weights())
15. Perform the following equation
new_weight = alpha *Error + previous_weight
Assign the initial value of new_weight=0
Randomly create 100 values for error. Update the new_weight for every value of error
new_weight=0
Error = tf.random.normal((100,))
alpha = 0.01
​
for i in Error:
    previous_weight = new_weight
    new_weight = alpha *i + previous_weight
    print(f"Previous : {previous_weight}\t New : {new_weight}")

########################################################################################################################################################################
#Inclass_Session2_Question-1-1.ipynb

CIFAR-10 Dataset
CIFAR-10 is an established computer-vision dataset used for object recognition. It is a subset of the 80 million tiny images dataset and consists of 60,000 32x32 color images containing one of 10 object classes, with 6000 images per class. It was collected by Alex Krizhevsky, Vinod Nair, and Geoffrey Hinton.

In fact, even Tensorflow and Keras allow us to import and download the MNIST dataset directly from their API.

labels = [‘airplane’, ‘automobile’, ‘bird’, ‘cat’, ‘deer’, ‘dog’, ‘frog’, ‘horse’, ‘ship’, ‘truck’]

Import tensorflow and check it's version

import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt
Let's load CIFAR dataset

from tensorflow.keras.datasets import cifar10
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
1. Print shape of the data and understand howmany images of different class exist in this datset
X_train.shape
X_test.shape
2. Visualize some images using matplotlib
plt.imshow(X_train[0])
plt.imshow(X_train[1000])
plt.imshow(X_train[5354])
3. Convert the RGB Image to Grayscale(For easier computation)
Hint: tf.image.rgb_to_grayscale(X_train)

The above code will give the result as tensor, take only the numpy part from it and procced.

tf_train_gr = tf.image.rgb_to_grayscale(X_train).numpy()
tf_test_gr = tf.image.rgb_to_grayscale(X_test).numpy()
plt.imshow(tf_train_gr[0].reshape(32,32),cmap='gray', vmin=0, vmax=255)
4. Normalize the data so that data is in range 0-1
tf_train_gr_norm = tf.keras.utils.normalize(tf_train_gr, axis=-1, order=2)
tf_test_gr_norm  = tf.keras.utils.normalize(tf_test_gr,  axis=-1, order=2)
5. Reshape train and test images into one dimensional vector
tf_train_gr_norm.shape
tf_train_gr_norm_res = tf.reshape(tf_train_gr_norm, [X_train.shape[0], -1])
tf_test_gr_norm_res = tf.reshape(tf_test_gr_norm, [X_test.shape[0], -1])
6. Print shape of data and number of images
tf_train_gr_norm_res.shape
tf_test_gr_norm_res.shape
7. One-hot encode the class vector
Hint: from tensorflow.keras.utils import to_categorical

from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)
y_train.shape
y_test.shape
DNN
08. Construct the Deep Neural Network of following architecture
    input_neurons x 64 x 32 x 32 x output_neurons
model = tf.keras.models.Sequential([
  tf.keras.layers.InputLayer(input_shape = 1024),
  tf.keras.layers.Dense(64, activation='relu'),
  tf.keras.layers.Dense(32, activation='relu'),
  tf.keras.layers.Dense(32, activation='relu'),
  tf.keras.layers.Dense(10)
])
09. Compile and fit the model
let's compile our model
loss: "categorical_crossentropy"
metrics: "accuracy"
optimizer: "sgd"
then next step will be to fit model
give train data - training features and labels
batch size: 32
epochs: 50
give validation data - testing features and labels
model.compile(optimizer='sgd',
              loss=tf.keras.losses.CategoricalCrossentropy(),#from_logits=True
              metrics=['accuracy'])
model.fit(tf_train_gr_norm_res, y_train, epochs=50, batch_size=32)
10. Calculate Final loss and accuracy on test data
model.evaluate(tf_test_gr_norm_res,  y_test, verbose=2)

########################################################################################################################################################################
#Inclass_Session2_Question.ipynb

CIFAR-10 Dataset
CIFAR-10 is an established computer-vision dataset used for object recognition. It is a subset of the 80 million tiny images dataset and consists of 60,000 32x32 color images containing one of 10 object classes, with 6000 images per class. It was collected by Alex Krizhevsky, Vinod Nair, and Geoffrey Hinton.

In fact, even Tensorflow and Keras allow us to import and download the MNIST dataset directly from their API.

labels = [‘airplane’, ‘automobile’, ‘bird’, ‘cat’, ‘deer’, ‘dog’, ‘frog’, ‘horse’, ‘ship’, ‘truck’]

Import tensorflow and check it's version

import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt
​
from warnings import filterwarnings
filterwarnings('ignore')
Let's load CIFAR dataset

from tensorflow.keras.datasets import cifar10
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
1. Print shape of the data and understand howmany images of different class exist in this datset
X_train.shape
y_train.shape
X_test.shape
y_train.shape
import pandas as pd
x=pd.Series(y_train.flatten())
x.value_counts()
​
2. Visualize some images using matplotlib
def plot_image(img):
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
​
  plt.imshow(img, cmap=plt.cm.binary)
for i in range(5):
    plot_image( X_train[i])
    plt.show()
3. Convert the RGB Image to Grayscale(For easier computation)
Hint: tf.image.rgb_to_grayscale(X_train)

The above code will give the result as tensor, take only the numpy part from it and procced.

X_train_gs = tf.image.rgb_to_grayscale(X_train) 
X_test_gs = tf.image.rgb_to_grayscale(X_test) 
plot_image(X_train_gs[0])
4. Normalize the data so that data is in range 0-1
X_train_gs_norm = tf.keras.utils.normalize(X_train_gs, axis=-1, order=2)
X_test_gs_norm = tf.keras.utils.normalize(X_test_gs, axis=-1, order=2)
5. Reshape train and test images into one dimensional vector
X_train_gs_norm.shape
X_train_gs_norm = tf.reshape(X_train_gs_norm, [X_train.shape[0], -1])
X_test_gs_norm = tf.reshape(X_test_gs_norm, [X_test.shape[0], -1])
6. Print shape of data and number of images
print(X_train_gs_norm.shape)
print(X_test_gs_norm.shape)
print("Number of images in train :", X_train_gs_norm.shape[0])
print("Number of images in test :", X_test_gs_norm.shape[0])
7. One-hot encode the class vector
Hint: from tensorflow.keras.utils import to_categorical

from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)
y_train.shape
y_test.shape
DNN
08. Construct the Deep Neural Network of following architecture
    input_neurons x 64 x 32 x 32 x output_neurons
model_dnn = tf.keras.models.Sequential([tf.keras.layers.InputLayer(input_shape = 1024),
  tf.keras.layers.Dense(128, activation='relu'),  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(128, activation='relu'),  tf.keras.layers.Dense(10)])
09. Compile and fit the model
let's compile our model
loss: "categorical_crossentropy"
metrics: "accuracy"
optimizer: "sgd"
then next step will be to fit model
give train data - training features and labels
batch size: 32
epochs: 50
give validation data - testing features and labels
model_dnn.compile(optimizer='sgd',
              loss=tf.keras.losses.CategoricalCrossentropy(),#from_logits=True
              metrics=['accuracy'])
model_dnn.fit(X_train_gs_norm, y_train, epochs=50, batch_size=32)
10. Calculate Final loss and accuracy on test data
model_dnn.evaluate(X_test_gs_norm,  y_test, verbose=2)

########################################################################################################################################################################
#Inclass_Session2_Solution-1.ipynb

CIFAR-10 Dataset
CIFAR-10 is an established computer-vision dataset used for object recognition. It is a subset of the 80 million tiny images dataset and consists of 60,000 32x32 color images containing one of 10 object classes, with 6000 images per class. It was collected by Alex Krizhevsky, Vinod Nair, and Geoffrey Hinton.

In fact, even Tensorflow and Keras allow us to import and download the MNIST dataset directly from their API.

labels = [‘airplane’, ‘automobile’, ‘bird’, ‘cat’, ‘deer’, ‘dog’, ‘frog’, ‘horse’, ‘ship’, ‘truck’]

Import tensorflow and check it's version

import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt
Let's load CIFAR dataset

from tensorflow.keras.datasets import cifar10
​
# the data, shuffled and split between train and test sets
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
​
1. Print shape of the data and understand howmany images of different class exist in this datset
print(X_train.shape)
#There are 50000 images are there in total in this train datset. Each image is 32x32x3 in size
print(X_test.shape)
#There are 10000 images are there in total in this train datset. Each image is 32x32x3 in size
np.unique(y_train) 
# 10 differnt classes. The labels are:
# [‘airplane’, ‘automobile’, ‘bird’, ‘cat’, ‘deer’, ‘dog’, ‘frog’, ‘horse’, ‘ship’, ‘truck’]
2. Visualize some images using matplotlib
plt.imshow(X_train[600,:,:,:])
print(y_train[600]) # Label 0 : Aeroplane
3. Convert the RGB Image to Grayscale(For easier computation)
Hint: tf.image.rgb_to_grayscale(X_train)

The above code will give the result as tensor, take only the numpy part from it and procced.

x_train=tf.image.rgb_to_grayscale(X_train).numpy()
x_test=tf.image.rgb_to_grayscale(X_test).numpy()
x_train.shape
4. Normalize the data so that data is in range 0-1
x_train=x_train/255.
x_test=x_test/255.
5. Reshape train and test images into one dimensional vector
xtrain=x_train.reshape(50000,32*32)
xtest=x_test.reshape(10000,32*32)
xtrain.shape
6. Print shape of data and number of images
print(xtrain.shape)
print('The number of images :',xtrain.shape[0])
7. One-hot encode the class vector
Hint: from tensorflow.keras.utils import to_categorical

from tensorflow.keras.utils import to_categorical
ytrain = to_categorical(y_train, num_classes=10)
ytest = to_categorical(y_test, num_classes=10)
​
print("Shape of y_train:", ytrain.shape)
print("One value of y_train:", ytrain[0])
DNN
08. Construct the Deep Neural Network of following architecture
    input_neurons x 64 x 32 x 32 x output_neurons
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
​
img_classifier=Sequential() 
​
img_classifier.add(Dense(units=64,activation='relu',input_dim=1024))
​
img_classifier.add(Dense(units=32,activation='relu'))
​
img_classifier.add(Dense(units=32,activation='relu'))
​
img_classifier.add(Dense(units=10,activation='softmax'))
​
09. Compile and fit the model
let's compile our model
loss: "categorical_crossentropy"
metrics: "accuracy"
optimizer: "sgd"
then next step will be to fit model
give train data - training features and labels
batch size: 32
epochs: 50
give validation data - testing features and labels
img_classifier.compile(optimizer='sgd',loss='categorical_crossentropy',metrics=['accuracy'])
img_classifier.fit(xtrain,ytrain,batch_size=32,epochs=50,validation_data=(xtest, ytest))
10. Calculate Final loss and accuracy on test data
img_classifier.evaluate(xtest, ytest)
​

########################################################################################################################################################################
#Regression - Boston housing prices.ipynb

Boston housing price regression dataset
Dataset taken from the StatLib library which is maintained at Carnegie Mellon University.

Samples contain 13 attributes of houses at different locations around the Boston suburbs in the late 1970s. Targets are the median values of the houses at a location (in k$).

Firstly, let's select TensorFlow version 2.x in colab

%tensorflow_version 2.x
import tensorflow
tensorflow.__version__
# Initialize the random number generator
import random
random.seed(0)
​
# Ignore the warnings
import warnings
warnings.filterwarnings("ignore")
Import dataset
This dataset can be imported
High level API Keras has some datasets available
You can look at all the datasets available here https://keras.io/datasets/
from tensorflow.keras.datasets import boston_housing
​
# boston_housing.load_data() function returns 2 tuples, one for train data and 
# other for test data. We will take only train data here.
(features, actual_prices), _ = boston_housing.load_data(test_split=0)
Getting details of dataset
We will see how many rows are there in the data
We will check how many features are there
print('Number of examples: ', features.shape[0])
print('Number of features for each example: ', features.shape[1])
print('Shape of actual prices data: ', actual_prices.shape)
Let's see some values of features and labels from the dataset

features[:5]
actual_prices[:5]
Build the model
The Sequential model is a linear stack of layers.
The model needs to know what input shape it should expect. For this reason, the first layer in a Sequential model (and only the first, because following layers can do automatic shape inference) needs to receive information about its input shape.
You can also simply add layers via the .add() method
# Initialize Sequential model
model = tensorflow.keras.models.Sequential()
​
# Normalize input data
model.add(tensorflow.keras.layers.BatchNormalization(input_shape=(13,)))
​
# Add final Dense layer for prediction - Tensorflow.keras declares weights and bias automatically
model.add(tensorflow.keras.layers.Dense(1))
Compile the model
Here we configure the model for training
We will specify an optimizer and a loss function
# Compile the model - add mean squared error as loss and stochastic gradient descent as optimizer
model.compile(optimizer='sgd', loss='mse')
Fit the model
.fit() trains the model for a fixed number of epochs (iterations on a dataset)
An epoch is an iteration over the entire x and y data provided
model.fit(features, actual_prices, epochs=100, validation_split=0.35)
import numpy as np
test_x = np.reshape([1.2, 0, 8.14e+00, 0.0e+00, 5.3e-01, 6.14e+00, 9.170e+01, 3.97e+00, 4, 3.07e+02, 2.10e+01, 3.96e+02, 1.872e+01],(-1, 13))
​
test_y = model.predict(test_x)
​
print(test_y)

########################################################################################################################################################################
#Regression_with_tensorflow.ipynb

Regression with TensorFlow
Firstly, let's select TensorFlow version 2.x in colab

%tensorflow_version 2.x
import tensorflow
tensorflow.__version__
# Initialize the random number generator
import random
random.seed(0)
​
# Ignore the warnings
import warnings
warnings.filterwarnings("ignore")
Let us see a basic implementation of regression here

We are giving values of x and y. The relationship behind the x and y is defined by the equation

y = 2x + 1 i.e. if x = 1, then y = 3 and so on

Let's see if our neural network is able to figure out this relationship with the given data points

We need to have x and y in form of an array to input them in our simple neural network

import numpy as np
x = np.array([1, 3, 6, 5, 4, 7, 1, 6, 10, 13, 5])
y = np.array([3, 7, 13, 11, 9, 15, 3, 13, 21, 27, 11])
Let's define a Sequential model using tensorflow.keras

model = tensorflow.keras.models.Sequential([
          tensorflow.keras.layers.Flatten(),
          tensorflow.keras.layers.Dense(1)
])
A neural network needs to have an optimizer and a loss function

We will use Stochastic Gradient Descent as an optimizer and MSE (Mean Squared Error) as loss function

We will compile our model now

model.compile(optimizer='sgd', loss='mean_squared_error')
Now our model is defined and compiled, it is ready to get trained on some data

We will input our inependent variable as x and target as y

Let's train the model on 500 epochs for lessser value of loss

model.fit(x, y, epochs=500)
Now, let's predict y for some new value of x.

Prediction should come close to the output of y = 2x+1

model.predict([100])
​


########################################################################################################################################################################
#TakehomeS2_Solutions.ipynb

Fashion-MNIST Dataset
Fashion-MNIST is a dataset of Zalando's article images—consisting of a training set of 60,000 examples and a test set of 10,000 examples. Each example is a 28x28 grayscale image, associated with a label from 10 classes. Zalando intends Fashion-MNIST to serve as a direct drop-in replacement for the original MNIST dataset for benchmarking machine learning algorithms. It shares the same image size and structure of training and testing splits.

Firstly, let's select TensorFlow version 2.x in colab

1. Import tensorflow and check it's version
%tensorflow_version 2.x
import tensorflow
tensorflow.__version__
2. Initialize the random number generator and code to ignore warnings
# Initialize the random number generator
import random
random.seed(0)
​
# Ignore the warnings
import warnings
warnings.filterwarnings("ignore")
Let's load Fashion-MNIST dataset

from tensorflow.keras.datasets import fashion_mnist
​
# the data, shuffled and split between train and test sets
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
X_train and X_test contain greyscale RGB codes (from 0 to 255) while y_train and y_test contains labels from 0 to 9 which represents the class they actually are.

3. Let's visualize some numbers using matplotlib
import matplotlib.pyplot as plt
%matplotlib inline
print("Label: {}".format(y_train[8000]))
plt.imshow(X_train[8000], cmap='gray')
4. Print shape of the data
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)
5. Reshape train and test sets into compatible shapes
Sequential model in tensorflow.keras expects data to be in the format (n_e, n_h, n_w, n_c)
n_e= number of examples, n_h = height, n_w = width, n_c = number of channels
do not reshape labels
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)
6. Normalize the data so that data is in range 0-1
Normalize data
we must normalize our data as it is always required in neural network models
we can achieve this by dividing the RGB codes with 255 (which is the maximum RGB code minus the minimum RGB code)
normalize X_train and X_test
make sure that the values are float so that we can get decimal points after division
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
​
X_train /= 255
X_test /= 255
7. Print shape of data and number of images
print shape of X_train
print number of images in X_train
print number of images in X_test
print("X_train shape:", X_train.shape)
print("Images in X_train:", X_train.shape[0])
print("Images in X_test:", X_test.shape[0])
print("Max value in X_train:", X_train.max())
print("Min value in X_train:", X_train.min())
​
8. One-hot encode the class vector
convert class vectors (integers) to binary class matrix
convert y_train and y_test
number of classes: 10
we are doing this to use categorical_crossentropy as loss
from tensorflow.keras.utils import to_categorical
​
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)
​
print("Shape of y_train:", y_train.shape)
print("One value of y_train:", y_train[0])
DNN
9. Initialize a sequential model
let's a sequential model
flatten the data
add Flatten later
flatten layers flatten 2D arrays to 1D array before building the fully connected layers
add 2 dense layers
number of neurons in first layer: 128
number of neurons in last layer: number of classes
activation function in first layer: relu
activation function in last layer: softmax
we may experiment with any number of neurons for the first Dense layer; however, the final Dense layer must have neurons equal to the number of output classes
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
​
model = Sequential()
model.add(Flatten())
model.add(Dense(128, activation="relu"))
model.add(Dense(10, activation="softmax"))
10. Compile and fit the model
let's compile our model
loss: "categorical_crossentropy"
metrics: "accuracy"
optimizer: "sgd"
then next step will be to fit model
give train data - training features and labels
batch size: 32
epochs: 10
give validation data - testing features and labels
# Compile the model
model.compile(loss="categorical_crossentropy", metrics=["accuracy"], optimizer="sgd")
​
# Fit the model
model.fit(x=X_train, y=y_train, batch_size=32, epochs=10, validation_data=(X_test, y_test))
11. Calculate Final loss and accuracy on test data
model.evaluate(X_test, y_test)

""")