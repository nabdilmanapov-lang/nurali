#Search function
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

#The findall() function returns a list containing all matches.
import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#The list contains the matches in the order they are found
import re
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

#The split() Function
#Split at each white-space character:
import re
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
#You can control the number of occurrences by specifying the maxsplit parameter:
import re
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
 
#The sub() function replaces the matches with the text of your choice:

import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

#You can control the number of replacements by specifying the count parameter:
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
 
#A Match Object is an object containing information about the search and the result.
import re
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object
#The Match object has properties and methods used to retrieve information about the search, and the result:
#.span() returns a tuple containing the start-, and end positions of the match.
#.string returns the string passed into the function
#.group() returns the part of the string where there was a match
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

#Print the string passed into the function:
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

#Print the part of the string where there was a match.
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
