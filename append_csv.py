import os
import sys
import testcsv
import warnings
import numpy as np
warnings.filterwarnings("ignore")

csv_contents = []
start_appender = []
end_appender = []
timestamps = []
next_start_appender = []
next_end_appender = []

directory_path = "C:/Users/dereje/Desktop/Media_Monitoring_Project/video_fingerprinting-master/video_fingerprinting-master/Test/contents/"

for csv_files in os.listdir(directory_path):
	if csv_files.lower().endswith((".csv")):
 		csv_contents.append(csv_files)


for i in range(len(csv_contents)):
	timestamps.append(testcsv.scene_segment_informations(str(directory_path + csv_contents[i])))
	start_appender.append(timestamps[i][0][1:])
	end_appender.append(timestamps[i][1][1:])


offset_factor = [float(end_appender[0][-1])]





if (len(csv_contents) > 1):
	for y in range(len(csv_contents) - 1):
		offset_factor.append(float(offset_factor[y]) + float(end_appender[y + 1][-1]))
		for i in range(len(start_appender[y+1])):
			next_start_appender.append(float(start_appender[y+1][i]) + float(offset_factor[y]))
			next_end_appender.append(float(end_appender[y+1][i]) + float(offset_factor[y]))
			
	start_timestamp = np.concatenate((np.array(start_appender[0]),np.array(next_start_appender)))
	end_timestamp = np.concatenate((np.array(end_appender[0]),np.array(next_end_appender)))
else:
	start_timestamp = np.concatenate((np.array(start_appender[0])))
	end_timestamp = np.concatenate((np.array(end_appender[0])))
	