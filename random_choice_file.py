import os
import sys
import cv2
import numpy as np
from PIL import Image
import random
import glob
import datetime

class random_pickup:
	def __init__(self, data_dir):
		self.dt = datetime.datetime.now().strftime('%y%m%d')
		if os.path.exists(data_dir):
			self.dt_dir = os.path.join(data_dir, self.dt + '-pickup')
			print(self.dt_dir)
			os.mkdir(os.path.join(data_dir, self.dt))

		else:
			print(f"Not exists 『{data_dir}』 !!!")
			sys.exit()

	def random_choice(self, datas, num_images, len_images):
		for i in range(int(num_images)):
			self.random_number = random.uniform(0, len_images)
			choice_image = cv2.imread(datas[int(self.random_number)])
			print(datas[int(self.random_number)])
			file_name = os.path.split(datas[int(self.random_number)])
			print(file_name[0])
			print(os.path.join(file_name[0], self.dt_dir, file_name[-1]))
			#cv2.imwrite(os.path.join(file_name[0],'pickup_files',file_name[-1]), choice_image)

	def load_data(self, data_dir):
		self.datas = glob.glob(data_dir + '/*.jpg')
		return self.datas

def main():
	print("data_dir : ",end="")
	data_dir = input()

	rp = random_pickup(data_dir)

	images = rp.load_data(data_dir)
	print(images)
	
	print("How many images do you want? : ",end="")
	num_image = input()
	len_datas = len(images)
	print(len_datas)
	
	rp.random_choice(images, num_image, len_datas)

if __name__ == '__main__':
	main()
