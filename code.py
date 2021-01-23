import random
import pygame

width_h = 0
height_t = 0
width_h_h = 0
height_t_t = 0
x = 1
y = 1
x_x = 1
y_y = 1

sc = pygame.display.set_mode((600, 600), pygame.FULLSCREEN)

a = [[0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 0, 0, 0, 0, 0, 0],
     [1, 1, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 1, 0, 0],
     [1, 0, 0, 0, 0, 0, 1, 0]]
#print(a)
e = 0
q = 0
e_e = e-1
q_q = q+1
e_ = e+1
q_ = q-1

x1 = 0
x2 = 0
x3 = 0
x4 = 0

x5 = 0
x6 = 0
x7 = 0
x8 = 0

final = 7
start = 0

start_cell = a[start][start]
current_cell = a[e][q]
#print(current_cell, e, q)
final_cell = a[final][final]

top = a[e_e][q]
right = a[e][q_q]
bottom = a[e_][q]
left = a[e][q_]
neighbours = [top, right, bottom, left]
while q != start:
    if start>q:
        q+=1
        x5 += 1
    else:
        q-=1
        x5 += 1
    if q == start:
        while e_e != start:
            if start>e_e:
                e_e+=1
                x5+=1
            else:
                e_e -= 1
                x5 += 1
#print(x5)
q = 0
e_e = e-1
while q_q != start:
    if start>q_q:
        q_q+=1
        x6+=1
    else:
        q_q-=1
        x6+=1
    if q_q == start:
        while e != start:
            if start>e:
                e+=1
                x6+=1
            else:
                e-=1
                x6+=1
#print(x6)
e = 0
q_q = q+1
while q != start:
    if start>q:
        q+=1
        x7+=1
    else:
        q-=1
        x7+=1
    if q == start:
        while e_ != start:
            if start>e_:
                e_+=1
                x7+=1
            else:
                e_-=1
                x7+=1
#print(x7)
e_ = e+1
q = 0
while q_ != start:
    if start>q_:
        q_+=1
        x8+=1
    else:
        q_-=1
        x8+=1
    if q_ == start:
        while e == 0:
            if start>e:
                e+=1
                x8+=1
            else:
                e-=1
                x8+=1
#print(x8)
q_ = q-1
e = 0

while q != final:
    if final>q:
        q += 1
        x1 += 1
    else:
        q -= 1
        x1 += 1
    if q == final:
        while e_e != final:
            if final>e_e:
                e_e += 1
                x1 += 1
            else:
                e_e -= 1
                x1 += 1
#print(x1)
q = 0
e_e = e-1
while q_q != final:
    if final>q_q:
        q_q += 1
        x2 += 1
    else:
        q_q -= 1
        x2 += 1
    if q_q == final:
        while e != final:
            if final>e:
                e += 1
                x2 += 1
            else:
                e -= 1
                x2 += 1
#print(x2)
q_q = q+1
e = 0
while q != final:
    if final>q:
        q += 1
        x3 += 1
    else:
        q -= 1
        x3 += 1
    if q == final:
        while e_ != final:
            if final>e_:
                e_ += 1
                x3 += 1
            else:
                e_ -= 1
                x3 += 1
#print(x3)
q = 0
e_ = e+1
while q_ != final:
    if final>q_:
        q_+=1
        x4+=1
    else:
        q_-=1
        x4+=1
    if q_ == final:
        while e != final:
            if final>e:
                e+=1
                x4+=1
            else:
                e-=1
                x4+=1
#print(x4)
q_ = q-1
e = 0

cost2_left= x4*60
cost2_top = x1*60
cost2_right = x2*60
cost2_bottom = x3*60

#print(cost2_top, cost2_right, cost2_bottom, cost2_left)
cost1_top = x5*60
cost1_right = x6*60
cost1_bottom = x7*60
cost1_left = x8*60
#print(cost1_top, cost1_right, cost1_bottom, cost1_left)



totalcost_top = cost1_top+cost2_top
totalcost_right = cost1_right+cost2_right
totalcost_bottom = cost1_bottom+cost2_bottom
totalcost_left = cost1_left+cost2_left



#print(totalcost_top, totalcost_right, totalcost_bottom, totalcost_left)
totalcost = [totalcost_top, totalcost_right, totalcost_bottom, totalcost_left]
_min_ = min(totalcost)

#print(_min_)

#print(final)

totalcost_2 = [totalcost_top, totalcost_right, totalcost_bottom]   #left
_min_2 = min(totalcost_2)
#print(_min_2)
totalcost_3 = [totalcost_top, totalcost_bottom, totalcost_left]    #right
_min_3 = min(totalcost_3)
#print(_min_3)
totalcost_4 = [totalcost_right, totalcost_bottom, totalcost_left]  #top
_min_4 = min(totalcost_4)
#print(_min_4)
totalcost_5 = [totalcost_right, totalcost_top, totalcost_left]     #bottom
_min_5 = min(totalcost_5)
#print(_min_5)

while q != final and e != final:
    if e != final:
        current_cell = a[e][q]
        if _min_ == totalcost_top:
            if a[e - 1][q] != 1:
                e = e - 1
                y_y = y_y-50
                height_t_t -=1
            else:
                if _min_4 == totalcost_right:
                    q = q + 1
                    x_x = x_x+50
                    width_h_h += 1
                elif _min_4 == totalcost_bottom:
                    e = e + 1
                    y_y = y_y+50
                    height_t_t += 1
                elif _min_4 == totalcost_left:
                    q = q - 1
                    x_x = x_x - 50
                    width_h_h -= 1
        elif _min_ == totalcost_right:
            if a[e][q + 1] != 1:
                q = q + 1
                x_x = x_x + 50
                width_h_h += 1
            else:
                if _min_3 == totalcost_top:
                    e = e - 1
                    y_y = y_y - 50
                    height_t_t -= 1
                elif _min_3 == totalcost_left:
                    q = q - 1
                    x_x += 50
                    width_h_h -= 1
                elif _min_3 == totalcost_bottom:
                    e = e + 1
                    y_y += 50
                    height_t_t += 1
        elif _min_ == totalcost_bottom:
            if a[e + 1][q] != 1:
                e = e + 1
                y_y += 50
                height_t_t += 1
            else:
                if _min_5 == totalcost_top:
                    e = e - 1
                    y_y -= 50
                    height_t_t -= 1
                elif _min_5 == totalcost_right:
                    q = q + 1
                    x_x += 50
                    width_h_h += 1
                elif _min_5 == totalcost_left:
                    q = q - 1
                    x_x -= 50
                    width_h_h -= 1
        elif _min_ == totalcost_left:
            if a[e][q - 1] != 1:
                q = q - 1
                x_x -= 50
                width_h_h -= 1
            else:
                if _min_2 == totalcost_top:
                    e = e - 1
                    y_y -= 50
                    height_t_t -= 1
                elif _min_2 == totalcost_right:
                    q = q + 1
                    x_x += 50
                    width_h_h += 1
                elif _min_2 == totalcost_bottom:
                    e = e + 1
                    y_y += 50
                    height_t_t += 1
        elif _min_ == totalcost_top:
            if _min_ == totalcost_right:
                randomiser = random.randint(0, 1)
                if randomiser == 0:
                    e = e - 1
                    y_y -= 50
                    height_t_t -= 1
                else:
                    q = q + 1
                    x_x += 50
                    width_h_h += 1
        elif _min_ == totalcost_bottom:
            if _min_ == totalcost_left:
                randomiser = random.randint(0, 1)
                if randomiser == 0:
                    e = e + 1
                    y_y += 50
                    height_t_t += 1
                else:
                    q = q - 1
                    x_x -= 50
                    width_h_h -= 1
        elif _min_ == totalcost_right:
            if _min_ == totalcost_left:
                randomiser = random.randint(0, 1)
                if randomiser == 0:
                    q = q + 1
                    x_x += 50
                    width_h_h += 1
                else:
                    q = q - 1
                    x_x -= 50
                    width_h_h -= 1
    if a[height_t_t][width_h_h] == 0:
        pygame.draw.rect(sc, (255, 255, 0), (x_x, y_y, 50, 50))

current_cell = a[e][q]
#print("current_cell1: ", current_cell, e, q, totalcost_top, totalcost_right, totalcost_bottom, totalcost_left)
if e == 7:
    while q != 7:
        q += 1
        x_x += 50
        width_h_h +=1
if q == 7:
    while e != 7:
        height_t_t += 1
        e += 1
        y_y += 50
current_cell = a[e][q]
if a[height_t_t][width_h_h] == 0:
    pygame.draw.rect(sc, (255, 255, 0), (x_x, y_y, 50, 50))
#print("current_cell1: ", current_cell, e, q, totalcost_top, totalcost_right, totalcost_bottom, totalcost_left)

if a[0][0] == 0:
    pygame.draw.rect(sc, (200, 200, 200), (1, 1, 50, 50))
    pygame.draw.rect(sc, (250, 0, 0), (351, 351, 50, 50))
    pygame.display.flip()

while height_t != 8:
    while width_h != 7:
        width_h +=1
        x += 50
        if a[height_t][width_h] == 0:
            pygame.draw.rect(sc, (0, 250, 0), (x, y, 50, 50), 2)
            pygame.display.flip()
        else:
            pygame.draw.rect(sc, (0, 0, 250), (x, y, 50 ,50))
            pygame.display.flip()
        #print(height_t, width_h, x, y)
        if width_h == 7:
            height_t += 1
            y += 50
            width_h = width_h - 7
            x = 1
            if a[height_t][width_h] == 0:
                pygame.draw.rect(sc, (0, 250, 0), (x, y, 50, 50), 2)
                pygame.display.flip()
            else:
                pygame.draw.rect(sc, (0, 0, 250), (x, y, 50, 50))
                pygame.display.flip()
            #print(height_t, width_h, x, y)
            if height_t == 7:
                while width_h != 7:
                    width_h += 1
                    x += 50
                    if a[height_t][width_h] == 0:
                        pygame.draw.rect(sc, (0, 250, 0), (x, y, 50, 50), 2)
                        pygame.display.flip()
                    else:
                        pygame.draw.rect(sc, (0, 0, 250), (x, y, 50, 50))
                        pygame.display.flip()
                    #print(height_t, width_h, x, y)
            if height_t == 8:
                break

pygame.draw.rect(sc, (100, 100, 100), (351, 351, 50, 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
