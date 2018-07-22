Install Anaconda with 3.5 Python
Open Anaconda Navigator through Administrator
Install Tensorflow with Pip
Install Keras with Pip
Check if Flask is installed
Check if Flask is working with this code:

helloworld.py

from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
app.run(debug=True,port=8085)

create a training model in keras: pima.py

jsonify using the following code at the bottom:

model_json = model.to_json()
with open("model.json","w") as json_file:
 json_file.write(model_json)
model.save_weights("model.h5")

open conda terminal through anaconda root

python pima.py will create the model

create app.py ( a flask app to apify the application and call the backend)

create load.py to load the model

create index.html with ajax call through jquery/js

create templates folder in the same directory and keep the index.html there.

save app.py 

open conda terminal through anaconda root

python app.py will deploy the application

access through browser

Be happy with Flask, Keras, Tensorflow, Deep Neural Network (for two class classification)

