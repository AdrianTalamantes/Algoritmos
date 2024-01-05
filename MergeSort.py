# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 08:49:25 2021

"""

def MergeSort(numList = [], n=0, verbose = False):
    if verbose:
        print('Mergesort (',n,'):',numList)
    if len(numList)<2:
        return numList
    else:
        L = len(numList)
        leftList = MergeSort(numList[:L//2],n+1, verbose=verbose)
        rightList = MergeSort(numList[L//2:],n+1, verbose=verbose)
        sortedList = []
        while len(leftList)>0 and len(rightList)>0:
            if leftList[0] < rightList[0]:
                sortedList.append(leftList.pop(0))
            else:
                sortedList.append(rightList.pop(0))
        for i in range(len(leftList)):
            sortedList.append(leftList.pop(0))
        for i in range(len(rightList)):
            sortedList.append(rightList.pop(0))
        if verbose:
            print('Merged (',n,')',sortedList)
        return sortedList
    
numList  = [5,6,4,7,8,5,0,1,2,3,9]
print(MergeSort(numList))