from flask import Flask, render_template, request
from scipy.misc import imsave, imread, imresize
import numpy as np
import keras.models
import re
import sys
import os

sys.path.append(os.path.abspath('./model'))

from load import *
app = Flask(__name__)
global model, graph
model, graph = init()


@app.route('/')
def index():
 return render_template('index.html')
 
@app.route('/predict', methods=['GET'])
def predict():
 print("My Model",model, graph)
 dataset = np.loadtxt("pima-indians-diabetes.csv", delimiter=",")
 X = dataset[:,0:8]
 with graph.as_default():
  print("in",X)
  predictions = model.predict(X)
  rounded = [round(x[0]) for x in predictions]
  print("out",rounded)
  #response=np.array_str(np.argmax(out, axis=0))
  
  response=' '.join(map(str, rounded))
  #print("argmax",np.argmax(out, axis=0))
  return response

def index():
 return render_template('index.html')
 
 
if __name__ =='__main__':
 app.run(debug=True,port=8085)

