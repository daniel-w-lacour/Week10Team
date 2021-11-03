# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, nor tolerate those who do"
#   "I have not given or received any unauthorized aid on this assignment"
#
# Names: 	Daniel La Cour
#           Adrian Munoz
#           Nathan Gill
#           Jonathan Molyneux
# Section: 557
# Assignment: Lab10Team Act 1
# Date: 3 November 2021

# Daniel's
def count(array): # counts the intsances of items in an array, returns them as a dictionary
    seenvalues = {} # dictionary that holds the extension and the number of occurrences
    for i in array:
        if i in seenvalues.keys(): # if the extension has been seen before
            seenvalues[i] += 1 # increments the extensions seen count
        else:
            seenvalues[i] = 1 # initialize extension in dict
    return seenvalues # returns the dictionary
# Adrian's

# Nathan's

# Jonathan's