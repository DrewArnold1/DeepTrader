import pandas as pd
import tensorflow as tf

usdjpy = pd.read_csv("/Users/Drew/Documents/Forex/Candlesticks/USDJPY_data.csv")

tf.split(2, 2, usdjpy)