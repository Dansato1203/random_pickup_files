import os
import sys
import cv2
import numpy as np
from PIL import Image
import random
import glob

def random_choice(datas, num_images, len_images):
	"""
	image_list = np.zeros((0, 3, 480, 640), dtype=np.float32)
	for i in range(int(num_images)):
		random_number = random.uniform(0, len_images)
		#choice_image = cv2.imread(datas[int(random_number)])
		choice_image = np.array(Image.open(datas[int(random_number)]))
		image_list.append(choice_image)
		return image_list
	"""
	os.mkdir('pickup_files')
	for i in range(int(num_images)):
		random_number = random.uniform(0, len_images)
		choice_image = cv2.imread(datas[int(random_number)])
		print(datas[int(random_number)])
		file_name = os.path.split(datas[int(random_number)])
		print(file_name[0])
		print(os.path.join(file_name[0],'pickup_files',file_name[-1]))
		#cv2.imwrite(os.path.join(file_name[0],'pickup_files',file_name[-1]), choice_image)

def load_data(data_dir):
	if not os.path.exists(data_dir):
		print(f"Not exists 『{data_dir}』 !!!")
		sys.exit()
	datas = glob.glob(data_dir + '/*.jpg')
	return datas

def main ():
	print("data_dir : ",end="")
	data_dir = input()
	images = load_data(data_dir)
	print(images)
	print("How many images do you want? : ",end="")
	num_image = input()
	len_datas = len(images)
	print(len_datas)
	a = random_choice(images, num_image, len_datas)
	#print(a[1])

if __name__ == '__main__':
	main()
