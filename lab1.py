from __future__ import division

class Student:
    courseMarks={}
    name= ""
    def __init__(self, name, family):
        self.name = name + " " + family
        
    def addCourseMark(self, course, mark):
        self.courseMarks[course] = mark
        
    def average(self):
        sumOfMarks = sum(self.courseMarks.values())
        numOfMarks = len(self.courseMarks)
        return sumOfMarks/numOfMarks
    
if __name__ == '__main__':
    firstName = raw_input("Enter the student's first name: ")
    lastName = raw_input("Enter the student's last name: ")
    
    aStudent = Student(firstName, lastName)
    
    while(True):
        courseName = raw_input("Enter the course name, or q to quit: ")
        if(courseName == 'q'):
            break
        courseMark = int(raw_input("Enter the course mark: "))
        aStudent.addCourseMark(courseName, courseMark)
    
    print ("%s has a current average of %f"%(aStudent.name, aStudent.average()))