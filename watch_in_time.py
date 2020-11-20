import os 
def specific_time_stream(file,specific_time):
	program = str("C:/Users/dereje/Downloads/mplayer-svn-38151-x86_64/mplayer.exe")
	cmd = program + str(" ") + str(file) + " -ss " + str(specific_time)
	return os.system(cmd)
