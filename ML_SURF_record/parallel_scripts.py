import subprocess
import thread
import time

# def thread1():
# 	args = ["-n", "--vcodec", "rawvideo"]
# 	subprocess.Popen(["/usr/bin/python", '/home/jagrawal/Documents/ML_ImitLearning_SURF2/recordscreen.py'] + args)

# def thread2():
# 	subprocess.Popen(["/usr/bin/python", '/home/jagrawal/Documents/ML_ImitLearning_SURF2/py-keylogger/keylogger.py'])


args = ["-n", "--vcodec", "rawvideo"]
subprocess.Popen(["/usr/bin/python", '/home/jagrawal/Documents/ML_ImitLearning_SURF2/recordscreen.py'] + args)
subprocess.Popen(["/usr/bin/python", '/home/jagrawal/Documents/ML_ImitLearning_SURF2/py-keylogger/keylogger.py'])


