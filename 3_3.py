score = input("Enter Score: ")
r = float(score)
if (0.0<r<1.0):
    if (r>=0.9):
        print("A")
    elif (r>=0.8):
            print("B")
    elif (r>=0.7):
        print("C")
    elif (r>=0.6):
        print("D")
    else:
        print("F")

else:
    print("error")
    exit()
