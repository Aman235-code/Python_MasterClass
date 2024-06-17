words = ["Donkey","bad","ganda"]
with open("four.txt","r") as f:
    content = f.read()

for word in words:
    content = content.replace(word,"#"*len(word))

with open("four.txt","w") as f:
    f.write(content)