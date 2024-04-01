import random
import pygame
pygame.init()

def pochas(matr):
    a = 0
    b = 1
    da = 0
    db = 1
    save = matr[0][0]
    for i in range(17):
        matr[a][b], save = save, matr[a][b]
        if b == 2:
            da = 1
            db = 0
        if a == 2:
            da = 0
            db = -1
        if b == 0:
            db = 0
            da = -1
        if a == 0 and b == 0:
            da = 0
            db = 1
        b += db
        a += da

def protchas(matr):
    a = 1
    b = 0
    da = 1
    db = 0
    save = matr[0][0]
    for i in range(17):
        matr[a][b], save = save, matr[a][b]
        if a == 2:
            da = 0
            db = 1
        if b == 2:
            da = -1
            db = 0
        if a == 0:
            db = -1
            da = 0
        if a == 0 and b == 0:
            da = 1
            db = 0
        b += db
        a += da

def R():
    for i in range(3):
        green[i][2], white[i][2], blue[2-i][0], yellow[i][2] = yellow[i][2], green[i][2], white[i][2], blue[2-i][0]
    pochas(red)

def R1():
    for i in range(3):
        green[i][2], white[i][2], blue[2-i][0], yellow[i][2] = white[i][2], blue[2-i][0], yellow[i][2], green[i][2]
    protchas(red)

def L():
    for i in range(3):
        green[i][0], white[i][0], blue[2-i][2], yellow[i][0] = white[i][0], blue[2-i][2], yellow[i][0], green[i][0]
    pochas(orange)

def L1():
    for i in range(3):
        green[i][0], white[i][0], blue[2-i][2], yellow[i][0] = yellow[i][0], green[i][0], white[i][0], blue[2-i][2]
    protchas(orange)

def U():
    for i in range(3):
        green[0][i], orange[0][i], blue[0][i], red[0][i] = red[0][i], green[0][i], orange[0][i], blue[0][i]
    pochas(white)

def U1():
    for i in range(3):
        green[0][i], orange[0][i], blue[0][i], red[0][i] = orange[0][i], blue[0][i], red[0][i], green[0][i]
    protchas(white)

def D():
    for i in range(3):
        green[2][i], orange[2][i], blue[2][i], red[2][i] = orange[2][i], blue[2][i], red[2][i], green[2][i]
    pochas(yellow)

def D1():
    for i in range(3):
        green[2][i], orange[2][i], blue[2][i], red[2][i] = red[2][i], green[2][i], orange[2][i], blue[2][i]
    protchas(yellow)

def F():
    for i in range(3):
        orange[i][2], white[2][2-i], red[2-i][0], yellow[0][i] = yellow[0][i], orange[i][2], white[2][2-i], red[2-i][0]
    pochas(green)

def F1():
    for i in range(3):
        orange[i][2], white[2][2-i], red[2-i][0], yellow[0][i] = white[2][2-i], red[2-i][0], yellow[0][i], orange[i][2]
    protchas(green)

def B():
    for i in range(3):
        orange[i][0], white[0][2-i], red[2-i][2], yellow[2][i] = white[0][2-i], red[2-i][2], yellow[2][i], orange[i][0]
    pochas(blue)

def B1():
    for i in range(3):
        orange[i][0], white[0][2-i], red[2-i][2], yellow[2][i] = yellow[2][i], orange[i][0], white[0][2-i], red[2-i][2]
    protchas(blue)

def Rw():
    for j in range(2,0,-1):
        for i in range(3):
            green[i][j], white[i][j], blue[2 - i][2-j], yellow[i][j] = yellow[i][j], green[i][j], white[i][j], blue[2 - i][2-j]
    pochas(red)

def Rw1():
    for j in range(2,0,-1):
        for i in range(3):
            green[i][j], white[i][j], blue[2 - i][2-j], yellow[i][j] = white[i][j], blue[2 - i][2-j], yellow[i][j], green[i][j]
    protchas(red)

def Lw():
    for j in range(2):
        for i in range(3):
            green[i][j], white[i][j], blue[2 - i][2-j], yellow[i][j] = white[i][j], blue[2 - i][2-j], yellow[i][j], green[i][j]
    pochas(orange)

def Lw1():
    for j in range(2):
        for i in range(3):
            green[i][j], white[i][j], blue[2 - i][2-j], yellow[i][j] = yellow[i][j], green[i][j], white[i][j], blue[2 - i][2-j]
    protchas(orange)

def M1():
    for i in range(3):
        green[i][1], white[i][1], blue[2-i][1], yellow[i][1] = yellow[i][1], green[i][1], white[i][1], blue[2-i][1]

def M():
    for i in range(3):
        green[i][1], white[i][1], blue[2-i][1], yellow[i][1] = white[i][1], blue[2-i][1], yellow[i][1], green[i][1]

def Fw():
    for j in range(2,0,-1):
        for i in range(3):
            orange[i][j], white[j][2 - i], red[2 - i][2 - j], yellow[2 - j][i] = yellow[2 - j][i], orange[i][j], white[j][2 - i], red[2 - i][2 - j]
    pochas(green)

def Fw1():
    for j in range(2,0,-1):
        for i in range(3):
            orange[i][j], white[j][2 - i], red[2 - i][2 - j], yellow[2 - j][i] = white[j][2 - i], red[2 - i][2 - j], yellow[2 - j][i], orange[i][j]
    protchas(green)
def Y():
    for j in range(3):
        for i in range(3):
            green[j][i], red[j][i], blue[j][i], orange[j][i] = red[j][i], blue[j][i], orange[j][i], green[j][i]
    pochas(white)
    protchas(yellow)

def Y1():
    for j in range(3):
        for i in range(3):
            green[j][i], red[j][i], blue[j][i], orange[j][i] = orange[j][i], green[j][i], red[j][i], blue[j][i]
    pochas(yellow)
    protchas(white)

def moves(x):
    if x == 'R':
        R()
    if x == "R'":
        R1()
    if x == 'L':
        L()
    if x == "L'":
        L1()
    if x == 'U':
        U()
    if x == "U'":
        U1()
    if x == 'F':
        F()
    if x == "F'":
        F1()
    if x == 'B':
        B()
    if x == "B'":
        B1()
    if x == 'D':
        D()
    if x == "D'":
        D1()
    if x == "R2":
        R()
        R()
    if x == "U2":
        U()
        U()
    if x == "L2":
        L()
        L()
    if x == "D2":
        D()
        D()
    if x == "B2":
        B()
        B()
    if x == "F2":
        F()
        F()
    if x == 'Rw':
        Rw()
    if x == "Rw'":
        Rw1()
    if x == 'Rw2':
        Rw()
        Rw()
    if x == 'Lw':
        Lw()
    if x == "Lw'":
        Lw1()
    if x == 'Lw2':
        Lw()
        Lw()
    if x == 'Fw':
        Fw()
    if x == "Fw'":
        Fw1()
    if x == 'Fw2':
        Fw()
        Fw()
    if x == 'M':
        M()
    if x == "M'":
        M1()
    if x == 'M2':
        M()
        M()
    if x == 'y':
        Y()
    if x == "y'":
        Y1()

def cross():
    solve = ''
    if yellow[0][1] == yellow[1][1] or yellow[1][0] == yellow[1][1] or yellow[2][1] == yellow[1][1] or yellow[1][2] == yellow[1][1]:
        while True:
            if (red[2][1] == red[1][1] and yellow[1][2] == yellow[1][1]) or (orange[2][1] == orange[1][1] and yellow[1][0] == yellow[1][1]) or (
                    blue[2][1] == blue[1][1] and yellow[2][1] == yellow[1][1]) or (green[2][1] == green[1][1] and yellow[0][1] == yellow[1][1]):
                break
            D()
            solve += 'D '
            solve = solve.replace('D D ', 'D2 ')
            solve = solve.replace('D D D ', "D' ")
    while yellow[0][1] != yellow[1][1] or yellow[1][0] != yellow[1][1] or yellow[2][1] != yellow[1][1] or yellow[1][2] != yellow[1][1] or green[2][1] != green[1][1] or red[2][1] != red[1][1] or blue[2][1] != blue[1][1] or orange[2][1] != orange[1][1]:
        if orange[1][2] == yellow[1][1] and green[1][0] == green[1][1]:
            F1()
            solve += "F' "
        elif red[1][0] == yellow[1][1] and green[1][2] == green[1][1]:
            F()
            solve += "F "
        elif green[1][2] == yellow[1][1] and red[1][0] == red[1][1]:
            R1()
            solve += "R' "
        elif blue[1][0] == yellow[1][1] and red[1][2] == red[1][1]:
            R()
            solve += 'R '
        elif red[1][2] == yellow[1][1] and blue[1][0] == blue[1][1]:
            B1()
            solve += "B' "
        elif orange[1][0] == yellow[1][1] and blue[1][2] == blue[1][1]:
            B()
            solve += "B "
        elif blue[1][2] == yellow[1][1] and orange[1][0] == orange[1][1]:
            L1()
            solve += "L' "
        elif green[1][0] == yellow[1][1] and orange[1][2] == orange[1][1]:
            L()
            solve += "L "

        elif white[2][1] == yellow[1][1]:
            if green[0][1] == green[1][1]:
                moves('F2')
                solve += 'F2 '
            elif green[0][1] == red[1][1]:
                U1(); R(); R()
                solve += "U' R2 "
            elif green[0][1] == blue[1][1]:
                U(); U(); B(); B()
                solve += 'U2 B2 '
            elif green[0][1] == orange[1][1]:
                U(); L(); L()
                solve += 'U L2 '
        elif green[0][1] == yellow[1][1]:
            if white[2][1] == green[1][1]:
                if (red[2][1] == red[1][1] and yellow[1][2] == yellow[1][1]) or (orange[2][1] == orange[1][1] and yellow[1][0] == yellow[1][1]) or (blue[2][1] == blue[1][1] and yellow[2][1] == yellow[1][1]):
                    F(); D(); R1(); D1()
                    solve += "F D R' D' "
                else:
                    F(); R1(); D1()
                    solve += "F R' D' "
            elif white[2][1] == red[1][1]:
                if green[2][1] == green[1][1] and yellow[0][1] == yellow[1][1]:
                    F(); R1(); F1()
                    solve += "F R' F' "
                else:
                    F(); R1()
                    solve += "F R' "
            elif white[2][1] == blue[1][1]:
                if red[2][1] == red[1][1] and yellow[1][2] == yellow[1][1]:
                    U1(); R(); B1(); R1()
                    solve += "U' R B' R' "
                else:
                    U1(); R(); B1()
                    solve += "U' R B' "
            elif white[2][1] == orange[1][1]:
                if green[2][1] == green[1][1] and yellow[0][1] == yellow[1][1]:
                    F1(); L(); F()
                    solve += "F' L F "
                else:
                    F1(); L()
                    solve += "F' L "

        elif white[1][0] == yellow[1][1]:
            if orange[0][1] == green[1][1]:
                U1(); F(); F()
                solve += "U' F2 "
            elif orange[0][1] == red[1][1]:
                U(); U(); R(); R()
                solve += 'U2 R2 '
            elif orange[0][1] == blue[1][1]:
                U(); B(); B()
                solve += 'U B2 '
            elif orange[0][1] == orange[1][1]:
                L(); L()
                solve += 'L2 '
        elif orange[0][1] == yellow[1][1]:
            if white[1][0] == green[1][1]:
                if orange[2][1] == orange[1][1] and yellow[1][0] == yellow[1][1]:
                    L(); F1(); L1()
                    solve += "L F' L' "
                else:
                    L(); F1()
                    solve += "L F' "
            elif white[1][0] == red[1][1]:
                if green[2][1] == green[1][1] and yellow[0][1] == yellow[1][1]:
                    U1(); F(); R1(); F1()
                    solve += "U' F R' F' "
                else:
                    U1(); F(); R1()
                    solve += "U' F R' "
            elif white[1][0] == blue[1][1]:
                if orange[2][1] == orange[1][1] and yellow[1][0] == yellow[1][1]:
                    L1(); B(); L()
                    solve += "L' B L "
                else:
                    L1(); B()
                    solve += "L' B "
            elif white[1][0] == orange[1][1]:
                if (red[2][1] == red[1][1] and yellow[1][2] == yellow[1][1]) or (green[2][1] == green[1][1] and yellow[0][1] == yellow[1][1]) or (blue[2][1] == blue[1][1] and yellow[2][1] == yellow[1][1]):
                    L(); D(); F1(); D1()
                    solve += "L D F' D' "
                else:
                    L(); F1(); D1()
                    solve += "L F' D' "

        elif white[0][1] == yellow[1][1]:
            if blue[0][1] == green[1][1]:
                U(); U(); F(); F()
                solve += 'U2 F2 '
            elif blue[0][1] == red[1][1]:
                U(); R(); R()
                solve += 'U R2 '
            elif blue[0][1] == blue[1][1]:
                B(); B()
                solve += 'B2 '
            elif blue[0][1] == orange[1][1]:
                U1(); L(); L()
                solve += "U' L2 "
        elif blue[0][1] == yellow[1][1]:
            if white[0][1] == green[1][1]:
                if red[2][1] == red[1][1] and yellow[1][2] == yellow[1][1]:
                    U(); R1(); F(); R()
                    solve += "U R' F R "
                else:
                    U(); R1(); F()
                    solve += "U R' F "
            elif white[0][1] == red[1][1]:
                if blue[2][1] == blue[1][1] and yellow[2][1] == yellow[1][1]:
                    B1(); R1(); B()
                    solve += "B' R' B "
                else:
                    B1(); R()
                    solve += "B' R "
            elif white[0][1] == blue[1][1]:
                if (red[2][1] == red[1][1] and yellow[1][2] == yellow[1][1]) or (green[2][1] == green[1][1] and yellow[0][1] == yellow[1][1]) or (orange[2][1] == orange[1][1] and yellow[1][0] == yellow[1][1]):
                    U(); R(); B1(); R1()
                    solve += "U R B' R' "
                else:
                    B1(); R(); D()
                    solve += "B' R D "
            elif white[0][1] == orange[1][1]:
                if blue[2][1] == blue[1][1] and yellow[2][1] == yellow[1][1]:
                    B(); L1(); B1()
                    solve += "B L' B' "
                else:
                    B(); L1()
                    solve += "B L' "

        elif white[1][2] == yellow[1][1]:
            if red[0][1] == green[1][1]:
                U(); F(); F()
                solve += "U F2 "
            elif red[0][1] == red[1][1]:
                R(); R()
                solve += "R2 "
            elif red[0][1] == blue[1][1]:
                U1(); B(); B()
                solve += "U' B2 "
            elif red[0][1] == orange[1][1]:
                U(); U(); L(); L()
                solve += "U2 L2 "
        elif red[0][1] == yellow[1][1]:
            if white[1][2] == green[1][1]:
                if red[2][1] == red[1][1] and yellow[1][2] == yellow[1][1]:
                    R1(); F(); R()
                    solve += "R' F R "
                else:
                    R1(); F()
                    solve += "R' F "
            elif white[1][2] == red[1][1]:
                if (blue[2][1] == blue[1][1] and yellow[2][1] == yellow[1][1]) or (green[2][1] == green[1][1] and yellow[0][1] == yellow[1][1]) or (orange[2][1] == orange[1][1] and yellow[1][0] == yellow[1][1]):
                    R1(); D1(); F(); D()
                    solve += "R' D' F D "
                else:
                    R1(); F(); D()
                    solve += "R' F D "
            elif white[1][2] == blue[1][1]:
                if red[2][1] == red[1][1] and yellow[1][2] == yellow[1][1]:
                    R(); B1(); R1()
                    solve += "R B' R' "
                else:
                    R(); B1()
                    solve += "R B' "
            elif white[1][2] == orange[1][1]:
                if green[2][1] == green[1][1] and yellow[0][1] == yellow[1][1]:
                    U(); F1(); L(); F()
                    solve += "U F' L F "
                else:
                    U(); F(); L()
                    solve += "U F L "
        elif green[1][2] == yellow[1][1]:
            if red[1][0] == green[1][1]:
                if (red[2][1] == red[1][1] and yellow[1][2] == yellow[1][1]) or (orange[2][1] == orange[1][1] and yellow[1][0] == yellow[1][1]) or (blue[2][1] == blue[1][1] and yellow[2][1] == yellow[1][1]):
                    D(); R1(); D1()
                    solve += "D R' D' "
                else:
                    R1(), D1()
                    solve += "R' D' "
            elif red[1][0] == blue[1][1]:
                if (red[2][1] == red[1][1] and yellow[1][2] == yellow[1][1]) or (green[2][1] == green[1][1] and yellow[0][1] == yellow[1][1]) or (orange[2][1] == orange[1][1] and yellow[1][0] == yellow[1][1]):
                    D1(); R1(); D()
                    solve += "D' R' D "
                else:
                    R1(); D()
                    solve += "R' D "
            elif red[1][0] == orange[1][1]:
                if green[2][1] == green[1][1] and yellow[0][1] == yellow[1][1]:
                    F(); F(); L(); F(); F()
                    solve += "F2 L F2 "
                else:
                    F(); F(); L()
                    solve += "F2 L "
        elif red[1][0] == yellow[1][1]:
            if green[1][2] == red[1][1]:
                if (blue[2][1] == blue[1][1] and yellow[2][1] == yellow[1][1]) or (green[2][1] == green[1][1] and yellow[0][1] == yellow[1][1]) or (orange[2][1] == orange[1][1] and yellow[1][0] == yellow[1][1]):
                    D1(); F(); D()
                    solve += "D' F D "
                else:
                    F(); D()
                    solve += "F D "
            elif green[1][2] == blue[1][1]:
                if red[2][1] == red[1][1] and yellow[1][2] == yellow[1][1]:
                    R(); R(); B1(); R(); R()
                    solve += "R2 B' R2 "
                else:
                    R(); R(); B1()
                    solve += "R2 B' "
            elif green[1][2] == orange[1][1]:
                if (red[2][1] == red[1][1] and yellow[1][2] == yellow[1][1]) or (green[2][1] == green[1][1] and yellow[0][1] == yellow[1][1]) or (blue[2][1] == blue[1][1] and yellow[2][1] == yellow[1][1]):
                    D(); F(); D1()
                    solve += "D F D' "
                else:
                    F(); D1()
                    solve += "F D' "
        elif red[1][2] == yellow[1][1]:
            if blue[1][0] == green[1][1]:
                if red[2][1] == red[1][1] and yellow[1][2] == yellow[1][1]:
                    R(); R(); F(); R(); R()
                    solve += "R2 F R2 "
                else:
                    R(); R(); F()
                    solve += "R2 F "
            elif blue[1][0] == red[1][1]:
                if (blue[2][1] == blue[1][1] and yellow[2][1] == yellow[1][1]) or (green[2][1] == green[1][1] and yellow[0][1] == yellow[1][1]) or (orange[2][1] == orange[1][1] and yellow[1][0] == yellow[1][1]):
                    D(); B1(); D1()
                    solve += "D B' D' "
                else:
                    B1(); D1()
                    solve += "B' D' "
            elif blue[1][0] == orange[1][1]:
                if (red[2][1] == red[1][1] and yellow[1][2] == yellow[1][1]) or (green[2][1] == green[1][1] and yellow[0][1] == yellow[1][1]) or (blue[2][1] == blue[1][1] and yellow[2][1] == yellow[1][1]):
                    D1(); B1(); D()
                    solve += "D' B' D "
                else:
                    B1(); D()
                    solve += "B' D "
        elif blue[1][0] == yellow[1][1]:
            if red[1][2] == green[1][1]:
                if (red[2][1] == red[1][1] and yellow[1][2] == yellow[1][1]) or (orange[2][1] == orange[1][1] and yellow[1][0] == yellow[1][1]) or (blue[2][1] == blue[1][1] and yellow[2][1] == yellow[1][1]):
                    D(); R1(); D1()
                    solve += "D R' D' "
                else:
                    R1(); D1()
                    solve += "R' D' "
            elif red[1][2] == blue[1][1]:
                if (red[2][1] == red[1][1] and yellow[1][2] == yellow[1][1]) or (green[2][1] == green[1][1] and yellow[0][1] == yellow[1][1]) or (orange[2][1] == orange[1][1] and yellow[1][0] == yellow[1][1]):
                    D1(); R(); D()
                    solve += "D' R D "
                else:
                    R(); D()
                    solve += "R D "
            elif red[1][2] == orange[1][1]:
                if blue[2][1] == blue[1][1] and yellow[2][1] == yellow[1][1]:
                    B(); B(); L1(); B(); B()
                    solve += "B2 L' B2 "
                else:
                    B(); B(); L1()
                    solve += "B2 L' "
        elif blue[1][2] == yellow[1][1]:
            if orange[1][0] == green[1][1]:
                if (red[2][1] == red[1][1] and yellow[1][2] == yellow[1][1]) or (orange[2][1] == orange[1][1] and yellow[1][0] == yellow[1][1]) or (blue[2][1] == blue[1][1] and yellow[2][1] == yellow[1][1]):
                    D1(); L1(); D()
                    solve += "D' L' D "
                else:
                    L1(); D()
                    solve += "L' D "
            elif orange[1][0] == red[1][1]:
                if blue[2][1] == blue[1][1] and yellow[2][1] == yellow[1][1]:
                    B(); B(); R1(); B(); B()
                    solve += "B2 R' B2 "
                else:
                    B(); B(); R1()
                    solve += "B2 R' "
            elif orange[1][0] == blue[1][1]:
                if (red[2][1] == red[1][1] and yellow[1][2] == yellow[1][1]) or (green[2][1] == green[1][1] and yellow[0][1] == yellow[1][1]) or (orange[2][1] == orange[1][1] and yellow[1][0] == yellow[1][1]):
                    D(); L1(); D1()
                    solve += "D L' D' "
                else:
                    L1(); D1()
                    solve += "L' D' "
        elif orange[1][0] == yellow[1][1]:
            if blue[1][2] == green[1][1]:
                if orange[2][1] == orange[1][1] and yellow[1][0] == yellow[1][1]:
                    L(); L(); F1(); L(); L()
                    solve += "L2 F' L2 "
                else:
                    L(); L(); F1()
                    solve += "L2 F' "
            elif blue[1][2] == red[1][1]:
                if (blue[2][1] == blue[1][1] and yellow[2][1] == yellow[1][1]) or (green[2][1] == green[1][1] and yellow[0][1] == yellow[1][1]) or (orange[2][1] == orange[1][1] and yellow[1][0] == yellow[1][1]):
                    D(); B(); D1()
                    solve += "D B D' "
                else:
                    B(); D1()
                    solve += "B D' "
            elif blue[1][2] == orange[1][1]:
                if (red[2][1] == red[1][1] and yellow[1][2] == yellow[1][1]) or (green[2][1] == green[1][1] and yellow[0][1] == yellow[1][1]) or (blue[2][1] == blue[1][1] and yellow[2][1] == yellow[1][1]):
                    D1(); B(); D()
                    solve += "D' B D "
                else:
                    B(); D()
                    solve ++ "B D "
        elif orange[1][2] == yellow[1][1]:
            if green[1][0] == red[1][1]:
                if (blue[2][1] == blue[1][1] and yellow[2][1] == yellow[1][1]) or (green[2][1] == green[1][1] and yellow[0][1] == yellow[1][1]) or (orange[2][1] == orange[1][1] and yellow[1][0] == yellow[1][1]):
                    D1(); F1(); D()
                    solve += "D' F' D "
                else:
                    F1(); D()
                    solve += "F' D "
            elif green[1][0] == blue[1][1]:
                if orange[2][1] == orange[1][1] and yellow[1][0] == yellow[1][1]:
                    L(); L(); B(); L(); L()
                    solve += "L2 B L2 "
                else:
                    L(); L(); B()
                    solve += "L2 B "
            elif green[1][0] == orange[1][1]:
                if (red[2][1] == red[1][1] and yellow[1][2] == yellow[1][1]) or (green[2][1] == green[1][1] and yellow[0][1] == yellow[1][1]) or (blue[2][1] == blue[1][1] and yellow[2][1] == yellow[1][1]):
                    D(); F1(); D1()
                    solve += "D F' D' "
                else:
                    F1(); D1()
                    solve += "F' D' "
        elif green[1][0] == yellow[1][1]:
            if orange[1][2] == green[1][1]:
                if (red[2][1] == red[1][1] and yellow[1][2] == yellow[1][1]) or (orange[2][1] == orange[1][1] and yellow[1][0] == yellow[1][1]) or (blue[2][1] == blue[1][1] and yellow[2][1] == yellow[1][1]):
                    D1(); L(); D()
                    solve += "D' L D "
                else:
                    L(); D()
                    solve += "L D "
            elif orange[1][2] == red[1][1]:
                if green[2][1] == green[1][1] and yellow[0][1] == yellow[1][1]:
                    F(); F(); R1(); F(); F()
                    solve += "F2 R' F2 "
                else:
                    F(); F(); R1()
                    solve += "F2 R' "
            elif orange[1][2] == blue[1][1]:
                if (red[2][1] == red[1][1] and yellow[1][2] == yellow[1][1]) or (green[2][1] == green[1][1] and yellow[0][1] == yellow[1][1]) or (orange[2][1] == orange[1][1] and yellow[1][0] == yellow[1][1]):
                    D(); L(); D1()
                    solve += "D L D' "
                else:
                    L(); D1()
                    solve += "L D' "

        elif yellow[1][2] == yellow[1][1] and red[2][1] != red[1][1]:
            R(); R()
            solve += 'R2 '
        elif red[2][1] == yellow[1][1]:
            R()
            solve += "R "

        elif yellow[1][0] == yellow[1][1] and orange[2][1] != orange[1][1]:
            L(); L()
            solve += 'L2 '
        elif orange[2][1] == yellow[1][1]:
            L1()
            solve += "L' "

        elif yellow[0][1] == yellow[1][1] and green[2][1] != green[1][1]:
            F(); F()
            solve += "F2 "
        elif green[2][1] == yellow[1][1]:
            F()
            solve += "F "

        elif yellow[2][1] == yellow[1][1] and blue[2][1] != blue[1][1]:
            B(); B()
            solve += "B2 "
        elif blue[2][1] == yellow[1][1]:
            B1()
            solve += "B' "

    solve = solve.replace("D D' ", '')
    solve = solve.replace("D' D ", '')
    solve = solve.replace("D' D' ", 'D2 ')
    solve = solve.replace("D2 D ", "D' ")
    solve = solve.replace("F' F' ", 'F2 ')
    solve = solve.replace("F2 F ", "F' ")
    solve = solve.replace("D D ", 'D2 ')
    solve = solve.replace("R2 R' ", "R ")
    solve = solve.replace("L L ", "L2 ")
    solve = solve.replace("L2 L' ", "L ")
    solve = solve.replace("B B2 ", "B' ")
    solve = solve.replace("R2 R ", "R' ")
    solve = solve.replace("R R2 ", "R' ")
    if solve == '': solve = 'skip'
    text = font.render('Cross: ' + solve, True, colorblack)
    screen.blit(text, [500, 150])

def F2L():
    solve = ''
    for i in range(4):
        yy = 0
        if not((yellow[0][2] == yellow[1][1] and green[2][2] == green[1][1] and red[2][0] == red[1][1]) or (yellow[0][2] == green[1][1] and green[2][2] == red[1][1] and red[2][0] == yellow[1][1]) or (yellow[0][2] == red[1][1] and green[2][2] == yellow[1][1] and red[2][0] == green[1][1])):
            if (yellow[0][0] == yellow[1][1] and orange[2][2] == green[1][1] and green[2][0] == red[1][1]) or (yellow[0][0] == green[1][1] and orange[2][2] == red[1][1] and green[2][0] == yellow[1][1]) or (yellow[0][0] == red[1][1] and orange[2][2] == yellow[1][1] and green[2][0] == green[1][1]):
                L1(); U1(); L()
                solve += "L' U' L "
            elif (yellow[2][0] == yellow[1][1] and blue[2][2] == green[1][1] and orange[2][0] == red[1][1]) or (yellow[2][0] == green[1][1] and blue[2][2] == red[1][1] and orange[2][0] == yellow[1][1]) or (yellow[2][0] == red[1][1] and blue[2][2] == yellow[1][1] and orange[2][0] == green[1][1]):
                L(); U(); U(); L1()
                solve += "L U2 L' "
            elif (yellow[2][2] == yellow[1][1] and red[2][2] == green[1][1] and blue[2][0] == red[1][1]) or (yellow[2][2] == green[1][1] and red[2][2] == red[1][1] and blue[2][0] == yellow[1][1]) or (yellow[2][2] == red[1][1] and red[2][2] == yellow[1][1] and blue[2][0] == green[1][1]):
                R1(); U(); U(); R(); U1()
                solve += "R' U2 R U' "
            else:
                while not((white[2][2] == yellow[1][1] and green[0][2] == red[1][1] and red[0][0] == green[1][1]) or (white[2][2] == green[1][1] and green[0][2] == yellow[1][1] and red[0][0] == red[1][1]) or (white[2][2] == red[1][1] and green[0][2] == green[1][1] and red[0][0] == yellow[1][1])):
                    U()
                    solve += 'U '

        if not((green[1][2] == green[1][1] and red[1][0] == red[1][1]) or (green[1][2] == red[1][1] and red[1][0] == green[1][1])):
            if (green[1][0] == green[1][1] and orange[1][2] == red[1][1]) or (green[1][0] == red[1][1] and orange[1][2] == green[1][1]):
                L1();  U1(); L(); U()
                solve += "L' U' L U "
            elif (orange[1][0] == green[1][1] and blue[1][2] == red[1][1]) or (orange[1][0] == red[1][1] and blue[1][2] == green[1][1]):
                L(); U1(); L1(); U()
                solve += "L U' L' U "
            elif (blue[1][0] == green[1][1] and red[1][2] == red[1][1]) or (blue[1][0] == red[1][1] and red[1][2] == green[1][1]):
                R1(); U(); R()
                solve += "R' U R "
            if (yellow[0][2] == yellow[1][1] and green[2][2] == green[1][1] and red[2][0] == red[1][1]) or (yellow[0][2] == green[1][1] and green[2][2] == red[1][1] and red[2][0] == yellow[1][1]) or (yellow[0][2] == red[1][1] and green[2][2] == yellow[1][1] and red[2][0] == green[1][1]):
                while not((green[0][1] == green[1][1] and white[2][1] == red[1][1]) or (green[0][1] == red[1][1] and white[2][1] == green[1][1])):
                    U()
                    solve += 'U '
        if green[0][2] == green[1][1] and white[2][2] == red[1][1] and red[0][0] == yellow[1][1]:
            if green[0][1] == green[1][1] and white[2][1] == red[1][1]:
                Y(); U1(); L1(); U(); L()
                yy = 1
                solve += "y U' L' U L "
            elif green[0][1] == red[1][1] and white[2][1] == green[1][1]:
                if red[1][2] == red[1][1] and red[2][2] == red[1][1] and blue[1][0] == blue[1][1] and blue[2][0]== blue[1][1] and yellow[2][2] == yellow[1][1]:
                    R1(); U(); U(); R(); R(); U(); R(); R(); U(); R()
                    solve += "R' U2 R2 U R2 U R "
                else:
                    R1(); U(); U(); R(); R(); U(); R1()
                    solve += "R' U2 R2 U R' "
            elif white[1][0] == green[1][1] and orange[0][1] == red[1][1]:
                U1(); R(); U(); R1(); U(); R(); U(); R1()
                solve += "U' R U R' U R U R' "
            elif white[1][0] == red[1][1] and orange[0][1] == green[1][1]:
                Y(); U(); L1(); U1(); L(); U(); U(); L1(); U(); L()
                yy = 1
                solve += "y U L' U' L U2 L' U L "
            elif white[0][1] == green[1][1] and blue[0][1] == red[1][1]:
                R(); U(); R1()
                solve += "R U R' "
            elif white[0][1] == red[1][1] and blue[0][1] == green[1][1]:
                Y(); U(); L1(); U(); U(); L(); U(); U(); L1(); U(); L()
                yy = 1
                solve += "y U L' U2 L U2 L' U L "
            elif white[1][2] == red[1][1] and red[0][1] == green[1][1]:
                R(); U1(); R1(); U(); U(); F1(); U1(); F()
                solve += "R U' R' U2 F' U' F "
            elif white[1][2] == green[1][1] and red[0][1] == red[1][1]:
                U1(); R(); U1(); R1(); U(); R(); U(); R1()
                solve += "U' R U' R' U R U R' "
            elif green[1][2] == red[1][1] and red[1][0] == green[1][1]:
                U(); F1(); U1(); F(); U1(); R(); U(); R1()
                solve += "U F' U' F U' R U R' "
            elif green[1][2] == green[1][1] and red[1][0] == red[1][1]:
                U(); R(); U(); R1(); U(); U(); R(); U(); R1()
                solve += "U R U R' U2 R U R' "

        elif white[2][2] == green[1][1] and green[0][2] == yellow[1][1] and red[0][0] == red[1][1]:
            if white[2][1] == red[1][1] and green[0][1] == green[1][1]:
                Y(); U(); L1(); U(); L(); U1(); L1(); U1(); L()
                yy = 1
                solve += "y U L' U L U' L' U' L "
            elif white[2][1] == green[1][1] and green[0][1] == red[1][1]:
                R(); U(); R1(); U(); U(); R(); U1(); R1(); U(); R(); U1(); R1()
                solve += "R U R' U2 R U' R' U R U' R' "
            elif white[1][0] == green[1][1] and orange[0][1] == red[1][1]:
                U1(); R(); U(); U(); R1(); U(); U(); R(); U1(); R1()
                solve += "U' R U2 R' U2 R U' R' "
            elif white[1][0] == red[1][1] and orange[0][1] == green[1][1]:
                F1(); U1(); F()
                solve += "F' U' F "
            elif white[0][1] == green[1][1] and blue[0][1] == red[1][1]:
                U1(); R(); U(); R1(); U(); U(); R(); U1(); R1()
                solve += "U' R U R' U2 R U' R' "
            elif white[0][1] == red[1][1] and blue[0][1] == green[1][1]:
                U1(); R(); U1(); R1(); U(); F1(); U1(); F()
                solve += "U' R U' R' U F' U' F "
            elif white[1][2] == red[1][1] and red[0][1] == green[1][1]:
                U1(); R(); U(); U(); R1(); U(); F1(); U1(); F()
                solve += "U' R U2 R' U F' U' F "
            elif white[1][2] == green[1][1] and red[0][1] == red[1][1]:
                U(); R(); U1(); R1()
                solve += "U R U' R' "
            elif green[1][2] == red[1][1] and red[1][0] == green[1][1]:
                U1(); R(); U(); R1(); U(); F1(); U1(); F()
                solve += "U' R U R' U F' U' F "
            elif green[1][2] == green[1][1] and red[1][0] == red[1][1]:
                U1(); R(); U1(); R1(); U(); U(); R(); U1(); R1()
                solve += "U' R U' R' U2 R U' R' "

        elif white[2][2] == yellow[1][1] and green[0][2] == red[1][1] and red[0][0] == green[1][1]:
            if green[0][1] == green[1][1] and white[2][1] == red[1][1]:
                Y(); L1(); U(); U(); L(); U(); L1(); U1(); L()
                yy = 1
                solve += "y L' U2 L U L' U' L "
            elif green[0][1] == red[1][1] and white[2][1] == green[1][1]:
                U(); R(); U1(); R1(); U1(); R(); U1(); R1(); U(); R(); U1(); R1()
                solve += "U R U' R' U' R U' R' U R U' R' "
            elif white[1][0] == green[1][1] and orange[0][1] == red[1][1]:
                U(); U(); R(); U(); R1(); U(); R(); U1(); R1()
                solve += "U2 R U R' U R U' R' "
            elif white[1][0] == red[1][1] and orange[0][1] == green[1][1]:
                Y(); U1(); L1(); U(); U(); L(); U1(); L1(); U(); L()
                yy = 1
                solve += "y U' L' U2 L U' L' U L  "
            elif white[0][1] == green[1][1] and blue[0][1] == red[1][1]:
                U(); R(); U(); U(); R1(); U(); R(); U1(); R1()
                solve += "U R U2 R' U R U' R' "
            elif white[0][1] == red[1][1] and blue[0][1] == green[1][1]:
                Y(); U(); U(); L1(); U1(); L(); U1(); L1(); U(); L()
                yy = 1
                solve += "y U2 L' U' L U' L' U L "
            elif white[1][2] == red[1][1] and red[0][1] == green[1][1]:
                F(); U(); R(); U1(); R1(); F1(); R(); U1(); R1()
                solve += "F U R U' R' F' R U' R' "
            elif white[1][2] == green[1][1] and red[0][1] == red[1][1]:
                R(); U(); U(); R1(); U1(); R(); U(); R1()
                solve += "R U2 R' U' R U R' "
            elif green[1][2] == green[1][1] and red[1][0] == red[1][1]:
                R(); U(); R1(); U1(); R(); U(); R1(); U1(); R(); U(); R1()
                solve += "R U R' U' R U R' U' R U R' "
            elif green[1][2] == red[1][1] and red[1][0] == green[1][1]:
                R(); U1(); R1(); U(); Y(); L1(); U(); L()
                yy = 1
                solve += "R U' R' U y L' U L"
        elif yellow[0][2] == yellow[1][1] and green[2][2] == green[1][1] and red[2][0] == red[1][1]:
            if white[2][1] == green[1][1] and green[0][1] == red[1][1]:
                Y(); U(); U(); L1(); U(); L(); F1(); L(); F(); L1()
                yy = 1
                solve += "y U2 L' U L F' L F L' "
            elif white[2][1] == red[1][1] and green[0][1] == green[1][1]:
                U(); R(); U1(); R1(); U1(); Y(); L1(); U(); L()
                yy = 1
                solve += "U R U' R' U' y L' U L "
            elif green[1][2] == red[1][1] and red[1][0] == green[1][1]:
                R(); U1(); R1(); U(); Y(); L1(); U(); U(); L(); U(); U(); L1(); U(); L()
                yy = 1
                solve += "R U' R' U y L' U2 L U2 L' U L "
        elif green[2][2] == red[1][1] and yellow[0][2] == green[1][1] and red[2][0] == yellow[1][1]:
            if white[2][1] == green[1][1] and green[0][1] == red[1][1]:
                U1(); R(); U(); R1(); U1(); R(); U(); R1()
                solve += "U' R U R' U' R U R' "
            elif white[2][1] == red[1][1] and green[0][1] == green[1][1]:
                R(); U(); R1(); U(); U(); Y(); L1(); U(); L()
                yy = 1
                solve += "R U R' U2 y L' U L "
            elif green[1][2] == green[1][1] and red[1][0]  == red[1][1]:
                R(); U1(); R1(); U(); R(); U(); U(); R1(); U(); R(); U1(); R1()
                solve += "R U' R' U R U2 R' U R U' R' "
            elif green[1][2] == red[1][1] and red[1][0]  == green[1][1]:
                R(); U(); R1(); U1(); R(); U1(); R1(); U(); U(); F1(); U1(); F()
                solve += "R U R' U' R U' R' U2 F' U' F "
        elif green[2][2] == yellow[1][1] and yellow[0][2] == red[1][1] and red [2][0] == green[1][1]:
            if white[2][1] == green[1][1] and green[0][1] == red[1][1]:
                U1(); R(); U1(); R1(); U(); R(); U1(); R1()
                solve += "U' R U' R' U R U' R' "
            elif white[2][1] == red[1][1] and green[0][1] == green[1][1]:
                R1(); F(); R(); F1(); U(); R(); U1(); R1()
                solve += "R' F R F' U R U' R' "
            elif green[1][2] == green[1][1] and red[1][0]  == red[1][1]:
                R(); U1(); R1(); U1(); R(); U(); R1(); U(); U(); R(); U1(); R1()
                solve += "R U' R' U' R U R' U2 R U' R' "
            elif green[1][2] == red[1][1] and red[1][0] == green[1][1]:
                R(); U1(); R1(); U1(); R(); U1(); R1(); U(); F1(); U1(); F()
                solve += "R U' R' U' R U' R' U F' U' F "



        solve = solve.replace("R R' ", "")
        solve = solve.replace("R' R ", "")
        solve = solve.replace("U U' ", '')
        solve = solve.replace("U' U ", "")
        solve = solve.replace("L L' ", "")
        solve = solve.replace("U U U U ", "")
        solve = solve.replace("U U U ", "U' ")
        solve = solve.replace("U U ", 'U2 ')
        solve = solve.replace("U' U' ", 'U2 ')
        solve = solve.replace("U' U2 ", "U ")
        solve = solve.replace("U U2 ", "U' ")
        solve = solve.replace("U2 U' ", "U ")
        solve = solve.replace("U y U' ", 'y ')
        solve = solve.replace("U' y U ", 'y ')
        solve = solve.replace("U' y U' ", 'y U2 ')
        solve = solve.replace("U y U ", 'y U2 ')
        solve = solve.replace("U2 U2 ", '')
        solve = solve.replace("U2 y U2 ", 'y ')
        solve = solve.replace("U2 y U ", "y U' ")
        solve = solve.replace("U y U2 ", "y U' ")
        solve = solve.replace('y y ', 'y2 ')
        solve = solve.replace("R R ", "R2 ")
        solve = solve.replace("L L ", "L2 ")
        solve = solve.replace("R2 R ", "R' ")
        solve = solve.replace("R R2 ", "R' ")

        if i == 0:
            text = font.render('1 pair: ' + solve, True, colorblack)
            screen.blit(text, [500, 180])
        elif i == 1:
            text = font.render('2 pair: ' + solve, True, colorblack)
            screen.blit(text, [500, 210])
        elif i == 2:
            text = font.render('3 pair: ' + solve, True, colorblack)
            screen.blit(text, [500, 240])
        elif i == 3:
            text = font.render('4 pair: ' + solve, True, colorblack)
            screen.blit(text, [500, 270])
        if yy == 0:
            solve = 'y '
            if i != 3:
                Y()
        else: solve = ''

def OLL():
    solve = ''
    while white[0][0] != white[1][1] or white[0][1] != white[1][1] or white[0][2] != white[1][1] or white[1][0] != white[1][1] or white[1][2] != white[1][1] or white[2][0] != white[1][1] or white[2][1] != white[1][1] or white[2][2] != white[1][1]:
        #Глаза
        if white[0][1] == white[1][0] == white[1][2] == white[2][0] == white[2][1] == white[2][2] == blue[0][0] == blue[0][2] == white[1][1]:
            R(); R(); D1(); R(); U(); U(); R1(); D(); R(); U(); U(); R()
            solve += "R2 D' R U2 R' D R U2 R "
        #Уши
        elif white[0][1] == white[1][0] == white[1][2] == white[2][0] == white[2][1] == white[2][2] == orange[0][0] == red[0][2] == white[1][1] == white[1][1]:
            R1(); F1(); R(); U(); R1(); U1(); R1(); F(); R(); U(); R()
            solve += "R' F' R U R' U' R' F R U R "
        #Восьмёрка
        elif white[0][0] == white[0][1] == white[1][0] == white[1][2] == white[2][1] == white[2][2] == green[0][0] == red[0][2] == white[1][1]:
            R1(); F(); R(); U(); R1(); U1(); R(); F1(); R(); U(); R()
            solve += "R' F R U R' U' R' F' R U R "
        #Двойные глаза
        elif white[0][1] == white[1][2] == white[1][0] == white[2][1] == green[0][0] == green[0][2] == blue[0][0] == blue[0][2] == white[1][1]:
            R(); U(); U(); R1(); U1(); R(); U(); R1(); U1(); R(); U1(); R1()
            solve += "R U2 R' U' R U R' U' R U' R' "
        #Вертолёт
        elif white[0][1] == white[1][2] == white[1][0] == white[2][1] == green[0][2] == blue[0][0] == orange[0][0] == orange[0][2] == white[1][1]:
            R(); U(); U(); R(); R(); U1(); R(); R(); U1(); R(); R(); U(); U(); R()
            solve += "R U2 R2 U' R2 U' R2 U2 R "
        #Рыбка (прямая)
        elif white[0][1] == white[1][2] == white[1][0] == white[2][0] == white[2][1] == green[0][2] == red[0][2] == blue[0][2] == white[1][1]:
            R(); U(); R1(); U(); R(); U(); U(); R1()
            solve += "R U R' U R U2 R' "
        #Рыбка (обратная)
        elif white[0][1] == white[0][2] == white[1][0] == white[1][2] == white[2][1] == green[0][0] == orange[0][0] == red[0][0] == white[1][1]:
            R(); U(); U(); R1(); U1(); R(); U1(); R1()
            solve += "R U2 R' U' R U' R' "
        #Точка (3 на 2 сторонах)
        elif orange[0][0] == orange[0][1] == orange[0][2] == green[0][1] == blue[0][1] == red[0][0] == red[0][1] == red[0][2] == white[1][1]:
            R(); U(); U(); R(); R(); F(); R(); F1(); U(); U(); R1(); F(); R(); F1()
            solve += "R U2 R2 F R F' U2 R' F R F' "
        #Точка (3 на 1 стороне)
        elif orange[0][0] == orange[0][1] == orange[0][2] == green[0][1] == blue[0][1] == green[0][2] == red[0][1] == blue[0][0] == white[1][1]:
            F(); R(); U(); R1(); U1(); Fw(); F1(); R(); U(); R1(); U1(); Fw1()
            solve += "F R U R' U' S R U R' U' Fw' "
        #Запятая (левая)
        elif white[2][0] == green[0][1] == green[0][2] == red[0][1] == red[0][2] == blue[0][1] == blue[0][2] == orange[0][1] == white[1][1]:
            Rw1(); R(); R(); U(); R1(); U(); Rw(); U(); U(); Rw1(); U(); R1(); Rw
            solve += "Rw' R2 U R' U Rw U2 Rw' U R' Rw "
        #Запятая (правая)
        elif white[2][2] == green[0][1] == green[0][0] == red[0][1] == blue[0][1] == blue[0][0] == orange[0][1] == orange[0][0] == white[1][1]:
            Rw1(); R(); U1(); Rw(); U(); U(); Rw1(); U1(); R(); U1(); R(); R(); Rw()
            solve += "Rw' R U' Rw U2 Rw' U' R U' R2 Rw "
        #Микки Маус
        elif white[0][0] == white[0][2] == green[0][1] == red[0][0] == red[0][1] == blue[0][1] == orange[0][1] == orange[0][2] == white[1][1]:
            Rw1(); R(); U(); R(); U(); R1(); U1(); M1(); R1(); F(); R(); F1()
            solve += "Rw' R U R U R' U' M' R' F R F' "
        #Микки Маус (с 3 на 1 стороне)
        elif white[0][0] == white[0][2] == green[0][1] == green[0][0] == red[0][1] == blue[0][1] == orange[0][1] == green[0][2] == white[1][1]:
            Rw(); U(); R1(); U(); R(); U(); U(); Rw(); Rw(); U1(); R(); U1(); R1(); U(); U(); Rw()
            solve += "Rw U R' U R U2 Rw2 U' R U' R' U2 Rw "
        #Диагоняль
        elif white[0][0] == white[2][2] == green[0][1] == blue[0][0] == red[0][1] == blue[0][1] == orange[0][1] == orange[0][2] == white[1][1]:
            R(); U(); R1(); U(); R1(); F(); R(); F1(); U(); U(); R1(); F(); R(); F1()
            solve += "R U R' U R' F R F' U2 R' F R F' "
        #Снежинка
        elif white[0][0] == white[2][2] == white[0][2] == white[2][0] == green[0][1] == red[0][1] == blue[0][1] == orange[0][1] == white[1][1]:
            Rw1(); R(); U(); R(); U(); R1(); U1(); M(); M(); U();R(); U1(); Rw1()
            solve += "Rw' R U R U R' U' M2 U R U' Rw' "
        #Н-ка
        elif white[0][0] == white[2][2] == white[0][2] == white[2][0] == white[1][0] == white[1][2] == green[0][1] == blue[0][1] == white[1][1]:
            R(); U(); R1(); U1(); M1(); U(); R(); U1(); Rw1()
            solve += "R U R' U' M' U R U' Rw' "
        #Змей
        elif white[0][0] == white[2][2] == white[0][2] == white[2][0] == white[1][0] == white[0][1] == green[0][1] == red[0][1] == white[1][1]:
            Rw(); U(); R1(); U1(); M(); U(); R(); U1(); R1()
            solve += "Rw U R' U' M U R U' R' "
        #Палка (через пиф-паф)
        elif white[1][0] == white[1][2] == green[0][0] == green[0][1] == red[0][0] == red[0][2] == blue[0][1] == blue[0][2] == white[1][1]:
            F(); U(); R(); U1(); R1(); U(); R(); U1(); R1(); F1()
            solve += "F U R U' R' U R U' R' F' "
        #Палка (3 на 1 стороне)
        elif white[1][0] == white[1][2] == green[0][1] == red[0][0] == blue[0][0] == blue[0][1] == blue[0][2] == orange[0][2] == white[1][1]:
            F(); R(); U(); R1(); U(); Y1(); R1(); U1(); R(); U1(); R1()
            solve += "F R U R' U y' R' U' R U' R' "
        #Палка (нет 3-к)
        elif white[1][0] == white[1][2] == green[0][1] == red[0][0] == red[0][2] == blue[0][1] == orange[0][0] == orange[0][2] == white[1][1]:
            Rw1(); U1(); Rw(); U1(); R1(); U(); R(); U1(); R1(); U(); R(); Rw1(); U(); Rw()
            solve += "Rw' U' Rw U' R' U R U' R' U R Rw' U Rw "
        #Палка (3 на 2 сторонах)
        elif white[1][0] == white[1][2] == green[0][1] == green[0][0] == blue[0][0] == blue[0][1] == blue[0][2] == green[0][2] == white[1][1]:
            R1(); F(); R(); U(); R(); U1(); R(); R(); F1(); R(); R(); U1(); R1(); U(); R(); U(); R1()
            solve += "R' F R U R U' R2 F' R2 U' R' U R U R' "
        #Г-шка (через пиф-паф, правая)
        elif white[0][2] == white[1][0] == white[1][2] == green[0][0] == green[0][1] == red[0][0] == blue[0][1] == orange[0][0] == white[1][1]:
            Rw(); U(); Rw1(); R(); U(); R1(); U1(); Rw(); U1(); Rw1()
            solve += "Rw U Rw' R U R' U' Rw U' Rw' "
        #Г-шка (через пиф-паф, левая)
        elif white[0][0] == white[1][0] == white[1][2] == green[0][2] == green[0][1] == red[0][2] == blue[0][1] == orange[0][2] == white[1][1]:
            Lw1(); U1(); Lw(); L1(); U1(); L; U; R1(); F(); R()
            solve += "Lw' U' Lw L' U' L U R' F R "
        #Г-шка (правая)
        elif white[1][0] == white[1][2] == white[2][0] == green[0][1] == green[0][2] == red[0][2] == blue[0][1] == blue[0][2] == white[1][1]:
            Rw(); U1(); Rw1(); U1(); Rw(); U(); Rw1(); F1(); U(); F()
            solve += "Rw U' Rw' U' Rw U Rw' F' U F "
        #Г-шка (левая)
        elif white[1][0] == white[1][2] == white[0][0] == green[0][1] == green[0][0] == red[0][0] == blue[0][1] == blue[0][0] == white[1][1]:
            Rw1(); U(); Rw(); U(); Rw1(); U1(); Rw(); B(); U1(); B1()
            solve += "Rw' U Rw U Rw' U' Rw B U' B' "
        #Т-шка (1)
        elif white[1][0] == white[1][2] == white[0][2] == white[2][2] == green[0][1] == blue[0][1] == orange[0][0] == orange[0][2] == white[1][1]:
            F(); R(); U(); R1(); U1(); F1()
            solve += "F R U R' U' F' "
        #Т-шка (2)
        elif white[1][0] == white[1][2] == white[0][2] == white[2][2] == green[0][0] == green[0][1] == blue[0][1] == blue[0][2] == white[1][1]:
            R(); U(); R1(); U1(); R1(); F(); R(); F1()
            solve += "R U R' U' R' F R F' "
        #Скобка
        elif white[1][0] == white[1][2] == white[2][0] == white[2][2] == green[0][1] == red[0][2] == blue[0][1] == orange[0][0] == white[1][1]:
            R(); U(); R(); R(); U1(); R1(); F(); R(); U(); R(); U1(); F1()
            solve += "R U R2 U' R' F R U R U' F' "
        #Скобка (с 3 на стороне)
        elif white[0][1] == white[2][1] == white[0][0] == white[2][0] == red[0][0] == red[0][1] == red[0][2] == orange[0][1] == white[1][1]:
            R1(); U1(); R1(); F(); R(); F1(); U(); R()
            solve += "R' U' R' F R F' U R "
        #Пропеллер (через F)
        elif white[0][0] == white[1][1]  and white[1][0] == white[1][2] == white[2][2] == green[0][1] == blue[0][0] == blue[0][1] == orange[0][2]  == white[1][1]:
            R1(); F(); R(); U(); R1(); U1(); F1(); U(); R()
            solve += "R' F R U R' U' F' U R "
        #Пропеллер (через Ь)
        elif white[0][2] == white[1][0] == white[1][2] == white[2][0] == green[0][1] == red[0][0] == blue[0][1] == blue[0][2] == white[1][1]:
            R(); U(); U(); R1(); U1(); R(); U1(); R1(); F(); U(); R(); U1(); R1(); F1()
            solve += "R U2 R' U' R U' R' F U R U' R' F'  "
        #Стелс (через правый пиф-паф)
        elif white[0][1] == white[1][0] == green[0][1] == green[0][2] == red[0][1] == blue[0][0] == orange[0][0] == orange[0][2] == white[1][1]:
            F(); R(); U(); R1(); U1(); R(); U(); R1(); U1(); F1()
            solve += "F R U R' U' R U R' U' F' "
        #Стелс (через левый пиф-паф)
        elif white[0][1] == white[1][2] == green[0][0] == green[0][1] == red[0][0] == red[0][2] == blue[0][2] == orange[0][1] == white[1][1]:
            F1(); L1(); U1(); L(); U(); L1(); U1(); L(); U(); F()
            solve += "F' L' U' L U L' U' L U F "
        #Стелс (3 на 1 стороне и глаза, правый)
        elif white[0][1] == white[1][2] == green[0][1] == red[0][0] == red[0][2] == orange[0][0] == orange[0][1] == orange[0][2] == white[1][1]:
            Rw(); U(); R1(); U(); R(); U1(); R1(); U(); R(); U(); U(); Rw1()
            solve += "Rw U R' U R U' R' U R U2 Rw' "
        #Стелс(3 на 1 стороне и глаза. левый)
        elif white[1][2] == white[2][1] == red[0][0] == red[0][2] == blue[0][1] == orange[0][0] == orange[0][1] == orange[0][2] == white[1][1]:
            Rw1(); U1(); R(); U1(); R1(); U(); R(); U1(); R1(); U(); U(); Rw()
            solve += "Rw' U' R U' R' U R U' R' U2 Rw "
        #Стелс (3 на 1 стороне 2 на др, правый)
        elif white[0][1] == white[1][2] == green[0][1] == green[0][2] == blue[0][0] == orange[0][0] == orange[0][1] == orange[0][2] == white[1][1]:
            Rw(); U1(); Rw(); Rw(); U(); Rw(); Rw(); U(); Rw(); Rw(); U1(); Rw()
            solve += "Rw U' Rw2 U Rw2 U Rw2 U' Rw "
        #Стелс (3 на 1 стороне 2 на др, левый)
        elif white[2][1] == white[1][2] == blue[0][0] == blue[0][1] == green[0][2] == orange[0][0] == orange[0][1] == orange[0][2] == white[1][1]:
            Rw1(); U(); Rw(); Rw(); U1(); Rw(); Rw(); U1(); Rw(); Rw(); U(); Rw1()
            solve += "Rw' U Rw2 U' Rw2 U' Rw2 U Rw' "
        #Квадрат (правый)
        elif white[0][1] == white[0][2] == white[1][2] == green[0][0] == green[0][1] == red[0][0] == orange[0][0] == orange[0][1] == white[1][1]:
            Rw(); U(); U(); R1(); U1(); R(); U1(); Rw1()
            solve += "Rw U2 R' U' R U' Rw' "
        #Квадрат (левый)
        elif white[2][1] == white[2][2] == white[1][2] == blue[0][2] == blue[0][1] == red[0][2] == orange[0][2] == orange[0][1] == white[1][1]:
            Rw1(); U(); U(); R(); U(); R1(); U(); Rw()
            solve += "Rw' U2 R U R' U Rw "
        #Рюмка (правая)
        elif white[0][1] == white[2][0] == white[1][2] == green[0][2] == green[0][1] == red[0][2] == blue[0][2] == orange[0][1] == white[1][1]:
            Rw(); U(); R1(); U(); R(); U1(); R1(); U1(); M(); U(); R(); U1(); R1();
            solve += "Rw U R' U R U' R' U' M U R U' R' "
        #Рюмка (левая)
        elif white[0][1] == white[2][2] == white[1][0] == green[0][0] == green[0][1] == red[0][1] == blue[0][0] == orange[0][0] == white[1][1]:
            R(); U(); R1(); U1(); R1(); F(); R(); R(); U(); R1(); U1(); F1()
            solve += "R U R' U' R' F R2 U R' U' F' "
        #Молния (через Rw)
        elif white[0][1] == white[2][0] == white[1][0] == green[0][2] == green[0][1] == red[0][1] == red[0][2] == blue[0][2] == white[1][1]:
            Rw(); U(); R1(); U(); R(); U(); U(); Rw1()
            solve += "Rw U R' U R U2 Rw' "
        #Молния (через F)
        elif white[0][1] == white[2][2] == white[1][2] == green[0][0] == green[0][1] == orange[0][0] == orange[0][1] == blue[0][0] == white[1][1]:
            R(); U(); U(); R1(); U(); U(); R1(); F(); R(); F1()
            solve += "R U2 R' U2 R' F R F' "
        #Молния (через М ,правая)
        elif white[2][1] == white[2][2] == white[1][0] == green[0][0] == red[0][1] == orange[0][0] == blue[0][1] == blue[0][0] == white[1][1]:
            M(); U(); U(); R1(); U1(); R(); U1(); R1(); U(); U(); R(); U(); M1()
            solve += "M U2 R' U' R U' R' U2 R U M' "
        #Молния (через М, левая)
        elif white[0][1] == white[0][2] == white[1][0] == green[0][1] == red[0][1] == orange[0][2] == green[0][2] == blue[0][2] == white[1][1]:
            M1(); U(); U(); R(); U(); R1(); U(); R(); U(); U(); R1(); U1(); M()
            solve += "M' U2 R U R' U R U2 R' U' M "
        #Мягкий знак (левый через пиф-паф)
        elif white[1][0] == white[2][0] == white[2][1] == white[0][0] == red[0][0] == red[0][1] == red[0][2] == blue[0][1] == white[1][1]:
            Fw1(); L1(); U1(); U1(); L(); U(); Fw()
            solve += "Fw' L' U' L U Fw "
        #Мягкий знак (правй через пиф-паф
        elif white[1][2] == white[2][2] == white[2][1] == white[0][2] == orange[0][0] == orange[0][1] == orange[0][2] == blue[0][1] == white[1][1]:
            Fw(); R(); U(); R1(); U1(); Fw1()
            solve += "Fw R U R' U' Fw' "
        #Мягкий знак через F
        elif white[0][0] == white[1][0] == white[2][0] == white[2][1] == green[0][2] == red[0][1] == blue[0][0] == blue[0][1] == white[1][1]:
            R1(); F(); R(); U(); R1(); U1(); F(); F(); U(); F(); R()
            solve += "R' F R U R' U' F2 U F R "
        #Мягкий знак через S
        elif white[0][2] == white[1][2] == white[2][2] == white[2][1] == green[0][0] == orange[0][1] == blue[0][2] == blue[0][1] == white[1][1]:
            Fw(); F1(); R(); U(); R1(); U1(); R1(); F(); R(); Fw()
            solve += "S R U R' U' R' F R Fw' "
        #М-ка (левая)
        elif white[0][1] == white[0][2] == white[1][0] == white[2][0] == green[0][1] == red[0][0] == blue[0][2] == red[0][1] == white[1][1]:
            R(); U(); R1(); U(); R(); U1(); R1(); U1();  R1(); F(); R(); F()
            solve += "R U R' U R U' R' U' R' F R F' "
        #М-ка (правая)
        elif white[0][0] == white[0][1] == white[1][2] == white[2][2] == green[0][1] == blue[0][0] == orange[0][2] == orange[0][1] == white[1][1]:
            L1(); U1(); L(); U1(); L1();  U(); L(); U(); L(); F1(); L1(); F()
            solve += "L' U' L U' L' U L U L F' L' F "
        #Галстук  (через R U2)
        elif white[2][1] == white[2][2] == white[1][2] == white[0][0] == blue[0][1] == red[0][2] == orange[0][1] == green[0][0] == white[1][1]:
            R(); U(); U(); R(); R(); F(); R(); F1(); R(); U(); U(); R1()
            solve += "R U2 R2 F R F' R U2 R' "
        #Галстук (обр Т)
        elif white[0][0] == white[0][1] == white[1][0] == white[2][2] == green[0][0] == green[0][1] == red[0][1] == red[0][2] == white[1][1]:
            F(); R(); U1(); R1(); U1(); R(); U(); R1(); F1()
            solve += "F R U' R' U' R U R' F' "
        #Петух (глаза сзади)
        elif white[2][0] == white[0][1] == white[1][0] == white[2][2] == green[0][1] == red[0][1] == blue[0][0] == blue[0][2] == white[1][1]:
            R(); U(); R1(); U(); R(); U(); U(); R1(); F(); R(); U(); R1(); U1(); F1()
            solve += "R U R' U R U2 R' F R U R' U' F' "
        #Петух (глаза спереди)
        elif white[0][0] == white[0][2] == white[1][0] == white[2][1] == green[0][0] == green[0][2] == red[0][1] == blue[0][1] == white[1][1]:
            R1(); U1(); R(); U1(); R1(); U(); U(); R(); F(); R(); U(); R1(); U1(); F1()
            solve += "R' U' R U' R' U2 R F R U R' U' F' "
        #Петух (без глаз через F)
        elif white[2][0] == white[0][1] == white[1][0] == white[2][2] == green[0][1] == red[0][1] == red[0][2] == orange[0][0] == white[1][1]:
            F(); R1(); F(); R(); R(); U1(); R1(); U1(); R(); U(); R1(); F(); F()
            solve += "F R' F R2 U' R' U' R U R' F2 "
        #Петух (без глаз через R U)
        elif white[0][1] == white[0][2] == white[1][0] == white[2][2] == green[0][0] == green[0][1] == red[0][1] == blue[0][2] == white[1][1]:
            R(); U(); R1(); U1(); R(); U1(); R1(); F1(); U1(); F(); R(); U(); R1()
            solve += "R U R' U' R U' R' F' U' F R U R' "
        else:
            U()
            solve += 'U '
    solve = solve.replace("U U U ", "U' ")
    solve = solve.replace("U U ", "U2 ")
    if solve == '':
        solve = 'skip'
    text = font.render('OLL: ' + solve, True, colorblack)
    screen.blit(text, [500, 300])

def PLL():
    solve = ''
    while green[0][0] != green[1][1] or green[0][1] != green[1][1] or green[0][2] != green[1][1] or red[0][0] != red[1][1] or red[0][1] != red[1][1] or red[0][2] != red[1][1] or blue[0][0] != blue[1][1] or blue[0][1] != blue[1][1] or blue[0][2] != blue[1][1] or orange[0][0] != orange[1][1] or orange[0][1] != orange[1][1] or orange[0][2] != orange[1][1]:
        #Треугольник углов (глаза сзади)
        if green[0][0] == green[0][1] and orange[0][1] == orange[0][2] and  blue[0][0] == blue[0][2] and green[0][2] == orange[0][0]:
            Lw1(); U(); R1(); D(); D(); R(); U1(); R1(); D(); D(); R(); R(); Lw(); R1()
            solve += "Lw' U R' D2 R U' R' D2 R2 x' "
        #Треугольник углов (глаза справа)
        elif green[0][0] == green[0][1] and orange[0][1] == orange[0][2] and red[0][0] == red[0][2] and green[0][2] == orange[0][0]:
            Lw1(); R1(); D(); D(); R(); U(); R1(); D(); D(); R(); U1(); R(); Lw(); R1()
            solve += "x R2 D2 R U R' D2 R U' R x' "
        #Терминатор
        elif green[0][0] == blue[0][2] == orange[0][1] and green[0][2] == blue[0][0] == red[0][1]:
            Lw(); R1(); R(); U1(); R1(); D(); R(); U(); R1(); D1(); R(); U(); R1(); D(); R(); U1(); R1(); D1(); Lw1(); R();
            solve += "x' R U' R' D R U R' D' R U R' D R U' R' D' x "
        #Саночки
        elif green[0][0] == green[0][2] == orange[0][1] and orange[0][0] == orange[0][2] == green[0][1]:
            M(); M(); U1(); M(); M(); U1(); M1(); U(); U(); M(); M(); U(); U(); M1(); U(); U()
            solve += "M2 U' M2 U' M' U2 M2 U2 M' U2 "
        #Крест сторон
        elif green[0][0] == green[0][2] == blue[0][1] and blue[0][0] == blue[0][2] == green[0][1]:
            M(); M(); U1(); M(); M(); U(); U(); M(); M(); U1(); M(); M()
            solve += "M2 U' M2 U2 M2 U' M2 "
        #Теугольник сторон (правый)
        elif blue[0][0] == blue[0][1] == blue[0][2] and orange[0][0] == orange[0][2] == red[0][1]:
            M(); M(); U(); M(); U(); U(); M1(); U(); M(); M()
            solve += "M2 U M U2 M' U M2 "
        #Треугольник сторон (левый)
        elif blue[0][0] == blue[0][1] == blue[0][2] and red[0][0] == red[0][2] == orange[0][1]:
            M(); M(); U1(); M(); U(); U(); M1(); U1(); M(); M()
            solve += "M2 U' M U2 M' U' M2 "
        #Лямбда (прямая)
        elif orange[0][0] == orange[0][1] == orange[0][2] and green[0][1] == green[0][2] == blue[0][0]:
            R(); U(); R1(); F1(); R(); U(); R1(); U1(); R1(); F(); R(); R(); U1(); R1(); U1()
            solve +=  "R U R' F' R U R' U' R' F R2 U' R' U' "
        #Лямбда (обратная)
        elif orange[0][0] == orange[0][1] == orange[0][2] and green[0][0] == green[0][1] == red[0][2]:
            R1(); U(); U(); R(); U(); R1(); U(); U(); L(); U1(); R(); U(); L1()
            solve += "R' U2 R U R' U2 L U' R U L' "
        #Семёрка (глаза спереди)
        elif green[0][0] == green[0][2] == red[0][1] and orange[0][1] == orange[0][2] == blue[0][0]:
            R1(); U(); U(); R(); U(); U(); R1(); F(); R(); U(); R1(); U1(); R1(); F1(); R(); R(); U1()
            solve += "R' U2 R U2 R' F R U R' U' R' F' R2 U' "
        #Семёрка (глаза справа)
        elif green[0][0] == green[0][1] == red[0][2] and orange[0][0] == orange[0][2] == blue[0][1]:
            R(); U(); R1(); F1(); R(); U(); U(); R1(); U(); U(); R1(); F(); R(); U(); R(); U(); U(); R1(); U1()
            solve += "R U R' F' R U2 R' U2 R' F R U R U2 R' U' "
        #Т-шка
        elif green[0][0] == green[0][1] and blue[0][1] == blue[0][2] and orange[0][0] == orange[0][2] and orange[0][1] == green[0][2]:
            R(); U(); R1(); U1(); R1(); F(); R(); R(); U1(); R1(); U1(); R(); U(); R1(); F1()
            solve += "R U R' U' R' F R2 U' R' U' R U R' F' "
        #Копьё
        elif green[0][0] == green[0][1] == blue[0][2] and red[0][1] == red[0][2] == orange[0][0]:
            F(); R(); U1(); R1(); U1(); R(); U(); R1(); F1(); R(); U(); R1(); U1(); R1(); F(); R(); F1()
            solve += "F R U' R' U' R U R' F' R U R' U' R' F R F' "
        #Параллельный перенос
        elif orange[0][0] == orange[0][1] == orange[0][2] and green[0][0] == blue[0][1] and blue[0][2] == green[0][1]:
            R1(); U1(); F1(); R(); U(); R1(); U1(); R1(); F(); R(); R(); U1(); R1(); U1(); R(); U(); R1(); U(); R()
            solve += "R' U' F' R U R' U' R' F R2 U' R' U' R U R' U R "
        #Летающая тарелка
        elif green[0][0] == green[0][1] and orange[0][1] == orange[0][2] and green[0][2] == red[0][1] != orange[0][0]:
            R1(); U(); R1(); U1(); Y(); R1(); F1(); R(); R(); U1(); R1(); U(); R1(); F(); R(); F()
            solve += "R' U R' U' y R' F' R2 U' R' U R' F R F "
        #Буква Х (правая)
        elif green[0][1] == green[0][2] == blue[0][0] and blue[0][1] == blue[0][2] == green[0][0]:
            R(); U1(); L(); U(); U(); R1(); U(); L1(); R(); U1(); L(); U(); U(); R1(); U(); L1(); U1()
            solve += "R U' L U2 R' U L' R U' L U2 R' U L' U' "
        #Буква Х (левая)
        elif green[0][1] == green[0][0] == blue[0][2] and blue[0][0] == blue[0][1] == green[0][2]:
            R1(); U(); R(); U1(); R1(); F1(); U1(); F(); R(); U(); R1(); F(); R1(); F1(); R(); U1(); R()
            solve += "R' U R U' R' F' U' F R U R' F R' F' R U' R "
        #Восьмёрка (глаза справа)
        elif green[0][0] == green[0][1] ==  blue[0][2] and red[0][0] == red[0][2] == orange[0][1]:
            R(); R(); F(); F(); R(); U(); U(); R(); U(); U(); R1(); F(); R(); U(); R1(); U1(); R1(); F(); R(); R()
            solve += "R2 F2 R U2 R U2 R' F R U R' U' R' F R2 "
        #Восьмёрка (глаза сзади)
        elif green[0][0] == green[0][1] == red[0][2] and blue[0][0] == blue[0][2] == orange[0][1]:
            R(); R(); F1(); R(); U(); R(); U1(); R1(); F1(); R(); U(); U(); R1(); U(); U(); R1(); F(); F(); R(); R()
            solve += "R2 F' R U R U' R' F' R U2 R' U2 R' F2 R2 "
        #Восьмёрка (глаза слева, 2-ка спереди)
        elif green[0][1] == green[0][2] == blue[0][0] and orange[0][0] == orange[0][2] == red[0][1]:
            D1(); R(); R(); U(); R1(); U(); R1(); U1(); R(); U1(); R(); R(); D(); U1(); R1(); U(); R()
            solve += "D' R2 U R' U R' U' R U' R2 D U' R' U R "
        #Восьмёрка (глаза слева, 2-ка справа)
        elif red[0][1] == red[0][2] == green[0][0] and orange[0][0] == orange[0][2] == blue[0][1]:
            D(); R1(); U1(); R(); U(); D1(); R(); R(); U(); R1(); U(); R(); U1(); R(); U1(); R(); R()
            solve += "D R' U' R U D' R2 U R' U R U' R U' R2 "
        else:
            U()
            solve += "U "

    solve = solve.replace("U U U ", "U' ")
    solve = solve.replace("U U ", "U2 ")
    solve = solve.replace("U' U' ", "U2 ")
    solve = solve.replace("U' U2 ", "U ")
    solve = solve.replace("U' U ", '')
    if solve == '': solve ='skip'
    text = font.render('PLL: ' + solve, True, colorblack)
    screen.blit(text, [500, 330])

def color(c):
    if c == 'З':  color = colorgreen
    elif c == 'Б': color = colorwhite
    elif c == 'С': color = colorblue
    elif c == 'Ж': color = coloryellow
    elif c == 'О': color = colororange
    elif c == 'К': color = colorred
    return color

def draw():
    a = 40
    x = 3*a
    y = 60
    for i in range(9):
        pygame.draw.rect(screen,color(white[i // 3][i % 3]),[x,y,a,a],0)
        pygame.draw.rect(screen, colorblack, [x, y, a, a], 1)
        x += a
        if (i+1)%3 == 0:
            x = 3*a
            y += a
    x = 0
    for i in range(9):
        pygame.draw.rect(screen, color(orange[i // 3][i % 3]), [x, y, a, a], 0)
        pygame.draw.rect(screen, colorblack, [x, y, a, a], 1)
        x += a
        if (i + 1) % 3 == 0:
            x = 0
            y += a
    x += 3*a
    y = 3*a + 60
    for i in range(9):
        pygame.draw.rect(screen, color(green[i // 3][i % 3]), [x, y, a, a], 0)
        pygame.draw.rect(screen, colorblack, [x, y, a, a], 1)
        x += a
        if (i + 1) % 3 == 0:
            x = 3 * a
            y += a
    x += 3*a
    y = 3*a + 60
    for i in range(9):
        pygame.draw.rect(screen, color(red[i // 3][i % 3]), [x, y, a, a], 0)
        pygame.draw.rect(screen, colorblack, [x, y, a, a], 1)
        x += a
        if (i + 1) % 3 == 0:
            x = 6 * a
            y += a
    x += 3*a
    y = 3*a + 60
    for i in range(9):
        pygame.draw.rect(screen, color(blue[i // 3][i % 3]), [x, y, a, a], 0)
        pygame.draw.rect(screen, colorblack, [x, y, a, a], 1)
        x += a
        if (i + 1) % 3 == 0:
            x = 9 * a
            y += a
    x = 3*a
    for i in range(9):
        pygame.draw.rect(screen, color(yellow[i // 3][i % 3]), [x, y, a, a], 0)
        pygame.draw.rect(screen, colorblack, [x, y, a, a], 1)
        x += a
        if (i + 1) % 3 == 0:
            x = 3 * a
            y += a

green = [['З']*3 for i in range(3)]
green2 = [['З']*3 for i in range(3)]

white = [['Б']*3 for i in range(3)]
white2 = [['Б']*3 for i in range(3)]

red = [['К']*3 for i in range(3)]
red2 = [['К']*3 for i in range(3)]

orange = [['О']*3 for i in range(3)]
orange2 = [['О']*3 for i in range(3)]

blue = [['С']*3 for i in range(3)]
blue2 = [['С']*3 for i in range(3)]

yellow = [['Ж']*3 for i in range(3)]
yellow2 = [['Ж']*3 for i in range(3)]

print("Enter the scrumble:")
scramble = input().split()
for i in range(len(scramble)):
    moves(scramble[i])

colorblack = (0,0,0)
colorwhite = (255,255,255)
colorgreen = (0,255,0)
colorred = (255,0,0)
colorblue = (0,0,255)
coloryellow = (255,255,0)
colororange = (255,165,0)

size = [1050,500]
screen = pygame.display.set_mode(size)
screen.fill(colorwhite)
font = pygame.font.Font(None,30)

text = font.render('Solution:', True, colorblack)
screen.blit(text, [500, 100])
s = ''
for i in range(len(scramble)):
    s += str(scramble[i]) + ' '
text = font.render('Scramble: ' + s, True, colorblack)
screen.blit(text, [5, 5])

draw()
cross()
F2L()
OLL()
PLL()

pygame.display.flip()
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = False
