def main():
  
    i = get_positive_int()
    print("positive number: ", i)
def get_positive_int():
    while True:
        num = input("Give me a positive integer: \n")
        if float(num) > 0:
            break
    return num
main()