
from model import *
from data import *
import json
import re
def main(path):
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

list_obj = []
folder_path = './data/dataset/train_data/0000'
preprocessed_data = './data/dataset/preprocessed_data.json'
# with open(preprocessed_data, mode='w') as f:
# 	for i in range(10):
# 		for j in range(80):
# 			img_path = folder_path
# 			if(j < 10):
# 				img_path += str(i) + '_0' + str(j) + '.bmp'
# 			else:
# 				img_path += str(i) + '_' + str(j) + '.bmp'
# 			print(img_path)
# 			list_points = main(img_path)
# 			img = str(folder_path.split('/')[-1:])
# 			img = img[2:len(img) - 2]
# 			obj = {
# 				'img': img,
# 				'points': list_points
# 			}
# 			list_obj.append(obj)
# 			json.dump(list_obj, f)
img_path = './data/dataset/real_data/00000_18.bmp'
with open(preprocessed_data, mode='w') as f:
	list_points = main(img_path)
	img = str(folder_path.split('/')[-1:])
	img = img[2:len(img) - 2]
	print(img)
	obj = {
		'img': img,
		'points': list_points
	}
	list_obj.append(obj)
	json.dump(list_obj, f)