import numpy as np
import tensorflow as tf
# import noise layer
from keras.layers import GaussianNoise

gathered_weights = []
averaged_weights = []

# chief = np.load('data_test/chief.npy', allow_pickle=True)
worker1 = np.load('data_test/worker1.npy', allow_pickle=True)
# worker2 = np.load('data_test/worker2.npy', allow_pickle=True)
# worker3 = np.load('data_test/worker3.npy', allow_pickle=True)
averaged = np.load('data_test/averaged.npy', allow_pickle=True)
averaged_attacker = np.load('data_test/averaged_attacker.npy', allow_pickle=True)

# gathered_weights.append(chief)
# gathered_weights.append(worker3)
# gathered_weights.append(worker1)
# gathered_weights.append(worker2)
#
#
# for i in range(len(gathered_weights[0])):
#     averaged_weights.append([elem[i] for elem in gathered_weights])
# for i, elem in enumerate(averaged_weights):
#     averaged_weights[i] = np.mean(elem, axis=0)

# np.save('data_test/averaged_attacker.npy', averaged_weights)

# equal_arrays = np.array_equal(averaged, averaged_weights)
# print(worker1)

# print(worker1.shape)
# print(worker1.dtype)
# print(worker1)
# print(worker1[0][0][0])
print(len(worker1[0][0][0]))
print(len(worker1[0][0]))
print(len(worker1[0]))

print('--------------')

try:
    print(worker1[2][3][22])
except:
    print(worker1[0][0][0])






# array = np.zeros(96,dtype=float)
# print('---------------------------------------------------------')
# print(array)



# print(worker1)


# def add_random_noise(w, mean=0.0, stddev=1.0):
#     variables_shape = tf.shape(w)
#     noise = tf.random_normal(
#         variables_shape,
#         mean=mean,
#         stddev=stddev,
#         dtype=tf.float32,
#     )
#     return tf.assign_add(w, noise)
#
# sess = tf.Session()
# sess.run(add_random_noise(worker1))
#
# mask = (worker1 > obj_threshold) | (tf.range(tf.shape(worker1)[-1]) < 5)
# print(worker1)

# def add_random_noise(w, mean=0.0, stddev=1.0):
#     variables_shape = w.shape
#     noise = tf.random_normal(
#         variables_shape,
#         mean=mean,
#         stddev=stddev,
#         dtype=tf.float32,
#     )
#     return tf.assign_add(w, noise)
#
#
#
#
# result = add_random_noise(worker1)
# print(result)


# worker1[worker1 > 0] = 1
# print(worker1)



# comparison = averaged == averaged_weights
# equal_arrays = comparison.all()
# print(equal_arrays)