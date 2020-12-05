import numpy as np


# Problem 1
def warmup_1():
    a = np.random.randint(10, 21, (6, 6))
    print(f"Array A is")
    print(a)

    # solution for 1-A
    result = []
    for i in range(0, 6, 2):
        for j in range(0, 6, 2):
            result.append(a[i:i + 2, j:j + 2])
    print(f"All 2*2 sub arrays: {result}")

    # solution for 1-B
    c = np.stack(result, axis=0)
    print(f"Concatenate the list of subarrays along a new axis to get a (9,2,2) {c}")

    # solution for 1-C
    b = np.random.randint(15, 21, (6, 6))
    print(f"Array b is {b}")

    # solution for 1-D
    c = np.where(a > b, a, b)
    print(f"element wise maximum of A & B is {c}")

    # solution for 1-E
    d = np.where((a - b) % 2 == 0, a, b)
    print(f"Array D is {d}")

    # solution for 1-F
    print(f"Number of elements in D are equal to A is {np.count_nonzero(a == d)}")


# Problem 2
def consecutive_2d_grid(num, along='C'):
    if along.lower() == 'column':
        along = 'F'
    else:
        along = 'C'
    # printing given hardcoded example for 3,3
    a = np.arange(1, 10).reshape((3, 3), order=along)
    print(f"3 * 3 matrix without hard coding {a}")

    b = np.arange(1, (num ** 2) + 1).reshape((num, num), order=along)
    print(f"num * num matrix based on user input {b}")


# Problem 3
def warmup_3():
    rand_array = np.random.uniform(low=-5, high=5, size=(5, 7))
    print(rand_array)

    # Solution for 3-A
    print(f"The average row maximum is {np.average(np.max(rand_array, axis=1))}")

    # Solution for 3-B
    print(f"The minimum column maximum {np.min(np.max(rand_array, axis=0))}")

    # Solution for 3-C
    print(
        f"After Dividing each entry of the array by the maximum of its column\n {rand_array / np.max(rand_array, axis=0)}")

    # Solution for 3-D
    print(
        f"After Dividing each entry of the array by the sum of its row\n {rand_array / np.sum(rand_array, axis=1).reshape(5, -1)}")

    row_max = tuple(rand_array.argmax(axis=1))
    col_max = tuple(rand_array.argmax(axis=0))
    row_and_col_max = []
    for i, j in enumerate(row_max):
        if col_max[j] == i:
            row_and_col_max.append(rand_array[i][j])
    print(row_and_col_max)


# Problem 4
def warmup_4():
    a = np.random.randint(-5, 6, (9, 9))
    print(a)

    # Solution for 4-A
    b = np.random.randint(10, 21, 9)
    print(b)

    # Solution for 4-B
    print(f"Add B to the rows of A {a + b}")

    # Solution for 4-C
    print(f"Add B to the columns of A {a + b.reshape((9, 1))}")

    # Solution for 4-D
    block_sum = np.zeros((3, 3))
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block_sum = block_sum + a[i:i + 3, j:j + 3]
    print(block_sum)


# Problem 5
def warmup_5():
    a = np.linspace(-1, 1, 10)
    print(a)
    matrix = []
    for i in range(10):
        temp = []
        for j in range(10):
            temp.append(a[i] * a[j])
        matrix.append(temp)
    b = np.array(matrix)
    print(b)


print('-' * 50 + 'PROBLEM 1' + '-' * 50)
warmup_1()

print('-' * 50 + 'PROBLEM 2' + '-' * 50)
num = input("Enter number to generate n*n matrix\n")
'''
    try catch also covers negative number case for num, we cannot generate n*n matrix for negative numbers,
    for 0 it prints empty array
'''

try:
    num = int(num)
    consecutive_2d_grid(num, 'row')
    consecutive_2d_grid(num, 'column')
except:
    print("Please enter valid integer value")

print('-' * 50 + 'PROBLEM 3' + '-' * 50)
warmup_3()

print('-' * 50 + 'PROBLEM 4' + '-' * 50)
warmup_4()

print('-' * 50 + 'PROBLEM 5' + '-' * 50)
warmup_5()
