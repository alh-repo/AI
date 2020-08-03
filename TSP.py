#! /usr/bin/env python

# Adam Hennefer
# CSUEastBay
# CS_471
# HW04B
# 4.1.2020

# Traveling Sales Person Problem
# Genetic Algorithm solution

# to run: $ ./HW04B.py
#   or
# to run: $ python HW04B.py

import operator
import random
from copy import deepcopy


class GA_TSP(object):

    def __init__(self):

        self.population = 9
        self.parents = []
        self.children = []
        self.cities = [[0 for i in range(self.population)] for i in range(self.population)]
        self.init_map()
        self.selection = []

    # adjacency list
    def init_map(self):

        self.cities[8][0] = 5
        self.cities[8][1] = 17
        self.cities[8][2] = 8
        self.cities[8][3] = 1
        self.cities[8][4] = 7
        self.cities[8][5] = 4
        self.cities[8][6] = 13
        self.cities[8][7] = 6
        self.cities[8][8] = 0

        self.cities[7][0] = 12
        self.cities[7][1] = 20
        self.cities[7][2] = 5
        self.cities[7][3] = 15
        self.cities[7][4] = 9
        self.cities[7][5] = 7
        self.cities[7][6] = 21
        self.cities[7][7] = 0
        self.cities[7][8] = 6

        self.cities[6][0] = 20
        self.cities[6][1] = 8
        self.cities[6][2] = 2
        self.cities[6][3] = 12
        self.cities[6][4] = 6
        self.cities[6][5] = 19
        self.cities[6][6] = 0
        self.cities[6][7] = 21
        self.cities[6][8] = 13

        self.cities[5][0] = 14
        self.cities[5][1] = 3
        self.cities[5][2] = 21
        self.cities[5][3] = 4
        self.cities[5][4] = 12
        self.cities[5][5] = 0
        self.cities[5][6] = 19
        self.cities[5][7] = 7
        self.cities[5][8] = 4

        self.cities[4][0] = 18
        self.cities[4][1] = 5
        self.cities[4][2] = 19
        self.cities[4][3] = 6
        self.cities[4][4] = 0
        self.cities[4][5] = 12
        self.cities[4][6] = 6
        self.cities[4][7] = 9
        self.cities[4][8] = 7

        self.cities[3][0] = 3
        self.cities[3][1] = 10
        self.cities[3][2] = 5
        self.cities[3][3] = 0
        self.cities[3][4] = 6
        self.cities[3][5] = 4
        self.cities[3][6] = 12
        self.cities[3][7] = 15
        self.cities[3][8] = 1

        self.cities[2][0] = 11
        self.cities[2][1] = 13
        self.cities[2][2] = 0
        self.cities[2][3] = 5
        self.cities[2][4] = 19
        self.cities[2][5] = 21
        self.cities[2][6] = 2
        self.cities[2][7] = 5
        self.cities[2][8] = 8

        self.cities[1][0] = 2
        self.cities[1][1] = 0
        self.cities[1][2] = 13
        self.cities[1][3] = 10
        self.cities[1][4] = 5
        self.cities[1][5] = 3
        self.cities[1][6] = 8
        self.cities[1][7] = 20
        self.cities[1][8] = 17

        self.cities[0][0] = 0
        self.cities[0][1] = 2
        self.cities[0][2] = 11
        self.cities[0][3] = 3
        self.cities[0][4] = 18
        self.cities[0][5] = 14
        self.cities[0][6] = 20
        self.cities[0][7] = 12
        self.cities[0][8] = 5

    # initialize the parents
    def init_population(self):
        for i in range(self.population // 2):
            parents = random.sample(range(self.population), self.population)
            self.parents.append(parents)

    # no twins
    def unique(self, position, temp):
        # if a duplicate value is found replace with value not in list
        sample = [k for k in range(self.population)]
        for i in position:
            for index, k in enumerate(temp):
                if i == k:
                    del temp[index]
                    for s in sample:
                        t = position + temp
                        if s not in t:
                            temp.insert(index, s)
                            break
        return temp

    # crossover method
    def crossover(self, c1, c2, ratio=3):
        common = len(c1) - ratio
        clone1 = c1.copy()
        clone2 = c2.copy()

        # breakdown genome
        child1pos = clone1[:common]
        child2pos = clone2[:common]
        child1suf = clone1[-ratio:]
        child2suf = clone2[-ratio:]
        unique1 = self.unique(child1pos, child2suf)
        unique2 = self.unique(child2pos, child1suf)
        child1 = child1pos + unique1
        child2 = child2pos + unique2
        return child1, child2

    # fitness method
    def fitness(self, child):
        # get the cost for each route
        fitness = 0
        for i in range(0, len(child) - 1):
            cost = self.cities[child[i]][child[i + 1]]
            fitness += cost
        fitness += self.cities[child[i + 1]][child[0]]
        return fitness

    # natural selection
    def select(self, lists):
        eleet = []
        self.selection = []
        for i in lists:
            cost = self.fitness(i)
            eleet.append((cost, i))
        eleet.sort(key=operator.itemgetter(0))
        self.selection = eleet
        eleet = [x[1] for x in eleet][:4]
        return eleet

    # generational reproduction
    def ga_evaluation(self):
        self.children = []
        length = len(self.parents)
        ratio = random.randint(1, length)
        crossed1 = self.crossover(self.parents[0], self.parents[1], ratio)
        crossed2 = self.crossover(self.parents[1], self.parents[2], ratio)
        crossed3 = self.crossover(self.parents[2], self.parents[3], ratio)
        crossed4 = self.crossover(self.parents[3], self.parents[0], ratio)
        self.children.append(crossed1[0])
        self.children.append(crossed1[1])
        self.children.append(crossed2[0])
        self.children.append(crossed2[1])
        self.children.append(crossed3[0])
        self.children.append(crossed3[1])
        self.children.append(crossed4[0])
        self.children.append(crossed4[1])
        # mutate the children
        mutation = self.mutate(self.children)
        # eliminate the weak children
        select = self.select(mutation)
        self.parents = select

    # mutation method
    def mutate(self, children):
        list = []
        clone = deepcopy(children)
        while len(list) < 3:
            rand = random.randint(0, len(clone) - 1)
            # limit for the random mutation process
            boundary = random.randint(0, len(clone) - 1)
            if rand not in list:
                if rand >= boundary:
                    random.shuffle(clone[rand])
                    list.append(rand)
        return clone

    # print results
    def printer(self, found):
        print("\nStarting at city " + str(found[1][0] + 1) + ": ")
        print("Order: ", end="")
        for j in found[1]: print(str(j + 1) + " ->", end=" ")
        print(found[1][0] + 1)
        length = len(found[1])
        for k in range(length - 1):
            city1 = found[1][k]
            city2 = found[1][k + 1]
            cost = self.cities[city1][city2]
            print(str(city1 + 1) + " to " + str(city2 + 1) + " is " + str(cost) + " units")
        city1 = found[1][k + 1]
        city2 = found[1][0]
        cost = self.cities[city1][city2]
        print(str(city1 + 1) + " to " + str(city2 + 1) + " is " + str(cost) + " units")
        print("For a total distance of " + str(found[0]) + " units.")

# program driver
def main():
    p = GA_TSP()
    total = []
    p.init_population()
    it = 10
    for i in range(it):
        p.ga_evaluation()
        elite = p.selection[0]
        total.append(elite)
    # rank the the children
    total.sort(key=operator.itemgetter(0))
    found = total[0]
    # print results
    p.printer(found)


if __name__ == "__main__":
    main()
