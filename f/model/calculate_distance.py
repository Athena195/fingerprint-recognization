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
