# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 15:12:32 2019

@author: Oyedokun Temitayo

Question B:
    The goal of this question is to write a software 
    library that accepts 2 version string as input and 
    returns whether one is greater than, equal, or less than the other. 
    As an example: “1.2” is greater than “1.1”. 
    Please provide all test cases you could think of.
"""


def getInput():
    """
    Function getInput()
    
    This function gets version input
    """
    #get user input
    version = input('Enter version:  ')
    
    assert version < 0, "Input Version must be greater than zero (0)."
    
    #return the line
    return version

    #for testing purpose
    #print(line)
    


#check if version is greater, lesser or equal
def processVersion(versions):
    """
    Function processVersion(versions):
        
    @params: 
            versions: this is a tuple for the two versions 
    @result:
        the result is a string that states if version is greater, lesser or equal.
        
    Description: 
        This function acceptes two versions and 
        determines if version is greater, lesser or equal
        
    """
    try:
        
        #unpack the versions
        (version1, version2) = versions
        
        #split the version input and convert to integer
        versionList1 = version1.split('.')
        versionList1 = list(map(int, versionList1))
        versionList2 = version2.split('.')
        versionList2 = list(map(int, versionList2))
        
        
        #assume that the version numbers will be equal in lenght
        if len(versionList1) != len(versionList2):
            raise Exception( "The version must be same in lenght" )
            
        #determine the lenght of the version input   
        count = len(versionList1)
        
        
        #check if version is greater, lesser or equAL
        for i in range(count):
            
            #calculate difference
            difference = float(versionList1[i] - versionList2[i])
            
            if difference == 0:
                continue
            
            elif difference < 0:
                return(f"version {version1} is less than {version2}.")
                
            elif difference > 0:
                return(f"version {version1} is greater than {version2}.")
        
        #the version is equal
        return (f"version {version1} is equal to {version2}.")
    except Exception as e:
        print(e)
        
    except ValueError as valueError:
        print('Error with your input value')
        print(valueError)




def checkVersion():
    """
    Function checkVersion()
    
    This function is the main function of the program. 
    It accepts two versions from user and
    determine wherther the versions are equal, greater or lesser.
    
    """
    #create a list to store the versions 
    versions = []
    
    #get two lines from user
    for i in range(2):
        print(f"Enter values for version_{i + 1} ")
        versions.append(getInput())
        
    print(versions)
    
    #check if lines overlap
    result = processVersion(versions)
    print(result)
    
    
    
if __name__ == '__main__':
    checkVersion()