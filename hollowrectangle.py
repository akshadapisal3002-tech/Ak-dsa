def rectangle(rows,cols):
    for i in range(rows):
        for j in range(cols):
            if i ==0 or i == rows-1:
                print("* ",end="")
            elif j == 0 or j == cols-1:
                print("* ", end = "")
            else:
                print("  ", end= "")
        print()
rectangle(5,5)