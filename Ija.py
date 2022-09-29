import random
import turtle
import math
import time

class Window:

    distance = 1
    Object = None
    Control = False

    def New_Window(Width, Height, BackrounColor):

        WindowA = turtle.Screen()

        if Width and Height:
            WindowA.setup(Width, Height)
        else:
            print("Did not find or define Width and Heigth")
            exit()
    
        if BackrounColor:
            WindowA.bgcolor(BackrounColor)
        else:
            print("Did not find or indentify Backround Color")

        
    def UpdateWindow():

        Window = turtle.update()
    class Object:
        
        def CreateObject(Width, Heigth, color, DrawMode, shape):
            global Object
            
            Window = turtle.Screen()

            Object = turtle.Turtle()
            
            if shape:
                Object.shape(shape)
            else:
                print("Shape is not valid")
                exit()

            if Width and Heigth:
                Object.shapesize(Width, Heigth)
            else:
                print("Heigth or Width is not valid or indentify'd")
                exit()
            Object.color(color)

            Object.direction = "Stop"
            if DrawMode == False or DrawMode == "False" or DrawMode == "false":
                Object.penup()
            elif DrawMode == True or DrawMode == "True" or DrawMode == "true":
                Object.pendown()
            else:
                print("Only accepting True Or False bool/statement")
                exit()
                
        def ChangeSizeOfObject(Width, Heigth):
            if Width and Heigth:
                Object.shapesize(Width, Heigth)
            else:
                print("Heigth or Width is not valid or indentify'd")
                exit()
        def GetRecentObject():
            if Object:
                return Object
            else:
                print("Object is not found, use the CreateObject(Width, Heigth, color, DrawMode, shape)")

        def SetDistance(Number):
            global distance

            distance = Number

        def TurnRigth(degree):
            if distance:
                Object.right(degree)
            else:
                print("Did not define or find the distance, use the SetDistance")
                exit()

        def TurnLeft(degree):
            if distance:
                Object.left(degree)
            else:
                print("Did not define or find the distance, use the SetDistance")
                exit()

        def GoFoward(HowManyTimes):
            for i in range(HowManyTimes):
                if distance:
                    Object.forward(distance)
                else:
                    print("Did not define or find the distance, use the SetDistance")
                    exit()
        
        def GoBackward(HowManyTimes):
            for i in range(HowManyTimes):
                if distance:
                    Object.backward(distance)
                else:
                    print("Did not define or find the distance, use the SetDistance")
                    exit()

        def ActicateControl():
            global Control

            Control = True
        
        def DeactivateControl():

            global Control

            Control = False

        def SetControlProperty(AbleToMove, BeIndependent):

            if AbleToMove == True:
                global distance

                distance = 0

            if BeIndependent == True:
                global Object

                Object = None

        def SetDirection(Name):
            Object.direction = Name

        def GetDirection():
            return Object.direction

class Math:
    
    generatedNumber = None

    def CreateRandomNumber(Times, WaitingBetweenEachNumber, MinNumber, MaxNumber):

        if Times:
            while Times != 0:
                if WaitingBetweenEachNumber:
                    time.sleep(WaitingBetweenEachNumber)
                    if MinNumber and MaxNumber:
                        global generatedNumber
                        Times -= 1
                        TheNumber = random.randint(MinNumber, MaxNumber)
                        generatedNumber = TheNumber
                    else:
                        print("MinNumber Or MaxNumber must be a number")
                else:
                    print("WaitingBetweenEachNumber must be a number or decimal")
                    exit()
        else:
            print("Times must be a number")
    def GetGeneratedRandomNumber():

        return generatedNumber

    class Operation:

        RecentNumber = None

        def GetRecentAnswer():
            return RecentNumber

        def Addition(A, B):
            global RecentNumber

            Answer = A + B
            RecentNumber = Answer

            print(f"Answer got is {Answer}")
            
        def Subtraction(A, B):
            global RecentNumber

            Answer = A - B
            RecentNumber = Answer

            print(f"Answer got is {Answer}")

        def Multiply(A, B):
            global RecentNumber

            Answer = A * B
            RecentNumber = Answer

            print(f"Answer got is {Answer}") 

        def Split(A, B):
            global RecentNumber
            if A != 0:
                Answer = A / B
                RecentNumber = Answer

                print(f"Answer got is {Answer}")
            else:
                print("Cannot devide by 0")
                exit()

        def Round(A):
            global RecentNumber


            Answer = round(A)
            RecentNumber = Answer

            print(f"Answer got is {Answer}")

        def RootSquare(Number):
            global RecentNumber

            Answer = Number * Number
            RecentNumber = Answer

            print(f"Answer got is {Answer}")

        def ClearRecentAnswer():
            global RecentNumber

            RecentNumber = None

class File:
    
    File = None

    def CreateFile(Name, FileType):
        global File
        file = open(f"{Name}.{FileType}")
        File = file

    def ReturnFile():
        return File


class Terminal:

    inputval = None

    def SendError(Message,Reason, Line):
        print(f"{Message}, {Reason} On line {Line}")
        exit()
    
    def Print(Message):
        print(Message)
    
    def Input(Message):
        global inputval

        a = input(Message)
        inputval = a    
    def GetValueInInput():
        return inputval

    class Table:

        MyTable = None

        def CreateTable():
            global MyTable

            MyTable = []

        def Insert(Index,Value):
            MyTable.insert(Index, Value)

        def InsertValue(Value):
            MyTable.append(Value)

        def RemoveByValue(Values):
            MyTable.remove(Values)

        def RemoveByIndex(Index):
            MyTable.pop(Index)
        
        def ClearTable():
            MyTable.clear()
        
        def CheckTable():
            print(MyTable)
            print("----------------------------------------------------------------------------------")
            for Val in MyTable:
                print(Val)

        def GetTable():
            return MyTable
        
        def GetValueByIndex(Index):

            return MyTable[Index]