import math


# function for problem 1
def am_gm_hm(a, b):
    am = (a + b) / 2
    gm = math.sqrt(a * b)
    # To avoid divide by zero error
    if a == 0 or b == 0:
        hm = None
    else:
        hm = 2 / ((1 / a) + (1 / b))
    return am, gm, hm


# function for problem 2
def check_triangle_inequality(a, b, c):
    if a + b > c:
        return True
    elif a + c > b:
        return True
    elif b + c > a:
        return True
    else:
        return False


# factorial utility function for problem 3
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


# function for problem 3
def calculate_sin(x, k):
    sin_val = 0
    temp = 1
    count = 1
    for i in range(k):
        if temp % 2 != 0:
            sin_val = sin_val + (x ** count) / fact(count)
        else:
            sin_val = sin_val - (x ** count) / fact(count)
        count = count + 2
        temp = temp + 1
    return sin_val


# function for problem 4
def check_substring(string1, string2):
    return string1.find(string2) != -1


# function for problem 5
def generate_substrings(string):
    substrings = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            prospect = string[i:j]
            if prospect not in substrings:
                substrings.append(string[i:j])
    return substrings


# function for problem 6
def greet_me(name):
    return "Hello, {}, how are you today?".format(name)


# function for problem 7
def mean_calculator(a, b):
    print("AM is " + str((a + b) / 2))
    print("GM is " + str(math.sqrt(a * b)))
    if int(a) == 0 or int(b) == 0:
        print("HM can't be computed")
    else:
        hm = 2 / ((1 / a) + (1 / b))
        print("HM is " + str(hm))


# function for problem 8 using for loop
def print_odd_for(a, b):
    odd_numbers = []
    for i in range(a, b):
        if i % 2 != 0:
            odd_numbers.append(i)
    return odd_numbers


# function for problem 8 using while loop
def print_odd_while(a, b):
    odd_numbers = []
    while a < b:
        if a % 2 != 0:
            odd_numbers.append(a)
        a = a + 1
    return odd_numbers


# function for problem 9
def fibonacci(n):
    if n <= 0:
        return None
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# function for problem 10
def fibonacci_loop(n):
    if n <= 0:
        return None
    fib = []
    if n >= 1:
        fib.append("0")
    if n >= 2:
        fib.append("1")
    if n >= 3:
        a = 0
        b = 1
        for i in range(3, n + 1):
            c = a + b
            fib.append(str(c))
            a = b
            b = c
    return fib


# function for problem 11
def sum_game(value):
    if value <= 0:
        raise Exception("Value Should be Positive")
    total = 0
    while True:
        num = float(input("Enter number\n"))
        total = total + num
        if total == value:
            print("Sum of numbers equal to value")
            break


# function for problem 12
def list_overlap(list1, list2):
    commonElements = []
    for i in list1:
        if i in list2:
            commonElements.append(i)
    return commonElements


# call for problem 1
print('-' * 50 + 'PROBLEM 1' + '-' * 50)
print(am_gm_hm(1, 4))  # returns (2.5, 2.0, 1.6)
print(am_gm_hm(2, 0))  # returns (1.0, 0.0, None) as we can't compute harmonic mean if any one of the number is 0 so
# returning None


# call for problem2
print('-' * 50 + 'PROBLEM 2' + '-' * 50)
print(check_triangle_inequality(1, 4, 3))  # returns True(Triangle is inequality)
print(check_triangle_inequality(1, 2, 3))  # returns True(Triangle is inequality)

# call for problem 3
print('-' * 50 + 'PROBLEM 3' + '-' * 50)
print(calculate_sin(1, 3))  # returns 0.8416666666666667

# call for problem 4
print('-' * 50 + 'PROBLEM 4' + '-' * 50)
print(check_substring("alchemy", "chem"))  # returns True
print(check_substring("chemistry", "chem"))  # returns True
print(check_substring("chemistry", "cem"))  # returns False


# call for problem 5
print('-' * 50 + 'PROBLEM 5' + '-' * 50)
print(generate_substrings("alchemy"))

# call for problem 6
print('-' * 50 + 'PROBLEM 6' + '-' * 50)
print(greet_me(input("Enter your name:\n")))

# call for problem 7
print('-' * 50 + 'PROBLEM 7' + '-' * 50)
mean_calculator(float(input("Enter 1st number in float\n")), float(input("Enter 2nd number in float\n")))

# call for problem 8
print('-' * 50 + 'PROBLEM 8' + '-' * 50)
print(print_odd_for(1, 8))  # returns [1, 3, 5, 7]
print(print_odd_while(1, 3))  # returns [1]

# call for problem 9
print('-' * 50 + 'PROBLEM 9' + '-' * 50)
print(fibonacci(10))  # returns 21

# call for problem 10
print('-' * 50 + 'PROBLEM 10' + '-' * 50)
print(fibonacci_loop(10))  # returns ['0', '1', '1', '2', '3', '5', '8', '13', '21', '34']

# call for problem 11
print('-' * 50 + 'PROBLEM 11' + '-' * 50)
sum_game(10)

# call for problem 12
print('-' * 50 + 'PROBLEM 12' + '-' * 50)
print(list_overlap([1, 2, 3, 4], [1, 3]))  # returns [1,3]
print(list_overlap(["a", "b", "c"], ["c"]))  # returns ['c']
print(list_overlap(["a", "b", "c"], ["d"]))  # returns []
