import pandas as pd
from matplotlib import pyplot as plt

df=pd.read_csv("grades.csv")



def printlist(df):
    print(df)

def findAverage(df):
    print("Which test would you like to find the average for? (1/2)")
    choice=int(input("Choice: "))
    sum=0
    if (choice==1):
        averages=df[df.test==1]
        for x in averages.grades:
            sum+=x
    elif (choice==2):
        averages=df[df.test==2]
        for x in averages.grades:
            sum+=x
    print("The average for test", choice, "in the class  is", sum/len(averages.grades))

def highestScoreFinder(df, num):
    test1score=df[df.test==num]
    highestScore=0

    for i in test1score.grades:
        highestStudents=[]
        if (i>highestScore):
            highestScore=i
            highestStudent=test1score[test1score.grades==highestScore]
                            
    print("These students: ")
    for l in highestStudent.names:
        print(l)
        print("have the highest score of", highestScore)
        print()


def findHighestTestScore(df):
    print("Would you like to find: ")
    print("1) Highest student scores")
    print("2) Find highest test score for test 1")
    print("3) Find highest test score for test 2")
    choice=int(input("Choice: "))
    print()

    if (choice==1):
        highestStudent=""
        highestScore=0

        studentNames=[]
        for i in df.names:
            if i not in studentNames:
                studentNames.append(i)

        for x in studentNames:
            total=0 
            tempNames=df[df.names==x]
            for k in tempNames.grades:
                total+=k
            if (total>highestScore):
                highestScore=total
                highestStudent=x
        print(highestStudent, "has the highest score of", highestScore)
     
    
    elif (choice==2):
        highestScoreFinder(df, 1)
    
    elif (choice==3):
        highestScoreFinder(df, 2)

def findSpecificStudent(df):
    student=input("Which student do you want to find?: ")
    students=[]
    for i in df.names:
        students.append(i)
    while (student not in students):
        student=input("That student is not in our class. Search for another student or press (0) to exit: ")
        if (student=="0"):
            return
    print(df[df.names==student])
    
def writeToFile():
    addedPerson=input("Who do you want to add to the Gradebook?: ")
    test1grade=int(input("What did "+ addedPerson+ " get on test 1?: "))
    test2grade=int(input("What did "+ addedPerson+ " get on test 2?: "))
    df={"names": [addedPerson, addedPerson],
        "grades": [test1grade, test2grade],
        "test": [1,2]    
    }
    newDf=pd.DataFrame(df)
    newDf.to_csv("grades.csv", header=False, mode="a", index=False)


choice=1
while(choice!=6):
    df=pd.read_csv("grades.csv")
    print()
    print("Choices:")
    print("1) Print class list")
    print("2) Find averages of test scores")
    print("3) Find highest test score")
    print("4) Find specific student's test scores")
    print("5) Add student's test scores")
    print("6) Exit")
    choice=int(input("Enter your choice: "))
    print()

    if (choice==1):
        printlist(df)

    elif (choice==2):
        findAverage(df)
    elif (choice==3):
        findHighestTestScore(df)
    elif (choice==4):
        findSpecificStudent(df)
    elif (choice==5):
        writeToFile()
