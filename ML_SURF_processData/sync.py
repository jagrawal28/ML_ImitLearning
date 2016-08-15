import datetime
import time

# set to be file storing keypresses
key_file = '/home/jagrawal/Documents/ML_ImitLearning_SURF2/tests/runs/updated_keylogs1.txt'
# set to be start time of video recording
#for5 a = 1468431967.676769
a = 1469040660.045558
b = time.ctime(int(a))
print b

# set to be number of frames per second
fps = 20
# set to be number of screen frames
total_frames = 1200

# set to be the name of the file in which the synced actions should be stored in
sync_action_file = "actions1.txt"


# convert inital recorrding time to appropriate format
init_datetime = time.ctime(int(a))
init_time_str = init_datetime[11:19] + ".000000"
init_time = datetime.datetime.strptime(init_time_str, '%H:%M:%S.%f')
print init_time


width = 160
height = 210

# function to fill array with frame recording times
def fill_frame_times_arr(init_time, num_frames, fps):
    times = []
    time = init_time
    times.append(time)
    for i in range(num_frames):
        #print time
        time = time + datetime.timedelta(milliseconds = 1000 / fps)
        times.append(time)
    return times 
# time for each frame
frame_times = fill_frame_times_arr(init_time, total_frames, fps)


# array to store times at which keys were pressed
key_times = []
# dictionary: key is time at which key was pressed, value is key that is pressed
action_dict = {}
# array to store actions for each frame after syncing
final_actions = []

# extract actions and times from file and store accordingly 
with open(key_file) as f:
    for line in f:
    	if "`" in line:
    		break
    	else:
        	a = line.split("<")
        	str_action_time = a[0]
        	action_time = datetime.datetime.strptime(str_action_time, '%H:%M:%S.%f')
        	key_times.append(action_time)
        	# extract only the action 
        	action = a[1][0:-2]
        	action_dict[action_time] = action 

# iterator for key press times
key_counter = 0
# maximum value of key counter
max_key_counter = len(action_dict)

# left iterator for frame recording times
frame_counter1 = 0
# right iterator for frame recording times
frame_counter2 = 1

# dictionary: key is frame number, value is key press corresponding to that frame
action_frame_dict = {}

# sync the times
while (frame_counter2 < total_frames + 1 and key_counter < max_key_counter):
    keys_pressed = []
    key_time = key_times[key_counter]
    frame1_time = frame_times[frame_counter1]
    frame2_time = frame_times[frame_counter2]

    print "key_press = %s, key_time = %s" % (action_dict[key_time], str(key_time))
    print "frame1_time = %s" % str(frame1_time)
    print "frame2_time = %s" % str(frame2_time)
    print "\n"
    
    # if the time that the key was pressed lies between the two times, store
    # the action corresponding to the key press
    if key_time >= frame1_time and key_time < frame2_time:
        print "WOOOOOOO"
        action = action_dict[key_times[key_counter]]
        print frame_counter2
        print "\n"
        key_counter += 1
    # if no key was pressed between the two times, the action is DoNothing
    else:
        action = "DoNothing"
        frame_counter1 += 1
        frame_counter2 += 1

    action_frame_dict[frame_counter1] = action 

# store final actions corresponding to each frame in output file
action_output_file = open(sync_action_file, "w")

for key in action_frame_dict:
    s = "%d: %s\n" % (key, action_frame_dict[key])
    action_output_file.write(s)

action_output_file.close()



# make a buffer of frame recording time and correpoonding frame rbg values
def make_buf(width, height, init_time, pix, fps, duration):
    final_buf = []
    frame_size = width * height
    start_frame = 0
    end_frame = frame_size - 1
    counter = 0
    time = init_time 
    delta_time = 1 / fps
    total_frames = fps * duration 
    while (counter < total_frames):
        temp_buf = []
        temp_buf.append(time)
        frame_pix = pix[start_frame:end_frame]

        temp_buf.append(frame_pix)

        start_frame += frame_size 
        end_frame += frame_size

        time += datetime.timedelta(milliseconds = 1000/60) 

        counter += 1

        final_buf.append(temp_buf)

    return final_buf