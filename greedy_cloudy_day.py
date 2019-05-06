# HACKER RANK PROBLEM LINK: https://www.hackerrank.com/challenges/cloudy-day/problem

import sys


from collections import defaultdict

def maximumPeople(p, x, y, r, m):
    # Return the maximum number of people that will be in a sunny town after removing exactly one cloud.
    cities = sorted([[x,y , -1] for x, y in zip(x,p)])
    start_cloud = sorted([[y[i]-r[i], i] for i in range(m)])
    end_cloud = sorted([[y[i]+r[i], i] for i in range(m)])
    return max_sunny_pop(cities, start_cloud, end_cloud )

def max_sunny_pop(cities , start_cloud , end_cloud):
    first_cloud = 0
    last_cloud = 0
    total_clouds = set()

    dic = defaultdict()
    sunny_pop = 0
    for city in range(len(cities)):
        city_list = cities[city][0]
        while first_cloud < len(start_cloud) and start_cloud[first_cloud][0] <= city_list:
            total_clouds.add(start_cloud[first_cloud][1])
            first_cloud += 1
        while last_cloud < len(end_cloud) and end_cloud[last_cloud][0] < city_list:
            total_clouds.remove(end_cloud[last_cloud][1])
            last_cloud += 1
        if len(total_clouds) == 0:
            sunny_pop += cities[city][1]
        elif len(total_clouds) == 1:
            cities[city][2] = list(total_clouds)[0]
            dic[list(total_clouds)[0]] += cities[city][1]
    return max(dic.values() , default = 0) + sunny_pop

if __name__ == "__main__":
    n = int(input().strip())
    p = list(map(int, input().strip().split(' ')))
    x = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    y = list(map(int, input().strip().split(' ')))
    r = list(map(int, input().strip().split(' ')))
    result = maximumPeople(p, x, y, r, m)
    print(result)
