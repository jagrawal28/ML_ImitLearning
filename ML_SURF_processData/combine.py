from glob import iglob
import shutil
import os
import os, sys
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]

#Open a file

# make sure action files are combined in the correct order
action_path = '/home/jagrawal/Documents/ML_ImitLearning_SURF2/runs/combine_actions'
action_dirs = os.listdir( action_path )
action_dirs.sort(key=natural_keys)
print action_dirs

# make sure video files are combined in right order
video_path = '/home/jagrawal/Documents/ML_ImitLearning_SURF2/runs/combine_videos'
video_dirs = os.listdir( video_path )
video_dirs.sort(key=natural_keys)
print video_dirs

#combine action files into one new file
destination1 = open('combined_action_files_new.txt', 'w')
for filename in action_dirs:
	f = os.path.join(action_path, filename)
	shutil.copyfileobj(open(f, 'r'), destination1)
destination1.close()

# combine video files into one new file
destination2 = open('/home/jagrawal/Documents/mountpoints/mount_keras/train_montezuma/combined_video_files.bin', 'wb')
for filename in video_dirs:
	f = os.path.join(video_path, filename)
	shutil.copyfileobj(open(f, 'rb'), destination2)
destination2.close()
