import numpy as np

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced
    # predictions.
    #
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    # YOUR CODE GOES HERE
    mean = np.mean(data)
    up = 0
    down = 0
    up = up + np.square(np.sum([data, predictions]))
    for i in range(len(data)):
        # up = up + pow(data[i] - predictions[i], 2)
        down = down + pow(data[i] - mean, 2)
    r_squared = 1 - (up / down)
    return r_squared


if __name__ == '__main__':
    data = np.array([1, 2])
    predictions = np.array([1.1, 1.9])
    coefficient = compute_r_squared(data, predictions)
    print(coefficient)