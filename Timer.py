import pygame,random
pygame.init()

def generate_scramble():
    mass = [['R', "R'", 'R2'], ['L', "L'", 'L2'], ['U', "U'", 'U2'], ['D', "D'", 'D2'], ['F', "F'", 'F2'], ['B', "B'", 'B2']]
    s = ''
    a = random.choice(mass)
    b = []
    for i in range(20):
        a = random.choice(mass)
        while a == b:
            a = random.choice(mass)
        s += random.choice(a) + ' '
        b = a
    return s

def cube_sweep(scramble):

    def pochas(matr):
        matr2 = [['']*3 for i in range(3)]
        for i in range(3):
            for j in range(3):
                matr2[j][2-i] = matr[i][j]
        return matr2
    def protchas(matr):
        matr2 = [['']*3 for i in range(3)]
        for i in range(3):
            for j in range(3):
                matr2[2-j][i] = matr[i][j]
        return matr2

    def color(c):
        if c == 'З':
            color = (0,255,0)
        elif c == 'Б':
            color = (255,255,255)
        elif c == 'С':
            color = (0,0,255)
        elif c == 'Ж':
            color = (255,255,0)
        elif c == 'О':
            color = (255,165,0)
        elif c == 'К':
            color = (255,0,0)
        return color


    green = [['З'] * 3 for i in range(3)]
    white = [['Б'] * 3 for i in range(3)]
    red = [['К'] * 3 for i in range(3)]
    orange = [['О'] * 3 for i in range(3)]
    blue = [['С'] * 3 for i in range(3)]
    yellow = [['Ж'] * 3 for i in range(3)]

    scramble = scramble.split()

    for x in scramble:
        if x == 'R':
            for i in range(3):
                green[i][2], white[i][2], blue[2 - i][0], yellow[i][2] = yellow[i][2], green[i][2], white[i][2], \
                                                                         blue[2 - i][0]
            red = pochas(red)
        elif x == "R'":
            for i in range(3):
                green[i][2], white[i][2], blue[2 - i][0], yellow[i][2] = white[i][2], blue[2 - i][0], yellow[i][2], \
                                                                         green[i][2]
            red = protchas(red)
        elif x == 'R2':
            for j in range(2):
                for i in range(3):
                    green[i][2], white[i][2], blue[2 - i][0], yellow[i][2] = yellow[i][2], green[i][2], white[i][2], \
                                                                             blue[2 - i][0]
                red = pochas(red)
        elif x == 'L':
            for i in range(3):
                green[i][0], white[i][0], blue[2 - i][2], yellow[i][0] = white[i][0], blue[2 - i][2], yellow[i][0], \
                                                                         green[i][0]
            orange = pochas(orange)
        elif x == "L'":
            for i in range(3):
                green[i][0], white[i][0], blue[2 - i][2], yellow[i][0] = yellow[i][0], green[i][0], white[i][0], \
                                                                         blue[2 - i][2]
            orange = protchas(orange)
        elif x == 'L2':
            for j in range(2):
                for i in range(3):
                    green[i][0], white[i][0], blue[2 - i][2], yellow[i][0] = white[i][0], blue[2 - i][2], yellow[i][0], \
                                                                             green[i][0]
                orange = pochas(orange)
        elif x == 'U':
            for i in range(3):
                green[0][i], orange[0][i], blue[0][i], red[0][i] = red[0][i], green[0][i], orange[0][i], blue[0][i]
            white = pochas(white)
        elif x == "U'":
            for i in range(3):
                green[0][i], orange[0][i], blue[0][i], red[0][i] = orange[0][i], blue[0][i], red[0][i], green[0][i]
            white = protchas(white)
        elif x == 'U2':
            for j in range(2):
                for i in range(3):
                    green[0][i], orange[0][i], blue[0][i], red[0][i] = red[0][i], green[0][i], orange[0][i], blue[0][i]
                white = pochas(white)
        elif x == 'D':
            for i in range(3):
                green[2][i], orange[2][i], blue[2][i], red[2][i] = orange[2][i], blue[2][i], red[2][i], green[2][i]
            yellow = pochas(yellow)
        elif x == "D'":
            for i in range(3):
                green[2][i], orange[2][i], blue[2][i], red[2][i] = red[2][i], green[2][i], orange[2][i], blue[2][i]
            yellow = protchas(yellow)
        elif x == 'D2':
            for j in range(2):
                for i in range(3):
                    green[2][i], orange[2][i], blue[2][i], red[2][i] = orange[2][i], blue[2][i], red[2][i], green[2][i]
                yellow = pochas(yellow)
        elif x == 'F':
            for i in range(3):
                orange[i][2], white[2][2 - i], red[2 - i][0], yellow[0][i] = yellow[0][i], orange[i][2], white[2][
                    2 - i], red[2 - i][0]
            green = pochas(green)
        elif x == "F'":
            for i in range(3):
                orange[i][2], white[2][2 - i], red[2 - i][0], yellow[0][i] = white[2][2 - i], red[2 - i][0], yellow[0][
                    i], orange[i][2]
            green = protchas(green)
        elif x == 'F2':
            for j in range(2):
                for i in range(3):
                    orange[i][2], white[2][2 - i], red[2 - i][0], yellow[0][i] = yellow[0][i], orange[i][2], white[2][
                        2 - i], red[2 - i][0]
                green = pochas(green)
        elif x == 'B':
            for i in range(3):
                orange[i][0], white[0][2 - i], red[2 - i][2], yellow[2][i] = white[0][2 - i], red[2 - i][2], yellow[2][
                    i], orange[i][0]
            blue = pochas(blue)
        elif x == "B'":
            for i in range(3):
                orange[i][0], white[0][2 - i], red[2 - i][2], yellow[2][i] = yellow[2][i], orange[i][0], white[0][
                    2 - i], red[2 - i][2]
            blue = protchas(blue)
        elif x == 'B2':
            for j in range(2):
                for i in range(3):
                    orange[i][0], white[0][2 - i], red[2 - i][2], yellow[2][i] = white[0][2 - i], red[2 - i][2], \
                                                                                 yellow[2][i], orange[i][0]
                blue = pochas(blue)
    a = 25
    x0 = a
    x = 3 * a + x0
    y0 = y = 370
    for i in range(9):
        pygame.draw.rect(screen, color(white[i // 3][i % 3]), [x, y, a, a], 0)
        pygame.draw.rect(screen, (0,0,0), [x, y, a, a], 1)
        x += a
        if (i + 1) % 3 == 0:
            x = 3 * a + x0
            y += a
    x = x0
    for i in range(9):
        pygame.draw.rect(screen, color(orange[i // 3][i % 3]), [x, y, a, a], 0)
        pygame.draw.rect(screen, (0,0,0), [x, y, a, a], 1)
        x += a
        if (i + 1) % 3 == 0:
            x = x0
            y += a
    x += 3 * a
    y = 3 * a + y0
    for i in range(9):
        pygame.draw.rect(screen, color(green[i // 3][i % 3]), [x, y, a, a], 0)
        pygame.draw.rect(screen, (0,0,0), [x, y, a, a], 1)
        x += a
        if (i + 1) % 3 == 0:
            x = 3 * a + x0
            y += a
    x += 3 * a
    y = 3 * a + y0
    for i in range(9):
        pygame.draw.rect(screen, color(red[i // 3][i % 3]), [x, y, a, a], 0)
        pygame.draw.rect(screen, (0,0,0), [x, y, a, a], 1)
        x += a
        if (i + 1) % 3 == 0:
            x = 6 * a + x0
            y += a
    x += 3 * a
    y = 3 * a + y0
    for i in range(9):
        pygame.draw.rect(screen, color(blue[i // 3][i % 3]), [x, y, a, a], 0)
        pygame.draw.rect(screen, (0,0,0), [x, y, a, a], 1)
        x += a
        if (i + 1) % 3 == 0:
            x = 9 * a + x0
            y += a
    x = 3 * a + x0
    for i in range(9):
        pygame.draw.rect(screen, color(yellow[i // 3][i % 3]), [x, y, a, a], 0)
        pygame.draw.rect(screen, (0,0,0), [x, y, a, a], 1)
        x += a
        if (i + 1) % 3 == 0:
            x = 3 * a + x0
            y += a

def draw_session(session):
    for i in range(len(session)):
        text = font_session.render(str(session[i][0]), True, black)
        if session_y0 <= session[i][2] <= session_y0 + height_session:
            screen.blit(text, session[i][1:3])

def draw_information():
    text = font2.render('Time:', True, black)
    screen.blit(text, [(size[0] - text.get_width()) // 2, time_y - 80])

    text = font2.render('Scramble:', True, black)
    screen.blit(text, [(size[0] - text.get_width()) // 2, scramble_y - 50])

    text = font2.render('Session:', True, black)
    screen.blit(text, [session_x0 + 70, session_y0 - 55])

    text = font3.render('Solves number: ' + str(count), True, black)
    screen.blit(text, [(size[0] - text.get_width())//2, count_y])

    text = font3.render('Session mean: ' + str(mean), True, black)
    screen.blit(text, [(size[0] - text.get_width())//2, mean_y])

    text = font3.render('Current mean of 3: ' + str(mean_of3), True, black)
    screen.blit(text, [(size[0] - text.get_width())//2, mean_of3_y])

    text = font3.render('Best mean of 3: ' + str(best_mean_of3), True, black)
    screen.blit(text, [(size[0] - text.get_width())//2, best_mean_of3_y])

    text = font3.render('Current average of 5: ' + str(avg5), True, black)
    screen.blit(text, [(size[0] - text.get_width())//2, avg5_y])

    text = font3.render('Best average of 5: ' + str(avg5), True, black)
    screen.blit(text, [(size[0] - text.get_width())//2, best_avg5_y])

    text = font3.render('Current mean of 12: ' + str(mean_of12), True, black)
    screen.blit(text, [(size[0] - text.get_width())//2, mean_of12_y])

    text = font3.render('Best mean of 12: ' + str(best_mean_of12), True, black)
    screen.blit(text, [(size[0] - text.get_width()) // 2, best_mean_of12_y])

    text = font3.render('Current mean of 50: ' + str(mean_of50), True, black)
    screen.blit(text, [(size[0] - text.get_width()) // 2, mean_of50_y])

    text = font3.render('Best mean of 50: ' + str(best_mean_of50), True, black)
    screen.blit(text, [(size[0] - text.get_width()) // 2, best_mean_of50_y])

    text = font3.render('Current mean of 100: ' + str(mean_of100), True, black)
    screen.blit(text, [(size[0] - text.get_width()) // 2, mean_of100_y])

    text = font3.render('Best mean of 100: ' + str(best_mean_of100), True, black)
    screen.blit(text, [(size[0] - text.get_width()) // 2, best_mean_of100_y])

    text = font3.render('Best result: ' + str(best), True, black)
    screen.blit(text, best_xy)

    text = font3.render('Worst result: ' + str(worst), True, black)
    screen.blit(text, worst_xy)

def mean_all():
    mean = 0.0
    for i in session:
        mean += i[0]
    if count != 0:
        mean /= count
    return round(mean, 1)

def current_mean_of_3():
    mean = 0.0
    if count >= 3:
        for i in range(3):
            mean += session[count-1-i][0]
        mean /= 3
    return round(mean,1)

def current_avg_of5():
    avg = 0.0
    a = []
    if count >= 5:
        for i in range(5):
            avg += session[count-1-i][0]
            a.append(session[count-1-i][0])
        avg -= (max(a) + min(a))
        avg /= 3
    return round(avg,1)

def currrent_mean_of12():
    mean = 0.0
    if count >= 12:
        for i in range(12):
            mean += session[count-1-i][0]
        mean /= 12
    return round(mean,1)

def current_mean_of50():
    mean = 0.0
    if count >= 50:
        for i in range(50):
            mean += session[count-1-i][0]
        mean /= 50
    return round(mean,1)

def current_mean_of100():
    mean = 0.0
    if count >= 100:
        for i in range(100):
            mean += session[count-1-i][0]
        mean /= 100
    return round(mean, 1)


black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (150,255,255)
grey = (200,230,230)
orange = (255,165,0)
brown = (139,69,19)
purple = (160,32,240)
DarkGreen = (0,128,0)

time_color = black

size = [1000, 620]
screen = pygame.display.set_mode(size)

done = True
main_done = True
done2 = False

font = pygame.font.Font(None, 150)
font2 = pygame.font.Font(None, 40)
font3 = pygame.font.Font(None, 25)
font_session = pygame.font.Font(None, 25)

clock = pygame.time.Clock()


while main_done:
    done2 = False
    done = True
    seconds = 0.0
    start = 0
    delete = 0

    time_y = 190
    scramble_y = time_y - 130
    scramble = generate_scramble()
    timer2 = str(seconds)
    text = font.render(timer2, True, time_color)
    time_x = (size[0] - text.get_width()) // 2
    length = text.get_width()

    session = []
    session_x0 = session_x = 725
    session_y0 = session_y = time_y - 25
    height_session = 435

    reserve = [0.0 for i in range(7)]

    dy = 20
    a = 7
    best = 0.0
    best_xy = [size[0]//2 - 450, session_y0 + 45]

    worst = 0.0
    worst_xy = [size[0]//2 - 450, session_y0 + 75]

    count = 0
    count_y = time_y + 130

    mean = 0.0
    mean_y = count_y + dy + a

    mean_of3 = 0.0
    mean_of3_y = mean_y + dy + a

    best_mean_of3 = 0.0
    best_mean_of3_y = mean_of3_y + dy

    avg5 = 0.0
    avg5_y = best_mean_of3_y + dy + a

    best_avg5 = 0.0
    best_avg5_y = avg5_y + dy

    mean_of12 = 0.0
    mean_of12_y = best_avg5_y + dy + a

    best_mean_of12 = 0.0
    best_mean_of12_y = mean_of12_y + dy

    mean_of50 = 0.0
    mean_of50_y = best_mean_of12_y + dy + a

    best_mean_of50 = 0.0
    best_mean_of50_y = mean_of50_y  + dy

    mean_of100 = 0.0
    mean_of100_y = best_mean_of50_y + dy + a

    best_mean_of100 = 0.0
    best_mean_of100_y = mean_of100_y + dy

    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
                main_done = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE:
                    done = False
                if event.key == pygame.K_SPACE:
                    time_color = green
                if event.key == pygame.K_MINUS:
                    if len(session) != 0 and delete == 0:
                        session_x = session[len(session)-1][1]
                        session_y = session[len(session)-1][2]
                        if seconds == best:
                            best = reserve[0]
                        if seconds == worst:
                            worst = reserve[1]
                        if current_mean_of_3() == best_mean_of3:
                            best_mean_of3 = reserve[2]
                        if current_avg_of5() == best_avg5:
                            best_avg5 = reserve[3]
                        if currrent_mean_of12() == best_mean_of12:
                            best_mean_of12 = reserve[4]
                        if current_mean_of50() == best_mean_of50:
                            best_mean_of50 = reserve[5]
                        if current_mean_of100() == best_mean_of100:
                            best_mean_of100 = reserve[6]
                        session.pop()
                        seconds = 0.0
                        count -= 1
                        delete = 1
                if len(session) != 0 and session[0][2] < session_y0:
                    if event.key == pygame.K_UP:
                        for i in session:
                            i[2] += 20
                if len(session) != 0 and session[len(session)-1][2] > session_y0 + height_session:
                    if event.key == pygame.K_DOWN:
                        for i in session:
                            i[2] -= 20

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    done2 = True
                    start = 1
                    time_color = black
                    start_ticks = pygame.time.get_ticks()
                    delete = 0

        while done2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = False
                    done2 = False
                    main_done = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        done2 = False
                        start = 0
                        if session_x + font_session.render(str(seconds), True, black).get_width() >= 980:
                            session_x = session_x0
                            session_y += 22
                        if session_y > session_y0 + height_session:
                            for i in session:
                                i[2] -= 22
                            session_y -= 22
                        session.append([seconds,session_x, session_y])
                        session_x += 8 + font_session.render(str(seconds), True, black).get_width()
                        scramble = generate_scramble()
                        if seconds < best or best == 0.0:
                            reserve[0] = best
                            best = seconds
                        if seconds > worst:
                            reserve[1] = worst
                            worst = seconds
                        count += 1

            if start == 1:
                    seconds = ((pygame.time.get_ticks() - start_ticks)//100)/10

            if seconds >= 60:
                timer2 = "{0:01}:{1:02}.{2:01}".format(int(seconds)//60, int(seconds)%60, int(seconds%1*10))
            else:
                timer2 = str(seconds)
            text = font.render(timer2, True, time_color)

            if abs(length - text.get_width()) > 10:
                time_x = (size[0] - text.get_width()) // 2
            length = text.get_width()

            screen.fill(cyan)

            pygame.draw.rect(screen, black, [0,0, size[0]-1, size[1]-1], 2)

            pygame.draw.rect(screen, grey, [size[0] // 2 - 200, time_y - 30, 400, 150], 0)
            pygame.draw.rect(screen, black, [size[0] // 2 - 200, time_y - 30, 400, 150], 1)

            screen.blit(text, [time_x, time_y])

            pygame.display.flip()

            clock.tick(10)

        mean = mean_all()

        mean_of3 = current_mean_of_3()
        if mean_of3 < best_mean_of3 or best_mean_of3 == 0:
            reserve[2] = best_mean_of3
            best_mean_of3 = mean_of3

        avg5 = current_avg_of5()
        if avg5 < best_avg5 or best_avg5 == 0:
            reserve[3] = best_avg5
            best_avg5 = avg5

        mean_of12 = currrent_mean_of12()
        if mean_of12 < best_mean_of12 or best_mean_of12 == 0:
            reserve[4] = best_mean_of12
            best_mean_of12 = mean_of12

        mean_of50 = current_mean_of50()
        if mean_of50 < best_mean_of50 or best_mean_of50 == 0:
            reserve[5] = best_mean_of50
            best_mean_of50 = mean_of50

        mean_of100 = current_mean_of100()
        if mean_of100 < best_mean_of100 or best_mean_of100 == 0:
            reserve[6] = best_mean_of100
            best_mean_of100 = mean_of100



        screen.fill(cyan)

        pygame.draw.rect(screen, black, [0, 0, size[0]-1, size[1]-1], 2)

        pygame.draw.rect(screen, grey, [session_x0-5, session_y0-5, 260, height_session], 0)
        pygame.draw.rect(screen, black, [session_x0-5, session_y0-5, 260, height_session], 1)


        pygame.draw.rect(screen, grey, [size[0] // 2 - 200, time_y - 30, 400, 150], 0)
        pygame.draw.rect(screen, black, [size[0] // 2 - 200, time_y - 30, 400, 150], 1)

        text = font.render(str(seconds), True, time_color)
        screen.blit(text, [(size[0] - text.get_width()) // 2, time_y] )

        text = font2.render(scramble, True, black)
        screen.blit(text, [(size[0] - text.get_width())//2, scramble_y])

        cube_sweep(scramble)

        draw_session(session)

        draw_information()

        pygame.display.flip()

        clock.tick(100)
pygame.quit()
