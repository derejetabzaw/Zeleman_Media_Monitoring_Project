import pandas as pd




def scene_segment_informations(csv_file):
	total_number_of_columns = 11

	scene_number_column = []
	start_time = []
	end_time = []
	length_seconds = []
	col_names = []
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
	if (total_number_of_scenes > total_number_of_columns):
		total_number_of_columns = total_number_of_scenes 
		col_names = []
		for i in range(total_number_of_columns):
			col_names.append("'" + "col_" + str(i + 1) + "'")
		data = pd.read_csv (csv_file, names = col_names , header = None)
		for i in range(total_number_of_scenes + 1):
			scene_number_column.append(data[col_names[0]][i + 1])
			start_time.append(data[col_names[3]][i + 1])
			end_time.append(data[col_names[6]][i + 1])
			length_seconds.append(data[col_names[9]][i + 1])
	else:
		for i in range(total_number_of_scenes + 1):
			scene_number_column.append(data[col_names[0]][i + 1])
			start_time.append(data[col_names[3]][i + 1])
			end_time.append(data[col_names[6]][i + 1])
			length_seconds.append(data[col_names[9]][i + 1])



	return start_time,end_time















