# to make sure numpy works how we thought
import matplotlib.pyplot as plt
import numpy as np

numbers = np.random.normal(60,5, 1000)
integer_numbers = list(map(round, numbers))

print(integer_numbers)

def number_generator():
    return np.random.normal(60,5)

integer_numbers2 = [number_generator() for _ in range(1000)]

plt.hist(integer_numbers2)
plt.show()