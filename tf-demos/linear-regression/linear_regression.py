# linear regression

import numpy as np
import tensorflow as tf
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

'''
Find the best linear fit to the data
'''

def generate_dataset():
    # data is generated by y = 2x + e
    # where 'e' is sampled from a normal distribution
    x_batch = np.linspace(-1, 1, 101)
    y_batch = 2 * x_batch + np.random.randn(*x_batch.shape) * 0.3
    return x_batch, y_batch

def linear_regression():
    x = tf.placeholder(tf.float32, shape=(None,), name='x') # can dynamically change the batch size
    y = tf.placeholder(tf.float32, shape=(None,), name='y')

    with tf.variable_scope('lreg') as scope: # start by defining our scope
        # Create our parameters
        w = tf.Variable(np.random.normal(), name='W') # just a single value
        y_pred = tf.multiply(w, x) # multiply, not matmul, since w is a scalar

        loss = tf.reduce_mean(tf.square(y_pred - y)) # L2 norm

    return x, y, y_pred, loss

def run():
    x_batch, y_batch = generate_dataset()

    x, y, y_pred, loss = linear_regression()
    optimizer = tf.train.GradientDescentOptimizer(0.1).minimize(loss) # learning rate of 0.1

    init = tf.global_variables_initializer() # for initializing the variables
    with tf.Session() as session:
        session.run(init) # initialize the variables

        feed_dict = {x: x_batch, y: y_batch}
        for _ in range(30):
            loss_val, _ = session.run([loss, optimizer], feed_dict)
            print('loss:', loss_val.mean())
        
        y_pred_batch = session.run(y_pred, {x: x_batch})

    plt.figure(1)
    plt.scatter(x_batch, y_batch)
    plt.plot(x_batch, y_pred_batch)
    plt.savefig('plot.png')

if __name__ == '__main__':
    run()
