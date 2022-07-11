from datetime import datetime


class Student():
    def __init__(self,fullName,firstName,lastName,AdmissionYear,GradYear,DOB,Age,NoofDropoutYear,CGPAofEachSem,GradeinEachSem,AvgCGPA,finalGrade):
        self.fullName = fullName
        self.firstName = firstName
        self.lastName = lastName
        self.AdmissionYear = AdmissionYear
        self.GradYear = GradYear 
        self.DOB = DOB
        self.Age = Age
        self.NoofDropoutYear = NoofDropoutYear
        self.CGPAofEachSem = CGPAofEachSem
        self.GradeinEachSem = GradeinEachSem
        self.AvgCGPA = AvgCGPA
        self.finalGrade = finalGrade

    @staticmethod
    def factory(self,firstName,lastName,AdmissionYear,GradYear,DOB,CGPAofEachSem):
        fullName = fistName+" "+lastName
        Age =  datetime.date.today().year - DOB.year
        
        NoofDropoutYear = GradYear-AdmissionYear-4
        
        GradeinEachSem = []
        sum = 0

        for cgpa in CGPAofEachSem:
            grade = "D"
            sum+=cgpa
            if cgpa > 8:
                grade="A"
            elif cgpa > 6:
                grade="B"
            elif cgpa > 5:
                grade="C"

            GradeinEachSem.append(grade)

        AvgCGPA = sum/len(CGPAofEachSem)

        if AvgCGPA > 8:
            finalGrade="A"
        elif AvgCGPA > 6:
            finalGrade="B"
        elif AvgCGPA > 5:
            finalGrade="C"
        else:
            finalGrade="D"

        return Student(fullName,firstName,lastName,AdmissionYear,GradYear,DOB,Age,NoofDropoutYear,CGPAofEachSem,GradeinEachSem,AvgCGPA,finalGrade)

    def printValue(self,property):
        print(getattr(self,property))
    
    def updateValue(self,property, value):
        setattr(self,property,value)

def main():
    student = Student.factory("Rohit","Patil",2016,2020,datetime.datetime(1999,2,1),[5,6,8])
    student.printValue("fullName")

                
            