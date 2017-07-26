

class Gene:

    def __init__(self, id, course, room, section, teacher, termYear, department, program):
        self.id = id
        self.course = course
        self.room = room
        self.section = section
        self.teacher = teacher
        self.termYear = termYear
        self.department = department
        self.program = program
    
    def display(self):
        s = """
            Id: {7}
            Course: {0}
            Teacher: {1}
            Room: {2}
            Students: {3}th year, section {4}, {5} {6}
        """.format(self.course, self.teacher,self.room, \
        self.termYear, self.section, self.department, self.program, self.id)
        print(s)

    def toStudentString(self):
        return "{0}th year, section {1}, {2} {3}".format(self.termYear, self.section, self.department, self.program)