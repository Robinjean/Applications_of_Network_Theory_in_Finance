from os import listdir
from scipy.stats import pearsonr
import numpy
import csv

def OpenFolder():
	correlation_matrix = []
	heading = ["~"]
	files = []
	path = "//home/aimsg/Documents/myAims/PROJECTNETWORK/newdata/"

	for f in listdir(path+"/"):
		heading.append(f.replace(".csv", ""))
		files.append(f)

	correlation_matrix.append(heading)
	
	for data in files:
		data_points = []
		with open (path + data) as data_csv_file:
			read_data_csv = csv.reader(data_csv_file, delimiter = ",")
			next(read_data_csv)
			for row in read_data_csv:
				data_points.append(row[4])

		correlations = [data.replace(".csv", "")]
		for peer in files:
			peer_points = []
			with open (path + peer) as peer_csv_file:
				read_peer_csv = csv.reader(peer_csv_file, delimiter = ",")
				next(read_peer_csv)
				for row in read_peer_csv:
					peer_points.append(row[4])

#			print(data_points)
#			print(peer_points)

			data_length = min([len(data_points), len(peer_points)])-1
			f_data_points = []
			f_peer_points = []

			for i in range(data_length):

				try:
					x = float(data_points[i])
					y = float(peer_points[i])
	
					f_data_points.append(x)
					f_peer_points.append(y)
				except:
					pass
				
			correlation_coefficient = pearsonr(f_data_points, f_peer_points)[0]
			correlations.append(correlation_coefficient)

		correlation_matrix.append(correlations)

		with open('correlation_matrix.csv', 'w') as file:
			writer = csv.writer(file)
			writer.writerows(correlation_matrix)

			
	print(correlation_matrix)
			


OpenFolder()
