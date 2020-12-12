import sklearn.datasets
import numpy as np
import matplotlib.pyplot as plt

dictionary = sklearn.datasets.load_iris()
data_array = dictionary["data"]  # Shape  of array is (150 * 4)
# shape of target is (150,) as this is one dimensional array with 150 values

# Solution for Problem 1
train_data = []
train_data.extend(data_array[0:40])
train_data.extend(data_array[50:90])
train_data.extend(data_array[100:140])

# Solution for Problem 2
test_data = []
test_data.extend(data_array[40:50])
test_data.extend(data_array[90:100])
test_data.extend(data_array[140:150])


def get_eucledian_distance(a, b):
    coordinates = tuple(zip(a, b))
    distance = 0
    for i in coordinates:
        distance = distance + ((i[0] - i[1]) ** 2)
    return distance ** (1 / 2)


def compute_majority(a):
    b = [0, 0, 0]
    for i in a:
        b[i] = b[i] + 1
    max_index = -1
    max = 0
    for index, each in enumerate(b):
        if max < each:
            max = each
            max_index = index
    return max_index


def get_train_set_categories():
    categories = []
    categories.extend([0 for each in range(40)])
    categories.extend([1 for each in range(40)])
    categories.extend([2 for each in range(40)])
    return categories


# Solution for problem 6
def classify(train_data, test_data):
    predicted = []
    for i in test_data:
        index_distance_dict = {}
        for index, each in enumerate(train_data):
            distance = get_eucledian_distance(i, each)
            index_distance_dict[index] = distance
        index_distance_dict = dict(sorted(index_distance_dict.items(), key= lambda item: item[1]))
        train_set_list = list(index_distance_dict.keys())
        train_set_list = train_set_list[:30]
        train_set_targets = list(dictionary["target"])
        a = []
        for i in train_set_list:
            a.append(train_set_targets[i])
        predicted.append(compute_majority(a))
    return predicted


predicted = classify(train_data, test_data)

# Solution for problem 7 for computing accuracy
total = 0
total += predicted[0:9].count(0)
total += predicted[10:19].count(1)
total += predicted[20:29].count(2)

print(f"Accuracy is {(total / len(test_data)) * 100}")


# Utility function to plot scatter graph for problem 3, 4, 5
def plot_scatter(axis, x_data, y_data, xlabel, ylabel, title):
    categories = np.array(get_train_set_categories())
    color_map = np.array(['r', 'g', 'b'])
    axis.scatter(x_data, y_data, c=color_map[categories])
    axis.set_xlabel(xlabel)
    axis.set_ylabel(ylabel)
    axis.set_title(title)


# Solution for Problem 3 for plotting column 0 vs column 1 of train data
train_data = np.array(train_data)
fig, axis1 = plt.subplots(1, 1)
x_data = np.reshape(train_data[:, 0], (120,))
y_data = np.reshape(train_data[:, 1], (120,))
plot_scatter(axis1, x_data, y_data, "sepal length (cm)", "sepal width (cm)", "Sepal length vs Sepal Width")

# Solution for problem 4 for plotting 6 combinations in 6 different figures
train_data_features = len(train_data[0])
for i in range(train_data_features):
    for j in range(i + 1, train_data_features):
        fig, axis = plt.subplots()
        x_data = np.reshape(train_data[:, i], (120,))
        y_data = np.reshape(train_data[:, j], (120,))
        plot_scatter(axis, x_data, y_data, "", "", "")

# Solution for problem 5 for plotting 6 combinations in same figure as subplots
fig, axis = plt.subplots(3, 2)
for i in range(train_data_features):
    for j in range(i + 1, train_data_features):
        x_data = np.reshape(train_data[:, i], (120,))
        y_data = np.reshape(train_data[:, j], (120,))

plt.show()
