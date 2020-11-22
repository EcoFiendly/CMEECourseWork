#!usr/bin/env python3

"""
Script illustrates the use of regex
"""

__appname__ = '[regexs.py]'
__author__ = 'Yewshen Lim (y.lim20@imperial.ac.uk)'
__version__ = '0.0.1'

import re
import urllib3

my_string = "a given string"

# find a space in the string
match = re.search(r'\s', my_string)
print(match) # tells you if a match was found
# to see match use
match.group()

# find digits in string
match = re.search(r'\d', my_string)
print(match) # no digit in string

# to know whether a pattern was matched, use if
MyStr = 'an example'

match = re.search(r'\w*\s', MyStr) # match unlimited words then space
if match:                      
    print('found a match:', match.group()) 
else:
    print('did not find a match')

# match 2 within the given string
match = re.search(r'2' , "it takes 2 to tango")
match.group()

# match digit within the given string
match = re.search(r'\d' , "it takes 2 to tango")
match.group()

# match a digit followed by everything after within the given string
match = re.search(r'\d.*' , "it takes 2 to tango")
match.group()

# match a space, 1 to 3 letters and another space within the given string
match = re.search(r'\s\w{1,3}\s', 'once upon a time')
match.group()

# match a space and unlimited letters at the end of the given string
match = re.search(r'\s\w*$', 'once upon a time')
match.group()

# match unlimited letters, a space, a digit, unlimited anything and a digit in
# the given string
# .group() directly returns the matched group
re.search(r'\w*\s\d.*\d', 'take 2 grams of H2O').group()

# match unlimited letters, unlimited anything and a space at the start of the
# given string
re.search(r'^\w*.*\s', 'once upon a time').group()

# *, +, and { } are all "greedy":
# They repeat the previous regex token as many times as possible
# To make them non-greedy and terminate at the first found instance of a pattern
# use ?

re.search(r'^\w*.*?\s', 'once upon a time').group()

# further illustrate greediness by matching a HTML tag
re.search(r'<.+>', 'This is a <EM>first</EM> test').group()

re.search(r'<.+?>', 'This is a <EM>first</EM> test').group()

# \ before . escapes the . so it becomes literal
re.search(r'\d*\.?\d*','1432.75+60.22i').group()

re.search(r'[AGTC]+', 'the sequence ATTCGT').group()

re.search(r'\s+[A-Z]\w+\s*\w+', \
    "The bird-shit frog's name is Theloderma asper.").group()

# look for email addresses in a string
MyStr = 'Samraat Pawar, s.pawar@imperial.ac.uk, Systems biology and \
    ecological theory'
match = re.search(r"[\w\s]+,\s[\w\.@]+,\s[\w\s]+", MyStr)
match.group()

# try on different pattern of email address
MyStr = 'Samraat Pawar, s-pawar@imperial.ac.uk, Systems biology and \
    ecological theory'
match = re.search(r"[\w\s]+,\s[\w\.@]+,\s[\w\s]+", MyStr)
# match.group() # error because there are no matches

match = re.search(r"[\w\s]+,\s[\w\.-]+@[\w\.-]+,\s[\w\s]+",MyStr)
match.group()

# Practicals: some regexercises

# 1. try regex we used for finding names ([\w\s]+) for cases where person's name
# has something unexpected, like a ? or a +. How to make it more robust
MyStr = 'Sam?raat Pawar, s-pawar@imperial.ac.uk, Systems biology and ecological\
 theory'

re.search(r'[\w\s]+.[\w\s]+', MyStr).group()

# translate the following regex into regular english
# r'^abc[ab]+\s\t\d'
# at start of the string exactly abc, then a or b then space once or more, tab, 
# numeric char

# r'^\d{1,2}\/\d{1,2}\/\d{4}$'
# start of string digit, one to two times, /, digit one to two times, /, digit 4
# times end of string
# matches dates

# r'\s*[a-zA-Z,\s]+\s*'
# zero or more occurence of spaces, a-z or A-Z then space once or more, zero or 
# more spaces
# matches a single alpha word

# write a regex to match dates in format YYYYMMDD, making sure that:
# only seemingly valid dates matche (ie year greater than 1900)
# first digit in month is either 0 or 1
# first digit in day =< 3
# r'19\d{2},[01]\d[^12]

re.search(r'19\d{2}[01]\d[123]\d*', "19001212").group()

# group regex patterns
MyStr = 'Samraat Pawar, s.pawar@imperial.ac.uk, Systems biology and \
    ecological theory'
match = re.search(r"[\w\s]+,\s[\w\.-]+@[\w\.-]+,\s[\w\s]+",MyStr)
match.group()

# without grouping regex
match.group(0)

# create groups using ( )
match = re.search(r"([\w\s]+),\s([\w\.-]+@[\w\.-]+),\s([\w\s&]+)",MyStr)
if match:
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))

# finding all matches
MyStr = "Samraat Pawar, s.pawar@imperial.ac.uk, Systems biology and \
    ecological theory; Another academic, a-academic@imperial.ac.uk, \
    Some other stuff thats equally boring; Yet another academic, \
    y.a_academic@imperial.ac.uk, Some other stuff thats even more boring"
# re.findall() returns a list of all the emails found
emails = re.findall(r'[\w\.-]+@[\w\.-]+', MyStr) 
for email in emails:
    print(email)

# finding in files
f = open('../../Week2/Data/TestOaksData.csv', 'r')
found_oaks = re.findall(r"Q[\w\s].*\s", f.read())

found_oaks

# groups within multiple matches
MyStr = "Samraat Pawar, s.pawar@imperial.ac.uk, Systems biology and \
    ecological theory; Another academic, a.academic@imperial.ac.uk, \
    Some other stuff thats equally boring; Yet another academic, \
    y.a.academic@imperial.ac.uk, Some other stuff thats even more boring"

found_matches = re.findall(r"([\w\s]+),\s([\w\.-]+@[\w\.-]+)", MyStr)
found_matches
for item in found_matches:
    print(item)

# extracting text from webpages
conn = urllib3.PoolManager() # open a connection
r = conn.request('GET', \
    'https://www.imperial.ac.uk/silwood-park/academic-staff/') 
webpage_html = r.data #read in the webpage's contents

# returned as bytes (not strings)
type(webpage_html)

# decode it
My_Data  = webpage_html.decode()
#print(My_Data)

# extract name of academics
pattern = r"Dr\s+\w+\s+\w+"
# example use of re.compile(); you can also ignore case  with re.IGNORECASE
regex = re.compile(pattern)
for match in regex.finditer(My_Data): # example use of re.finditer()
    print(match.group())

# improve matching to:
# include Prof names as well
# eliminate repeated matches
# group to separate title from first and second names
# extract names that have unexpected characters, such as in hyphenated names
pattern = r"(Dr\s|Prof\s)+?[\w\-\.\']+?\s+?[\w\-\.\']+?" # '|' means 'or'
regex = re.compile(pattern) 
matches = set()
for match in regex.finditer(My_Data):
    matches.add(match.group()) # save to set to prevent duplicates
print(matches)

# replace text
New_Data = re.sub(r'\t'," ", My_Data) # replace all tabs with a space
print(New_Data)