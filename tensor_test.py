# get data for tf and except errors
import platform
print(platform.platform())
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
print(tf.__version__)
import cv2

