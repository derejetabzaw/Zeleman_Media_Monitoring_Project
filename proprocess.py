import sys
#sys.path.append("C:/Python27/Lib/site-packages/ffmpeg/_probe.py")
#from moviepy.editor import VideoFileClip
import os
import ffprobe
import ffmpeg
from shutil import copy

#-*- coding: utf-8 -*-
import subprocess
if not os.path.exists("output"):
	os.makedirs("output")

def getLength(filename):
  result = subprocess.Popen(['ffprobe', filename],stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
  return [x for x in result.stdout.readlines() if "Duration" in x][0][11:23]
def to_minutes(sec):
	duration_in_minute = (sec / 60)
	return duration_in_minute

def get_sec(time_str):
    """Get Seconds from time."""
    h, m, s  = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + float(s) 

def runBash(command):
	os.system(command)

def crop(start,end,input,output):
	str = "ffmpeg -y -i " + input + " -ss  " + start + " -to " + end + " -c copy " + output
	#print str
	runBash(str)

def trimmer(duration_ad,duration_stream,segment_index,stream_video,ad_video):
	for i in range(segment_index):
		crop(str(i*duration_ad),str(duration_ad*(i + 1)),str(stream_video),str("output/out_" + str(i) + ".mpg"))
 		copy(ad_video,"output")
 	return

