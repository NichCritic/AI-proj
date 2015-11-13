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

def rewrite_paths(mypath, prefix='', generate_url=generate_url):
	output_data = []
	f = []
	idx = -1
	for (dirpath, dirnames, filenames) in os.walk(mypath):
		dirname = dirpath.split('/')[-1]
		print(dirname)
		for i, afile in enumerate(filenames):

			#print(i)
			#print(afile)
			url = generate_url(i, afile)
			#print(url)

			if dirname != '':
				os.rename(os.path.join(dirpath, afile), os.path.join(dirpath, prefix+url))
				output_data.append((idx, 'data/'+dirname+'/'+prefix+url))
		print(idx)
		idx+=1
	return output_data

def write_index(output_data):
	random.shuffle(output_data)

	
	prop = math.floor(0.25*len(output_data))
	test_data = output_data[:prop]
	training_data = output_data[prop:]

	with open('../data/train.txt', 'w') as f:
		f.write('\n'.join([f+' '+str(l) for l, f in training_data]))
	with open('../data/test.txt', 'w') as f:
		f.write('\n'.join([f+' '+str(l) for l, f in test_data]))


if __name__ == '__main__':

	mypath = '../data/'
	
	rewrite_paths(mypath, 'tmp')
	pathlist = rewrite_paths(mypath, '')	

	write_index(pathlist)


	
	#print(generate_url(0, 'test.jpg'))
	# print(generate_url(1, 'test.jpg'))
	# print(generate_url(26, 'test.jpg'))
	# print(generate_url(40, 'test.jpg'))
	# print(generate_url(1111, 'test.jpg'))

