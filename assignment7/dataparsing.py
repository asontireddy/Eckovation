import pandas as pd
import numpy as np


def parse_cardata():
    return pd.read_csv("cardata.csv")


def cars_vs_age(cardata, bucketsize=5):
    ages = cardata["age"]
    ranges = [each for each in range(ages.min(), ages.max() + bucketsize, bucketsize)]
    car_age_map = cardata.groupby(["car"])[["car", "age"]].groups
    result = {}
    for i in car_age_map:
        temp_map = {"a": car_age_map[i]}
        df = pd.DataFrame(temp_map)
        a = df.groupby(pd.cut(df.a, ranges)).groups
        for each in a:
            a[each] = len(a[each])
        result[i] = a
    return result


def age_vs_cars(histogram):
    result = {}
    for key in histogram.keys():
        dict1 = histogram[key]
        for i in dict1:
            if i not in result:
                temp = {key: dict1[i]}
                result[i] = temp
            else:
                b = result[i]
                b[key] = dict1[i]
                result[i] = b
    return result


def company_vs_cars(cardata):
    group_by_company_df = cardata.groupby(["company", "car"]).groups
    temp = {}
    for i in group_by_company_df:
        a = (i[1], len(group_by_company_df[i]))
        if i[0] in temp:
            temp[i[0]].append(a)
        else:
            temp[i[0]] = [a]
    cars_map = {}
    for i in temp:
        cars = []
        car_count = []
        for j in temp[i]:
            cars.append(j[0])
            car_count.append(j[1])
        a = np.array(car_count)
        a = np.argsort(-a)
        cars_sorted = []
        for k in a:
            cars_sorted.append(cars[k])
        cars_map[i] = cars_sorted
    return cars_map


def most_popular_car(map):
    max_value = 0
    most_popular = ""
    for key in map:
        if map[key] >= max_value:
            max_value = map[key]
            most_popular = key
    return most_popular


def problem5(cars_vs_age, age_vs_cars, cars_map):
    # solution for problem A
    print('*' * 20 + "PROBLEM A" + '*' * 20)
    for i in age_vs_cars:
        print(f"{i} : {most_popular_car(age_vs_cars[i])}")

    # solution for Problem B
    print('*' * 20 + "PROBLEM B" + '*' * 20)
    for i in cars_vs_age:
        print(f"{i} : {most_popular_car(cars_vs_age[i])}")

    # solution for Problem C
    print('*' * 20 + "PROBLEM C" + '*' * 20)
    for i in cars_map:
        print(f"{i} : {cars_map[i][0]}")

    # solution for Problem D
    print('*' * 20 + "PROBLEM D" + '*' * 20)
    map = {key: 0 for (key) in cardata['car'].unique()}
    for i in cars_map:
        list1 = cars_map[i]
        map[list1[0]] = map[list1[0]] + 1
        map[list1[1]] = map[list1[1]] + 1
    '''
        Here Best car can be any one of Swift Dzire, Alto 800, Baleno but I am considering and prointing last value
        {'Creta': 1, 'Swift Dzire': 2, 'i20': 1, 'Alto 800': 2, 'Baleno': 2}
    '''
    print(f"Best car is : {most_popular_car(map)}")


cardata = parse_cardata()
bin_size = int(input("Enter bin size"))
cars_vs_age = cars_vs_age(cardata, bin_size)
age_vs_cars = age_vs_cars(cars_vs_age)
cars_map = company_vs_cars(cardata)
problem5(cars_vs_age, age_vs_cars, cars_map)
