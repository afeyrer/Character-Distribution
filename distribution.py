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
txt=input("Please enter a string of text (the bigger the better): ").lower()
print('The distribution of characters in "'+txt+'" is: ')

a=txt.count("a")
b=txt.count("b")
c=txt.count("c")
d=txt.count("d")
e=txt.count("e")
f=txt.count("f")
g=txt.count("g")
h=txt.count("h")
i=txt.count("i")
jk=txt.count("j")
k=txt.count("k")
l=txt.count("l")
m=txt.count("m")
n=txt.count("n")
o=txt.count("o")
p=txt.count("p")
q=txt.count("q")
r=txt.count("r")
s=txt.count("s")
t=txt.count("t")
u=txt.count("u")
v=txt.count("v")
w=txt.count("w")
x=txt.count("x")
y=txt.count("y")
z=txt.count("z")

abc=list(string.ascii_lowercase)

thing=([a,b,c,d,e,f,g,h,i,jk,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z])
a1=zip(thing,abc)

a2=(sorted(list(a1)))
a2=a2[::-1]
print(a2)

for (x,y) in a2:
    print(y)
