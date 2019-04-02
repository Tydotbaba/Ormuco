# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 15:11:52 2019

@author: Oyedokun Temitayo

Question A:
    Your goal for this question is to write a program that accepts two lines 
    (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. 
    As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
	
Plan:
		
	get the user input
	the input format is (x1 x2)
	check if the lines overlaps
	print the result
"""


#get two inputs for the line
def getInput():
    """
    Function getInput()
    
    This function gets user input
    """
    #create a tuple to hold the line
    line = ()
    
    #get user input
    inputValue = input('Enter the line with space in-between, as in x1 x2:  ')
    
    #split the input string
    line = inputValue.split()
    
    # convert the line to float
    line = tuple(map(lambda x: int(x), line))
    print (line)
    
    #return the line
    return line

    #for testing purpose
    #print(line)
    


#check if the two lines overlap
def overlap(lines):
    """
    Function overlap(lines):
        
    @params: 
            lines: this is a list of tuples for the two lines 
    @result:
        the result is a string that states whether the two lines overlaps or not.
        
    Description: 
        This function acceptes two lines and determines whether the lines overlap or not
        
    """
    try:
        
        # create a variable to store the result
        resultString = f"line {lines[0]} and line {lines[1]} did not overlap."
        
        #check for ovelap
        if ((lines[0][1] > lines[1][0] and lines[0][0] < lines[1][1])  or 
            (lines[1][1] > lines[0][0] and lines[0][1] > lines[1][0])):
            resultString = f"line {lines[0]} and line {lines[1]} overlaps."
        
        #return the result
        return resultString
    except Exception as e:
        print('Your input is wrong, Please try again\n', e)



def calculateOverlap():
    """
    Function calculateOverlap()
    
    This function is the main function of the program. 
    It accepts two lines from user and determine wherther the lines overlap
    
    """
    #create a list to store the lines 
    lines =[]
    
    #get two lines from user
    for i in range(2):
        print(f"Enter values for line_{i + 1} ")
        lines.append(getInput())
        
    print(lines)
    
    #check if lines overlap
    result = overlap(lines)
    print(result)
    
    
    
if __name__ == '__main__':
    calculateOverlap()