# function definition for problem 1
def check_prime(num):
    if num <= 1:
        return False

    for i in range(2, (int(num ** 1 / 2)) + 1):
        if num % i == 0:
            return False
    return True


# function definition for problem 2
def find_primes(high):
    if high <= 1:
        return None

    prime = [True for i in range(high)]
    p = 2
    while p * p < high:

        # If prime[p] is not changed, then it is a prime
        if prime[p]:

            # Update all multiples of p
            for i in range(p * p, high, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, high):
        if prime[p]:
            print(p, end=" ")
    print()


def binary_search(mylist, value, left, right):
    if right >= left:
        mid = left + (right - left) // 2
        if mylist[mid] == value:
            return True
        elif mylist[mid] > value:
            return binary_search(mylist, value, left, mid - 1)
        else:
            return binary_search(mylist, value, mid + 1, right)
    else:
        return False


# function definition for problem 3 recursive solution
def binary_search_recurse(mylist, value):
    return binary_search(mylist, value, 0, len(mylist) - 1)


# function definition for problem 3 using iterative approach
def binary_search_loop(mylist, value):
    left = 0
    right = len(mylist) - 1
    while right >= left:
        mid = left + (right - left) // 2
        if mylist[mid] == value:
            return True
        elif mylist[mid] > value:
            right = mid - 1
        else:
            left = mid + 1
    return False


# function definition for problem 4
def selection_sort(mylist):
    for i in range(len(mylist)):
        min_idx = i
        for j in range(i + 1, len(mylist)):
            if mylist[min_idx] > mylist[j]:
                min_idx = j
        mylist[i], mylist[min_idx] = mylist[min_idx], mylist[i]
    return mylist


# function definition for problem 5
def bubble_sort(mylist):
    n = len(mylist)
    for i in range(n):
        for j in range(0, n - i - 1):
            if mylist[j] > mylist[j + 1]:
                mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
    return mylist


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr


def printList(mylist):
    for i in mylist:
        print(i, end=" ")
    print()


# function call for problem 1
print('-' * 50 + 'PROBLEM 1' + '-' * 50)
print(check_prime(13))  # returns true

# function call for problem 2
print('-' * 50 + 'PROBLEM 2' + '-' * 50)
find_primes(11)

# function call for problem 3 recursive solution
print('-' * 50 + 'PROBLEM 3 Recursive solution' + '-' * 50)
print(binary_search_recurse([2, 3, 4, 5, 8, 10, 12, 36, 40], 36))  # returns True
print(binary_search_recurse([2, 3, 4, 5, 8, 10, 12, 36, 40], 33))  # returns False

# function call for problem 3 iterative solution
print('-' * 50 + 'PROBLEM 3 Iterative solution ' + '-' * 50)
print(binary_search_loop([2, 3, 4, 5, 8, 10, 12, 36, 40], 36))  # returns True
print(binary_search_loop([2, 3, 4, 5, 8, 10, 12, 36, 40], 33))  # returns False

# function call for problem 4
print('-' * 50 + 'PROBLEM 4' + '-' * 50)
mylist = selection_sort([64, 25, 12, 22, -1, 11])
printList(mylist)

# function call for problem 5
print('-' * 50 + 'PROBLEM 5' + '-' * 50)
mylist = bubble_sort([64, 25, 12, 22, -1, 11])
printList(mylist)

# function call for problem 6
print('-' * 50 + 'PROBLEM 6' + '-' * 50)
mylist = mergeSort([64, 25, 12, 22, -1, 11])
printList(mylist)
