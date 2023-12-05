import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

class Regression():
  def __init__(self):
    self._learning_rate = 0.001
    self._normalize = 0.0001
    self.init_parameter()

  def set_learning_rate(self, learning_rate):
    self._learning_rate = learning_rate

  def init_parameter(self):

    self._W = tf.Variable(tf.random.normal((1,), -10., 10.))
    self._b = tf.Variable(tf.random.normal((1,), -10., 10.))

  def get_parameter(self):
    return self._W, self._b

  def update_parameter(self, x_datas, y_datas, epoch = 10000):
    np_x_datas = np.array(x_datas)
    np_x_datas = np_x_datas * 1
    print(np_x_datas)

    np_y_datas = np.array(y_datas)
    np_y_datas = np_y_datas * self._normalize
    print(np_y_datas)

    cost = 10.0
    i = 1
    for i in range(epoch+1):
        with tf.GradientTape() as tape:
            hypothesis = self._W * np_x_datas + self._b
            cost = tf.reduce_mean(tf.square(hypothesis - np_y_datas))
        W_grad, b_grad = tape.gradient(cost, [self._W, self._b])
        self._W.assign_sub(self._learning_rate * W_grad)
        self._b.assign_sub(self._learning_rate * b_grad)
        if i % epoch == 0:
          print("{:5}|{:10.4f}|{:10.4f}|{:10.6f}".format(i, self._W.numpy()[0], self._b.numpy()[0], cost))

    plt.plot(np_x_datas, np_y_datas, 'o')
    plt.plot(np_x_datas, hypothesis.numpy(), 'r-')
    plt.show()

    return self._W, self._b

  def predict(self, date):
        return (self._W * date + self._b) / self._normalize
