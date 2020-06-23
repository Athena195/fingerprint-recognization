import math
from math import pi
from math import sqrt
from math import cos, sin
import numpy as np
import json

def calculate_distance(vector1, vector2):
    sd = sqrt((vector1[1]-vector2[1])*(vector1[1]-vector2[1]) + (vector1[2]-vector2[2])*(vector1[2]-vector2[2]))
    dd = min(abs(vector1[3]-vector2[3]), 2*pi-abs(vector1[3]-vector2[3]))
    return (sd, dd)

def hough_transform(I, T, theta=0.5, err_theta=0.2, err_x=2, err_y=2, step_theta=math.pi/24):
    delta_theta = np.arange(0, 2*pi, step_theta)
    A = []
    for mt in T:
        for mi in I:
            for t in delta_theta:
                (sd, dd) = calculate_distance(mt, mi)
                if(dd < theta):
                    mt_matrix = np.array([[mt[1]], [mt[2]]])
                    mi_matrix = np.array([[mi[1]], [mi[2]]])
                    rotation = np.array([[cos(t), sin(t)*(-1)], [sin(t), cos(t)]])
                    delta_x_y = mt_matrix - rotation.dot(mi_matrix)
                    delta_x = np.arange(delta_x_y[0]-err_x, delta_x_y[0]+err_x)
                    delta_y = np.arange(delta_x_y[1]-err_y, delta_x_y[1]+err_y)
                    delta_t = np.arange(t-err_theta, t+err_theta)
                    for i in delta_t:
                        for j in delta_x:
                            for k in delta_y:
                                degree = round((180 / math.pi) * i)
                                if(len(A) == 0):
                                    A.append({
                                        'set': [round(j), round(k), degree],
                                        'count': 1
                                    })
                                else:
                                    for a in A:
                                        if(a['set'] == [round(j), round(k), degree]):
                                            a['count'] += 1
                                            break
                                        else:
                                            A.append({
                                                'set': [round(j), round(k), degree],
                                                'count': 1
                                            })
                                            break


    max_vote = 0
    result_set = []
    for a in A:
        if(a['count'] > max_vote):
            result_set = a['set']
            max_vote = a['count']

    return (result_set, max_vote)

def rotate_image(mi, delta_x, delta_y, delta_t):
    mi_matrix = np.array([[mi[1]], [mi[2]]])
    rotation = np.array([[cos(delta_t), sin(delta_t) * (-1)], [sin(delta_t), cos(delta_t)]])
    delta_x_y_matrix = np.array([[delta_x], [delta_y]])
    result_matrix = rotation.dot(mi_matrix) + delta_x_y_matrix
    return (result_matrix, mi[3] + delta_t)

def count_minuntiae_matching(I, T, delta_x, delta_y, delta_t, r, theta):
    count = 0
    check = np.zeros(T.shape)
    for mi in I:
        for t, mt in enumerate(T):
            if(check[t] == 0):
                rotated_minuntiae = rotate_image(mi, delta_x, delta_y, delta_t)
                (sd, dd) = calculate_distance(rotated_minuntiae, mt)
                if(sd <= r and dd <= theta):
                    count += 1
                    check[t] = 1
    return count

def count_brute_force(I, T, r0, t0):
    count = 0
    check = np.zeros(len(T))
    for mi in I:
        for i, mt in enumerate(T):
            if(check[i] == 0 and mi[0] == mt[0]):
                (sd, dd) = calculate_distance(mi, mt)
                if(sd <= r0 and dd <= t0):
                    count += 1
                    check[i] = 1
    return count

def brute_force(I, data, r0, t0):
    max_matching_point = 0
    index_matching = 0
    for i in data:
        if i['points'] == I:
            continue
        count = count_brute_force(I, i['points'], r0, t0)
        if (count > max_matching_point):
            max_matching_point = count
            index_matching = i
    return (index_matching, max_matching_point)

preprocessed_data = './preprocessed_data.json'

with open(preprocessed_data, mode='r') as f:
    data = json.load(f)
    I = { "img": "101_1.tif",
	    "points": [
                [0, 80, 223, 5.961434752782944],
                [0, 127, 150, 0.0],
                [0, 134, 254, 2.819842099193151],
                [0, 141, 135, 3.7295952571373605],
                [0, 141, 198, 2.819842099193151],
                [0, 150, 151, 0.3217505543966423],
                [0, 154, 216, 5.961434752782944],
                [0, 155, 27, 4.71238898038469],
                [0, 164, 237, 2.819842099193151],
                [0, 170, 59, 1.2490457723982544],
                [0, 176, 95, 0.982793723247329],
                [0, 178, 144, 0.7853981633974483],
                [0, 180, 158, 3.7295952571373605],
                [0, 188, 133, 3.9269908169872414],
                [0, 192, 212, 2.356194490192345],
                [1, 206, 202, 5.695182703632018],
                [0, 207, 131, 0.7853981633974483],
                [0, 208, 55, 4.124386376837122],
                [0, 211, 248, 5.695182703632018],
                [1, 231, 160, 0.982793723247329],
                [0, 231, 252, 2.1587989303424644],
                [1, 249, 193, 4.71238898038469],
                [0, 251, 80, 1.5707963267948966],
                [0, 259, 54, 1.2490457723982544],
                [1, 270, 183, 0.3217505543966423],
                [0, 289, 264, 2.1587989303424644],
                [0, 297, 188, 5.034139534781332],
                [1, 304, 193, 4.3906384259880475],
                [0, 305, 100, 1.5707963267948966],
                [0, 305, 155, 1.8925468811915387],
                [0, 308, 246, 1.5707963267948966],
                [0, 315, 187, 5.695182703632018],
                [0, 318, 234, 1.2490457723982544],
                [0, 333, 64, 1.2490457723982544],
                [1, 335, 208, 4.3906384259880475],
                [1, 346, 81, 4.71238898038469],
                [1, 349, 258, 4.71238898038469],
                [0, 350, 161, 2.356194490192345],
                [1, 356, 100, 4.71238898038469],
                [0, 356, 138, 1.8925468811915387],
                [0, 357, 240, 1.5707963267948966],
                [0, 361, 43, 1.5707963267948966],
                [1, 369, 256, 1.5707963267948966],
                [0, 371, 132, 1.8925468811915387],
                [0, 382, 124, 1.8925468811915387],
                [0, 400, 235, 0.7853981633974483],
                [0, 404, 60, 1.5707963267948966],
                [0, 406, 136, 5.3003915839322575],
                [0, 421, 266, 4.124386376837122],
                [0, 425, 32, 4.71238898038469],
                [0, 446, 160, 3.141592653589793],
                [0, 448, 79, 0.0],
                [0, 448, 144, 5.695182703632018],
                [1, 453, 219, 0.0],
                [0, 459, 135, 2.5535900500422257],
                [0, 472, 80, 5.497787143782138],
                [0, 473, 161, 5.961434752782944],
                [0, 479, 172, 3.141592653589793],
                [0, 480, 201, 2.819842099193151],
                [0, 493, 188, 5.961434752782944],
                [1, 494, 83, 0.0],
                [0, 495, 139, 5.961434752782944],
                [1, 495, 256, 5.497787143782138],
                [0, 498, 110, 5.961434752782944],
                [0, 521, 198, 2.819842099193151],
                [0, 528, 195, 0.0],
                [1, 529, 182, 5.3003915839322575],
                [0, 533, 117, 0.0]
            ]
          }
    print(brute_force(I['points'], data, 5, 1.0))

