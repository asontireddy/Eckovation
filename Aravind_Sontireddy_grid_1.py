def drawGrid(height, width):
    for i in range(height + 1):
        for j in range(width):
            print(' ' +'-'*3, end="")
        print()
        if i != height:
            for j in range(width + 1):
                print("|" + " "*3, end= "")
        print()


def validateList(mylist):
    if len(mylist) != 2:
        return False
    try:
        int(mylist[0])
        int(mylist[1])
        return True
    except Exception:
        return False


while True:
    val = input("Enter height,width of the grid?\n")
    if val == "exit":
        exit()
    mylist = val.strip().split(",")
    if not validateList(mylist):
        print("Invalid input")
    else:
        height = int(mylist[0])
        width = int(mylist[1])
        drawGrid(height, width)
