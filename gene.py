

class Gene:

    """
        Represents a gene in the algorithm holding the all the information needed in given course. 
    """

    def __init__(self, id, course, room, section, teacher, termYear, department, program):
        """
            Initializes the gene

            :param int id: unique ID for the given course
            :param str course: course name
            :param str room: a room name for the given course, initially None
            :param str/int section: section of the class, 1, 2, A, B
            :param str teacher: the teacher who is giving this course
            :param int termYear: the year of the course given to. 1st, 2nd or 3rd Year
            :param str department: department of the students, IT, Software Engineering, Computer Scince
            :program str program: wheather the students are Regular or Extension or any
        """
        self.id = id
        self.course = course
        self.room = room
        self.section = section
        self.teacher = teacher
        self.termYear = termYear
        self.department = department
        self.program = program
    
    def display(self):

        """
            Prints the course info. 
        """

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
        """
            Returns the string that represents the students who are taking course representing this gene
        """
        return "{0}th year, section {1}, {2} {3}".format(self.termYear, self.section, self.department, self.program)