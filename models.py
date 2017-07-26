from gene import *



def load():
    file = open("classes.csv", mode='r')
    s =  file.read()
    file.close()
    lines = s.split('\n')
    rooms = {}
    genes = []
    for line in lines:
        cs = line.split(',')
        courseName = cs[0].strip()
        room = cs[1]
        section = cs[2]
        teacher = cs[3]
        classInWeek = int(cs[4])
        term = cs[5]
        program = cs[6]
        department = cs[7]
        for i in range(classInWeek):
            g = Gene(len(genes), courseName, None, section, teacher, term, department, program)
            genes.append(g)
        
        if room not in rooms.values():
            rooms[len(rooms)] = room
        
    
    return genes, rooms
    

