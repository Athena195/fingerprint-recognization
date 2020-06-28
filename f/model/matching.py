from math import pi, sqrt, sin, cos
import numpy as np

def score(I, T):
    len_I = len(I)
    len_T = len(T)
    n = 0
    t = 15 # threshold for distance
    tt = 14 # threshold for theta
    for i in range(len_I)
        found = 0
        j = 0
        while found == 0 and j < len_T:
            dx = (I[i][1] - T[j][1])
            dy = (I[i][2] - T[j][2])
            d = sqrt(dx**2 + dy**2) #euclidean distance between Ii and Tj
            if d < t:
                DTheta = abs(I[i][3] - T[j][3]*180/pi)
                DTheta = min(DTheta, 360-DTheta)
                if DTheta < tt:
                    n += 1 # increase score
                    found = 1
        j += 1
    sm = sqrt(n**2/(len_I+len_T)) # similarity index



def transform2(T, alpha):
    len_T = len(T)
    Tnew = np.zeros()

        
def transform(M, i):
    len_M = len(M)
    xref = M[i][1]
    yref = M[i][2]
    thref = M[i][3]
    T = np.zeros((len, 4))
    R = [[cos(thref), sin(thref), 0], [(-1)*sin(thref), cos(thref), 0], [0, 0, 1]]
    for j in range(len_M):
        B = [M[j][1]-xref, M[j][2]-yref, M[j][3]-thref]
        
