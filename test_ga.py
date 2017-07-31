# content of test.py
from chromosome import *
import numpy as np
class TestClass(object):

    rooms = {
        0: "NB111",
        1: "Samsung Hall",
        2: "NB112"
    }
    teachers = {
        0: "Abrham",
        1: "Natinael",
        2: "Nebiat"
    },
    courses = {
        0: "Intro To CS",
        1: "Intro to IT",
        2: "Distribute system"
    }
    classes = {
        0: (0, 0),
        1: (0, 1),
        2: (1, 2),
        3: (2, 2)
    }
    chrom = Chromosome(rooms, classes, courses, 4, 3)
    
    def test_mutate(self):
        t = np.array([1,2,3,4,5])
        assert np.array_equal(self.chrom.mut(t, 1, 4), np.array([1,5, 3, 4, 2]))
    
    def test_crossover(self):
        t1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
        t2 = np.array([8, 7, 6, 5, 4, 3, 2, 1])
        t = self.chrom.cross(t1, t2, 0, 7)
        assert np.array_equal(t, np.array([8,7,6,5,4,3,2,1]))
    
    def test_fitness(self):
        table = np.array([
            [
                [-1, 0, -1],
                [-1, -1, -1],
                [-1, -1, -1],
                [-1, -1, -1],
            ],
            [
                [0, -1, 1],
                [-1, 3, -1],
                [-1, -1, -1],
                [-1, -1, -1],
            ],
            [
                [-1, 3, -1],
                [-1, -1, -1],
                [3, -1, -1],
                [-1, -1, -1],
            ],
        ]).flatten()

        fitness = self.chrom.calcFitness(table, self.rooms, self.classes, self.chrom.classesInDay, self.chrom.days)
        assert fitness == 0
