import numpy as np

def load_data():

	remote_path_act = '/tmp/jagrawal/data/data/combined_action_files.txt'
	remote_path_vid = '/tmp/jagrawal/data/data/combined_video_files.bin'

	nb_train = 52400
	nb_test = 10000
	nb_total = 62400

	x = np.fromfile(remote_path_vid, dtype=np.uint8)
	x1 = x[:nb_train * 3 * 160 * 210]
	x_train = np.reshape(x1, (nb_train, 3, 160, 210))

	x2 = x[nb_train * 3 * 160 * 210:nb_total * 3 * 160 * 210]
	x_test = np.reshape(x2, (nb_test, 3, 160, 210)) 

	action_file = open(remote_path_act, "r")

	y_orig = action_file.readlines()
	action_dict = {'DoNothing\n':0, 'JUMP\n':1, 'RIGHT\n':2, 'DOWN\n':3, 'LEFT\n': 4, 'UP\n': 5}
	new_y = []

	for line in y_orig:
		a = line.split(': ')
		new_y.append(action_dict[a[1]])

	y = np.array(new_y)
	y_train = y[:nb_train]
	y_test = y[nb_train:nb_train + nb_test]
	print("hi")
	print(
	return (x_train, y_train), (x_test, y_test)
