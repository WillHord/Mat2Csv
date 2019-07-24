import scipy.io
import numpy as np
import argparse
import glob, os

parser = argparse.ArgumentParser(description='Convert .mat files to csv files')
parser.add_argument('-f', '--file', metavar='', type=str, help='Choose a specific file to convert')
parser.add_argument('-d', '--directory', metavar='', type=str, help='Choose a specific file to convert')
parser.add_argument('-o', '--out', metavar='', type=str, help='Choose output directory')

args = parser.parse_args()
if args.out:
	args.out
else:
	args.out = '.'

if __name__ == '__main__':
	if args.file:
		data = scipy.io.loadmat(args.file)
		for i in data:
			if '__' not in i and 'readme' not in i:
				np.savetxt((str(args.out)+'/'+i+".csv"),data[i],fmt='%s',delimiter=',')
		print("Finished converting {}".format(args.file))
	elif args.directory:
		os.chdir(args.directory)
		for file in glob.glob("*.mat"):
			dir = args.directory
			temp = (os.path.join(dir,file))
			data = scipy.io.loadmat('/Users/willhord/Documents/Github/Mat2csv/'+temp)
			for i in data:
				if '__' not in i and 'readme' not in i:
					np.savetxt(str(os.path.join(args.out, file+'_'+i+".csv")), data[i], fmt='%s', delimiter=',')
			print("Finished converting {}".format(file))
	else:
		print("Try again \nUse -h to show the help menu")
