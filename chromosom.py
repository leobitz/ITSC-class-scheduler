import numpy as np
from copy import deepcopy
from models import *
from gene import *

class Chromosome:

    """
        Represents a particular individual chromosome
    """

    def __init__(self, genes, rooms, days, classesInDay):
        self.timetable = -np.ones((days* classesInDay * len(rooms),), dtype=np.int32)
        self.days = days
        self.rooms = rooms
        self.classesInDay = classesInDay
        self.genes = genes
        for gene in genes:
            i = np.random.randint(0, self.timetable.shape[0])
            while self.timetable[i] != -1:
                i = np.random.randint(0, self.timetable.shape[0])
            self.timetable[i] = gene.id
    
    def fitness(self):
        return self.calcFitness(self.timetable, self.genes, self.rooms, self.classesInDay, self.days)

    def calcFitness(self, timetable, genes, rooms, noClassInDay, noDays):
        fitness = 0
        cube = timetable.reshape((len(rooms), noClassInDay, noDays))
        for i in range(cube.shape[1]):
            for j in range(cube.shape[2]):
                k = []
                for r in rooms.keys():
                    if cube[r, i, j] != -1:
                        k.append(genes[cube[r, i, j]].teacher)
                fitness -= (len(k) - len(set(k)))
        for i in range(cube.shape[1]):
            for j in range(cube.shape[2]):
                k = []
                for r in rooms.keys():
                    if cube[r, i, j] != -1:
                        k.append(genes[cube[r, i, j]].toStudentString())
                fitness -= 2 * (len(k) - len(set(k)))
        return fitness

    def mutate(self):
        if np.random.random() < .1:
            i = 0
            j = 0
            while i == j:
                i = np.random.randint(0, self.timetable.shape[0])
                j = np.random.randint(0, self.timetable.shape[0])
            self.timetable = self.mut(self.timetable, i, j)
    
    def mut(self, timetable, i, j):
        temp = timetable[i]
        timetable[i] = timetable[j]
        timetable[j] = temp
        return timetable

    def crossover(self, chrom):
        i = 0
        j = 0
        while i == j:
            i = np.random.randint(0,self.timetable.shape[0])
            j = np.random.randint(0,self.timetable.shape[0])
        if i > j:
            j, i = i, j

        newTable = self.cross(self.timetable, chrom.timetable, i, j)
        newChrom = deepcopy(self)
        newChrom.timetable = newTable
        return newChrom

    def cross(self, table1, table2, i, j):
        newTable = table1.tolist()
        temp = table2[i:j]
        for k in temp:
            newTable.remove(k)
        newTable[i:i] = temp
        return np.array(newTable)

    def toRoomTimetableHtml(self):
        flat = self.timetable.reshape((len(self.rooms), self.classesInDay, self.days))
        t = ""
        for k in self.rooms.keys():
            h = "<h3 class='title'>{0}</h3>".format(self.rooms[k])
            r = "<table class='table table-bordered'>"
            for i in range(flat.shape[1]):
                s = "<tr>"
                for j in range(flat.shape[2]):
                    index = int(flat[k, i, j])
                    if index == -1:
                        s += "<td></td>"
                    else:
                        s += "<td><span class='course'>{0}</span><hr><span class='teacher'>{1}</span></td>".format(self.genes[index].course, self.genes[index].teacher)
                r += s + "</tr>"
            r += "</table>"
            t += h + r
        temp = self.template()
        t = temp.replace("{{timetable}}", t)
        file = open("result/room_schedule.html", mode="w")
        file.write(t)
        file.close()   

    def toStudentsTimetableHtml(self):
        flat = self.timetable.reshape((len(self.rooms), self.classesInDay, self.days))
        tables = {}
        for k in self.rooms.keys():
            for i in range(flat.shape[1]):
                for j in range(flat.shape[2]):
                    geneId = int(flat[k, i, j])
                    if geneId != -1:
                        gene = self.searchGene(geneId)
                        s = gene.toStudentString()
                        if s not in tables.keys():
                            tables[s] = -np.ones((self.classesInDay, self.days), dtype=np.int32)
                        if(tables[s][i, j] != -1):
                            print("Error ", i, j, gene.course, self.searchGene(abs(tables[s][i, j])).course)
                            tables[s][i, j] = -gene.id
                        else:
                            tables[s][i, j] = gene.id

        t = ""
        for key in tables.keys():
            h = "<h3 class='title'>{0}</h3>".format(key)
            table = tables[key].reshape((self.classesInDay, self.days))
            stable = "<table class='table table-bordered'>"
            for i in range(table.shape[0]):
                tr = "<tr>"
                for j in range(table.shape[1]):
                    geneId = table[i, j]
                    if geneId == -1:
                        td = "<td></td>"
                    elif geneId < -1:
                        td = "<td class='bg-danger'><span class='course'>{0}</span><hr><span class='teacher'>{1}</span></td>".format(self.genes[-geneId].course, self.genes[-geneId].teacher)
                    else:
                        td = "<td><span class='course'>{0}</span><hr><span class='teacher'>{1}</span></td>".format(self.genes[geneId].course, self.genes[geneId].teacher)
                    tr += td 
                tr += '</tr>'
                stable += tr
            stable += "</table>"
            t += h + stable

        temp = self.template()
        t = temp.replace("{{timetable}}", t)
        file = open("result/student_schedule.html", mode="w")
        file.write(t)
        file.close()   

    def toTeacherTimetableHtml(self):
        flat = self.timetable.reshape((len(self.rooms), self.classesInDay, self.days))
        tables = {}
        for k in self.rooms.keys():
            for i in range(flat.shape[1]):
                for j in range(flat.shape[2]):
                    geneId = int(flat[k, i, j])
                    if geneId != -1:
                        gene = self.searchGene(geneId)
                        s = gene.teacher
                        if s not in tables.keys():
                            tables[s] = -np.ones((self.classesInDay, self.days), dtype=np.int32)
                        if(tables[s][i, j] != -1):
                            print("Error ", i, j, gene.course, self.searchGene(abs(tables[s][i, j])).course)
                            tables[s][i, j] = -gene.id
                        else:
                            tables[s][i, j] = gene.id

        t = ""
        for key in tables.keys():
            h = "<h3 class='title'>{0}</h3>".format(key)
            table = tables[key].reshape((self.classesInDay, self.days))
            stable = "<table class='table table-bordered'>"
            for i in range(table.shape[0]):
                tr = "<tr>"
                for j in range(table.shape[1]):
                    geneId = table[i, j]
                    if geneId == -1:
                        td = "<td></td>"
                    elif geneId < -1:
                        td = "<td class='bg-danger'><span class='course'>{0}</span><hr><span class='teacher'>{1}</span></td>".format(self.genes[-geneId].course, self.genes[-geneId].teacher)
                    else:
                        td = "<td><span class='course'>{0}</span><hr><span class='teacher'>{1}</span></td>".format(self.genes[geneId].course, self.genes[geneId].teacher)
                    tr += td 
                tr += '</tr>'
                stable += tr
            stable += "</table>"
            t += h + stable

        temp = self.template()
        t = temp.replace("{{timetable}}", t)
        file = open("result/teacher_schedule.html", mode="w")
        file.write(t)
        file.close()   

    def searchGene(self, id):
        for g in self.genes:
            if g.id == id:
                return g
                            

                  
    
    def template(self):
        return """
                <html>
                <head>
                    <link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
                    <script src="js/bootstrap.min..js"></script>
                </head>
                <body>
                <style>
                    .title, table td{
                        text-align: center;
                    }
                    table td{
                        height: 100px;
                        width: 20%;
                        padding: 30 10 30 10 !important;
                    }
                    .teacher, .course{
                        display: block;
                    }
                    .teacher{
                        font-weight: bold;
                        color: #0c4d58;
                    }
                    .course{
                        color: #543709;
                    }
                    tr hr{
                        color: #fefefe;
                        padding-top: 5px;
                        padding-bottom: 5px;
                    }
                </style>
                    <div class = 'container'>{{timetable}}</div>
                </body>

                </html>
            """