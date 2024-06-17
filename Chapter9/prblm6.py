# with open("log.txt") as f:
#     content = f.read()

# if("python" in content):
#     print("present")
# else:
#     print("Not resent")

# line = 1
# with open("log.txt") as f:
#     lines = f.readlines()
    
# for l in lines:
#         if("python" in l):
#             print(f"present, {line}")
#             break
#         line+=1
# else:
#     print("Not present")

# with open("this.txt") as f:
#     c = f.read()

# with open("this_copy.txt","w") as f:
#     f.write(c)

# with open("this_copy.txt","w") as f:
#     f.write("")

with open("old.txt") as f:
    c = f.read()

with open("renamed_by_python.txt","w") as f:
    f.write(c)
