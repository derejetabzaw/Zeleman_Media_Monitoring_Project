
import sys
from glob import glob 
from sqed import sqed
import os
import json
import numpy as np

def matching(dirname):
    #dirname = sys.argv[1]
    files = glob(os.path.join(dirname, "*.json"))
    keys = {}
    for i,f in enumerate(files):
        keys[f] = chr(ord("1")+i)
        print keys[f], "=", f
    
    print " "*5,
    for f in files:
        print "%-8s"%keys[f],
    print
    sq_upper_bound = 0.15
    sq_d = []
    combination = []
    video_number_index = []
    for file0 in files:
        """file0 is filename"""
        print "%-5s"%keys[file0],
        for file1 in files:
            """file1 is filename"""
            with open(file0) as f:
                p = json.load(f)
            with open(file1) as f:
                q = json.load(f)
            d = sqed( 4, 2, 100, p[1:], q[1:] )
            
            if 0 < d < sq_upper_bound:    
                sq_d.append(d)
                combination = [file1,file0,keys[file0]]
            
            print "%5f"% d,   
        print
   
    files_length = len(sq_d)
    for i in range (files_length):
        if (0.0 < sq_d[i] < sq_upper_bound):
            video_number_index.append(sq_d[i])
    if combination != [] :
        information = [ "Yes" , combination[1],combination[2]]
    else:
        information = []
    print "NUMBER OF VIDEOS: " + str(len(video_number_index)/2) + '\n' + "SQUARED MEAN ERROR: " + str(video_number_index)
    #return combination[1:] if (len(video_number_index)/2 > 0) else str('No')
    return information if (len(video_number_index)/2 > 0) else ["No"]
def time_in_stream(dirname):
    files = glob(os.path.join(dirname, "*.*"))
    json_files = glob(os.path.join(dirname, "*.json"))
    print json_files
# if __name__ == "__main__":
#     matching("C:/Users/dereje/Desktop/Media_Monitoring_Project/Frontend/frontend_codes/output")