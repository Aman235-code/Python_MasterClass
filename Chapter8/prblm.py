# def natural(n):
#     if n == 0:
#         return 0
#     return n + natural(n-1)

# n = int(input("Enter a number: "))
# res = natural(n)
# print(res)
def rem(l,word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["anAman","amohan","Shubh","Ramesh","an"]
print(rem(l,"an"))