import os
import math
import random

def generate_url(i, url):
	INDEX = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	
	filename, file_extension = os.path.splitext(url)

	chars = []

	if i == 0:
		return 'A'+file_extension

	while i >= 1:
		i = math.floor(i)
		chars.append(INDEX[i % 26])
		i /= 26

	#print(chars)
	#print(file_extension)

	return ''.join(chars)+file_extension







if __name__ == '__main__':

	mypath = '../data/'
	output_data = []
	f = []
	# for (dirpath, dirnames, filenames) in os.walk(mypath):
	# 	#print(filenames)
	# 	for i, afile in enumerate(filenames):

	# 		print(i)
	# 		print(afile)
	# 		url = generate_url(i, afile)
	# 		print(url)
	# 		os.rename(os.path.join(dirpath, afile), os.path.join(dirpath, ''+url))
	# 		dirname = dirpath.split('/')[-1]
	# 		output_data.append((dirname, url))


	for dirpath, dirnames, filenames in os.walk(mypath):
		for filen in filenames:
			label = dirpath.split('/')[-1]
			if(filen != 'index.txt'):
				output_data.append((label, './data/'+label+'/'+filen))			

	random.shuffle(output_data)


	with open('index.txt', 'w') as f:
		f.write('\n'.join([l+' '+f for l, f in output_data]))
	#print(generate_url(0, 'test.jpg'))
	# print(generate_url(1, 'test.jpg'))
	# print(generate_url(26, 'test.jpg'))
	# print(generate_url(40, 'test.jpg'))
	# print(generate_url(1111, 'test.jpg'))

