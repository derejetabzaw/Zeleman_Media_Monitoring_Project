import os 



def video_threshold_scene_detector(Stream,commercial_ad_time_seconds):
	directory_threshold = (os.getcwd() + str("/")+str("cropped_threshold")).replace("\\","/")
	scenedetect_script = "scenedetect -i " + str(Stream) + " -o " + directory_threshold + " detect-threshold -m " + str(commercial_ad_time_seconds) + "s" + " split-video" + " list-scenes"
	#print scenedetect_script
	os.system(scenedetect_script)
def video_content_scene_detector(ad_length):
	directory_threshold = (os.getcwd() + str("/")+str("cropped_threshold")).replace("\\","/")
	for filename in os.listdir(directory_threshold):
	    if filename.endswith(".mp4"): 
	    	scenedetect_content_script = "scenedetect -i " + str((directory_threshold + str("/") + filename).replace("\\","/")) + " -o cropped_content detect-content -m " + str(ad_length) + "s" +  " split-video" + " list-scenes"
	    	os.system(scenedetect_content_script)
