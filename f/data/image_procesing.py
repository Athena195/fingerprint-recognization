
import numpy as np 
import cv2 as cv
import matplotlib.pyplot as plt
import pandas as pd


def read_image(path):
	x = cv.imread(path,cv.IMREAD_GRAYSCALE)
	return x
def read_image_rgb(path):
	image = cv.imread(path,cv.IMREAD_GRAYSCALE)
	#image = cv.resize(image,(96,96),interpolation = cv.INTER_AREA)
	return image

def read_images(paths):
	datas_return = []
	p = {}
	for path in paths:
		image = cv.imread(path,cv.IMREAD_GRAYSCALE)
		datas_return.append(image) 
		if str(image.shape) not in p:
			p[str(image.shape)] = 1
		else:
			p[str(image.shape)] += 1
	print(p)
	return np.array( datas_return )
def equalize_historgram(image):
	return cv.equalizeHist(image)
# infor_images = pd.read_csv('data_create_pretrainmodel.csv')
# read_images(infor_images['path'])
def show_image(image, title):
	plt.figure()
	plt.title(title)
	plt.imshow(image)
	plt.show()

'''ig = read_image_rgb('/home/dell/Desktop/f/data/dataset/real_data/00009.bmp')
show_image(ig,'resize')
ig = equalize_historgram(ig)
show_image(ig,'resize')
'''
