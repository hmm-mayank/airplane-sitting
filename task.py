# taken for loop and array refrence from Google for solving this problem 

filledSeats = 0  
number = 30   #total Number of Seat
row = 0    # to start from the beginning

def data(assgined):
    seats = []
    for i in assgined:
        rows = i[1]
        cols = i[0]
        mat = []
        for i in range(rows):
            mat.append([-1]*cols)
        seats.append(mat)
    return seats

def airplaneSitting(seats):
    blockSize = len(str(number))
    rows = [x[1] for x in assgined]
    cols = [x[0] for x in assgined]
    maximum = max(rows)
    top = True
    for i in range(maximum):
        rowlist = []
        rowlistl = []
        for j in range(length):
            row = ' '
            rowl = ' '
            if len(seats[j]) <= i:
                for k in range(cols[j]):
                    row += ' '*blockSize
                    rowl += ' '*blockSize
                    row += ' '
                    rowl += ' '
            else:
                row = ' '
                rowl = ' '
                for k in seats[j][i]:
                    if k == -1:
                        row += ' '*blockSize
                        rowl += ' '*blockSize
                        row += ' '
                        rowl += ' '
                    else:
                        row += str(k)+(' '*(blockSize - len(str(k))))
                        rowl += ' '*blockSize
                        row += ' '
                        rowl += ' '
            
            rowlist.append(row)
            rowlistl.append(rowl)
        if top:
            print('    '.join(rowlistl))
            top = False
        print('    '.join(rowlist))
        print('    '.join(rowlistl))

                
def fill_aisle_seats():
    # filledSeats = 0
    global filledSeats
    row = 0
    tempSwap = -1
    while filledSeats < number and filledSeats != tempSwap:
        tempSwap = filledSeats
        for i in range(length):
            if assgined[i][1] > row:
                if i == 0 and assgined[i][0] > 1:
                    filledSeats += 1
                    aisleCol = assgined[i][0] - 1
                    seats[i][row][aisleCol] = filledSeats
                    if filledSeats >= number:
                        break
                elif i == length - 1 and assgined[i][0] > 1:
                    filledSeats += 1
                    aisleCol = 0
                    seats[i][row][aisleCol] = filledSeats
                    if filledSeats >= number:
                        break
                else:
                    filledSeats += 1
                    aisleCol = 0
                    seats[i][row][aisleCol] = filledSeats
                    if filledSeats >= number:
                        break
                    if assgined[i][0] > 1:
                        filledSeats += 1
                        aisleCol = assgined[i][0] - 1
                        seats[i][row][aisleCol] = filledSeats
                        if filledSeats >= number:
                            break
        row += 1


def fill_window_seats():
    row = 0
    global filledSeats
    global number
    tempSwap = 0
    while filledSeats < number and filledSeats != tempSwap:
        tempSwap = filledSeats
        if assgined[0][1] > row:
            filledSeats += 1
            window = 0
            seats[0][row][window] = filledSeats
            if filledSeats >= number:
                break
        if assgined[length-1][1] > row:
            filledSeats += 1
            window = assgined[length-1][0] - 1
            seats[length-1][row][window] = filledSeats
            if filledSeats >= number:
                break
        row += 1

def fill_middle_seats(): #for filling Middle Seat
    row = 0
    tempSwap = 0
    global filledSeats # took global refrence from the Google
    while filledSeats < number and filledSeats != tempSwap:
        tempSwap = filledSeats
        for i in range(length):
            if assgined[i][1] > row:
                if assgined[i][0] > 2:
                    for col in range(1, assgined[i][0] - 1):
                        filledSeats += 1
                        seats[i][row][col] = filledSeats
                        if filledSeats >= number:
                            break
        row += 1


assgined = [[3,2],[4,3],[2,3],[3,4]]
seats = data(assgined)
length = len(assgined)


fill_aisle_seats()
fill_window_seats()
row = 0
tempSwap = 0
fill_middle_seats()


airplaneSitting(seats)
