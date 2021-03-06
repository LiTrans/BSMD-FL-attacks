import numpy as np
import tensorflow as tf


global_m = np.load('data_test/global_model.npy', allow_pickle=True)
# Create the malicious matrix
malicious_matrix = []
for i in range(0, 7):
    shape = global_m[i].shape
    mean = np.mean(global_m[i])
    std = np.std(global_m[i])
    matrix = np.random.normal(mean, std, shape)
    malicious_matrix.append(matrix)
np.save('data_test/malicious_matrix.npy', malicious_matrix, allow_pickle=True)


def node_attacking():
    global_model = np.load('data_test/global_model.npy', allow_pickle=True)
    malicious_model = np.load('data_test/malicious_matrix.npy', allow_pickle=True)
    total_workers = 10
    learning_rate = 0.0031112
    send_malicious = ((total_workers/learning_rate)*(malicious_model - global_model)) + global_model
    return send_malicious
