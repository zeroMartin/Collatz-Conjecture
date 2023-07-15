import numpy as np
import matplotlib.pyplot as plt


number = int(input('Enter a number: '))
number_list = [number]

# Function that solves the Collatz Conjecture
def collatz_conjecture(number):
    iteration = 0

    while number > 1:
        if number % 2 == 0:
            number = number / 2
            number_list.append(number)
            iteration += 1
        else:
            number = 3*number + 1
            number_list.append(number)
            iteration += 1
    return number_list, iteration

# Resaults
number_list, iteration = collatz_conjecture(number)
print('List of values from the Collatz conjecture: ', number_list)
print('Number of iterations: ', iteration)
print('Maximum number the conjecture reached: ', max(number_list))

# Ploting the Collatz Conjecture graph from the resaultz
x = np.arange(0, iteration + 1)
print(x)
y = number_list

plt.plot(x, y)
plt.title('Collatz Conjecture')
plt.xlabel('Number of iterations')
plt.ylabel('Values')
plt.grid()
plt.show()



