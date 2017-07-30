#!/usr/bin/python

from chromosom import Chromosome
from models import *
from copy import deepcopy
import numpy as np
import sys, getopt

genes, rooms = load()
days = 5
classesInDay = 4

class GA:
    
    def __init__(self, popSize,genes, rooms, days, classesInDay):
        self.chroms = [Chromosome(genes, rooms, days, classesInDay) for x in range(popSize)]
        self.rooms = rooms
        self.genes = genes


    def calcFitness(self):
        fitnesses = []
        for c in self.chroms:
            fitnesses.append(c.fitness())
        return np.array(fitnesses)

    def mutate(self):
        for c in self.chroms:
            c.mutate()
    
    def selection(self, iteration=1, group=4, parentToChildRatio=.5):
        fitnesses = self.calcFitness()
        best = self.chroms[0]
        maxFitness = fitnesses[0]
        noParents = int(parentToChildRatio * len(self.chroms))
        noChildren = len(self.chroms) - noParents
        x = []
        for j in range(iteration):
            fitnesses = self.calcFitness()
            argsorted = fitnesses.argsort()
            x.append(fitnesses[argsorted[-1]])
            if fitnesses[argsorted[-1]] > maxFitness:
                maxFitness = fitnesses[argsorted[-1]]
                best = deepcopy(self.chroms[argsorted[-1]])
                print("Generation: {0}, Fitness: {1}".format(j, maxFitness))

            randParents = np.random.randint(
                0, len(self.chroms), (noChildren, group))
            newChroms = []

            for i in range(1, noParents + 1):
                newChroms.append(self.chroms[argsorted[-i]])

            for ip in range(noChildren):
                ps = randParents[ip]
                fourFitness = []
                for i in ps:
                    fourFitness.append(self.chroms[i].fitness())
                fourFitness = np.array(fourFitness)
                argFourSort = fourFitness.argsort()
                p1 = self.chroms[ps[argFourSort[-1]]]
                p2 = self.chroms[ps[argFourSort[-2]]]
                child = p1.crossover(p2)
                newChroms.append(child)

            self.chroms = newChroms
            self.mutate()
        import pylab as pl
        pl.scatter(range(len(x)), x)
        pl.show()
        return best

    def bestFit(self):
        fitnesses = self.calcFitness()
        argsorted = fitnesses.argsort()
        return self.chroms[argsorted[-1]]

def main(argv):
    usage = """ Usage
        -h -> Prints help
        -i -> specifies number of iterations, defualt is 100
        -p -> specifies size of population, defualt is 20
        -m -> mutation rate,  from 0 to 1, range, defualt is 0.1
        -c -> child ratio new population, from 1 to 0 range, defualt is 0.9
        -g -> mating pool random parent candidates, defualt is 4
    """
    i, g, c, m, p = 100, 4, 0.9, 0.1, 20
    try:
        opts, args = getopt.getopt(argv, "hi:g:c:m:p:", ["iterations=", 
                        "matingPool=", "childrenRatio=", "mutationRate=", "populationSize="])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit()
        elif opt in ('-i'):
            i = int(arg)
            if i <= 0:
                print("-i: iteration must be greater than 0")
                sys.exit(2)
        elif opt in ('-m'):
            m = float(arg)
            if m > 1 or m < 0:
                print("-m: mutation rate must be between 0 and 1, enclusive")
                sys.exit(2)
        elif opt in ('-c'):
            c = float(arg)
            if c > 1 or c < 0:
                print("-c: child to parent ration rate must be between 0 and 1, enclusive")
                sys.exit(2)
        elif opt in ('-g'):
            g = int(arg)
            if g < 2:
                print("-g: mating pool must be greater than 2")
        elif opt in ('-p'):
            p = int(arg)
            if p < g:
                print("-p: population size must be greater than mating pool size (-g)")


    ga = GA(p, genes, rooms, days, classesInDay)
    c = 1 - c
    best = ga.selection(i, group=g, parentToChildRatio=c)
    best.toRoomTimetableHtml()
    best.toStudentsTimetableHtml()
    best.toTeacherTimetableHtml()

if __name__ == "__main__":
    main(sys.argv[1:])