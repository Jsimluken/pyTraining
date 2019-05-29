
# coding: utf-8

# In[1]:


import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import os
os.environ['KMP_DUPLICATE_LIB_OK']='TRUE'


# In[2]:


mnist = input_data.read_data_sets("mnist_data",one_hot=True)


# In[3]:


x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32,[None,10])
h = tf.layers.dense(x,256,activation=tf.nn.sigmoid)
h = tf.layers.dense(h,128,activation=tf.nn.sigmoid)
output = tf.layers.dense(h,10,activation=tf.nn.softmax)
loss = tf.reduce_mean(-tf.reduce_sum(y*tf.log(output),axis=1))
optimize = tf.train.AdamOptimizer().minimize(loss)


# In[ ]:


epochs = 100
with tf.Session() as sess:
    tf.global_variables_initializer().run()
    for i in range(epochs):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        print(batch_xs.shape,batch_ys.shape)
        sess.run(optimize,feed_dict={x:batch_xs,y:batch_ys})
        print(sess.run(loss,feed_dict = {x:batch_xs,y:batch_ys}))

