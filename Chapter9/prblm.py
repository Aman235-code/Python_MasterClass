f = open("poems.txt")
c = f.read()
if("twinkle" in c):
    print("Present")

else:
    print("Not present")
    
f.close()