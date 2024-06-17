word = "Donkey"
with open("four.txt","r") as f:
    content = f.read()

contentNew = content.replace(word,"######")

with open("four.txt","w") as f:
    f.write(contentNew)