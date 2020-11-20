
def time_converter(commercial_ad_time):

	HourTens = int(int(commercial_ad_time[1]) * 10 * 3600)
	HourOnes = int(int(commercial_ad_time[2]) * 3600)

	MinuteTens = int(int(commercial_ad_time[4]) * 10 * 60)
	MinuteOnes = int(int(commercial_ad_time[5]) * 60)

	SecondTens = int(int(commercial_ad_time[7]) * 10)
	SecondOnes = int(int(commercial_ad_time[8]))

	commercial_ad_time_seconds = int(HourTens + HourOnes + MinuteTens + MinuteOnes + SecondTens + SecondOnes) + 1
	return commercial_ad_time_seconds