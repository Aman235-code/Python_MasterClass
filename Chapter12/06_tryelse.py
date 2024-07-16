# try:
#     a = int(input("Hey, enter a number: "))
#     print(a)

# except Exception as e:
#     print(e)

# else:
#     print("Inside the else")

def main():
    try:
        a = int(input("Hey, enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return 

    finally:
        print("Inside the finally")

main()



