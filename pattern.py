rows=5
cols=5
val=1
for i in range(rows):
    for j in range(cols):
        print(f"{val:2}", end=' ')
        val+=1
    print()

#  1  2  3  4  5 
#  6  7  8  9 10 
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25

rows=5
cols=5
val=65
for i in range(rows):
    for j in range(cols):
        print(f"{chr(val)}", end=' ')
        val+=1
    print()
# A B C D E
# F G H I J
# K L M N O
# P Q R S T
# U V W X Y

row=5
col=5
for i in range(row):
    for j in range(col):
        if j<=i:
            print("*", end=" ")
    print()

# * 
# * * 
# * * * 
# * * * * 
# * * * * *

row=5
col=5
for i in range(row):
    val=1
    for j in range(col):
        if j<=i:
            print(val, end=" ")
            val+=1
    print()
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

row=5
col=5
val=65
for i in range(row):
    for j in range(col):
        if j<=i:
            print(chr(val), end=" ")
    val+=1       
    print()

# A
# B B
# C C C
# D D D D
# E E E E E

row=5
col=5
for i in range(row):
    for j in range(col):
            print('*', end=" ")
    col-=1       
    print()

# * * * * *
# * * * *
# * * * 
# * *
# *
row=5
col=5
val=1
for i in range(row):
    for j in range(col):
            print(val, end=" ")
    col-=1
    val+=1       
    print()
# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5 
row=5
col=5

for i in range(row):
    val=1
    for j in range(col):
            print(val, end=" ")
            val+=1
    col-=1       
    print()

# 1 2 3 4 5
# 1 2 3 4 
# 1 2 3
# 1 2
# 1
row=5
col=5
for i in range(row):
    print(' '*(row-i) ,end=' ')
    for j in range(col):
            if j<=i:
                print('*',end=" ")               
    print()
            #     * 
            #    * * 
            #   * * * 
            #  * * * * 
            # * * * * *
rows = 5
for i in range(rows):
    print("  " * (rows - i-1 ), end=" ")
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

rows = 5
val = 1
width = len(str(val))+2     
for i in range(rows):
    print(" " * width * (rows - i - 1), end="")
    for j in range(2 * i + 1):
        print(f"{val:{width}}", end="")
        val += 1
    print()

#               1
#            2  3  4
#         5  6  7  8  9
#     10 11 12 13 14 15 16
#  17 18 19 20 21 22 23 24 25
rows = 5
col=5
val = 1
width = len(str(val))+2     
for i in range(rows):
    print(" " * width * (rows - i -1), end="")
    for j in range(col):
     if j<=i:
        print(f"{val:{width}}", end="")
        val += 1
    print()
#               1
#            2  3
#         4  5  6
#      7  8  9 10
#  11 12 13 14 15
rows = 5
width = len(str(rows)) + 2  
for i in range(1, rows + 1):
    print(" " * width * (rows - i), end="")    
    for j in range(i, 2 * i):
        print(f"{j:{width}}", end="")    
    for j in range(2 * i - 2, i - 1, -1):
        print(f"{j:{width}}", end="")
    print()
for i in range( rows -1,0,-1):
    print(" " * width * (rows - i), end="")    
    for j in range(i, 2 * i):
        print(f"{j:{width}}", end="")    
    for j in range(2 * i - 2, i - 1, -1):
        print(f"{j:{width}}", end="")
    print()

#               1
#            2  3  2
#         3  4  5  4  3
#      4  5  6  7  6  5  4
#   5  6  7  8  9  8  7  6  5
#      4  5  6  7  6  5  4
#         3  4  5  4  3
#            2  3  2
#               1

rows = 5
val = 0
width = len(str(val))+2     
for i in range(rows):
    print(" " * width * (rows - i - 1), end="")
    for j in range(2 * i + 1):
        print(f"{val:{width}}", end="")
    val += 1
    print()
val-=1
for k in range(rows-1,0,-1):
    val -= 1
    print(" " * width * (rows - k ), end="")
    for s in range(2 * k - 1):
        print(f"{val:{width}}", end="")     
    print()
#               0
#            1  1  1
#         2  2  2  2  2
#      3  3  3  3  3  3  3
#   4  4  4  4  4  4  4  4  4
#      3  3  3  3  3  3  3
#         2  2  2  2  2
#            1  1  1
#               0

# coef = coef * (i - j + 1) / j
row=6
val=1
width=len(str(val))+2
for i in range(row):
    print(" "*width*(row-i-1), end='')
    coef=val
    for j in range(1,i+2):
        print(f"{coef:{width}}", end=" "*(width))
        coef=coef*(i-j+1)//j
    print()
#                  1   
#               1     1   
#            1     2     1   
#         1     3     3     1   
#      1     4     6     4     1   
#   1     5    10    10     5     1 

row=5
col=5
val=65
for i in range(row):
    print(" "*(row-i), end="")
    for j in range(col):
        if j<=i:
            print(chr(val), end=" ")
    val+=1       
    print()
#      A 
#     B B 
#    C C C 
#   D D D D 
#  E E E E E 


row=5
val=65
for i in range(row):
    print(" "*(row-i-1), end="")
    for j in range(2*i+1):
            print(f"{chr(val)}", end="")
    val+=1       
    print()

row=5
for i in range(row):
    for j in range(row):
        if j<=i:
            print("*" , end="")
    print()
    if i<(row-1):
     print("*"*5)
    
# *
# *****
# **
# *****
# ***
# *****
# ****
# *****
# *****
row =5
for i in range(row):
    for j in range(row):
        if j == i or j == row - i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


    # *   *
    #  * *
    #   *
    #  *  *
    # *    *
row=10
for i in range(row):
    for j in range (row):
        if(i==0 or j==i or j==row-1):
            print("*" ,end=" ")
        else:
            print(" ",end=" ")
    print()
# * * * * * * * * * * 
#   *               * 
#     *             * 
#       *           * 
#         *         * 
#           *       * 
#             *     * 
#               *   * 
#                 * * 
#                   * 
row=10
for i in range(row):
    for j in range (row):
        if( j==0 or j==i or j==row-1 or j==row-i-1):
            print("*" ,end=" ")
        else:
            print(" ",end=" ")
    print()
# *                 * 
# * *             * * 
# *   *         *   * 
# *     *     *     * 
# *       * *       * 
# *       * *       * 
# *     *     *     * 
# *   *         *   * 
# * *             * * 
# *                 * 

# ?