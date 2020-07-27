import re

s = input("Do you agree?\n")

if re.search("yes|y", s, re.IGNORECASE): #it will return true of false re.search("y(es)?")
    print("Agreed.")
if re.search("no|n", s):
    print(("Not agreed."))

#if re.search("^y(es)?$", s, re.IGNORECASE)
#^ It states search the beggining of the string
#$ it states search the end of string
#That way the input search can be tight with no room to ignore other words before yes
