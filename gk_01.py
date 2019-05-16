def multipclation_table():
    row = 1
    while row <= 9:
        col = 1
        while col <= row :
            a = col * row
            print("%d * %d = %d" % (col,row,a),end="\t")
            col += 1
        print("")
        row += 1



multipclation_table()