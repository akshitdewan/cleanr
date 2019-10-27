from flask import Flask
from flask import request
import werkzeug
from ml import *
import json

app = Flask(__name__)
image_files = []
image_names = []

@app.route('/', methods = ['GET', 'POST'])
def collect_image():
	print("request.files", request.files)
	imagefile = request.files['fileToUpload']
	print(imagefile)
	filename = werkzeug.utils.secure_filename(imagefile.filename)
	print("\nReceived image File name : " + imagefile.filename)
	imagefile.save(filename)
	image_files.append(imagefile)
	image_names.append(filename)
	return "Image Uploaded Successfully"

@app.route('/analyze', methods = ['GET'])
def analyze():
	# do things
	global image_files, image_names
	predictions = {}
	for name in image_names:
		predictions[name] = convert_floats(list(get_prediction(name)[0]))
	image_files = []
	image_names = []
	print(predictions)
	print(type(predictions))
	return json.dumps(predictions)

def list_to_dict(lst):
	d = {}
	for i in range(len(lst)):
		d[i] = float(lst[i])
	return d
def convert_floats(lst):
	for i in range(len(lst)):
		lst[i] = float(lst[i])
	return lst

print(get_prediction('img0.png'))