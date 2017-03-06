"""
distribution.py
Author: Abby Feyrer
Credit: None

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
import string
txt=input("Please enter a string of text (the bigger the better): ")
print('The distribution of characters in "'+txt+'" is: ')
txt=txt.lower()
a=0-txt.count("a")
b=0-txt.count("b")
c=0-txt.count("c")
d=0-txt.count("d")
e=0-txt.count("e")
f=0-txt.count("f")
g=0-txt.count("g")
h=0-txt.count("h")
i=0-txt.count("i")
jk=0-txt.count("j")
k=0-txt.count("k")
l=0-txt.count("l")
m=0-txt.count("m")
n=0-txt.count("n")
o=0-txt.count("o")
p=0-txt.count("p")
q=0-txt.count("q")
r=0-txt.count("r")
s=0-txt.count("s")
t=0-txt.count("t")
u=0-txt.count("u")
v=0-txt.count("v")
w=0-txt.count("w")
x=0-txt.count("x")
y=0-txt.count("y")
z=0-txt.count("z")

abc=list(string.ascii_lowercase)

thing=([a,b,c,d,e,f,g,h,i,jk,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z])
a1=zip(thing,abc)

a2=(sorted(list(a1)))

for (x,y) in a2:
    while x<0:
        print(y, end="")
        x=x+1
    print(" ")
