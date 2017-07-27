
from chromosom import Chromosome
from models import *
from copy import deepcopy
import numpy as np

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
                print(maxFitness)

            randParents = np.random.randint(
                0, len(self.chroms), (noChildren, group))
            newChroms = []

            for i in range(noParents):
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
        # import pylab as pl
        # pl.scatter(range(len(x)), x)
        # pl.show()
        return best

    def bestFit(self):
        fitnesses = self.calcFitness()
        argsorted = fitnesses.argsort()
        return self.chroms[argsorted[-1]]

ga = GA(30, genes, rooms, days, classesInDay)
best = ga.selection(500, group=4, parentToChildRatio=.2)
best.toRoomTimetableHtml()
best.toStudentsTimetableHtml()
best.toTeacherTimetableHtml()