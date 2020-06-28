
from model import *
from data import *
import json
import re
import os

# tìm minuntiae cho 1 ảnh
def main1(path):
	w = 16
	image = read_image_rgb(path)
	print(image.shape)
	show_image(image,'image')
	image = normalize(image,m0 = float(100), v0 = float(100))
	image_segment,norm_img,mask = create_segmented_and_variance_images(image, w = w, threshold=.4)
	image_oriented = calculate_angles(image_segment,w)
	show_image(visualize_angles(image, mask, image_oriented, W = w),'huong')
	print(image.shape)
	freq = ridge_freq(norm_img, mask, image_oriented, w, kernel_size = 5, minWaveLength = 5, maxWaveLength = 15)
	gabor_img = gabor_filter(norm_img, image_oriented, freq)
	show_image(gabor_img,'gabor')
	image_thinning = skeletonize(gabor_img)
	show_image(image_thinning,'image thining')
	list_point_minunate,result_im = get_minunatiaes_point(image_thinning,image_oriented)
	for i  in list_point_minunate:
		print(i)
	show_image(result_im,'dd')
	result = []
	for i in list_point_minunate:
		result.append([i[0], i[1][0], i[1][1], i[2]])
	return result

# tìm minuntiae cho toàn bộ data
def main(path):
	w = 16
	image = read_image_rgb(path)
	print(image.shape)
	# show_image(image,'image')
	image = normalize(image,m0 = float(100), v0 = float(100))
	image_segment,norm_img,mask = create_segmented_and_variance_images(image, w = w, threshold=.4)
	image_oriented = calculate_angles(image_segment,w)
	# show_image(visualize_angles(image, mask, image_oriented, W = w),'huong')
	print(image.shape)
	freq = ridge_freq(norm_img, mask, image_oriented, w, kernel_size = 5, minWaveLength = 5, maxWaveLength = 15)
	gabor_img = gabor_filter(norm_img, image_oriented, freq)
	# show_image(gabor_img,'gabor')
	image_thinning = skeletonize(gabor_img)
	# show_image(image_thinning,'image thining')
	list_point_minunate,result_im = get_minunatiaes_point(image_thinning,image_oriented)
	for i  in list_point_minunate:
		print(i)
	# show_image(result_im,'dd')
	result = []
	for i in list_point_minunate:
		result.append([i[0], i[1][0], i[1][1], i[2]])
	return result

list_obj = []
# tim minuntiae cho bộ dữ liệu 600 ảnh cũ
# result = '['
# folder_path = './data/dataset/train_data/0000'
# preprocessed_data = './data/dataset/preprocessed_600_images_data.json'
# with open(preprocessed_data, mode='w') as f:
# 	for i in range(10):
# 		for j in range(80):
# 			img_path = folder_path
# 			if(j < 10):
# 				img_path += str(i) + '_0' + str(j) + '.bmp'
# 			else:
# 				img_path += str(i) + '_' + str(j) + '.bmp'
# 			print(img_path)
# 			img = str(img_path.split('/')[-1:])
# 			print(img)
# 			if(img_path == './data/dataset/train_data/00000_27.bmp' 
# 				or img_path == './data/dataset/train_data/00002_52.bmp'
# 				or img_path == './data/dataset/train_data/00005_12.bmp'
# 				or img_path == './data/dataset/train_data/00006_56.bmp'
# 				or img_path == './data/dataset/train_data/00006_60.bmp'):
# 				continue
# 			else:
# 				img = img[2:len(img) - 2]
# 				list_points = main(img_path)
# 				obj = {
# 					'img': img,
# 					'points': list_points
# 				}
# 				list_obj.append(obj)
# 				result += str(obj) + ','
# 	result += ']'
# 	f.write(result)

# img_path = './data/dataset/real_data/00000_18.bmp'
# with open(preprocessed_data, mode='w') as f:
# 	list_points = main(img_path)
# 	img = str(folder_path.split('/')[-1:])
# 	img = img[2:len(img) - 2]
# 	print(img)
# 	obj = {
# 		'img': img,
# 		'points': list_points
# 	}
# 	list_obj.append(obj)

# 


# Tìm minuntiae cho bộ dữ liệu sample 80 ảnh
# result = '['
# folder_path = './data/dataset/sample/DB'
# preprocessed_data = './data/dataset/sample.json'
# with open(preprocessed_data, mode='w') as f:
# 	for k in range(1, 5):
# 		tmp_path = folder_path + str(k) + '/'
# 		for i in range(101, 111):
# 			for j in range(1, 9):
# 				img_path = tmp_path
# 				img_path += str(i) + '_' + str(j) + '.tif'
# 				print(img_path)
# 				list_points = main(img_path)
# 				img = str(img_path.split('/')[-1:])
# 				img = img[2:len(img) - 2]
# 				obj = {
# 					"img": img,
# 					"points": list_points
# 				}
# 				list_obj.append(obj)
# 				result += str(obj) + ','
# 		result += ']'
# 		f.write(result)
# 		json.dump(result, f)
# main('./data/dataset/sample/101_1.tif')


# Tìm minuntiae cho từng ảnh
# main1('./data/dataset/sample/101_2.tif')


# Đọc từng ảnh trong folder
# result = '['
# main_path = 'D:/My Document/HK8/HeCSDLDPT/BTL/fingerprint-recognization/f/data/dataset/train_data'
# list_imgs = os.listdir(main_path)
# preprocessed_data = './data/dataset/preprocessed_images_data.json'
# with open(preprocessed_data, mode='w') as f:
# 	for i in list_imgs:
# 		img_path = main_path + '/' + i
# 		print(img_path)
# 		list_points = main(img_path)
# 		obj = {
# 			'img': i,
# 			'points': list_points
# 		}
# 		result += str(obj) + ','
# 	result += ']'
# 	f.write(result)

def search_image(test_path, data_path):
	with open(data_path, mode='r') as f:
		data = json.load(f)
		I = main(test_path)
		return brute_force(I, data, 5, pi/180)

def search_matching(I, data):
	no_max = 0
	point = []
	for T in data:
		(ref, x) = hough_transform(I, T['points'])
		count = count_minuntiae_matching(I, T['points'], ref[0], ref[1], ref[2])
		if no_max < count:
			no_max = count
			point = T
	return (point, no_max)

# data_path = './data/dataset/preprocessed_images_data.json'
# test_path = 'D:/My Document/HK8/HeCSDLDPT/BTL/fingerprint-recognization/f/data/dataset/test_data'
# result_path = './data/dataset/result.txt'
# with open(data_path, mode='r') as f:
# 	data = json.load(f)
# 	with open(result_path, mode='w') as f:
# 		list_imgs = os.listdir(test_path)
# 		for i in list_imgs:
# 			img_path = test_path + '/' + i
# 			print(img_path)
# 			I = main(img_path)
# 			rel = search_matching(I, data)
# 			f.write(i + " - " + str(rel))
# 			f.write("\n")
# 			break

# result = '['
# main_path = 'D:/My Document/HK8/HeCSDLDPT/BTL/fingerprint-recognization/f/data/dataset/train/DB'
# result_data = './data/dataset/db1_data.json'
# with open(result_data, mode='w') as f:
# 	for i in range(1,2):
# 		tmp_path = main_path + str(i)
# 		list_imgs = os.listdir(tmp_path)
# 		for j in list_imgs:
# 			img_path = tmp_path + '/' + j
# 			print(img_path)
# 			list_points = main(img_path)
# 			obj = {
# 				'img': str(i) + '_' + str(j),
# 				'points': list_points
# 			}
# 			result += str(obj) + ','
# 	result += ']'
# 	f.write(result)	


# test_path = './data/dataset/test/DB'
# result_data = './data/dataset/result_sample.txt'
# data_path = './data/dataset/db_data.json'
# with open(result_data, mode='w') as f:
# 	for i in range(1,5):
# 		tmp_path = test_path + str(i)
# 		list_imgs = os.listdir(tmp_path)
# 		for j in list_imgs:
# 			img_path = tmp_path + '/' + j
# 			print(img_path)
# 			rel = search_image(img_path, data_path)
# 			f.write(str(i) + '_' + str(j) + " - " + str(rel))
# 			f.write("\n")


# I = main('./data/dataset/test/DB1/101_8.tif')
# data_path = './data/dataset/db1_data.json'
# data = []
# no_max = 0
# point = []
# with open(data_path, mode='r') as f:
# 	data = json.load(f)
# for T in data:
# 	(I1, x) = hough_transform(I, T['points'])
# 	print(I1, x)
# 	check = np.zeros(len(T['points']))
# 	count = 0
# 	for mi in I:
# 		mi_new = rotate_image(mi, delta_x=I1[0], delta_y=I1[1], delta_t=(I1[2]*pi/180))
# 		print(mi_new)
# 		for i, mt in enumerate(T['points']):
# 			(sd, dd) = calculate_distance(mt, mi)
# 			if check[i] == 0 and sd < 50 and dd < pi/8:
# 				count += 1
# 				check[i] = 1
# 	if(count > no_max):
# 		no_max = count
# 		point = T
# print(point, no_max)


test_path = 'D:/My Document/HK8/HeCSDLDPT/BTL/fingerprint-recognization/f/data/dataset/test/DB1'
list_test = os.listdir(test_path)

data_path = './data/dataset/db1_data.json'
data = []

result = './data/dataset/result_db1.json'
rel_file = open(result, mode='w')

with open(data_path, mode='r') as f:
	data = json.load(f)

for test in list_test:
	img_path = test_path + "/" + test
	print(img_path)
	I = main(img_path)
	no_max = 0
	point = []
	for T in data:
		check = np.zeros(len(T['points']))
		count = 0
		(I1, x) = hough_transform(I, T['points'])
		print(I1, x)
		for mi in I:
			mi_new = rotate_image(mi, delta_x=I1[0], delta_y=I1[1], delta_t=(I1[2]*pi/180))
			print(mi_new)
			for i, mt in enumerate(T['points']):
				(sd, dd) = calculate_distance(mt, mi_new)
				if check[i] == 0 and mt[0] == mi[0] and sd < 50 and dd < pi/24:
					count += 1
					check[i] = 1
		if(no_max < count):
			no_max = count
			point = T
	rel_file.write(test + ' - ' + str(point) + ' - ' + str(no_max) + '\n')
	print(point, no_max)


# (I1, x) = hough_transform(I, T)
# print(I1, x)
# check = np.zeros(len(T))
# count = 0
# for mi in I:
# 	# mi_new = rotate_image(mi, delta_x=I1[0], delta_y=I1[1], delta_t=(I1[2]*pi/180))
# 	# print(mi_new)
# 	for i, mt in enumerate(T):
# 		(sd, dd) = calculate_distance(mt, mi)
# 		if check[i] == 0 and sd < 50 and dd < pi/8:
# 			count += 1
# 			check[i] = 1
# print(count/len(I))