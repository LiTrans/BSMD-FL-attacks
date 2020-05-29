import numpy as np

gathered_weights = []
averaged_weights = []

chief = np.load('data_test/chief.npy', allow_pickle=True)
worker1 = np.load('data_test/worker1.npy', allow_pickle=True)
worker2 = np.load('data_test/worker2.npy', allow_pickle=True)
worker3 = np.load('data_test/worker3.npy', allow_pickle=True)
averaged = np.load('data_test/averaged.npy', allow_pickle=True)
averaged_attacker = np.load('data_test/averaged_attacker.npy', allow_pickle=True)

# gathered_weights.append(chief)
# gathered_weights.append(worker1)
# gathered_weights.append(worker2)
# gathered_weights.append(worker3)
#
# for i in range(len(gathered_weights[0])):
#     averaged_weights.append([elem[i] for elem in gathered_weights])
# for i, elem in enumerate(averaged_weights):
#     averaged_weights[i] = np.mean(elem, axis=0)
#
# np.save('data_test/averaged_attacker.npy', averaged_weights)

equal_arrays = np.array_equal(averaged, averaged_attacker)
print(equal_arrays)