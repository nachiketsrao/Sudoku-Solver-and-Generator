from tkinter import *
import random
import pickle
import csv
import os.path
from os import path
import os

#------------------------------------------------------------------------------

# Points table calculations :

# level 1: 100 points
# level 2: 300 points
# level 3: 500 points
# 1/12 of no. of seconds taken to be subtracted from the initial number
# multiply number of hints taken by 10 and subtract the product from the initial points.
# display rank, name, points
# try to store all this info in a csv

#------------------------------------------------------------------------------

# code that defines user object
class user:
    
    def __init__(self):
        self.name=""
        self.password=""
        self.num_solved=0
        self.number=0
        self.complete_sudoku = []
        self.points = 0
        self.timeSaved = [0,0,0]

    def check_name(name):
        
        if len(str(name))<=4:
            return False
        for i in str(name):
            
            if i.isalnum()==False:
                return False
        return True

    def pass_check(pas):
        if len(str(pas))<=4:
            return False
        return True
    
        
    def first_input(self):
        
        
        while user.check_name(self.name)==False:
            print("Incorrect input :")
            return False
            
        print("The final name is :",self.name)
        
        

        while  user.pass_check(self.password)==False:
            print("Incorrect")
            return False
                    

        print("The final password ",self.password)
        
        return True
######################################## FOR SAVING ####################################################    
         
    def edit_csv(self, arr, complete, seconds, hints_taken, level ):    # store sudoku into the csv
        global number
        global complete_sudoku
        import csv
        file_name = str(self.name) + ".csv"      # Name of the peron is the name of the csv file
        
        print(arr)
                                             # this chunk stores sudoku solved until now
        if path.exists(file_name):
            os.remove(file_name)
        f = open(file_name,'w')
        w=csv.writer(f)
        w.writerows(arr)
        f.close()
        
        #----------------------------------------------------------------
        
        file_name = str(self.name + 'Solved') + ".csv"      # Name of the peron is the name of the csv file
        
        print(complete)
        
        if path.exists(file_name):
            os.remove(file_name)                    # this chunk stores complete sudoku
        f = open(file_name,'w')
        w=csv.writer(f)
        w.writerows(complete)
        f.close()
        number =1
       #  self.complete_sudoku = complete
        print("File saved oola la la le o")
        #--------------------------------------------------------------------
        # when sudoku i saved, time taken unitl now istores in the points.csv
        import csv
        f=open('points.csv','r')
        w=csv.reader(f)
        lis=list(w)
        #print('lis test :',lis)
        f.close()
        
        #print(lis)
        
        for i in lis:
            if len(i)>0:
                if i[0] == self.name :
                    
                    #i[2] = str(int(float((i[2])))) + seconds)
                    #i[3] = str(int(float((i[3])))) + hints_taken)
                    i[2] = str(seconds)
                    i[3] = str(hints_taken)
                    i[4] = str(level)
                    break
        print(lis)       
        
        for i in range(len(lis)-1,-1,-1):
            if len(lis[i])==0:
                del(lis[i])
                
        f = open('points.csv','w')
        wr=csv.writer(f)    # check this function, it is clearing the whole thing
        wr.writerows(lis)
        f.close()
        #----------------------------------------------------------------------
        
    def get_csv(self):   
        
        file_name = str(self.name) + ".csv"
        f = open(file_name,'r')              # returns sudoku solved until now
        w=list(csv.reader(f))
        
        return(w)

    def get_fullSolved(self):
        file_name = str(self.name + 'Solved') + ".csv"
        f = open(file_name,'r')
        w=list(csv.reader(f))               # return complete sudoku
    
        return(w)
        
    def calculate_points(self, level, time, hints_taken) :   
        
        # takes time in seconds
        # level 1: 100 points
        # level 2: 300 points
        # level 3: 500 points
        # 1/12 of no. of seconds taken to be subtracted from the initial number
        # multiply number of hints taken by 10 and subtract the product from the initial points.
        # display rank, name, points
        
        initial = 0
        
        if level=='1':
            initial = 100
        elif level=='2':
            initial = 300
        else:
            initial = 500
        
        import csv
        f=open('points.csv','r')
        w=csv.reader(f)
        lis=list(w)
        #print('lis test :',lis)
        f.close()
        
        #print(lis)
        # comprehensive test feedback :
        print('Level : ',level)
        print('total time :',time)
        print('hints taken :',hints_taken)
        
        score = initial - time * (1/12)
            
        score = score - hints_taken * 10
        
        import csv
        f=open('points.csv','r')
        w=csv.reader(f)
        lis=list(w)
        #print('lis test :',lis)
        f.close()
        
        #print(lis)
        
        for i in lis:
            if len(i)>0:
                if i[0] == self.name :
                    
                    i[1] = str(int(float((i[1]))) + int(score))
                    i[2]=i[3]=i[4]='0'
                    break
        print(lis)       
        
        for i in range(len(lis)-1,-1,-1):
            if len(lis[i])==0:
                del(lis[i])
                
        f = open('points.csv','w')
        wr=csv.writer(f)    # check this function, it is clearing the whole thing
        wr.writerows(lis)
        f.close()
        
        # since sudoku has been solved, delete any saved version:
        
        file_name = str(self.name) + ".csv"      # Name of the peron is the name of the csv file
        
                                             # this chunk stores sudoku solved until now
        if path.exists(file_name):
            os.remove(file_name)
            
        file_name = str(self.name + 'Solved') + ".csv"      # Name of the peron is the name of the csv file
        
        
        if path.exists(file_name):
            os.remove(file_name)
        #--------------------------------------------------------
       