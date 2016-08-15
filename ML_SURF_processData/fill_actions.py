import datetime
import time
import sys

# command line arguments are input action file and numbe of updated action file
cmdargs = str(sys.argv)

input_file = str(sys.argv[1])
output_file = str(sys.argv[2])

# set to be file storing keypresses
key_file = input_file


# set to be the name of the file in which the synced actions should be stored in
updated_keylogs_file = output_file


# array to store times at which keys were pressed
key_times = []
actions = []
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
            actions.append(action)
            action_dict[action_time] = action 

counter1 =  0
counter2 = 1
counter3 = 2

actions_final = []
times_final = []


print len(actions)
while counter3 < len(actions):
    action1 = actions[counter1]
    action2 = actions[counter2]
    action3 = actions[counter3]
    time1 = key_times[counter1]
    time2 = key_times[counter2]
    time3 = key_times[counter3]

    lag1 = time2 - time1
    lag2 = time3 - time2

    insert_time = time1

    condition = lag1 >= datetime.timedelta(seconds = 0.4) and lag1 <= datetime.timedelta(seconds = 0.6) and lag2 <= datetime.timedelta(seconds = 0.1) and action1 == action2 and action2 == action3

    if (condition):
        while insert_time < time2:
            times_final.append(insert_time)
            actions_final.append(action1)
            insert_time = insert_time + datetime.timedelta(milliseconds = 40)
    else:
        times_final.append(time1)
        actions_final.append(action1)

    counter1 += 1
    counter2 += 1
    counter3 += 1 

# store final actions corresponding to each frame in output file
f = open(updated_keylogs_file, "w")

c = 0

for time in times_final:
    s_time = datetime.datetime.strftime(time, '%H:%M:%S.%f')
    s = "%s<%s>\n" % (s_time, actions_final[c])
    f.write(s)
    c += 1

f.close()


