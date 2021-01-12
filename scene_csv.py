import pandas as pd


def scene_segment_informations(csv_file,total_number_of_scenes):
	total_number_of_columns = 11
	col_names = []
	scene_number_column = []
	start_time = []
	end_time = []
	length_seconds = []
	for i in range(total_number_of_columns):
		col_names.append("'" + "col_" + str(i + 1) + "'")

	data = pd.read_csv (csv_file, names = col_names , header = None)
	total_number_of_scenes = len(data[col_names[0]][2:])
	if (total_number_of_scenes == 0):
		for i in range(total_number_of_scenes + 2):
			scene_number_column.append(data[col_names[0]][i])
			start_time.append(data[col_names[3]][i])
			end_time.append(data[col_names[6]][i])
			length_seconds.append(data[col_names[9]][i])
	else:
		for i in range(total_number_of_scenes + 1):
			scene_number_column.append(data[col_names[0]][i + 1])
			start_time.append(data[col_names[3]][i + 1])
			end_time.append(data[col_names[6]][i + 1])
			length_seconds.append(data[col_names[9]][i + 1])
	return start_time,end_time




















for i in range(total_number_of_columns):
	col_names.append("'" + "col_" + str(i + 1) + "'")

data = pd.read_csv (r'C:/Users/dereje/Desktop/Media_Monitoring_Project/video_fingerprinting-master/video_fingerprinting-master/Test/stream_example-Scenes.csv', names = col_names , header = None)
scene_number_column = []
start_time = []
end_time = []
length_seconds = []

# print data[col_names[1]]
for i in range(total_number_of_scenes + 1):
	scene_number_column.append(data[col_names[0]][i + 1])
	start_time.append(data[col_names[3]][i + 1])
	end_time.append(data[col_names[6]][i + 1])
	length_seconds.append(data[col_names[9]][i + 1])



# print scene_number_column[1:]
# print start_time[1:]
# print end_time[1:]
# print length_seconds[1:]
