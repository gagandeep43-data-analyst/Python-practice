#1.create and write to a file.

file = open("student.txt","w")
file.write("hii my name is mandeep kaur\ni am a data analyst")
file.write("\nthis is my beggining of whole journey")
file.close()


#2.Read entire file.

file = open("student.txt","r")
data = file.read()
print(data)
file.close

#3.Write multiple lines.

file = open("student.txt","w")
file.write("\nhello students")
file.write("\nmy father name is gurmeet singh")
file.write("\nmy mother name is sukhwinder kaur")
file.write("\nmy brother name is sukhpreet singh")
file.close()

#4.Read line by line.

file = open("student.txt","r")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

#5.Read all lines as list.

file = open("student.txt","r")
print(file.readlines())
file.close()

#6.Read file using loop.

file = open("student.txt","r")
for line in file:
    print(line.strip())
file.close()    

#7.Append data "a"

file = open("student.txt","a")
file.write("\nmy sister name is mandeep and sandeep")
file.close()

#8.count total lines.

file = open("student.txt","r")
count = 0
for line in file:
    count=count+1
print(count)    
file.close()

#9.count characters.
file = open("student.txt","r")
count = 0
for lines in file:
    for words in lines:
        count=count+1
print(count)        
file.close()

file = open("student.txt","r")
text = file.read()
print(len(text))
file.close()

#10count words.

file = open("student.txt","r")
text = file.read()
words = text.split()
print(len(words))
file.close()

#11.copy one file to another.

file1 = open("student.txt","r")
file2 = open("copy.txt","w")
data = file1.read()
file2.write(data)
file1.close()
file2.close()

#12.search a word.

file = open("student.txt","r")
data = file.read()
if "gurmeet" in data:
    print("found")
else:
    print("not found")
file.close()    

#13.replace a word.

file = open("student.txt","r")
data = file.read()
text = data.replace("name","naam")
print(text)
file.close()
file = open("student.txt","w")
file.write(text)
file.close()

#14.student marks file.

file = open("studentmarks.txt","w")
name = input("enter name:")
marks = input("enter marks:")
file.write(name+" "+marks)
file.close()

#15.Store multiple student record.

file = open("studentmarks.txt","w")
for i in range(3):
    name=input("enter name:")
    marks=input("enter marks:")
    result="\n"+name+" "+marks
    file.write(result)   
file.close()

#16.Find longest line.

file = open("student.txt","r")
longest=""
for line in file:
    if len(line) > len(longest):
        longest=line
print(longest)      
file.close()

#17.file using with statement.

with open("student.txt","r") as file:
    print(file.read())

#18.check whether file exists.

import os
if os.path.exists("student.txt"):
    print("file exists")
else:
    print("file not exists")

#19.Delete a file.

import os
os.remove("copy.txt")

#20.Exception Handling(Avoid file error).
try:
    file = open("second.txt","r")
    data = file.read()
    print(data)
    file.close()
except FileNotFoundError: 
    print("file does not exist.")  

##
a = "hello"
f = open("myfile.txt","a")
f.write(a)
f.close

f = open("first.txt")
print(f.read())
f.close()

f = open("first.txt")
data = f.read()
print(data)
f.close()
a = "this is a new line"
with open("first.txt","r+") as f:
    print(f.read())
    f.write("\nthis is a new line")

##
f = open("first.txt","r")
lines = f.readlines()
print(lines,type(lines))
f.close()

f = open("first.txt","r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)
line4 = f.readline()
print(line4,type(line4))
f.close()

##
#1.
file = open("work.txt","r")
data = file.read()
if "twinkle" in data:
    print("found")
else:
    print("not found")

#2.
import random
def game():
    print("you are playing a game...")
    score = random.randint(1,100)
    with open("worked.txt","r") as f:
        hiscore=f.read()
        if hiscore != "" :
            hiscore = int(hiscore)
        else:
            hiscore=0
    print("your score",score)        
    if (score>hiscore):
        with open("worked.txt","w") as f:
            f.write(str(score))
    return score   
game()  

#3.
def generatetable(n):
    table=""
    for i in range(1,11):
        table=table+str(n*i)+"\n"
        with open("tablesss/table_"+str(n),"w") as f:
            f.write(table)
for i in range(2,21):
    generatetable(i)

#4.
word = "donkey"
with open("word.txt","r") as f:
    content = f.read()
    new_content = content.replace(word,"#####")
    with open("word.txt","w") as f:
        f.write(new_content)

#5.
words = ["donkey","bad","carefull"]
with open("word.txt","r") as f:
    content = f.read()
    for word in words:
        content = content.replace(word,"#"*len(word))
    with open("word.txt","w") as f:
        f.write(content)

#6.
with open("log.txt","r") as f:
    content=f.read()
    if "python" in content:
        print("yes python is present in file")
    else:
        print("no python is not present in file")

#7.
with open("log.txt","r") as f:
    lines = f.readlines()
    lineno = 1
    for line in lines:
        if "python" in line:
            print("yes python is present in file: in lineno",lineno)
            break
        lineno+=1
    else:
        print("no python is not present in file")

#8.
with open("this.txt","r") as f:
    content = f.read()
    with open("this_copy.txt","w") as f:
        f.write(content)

#9.
with open("this.txt","r") as f:
    content1 = f.read()
with open("word.txt","r") as f:
    content2 = f.read()
if content1==content2:
    print("yes files are identical")    
else:
    print("no files are not identical")

#10.
with open("this.txt","w") as f:
    f.write("")

#11.
with open("old.txt","r") as f:
    content = f.read()
with open("renamed_python.txt","w") as f:
    f.write(content)   





