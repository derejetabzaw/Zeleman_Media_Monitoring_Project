import os
import sys
import scene_csv
import warnings
import numpy as np
import time_converter as tc
warnings.filterwarnings("ignore")

def normlaized_timestamps(directory_path):
	csv_contents = []
	start_appender = []
	end_appender = []
	timestamps = []
	next_start_appender = []
	next_end_appender = []


	'''List all csv files in the directory'''
	for csv_files in os.listdir(directory_path):
		if csv_files.lower().endswith((".csv")):
			csv_contents.append(csv_files)

	'''Start and End Timestamps'''
	for i in range(len(csv_contents)):
		timestamps.append(scene_csv.scene_segment_informations(str(directory_path + csv_contents[i])))
		start_appender.append(timestamps[i][0][1:])
		end_appender.append(timestamps[i][1][1:])

	'''Offset Factor to add for next start and end timestamps'''
	offset_factor = [float(end_appender[0][-1])]




	'''Next start and end timestamp appender'''
	if (len(csv_contents) > 1):
		for y in range(len(csv_contents) - 1):
			offset_factor.append(float(offset_factor[y]) + float(end_appender[y + 1][-1]))
			for i in range(len(start_appender[y+1])):
				# print (start_appender[y+1][i])
				next_start_appender.append(float(start_appender[y+1][i]) + float(offset_factor[y]))
				next_end_appender.append(float(end_appender[y+1][i]) + float(offset_factor[y]))
				
		start_timestamp = np.concatenate((np.array(start_appender[0]),np.array(next_start_appender)))
		end_timestamp = np.concatenate((np.array(end_appender[0]),np.array(next_end_appender)))
	else:
		start_timestamp = np.concatenate((np.array(start_appender[0])))
		end_timestamp = np.concatenate((np.array(end_appender[0])))


	return start_timestamp,end_timestamp