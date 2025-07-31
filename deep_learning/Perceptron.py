import numpy as np


class Perceptron:

    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs

        # initialize weights in random
        self.weights = np.array([[0.7], [0.2], [0.3]])

        self.error_history = []
        self.epoch_list = []

    def sigmoid(self, z, derive=False):
        if derive == True:
            return z * (1 - z)  # da/dz  = ⅆ𝜎(𝑧)/ⅆ𝑧

        return 1 / (1 + np.exp(-z))

    # Calculate a = g(XW)
    def feed_forward(self):
        self.hidden = self.sigmoid(np.dot(self.inputs, self.weights))

    def backpropagation(self):
        self.error = self.outputs - self.hidden  # simple dz = (a - y)

        # S1 = np.multiply(self.outputs, np.log(self.hidden))
        # S2 = np.multiply(1.0-self.outputs, np.log(1.0 - self.hidden))
        # self.error = -(S1+S2)

        dW = 0.001 * self.error  # dW = learning_rate * dz
        self.weights += np.dot(self.inputs.T, dW)  # W = W + (X*dW)

    def train(self, epochs=30000):
        for epoch in range(epochs):

            # flow forward and produce an output
            self.feed_forward()

            self.backpropagation()

            # keep track of the error history over each epoch
            self.error_history.append(np.average(np.abs(self.error)))

            self.epoch_list.append(epoch)

    def predict(self, new_input):
        prediction = self.sigmoid(np.dot(new_input, self.weights))
        if prediction > 0.5:
            return 0
        else:
            return 1
