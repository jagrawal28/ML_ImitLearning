#!/usr/bin/env python
# python_example.py
# Author: Ben Goodrich
#
# This is a direct port to python of the shared library example from
# ALE provided in doc/examples/sharedLibraryInterfaceExample.cpp
import sys
import numpy as np
from random import randrange
#sys.path.append('~/tools/Arcade-Learning-Environment-0.5.1/ale_python_interface')
from ale_python_interface import ALEInterface
from PIL import Image
import os
import load_model_func
import datetime

if len(sys.argv) < 2:
  print 'Usage:', sys.argv[0], 'rom_file'
  sys.exit()

ale = ALEInterface()

# Get & Set the desired settings
ale.setInt('random_seed', 123)

# Set USE_SDL to true to display the screen. ALE must be compilied
# with SDL enabled for this to work. On OSX, pygame init is used to
# proxy-call SDL_main.
USE_SDL = False
if USE_SDL:
  if sys.platform == 'darwin':
    import pygame
    pygame.init()
    ale.setBool('sound', False) # Sound doesn't work on OSX
  elif sys.platform.startswith('linux'):
    ale.setBool('sound', True)
  ale.setBool('display_screen', True)

# Load the ROM file
ale.loadROM(sys.argv[1])

loaded_model = load_model_func.load_trained_model

# Get the list of legal actions
legal_actions1 = ale.getLegalActionSet()
print type(legal_actions1)
print legal_actions1.shape
print legal_actions1.data
legal_actions = np.ndarray(shape = (6, ), buffer = np.array([0, 1, 2, 3, 4, 5]), dtype = int)
print legal_actions

# load the model which will be used to predict actions based on a given screen
loaded_model = load_model_func.load_trained_model()
print(type(loaded_model))

# create folder to store images which will then be converted into a video
curr_time = datetime.datetime.now().strftime("%I:%M%p %B %d, %Y")
newpath = r'/cs/ml/datasets/montezuma_imitation/ML_SURF_train/screendumps/' + curr_time
new_dir = os.makedirs(newpath)
print(new_dir)

# Play episodes
for episode in xrange(1):
  total_reward = 0
  frame_counter = 0

  #key is action based on video recording, value is same action based on emulator
  #{DoNothing, Jump, Right, Down , Left, Up}
  action_dict = {0:0, 1:1, 2:3, 3:5, 4:4, 5:2}
  a = 3

  while not ale.game_over():
    #a = legal_actions[randrange(len(legal_actions))]
   # print a
    # Apply an action and get the resulting reward
    reward = ale.act(action_dict[a]);
    #print reward
    total_reward += reward

    #grab screen and store in folder
    screen = ale.getScreenRGB()
    im = Image.fromarray(screen, 'RGB')
    im_path = os.path.join(newpath + "/im" + str(frame_counter) + ".png")
    im.save(im_path)
    print "Stored framedump to", im_path

    # use screen that was grabbed to predict the next action
    s = np.reshape(screen, (1, 3, 160, 210))
    action_prediction = loaded_model.predict_classes(s, batch_size=32, verbose=1)
    a = action_prediction[0]
    print(action_dict[a])

    frame_counter += 1

  print 'Episode', episode, 'ended with score:', total_reward
  print frame_counter

  ale.reset_game()
