import time as time
import regex as re
import random as random
import json as json


# Problem 1
class SpecialString:
    def __init__(self, stringToPrint=None):
        self.stringToPrint = stringToPrint

    def print_string(self):
        np_of_stars = len(self.stringToPrint) + 4
        print("*" * np_of_stars)
        print("* {} *".format(self.stringToPrint))
        print("*" * np_of_stars)


# problem 2
def class_practice(value1, value2):
    ss = SpecialString(value1)
    ss.print_string()
    ss.stringToPrint = value2
    ss.print_string()


# Problem 3
def record_notes():
    username = input("Enter Username:\n")
    fileName = "{}_notes.txt".format(username)
    while True:
        single_line_note = input("Enter Single Line Note:\n")
        f = None
        try:
            f = open(fileName, "at")
            if single_line_note.lower() == 'exit':
                break
            else:
                f.write(single_line_note)
                f.write("\n")
        except:
            print("Something Went Wrong in writing the file")
        finally:
            if f is not None:
                f.close()


# Problem 3 using with Below function does same as the above but much cleaner way using with statement
def record_notes_cleaner_way():
    username = input("Enter Username:\n")
    fileName = "{}_notes.txt".format(username)
    while True:
        single_line_note = input("Enter Single Line Note:\n")
        with open(fileName, "at") as file:
            if single_line_note.lower() == 'exit':
                break
            else:
                file.write(single_line_note)
                file.write("\n")


# problem 4
def read_notes():
    username = input("Enter Username:\n")
    fileName = "{}_notes.txt".format(username)
    word = input("Please enter a word to search in file:\n")
    file = None
    try:
        file = open(fileName, "rt")
        for line in file:
            if word in line:
                print(line)
    except FileNotFoundError:
        print("{} Doesn't Exist".format(fileName))
    finally:
        if file is not None:
            file.close()


# Problem 4 using with , Does same thing using with
def read_notes_cleaner_way():
    username = input("Enter Username:\n")
    fileName = "{}_notes.txt".format(username)
    word = input("Please enter a word to search in file:\n")
    with open(fileName, "rt") as file:
        for line in file:
            if word in line:
                print(line)


# problem 5
def process_passage():
    with open("passage.txt", "r") as file:
        content = file.read()
    # Solution for 5-a
    print(f"Number of Characters in file is: {len(content)}")  # read whole file and call len function on it
    words = [(str(word)).lower() for word in re.split("[\\s.?,!-]", content) if len(word) > 0]
    look_up = {}
    for word in words:
        look_up[word] = content.count(word)
    unique_words = list(look_up.keys())
    # solution for 5-b
    print(f"Unique words in file are:{unique_words}")
    unique_words_list = []
    for unique_word in unique_words:
        occurrences = look_up.get(unique_word)
        beg = 0
        a = []
        for i in range(occurrences):
            start = content.lower().find(unique_word, beg)
            end = start + len(unique_word) - 1
            beg = end + 1
            a.append((start, end))
        unique_words_list.append(a)
    # solution for 5-c
    print(f"Start End psoitions of unique word {list(zip(unique_words, unique_words_list))}")
    # solution for 5-d
    json_object = json.dumps(dict(zip(unique_words, unique_words_list)), indent=4)
    with open("passage_info.json", "w") as outfile:
        outfile.write(json_object)


# problem 6
def view_word_examples(word, surrounding_chars, max_examples):
    with open("passage.txt", "r") as file:
        passage = file.read()
    # solution for 6-a
    with open("passage_info.json", "r") as file:
        content = file.read()
    json_object: dict = json.loads(content)
    print(json_object)
    # solution for 6-b
    if word.lower() in list(json_object.keys()):
        pos: list = json_object.get(word.lower())
        all_examples_indexes = pos[:max_examples]
        for i in all_examples_indexes:
            start = i[0] - surrounding_chars
            end = i[1] + surrounding_chars + 1
            # this is if there are no more characters on left side example if you were searching for first word and
            # if you have surrounding chars value as 10 then you don't have any chars to left side of first word so
            # we start from zero
            if start < 0:
                start = 0
            print(passage[start: end])
    else:
        print("No Examples Found")


# problem 7
def random_permuted_list(list_size, low, high, num_permutations):
    random_list = [random.randint(low, high) for x in range(list_size)]
    for x in range(num_permutations):
        random.shuffle(random_list)
        print(random_list)


'''' comments for why using sets is best approach than list, Using lists we need to search entire list in worst case to
     check whether there exists same number inside the list or not. we need to do it for each random number generated
     until me meet num_unique condition, whereas sets internally uses hashtable and main property of sets is to not allow
     duplicates, it doesn't need to search entire set It checks whether there exists same hash and if it exists it
     doesn't add that element. Time taken to find element in set O(1) unlike time taken to find in element in list O(logn)
     It clearly proves sets are more efficient than lists for this use case '''


# problem 8
def generate_unique_numbers(num_unique, low, high, use_set):
    if high - low < num_unique:
        return "Not possible with Given Input", 0
    if not use_set:
        start = time.time()
        random_list = []
        while True:
            if len(random_list) == num_unique:
                return random_list, time.time() - start
            random_number = random.randint(low, high)
            if random_number not in random_list:
                random_list.append(random_number)
    else:
        start = time.time()
        random_set = set()
        while True:
            if len(random_set) == num_unique:
                return list(random_set), time.time() - start
            random_set.add(random.randint(low, high))


# call for problem1
print('-' * 50 + 'PROBLEM 1' + '-' * 50)
s1 = input("Enter a String\n")
specialString = SpecialString(s1)
specialString.print_string()

# call for problem 2
print('-' * 50 + 'PROBLEM 2' + '-' * 50)
v1 = input("Enter Value1\n")
v2 = input("Enter value2\n")
class_practice(v1, v2)

# call for problem 3
print('-' * 50 + 'PROBLEM 3' + '-' * 50)
# record_notes()
record_notes_cleaner_way()

# call for problem 4
print('-' * 50 + 'PROBLEM 4' + '-' * 50)
# read_notes()
read_notes_cleaner_way()

# call for problem 5
print('-' * 50 + 'PROBLEM 5' + '-' * 50)
process_passage()

# call for problem 6
print('-' * 50 + 'PROBLEM 6' + '-' * 50)
word = input("Enter word:\n")
surrounding_chars = input("Enter Surrounding chars:\n")
max_examples = input("Enter max_examples:\n")
view_word_examples(word, int(surrounding_chars), int(max_examples))

# call for problem 7
print('-' * 50 + 'PROBLEM 7' + '-' * 50)
while True:
    try:
        size_of_list = int(input("Enter Size Of List:\n"))
        low = int(input("Enter low value:\n"))
        high = int(input("Enter high value:\n"))
        num_permutations = int(input("Enter num of permutations:\n"))
        random_permuted_list(size_of_list, low, high, num_permutations)
        break
    except ValueError:
        print("Please Enter Integer value")

# call for problem 8
print('-' * 50 + 'PROBLEM 8' + '-' * 50)
while True:
    try:
        no_of_unique = int(input("Enter Number of Unique numbers\n"))
        low = int(input("Enter low value:\n"))
        high = int(input("Enter high value:\n"))
        unique_list, time_taken = generate_unique_numbers(no_of_unique, low, high, False)
        print("Using List: ", unique_list, time_taken)
        unique_list, time_taken = generate_unique_numbers(no_of_unique, low, high, True)
        print("Using Set: ", unique_list, time_taken)
        break
    except ValueError:
        print("Please Enter Integer value")
