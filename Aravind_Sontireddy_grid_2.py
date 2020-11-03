def drawGrid(height, width, special_cells):
    for i in range(height + 1):
        for j in range(width):
            print(' ' + '-' * 3, end="")
        print()
        if i != height:
            for j in range(width + 1):
                l = [i, j]
                if len(special_cells) != 0 and l in special_cells:
                    print("| " + "X ", end="")
                else:
                    print("|" + " " * 3, end="")
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


def validateSpecialCellsIndexBound(height1, width1, specialCell):
    if specialCell[0] >= height1 or specialCell[1] >= width1:
        return False
    return True


while True:
    special_cells = []
    valid = True
    val = input("Enter height,width of the grid?\n")
    if val == "exit":
        exit()
    mylist = val.strip().split(",")
    if not validateList(mylist):
        print("Invalid input")
        valid = False
    else:
        while True:
            row_col = input("Enter special cell as 'ROWNUM,COLNUM' (zero-indexed) or an empty line to print\n")
            if len(row_col.strip()) == 0:
                valid = True
                break
            else:
                row_col = row_col.strip().split(",")
                # validateSpecialCellsIndexBound is used to check whether special cells input lies inside actual Grid
                # ex:  1*1 Grid cannot have 2*2 specia cell
                if not validateList(row_col) or not validateSpecialCellsIndexBound(int(mylist[0]), int(mylist[1]), [int(row_col[0]), int(row_col[1])]):
                    print("Invalid input")
                    valid = False
                    break
                else:
                    special_cells.append([int(row_col[0]), int(row_col[1])])
    if valid:
        height = int(mylist[0])
        width = int(mylist[1])
        drawGrid(height, width, special_cells)
