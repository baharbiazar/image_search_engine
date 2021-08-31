
import os
import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))


from src.helper import FeatureExtractor , search

from flask import Flask, render_template, request

from werkzeug.utils import secure_filename
import urllib.request
import datetime
import pickle
import pandas as pd
import numpy as np
import re


print(os.listdir(path = "."))
# exit()

array_reloaded = np.load('../model/alloffeatnumpy.npy')
    
with open("static/image_paths.txt", "rb") as fp: # Unpickling
    image_paths = pickle.load(fp)

url_df = pd.read_csv('../data/wayfair_urls.csv')


UPLOAD_FOLDER = './static/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route("/image", methods=["POST", "GET"])
def image():
    if request.method == 'POST':
        f = request.files['file']
        test_path_and_file = './static/uploads/' + ''.join(str(secure_filename(f.filename)).strip().split())
        print(os.path.abspath(test_path_and_file))
        f.save(test_path_and_file)

        # Code goes here to function to put file through model and find similar images

        query_path = test_path_and_file
        search_results, skus = search(query_path, 20)
        print(search_results)
        print(skus)

        urls = []
        for i in skus:

            try:
                urls.append(url_df[url_df.name == i]['link'].values[0])
            except:
                urls.append('https://www.wayfair.com/keyword.php?keyword='+ i)
        print(urls)

        return render_template('results.html',
            original_image = test_path_and_file,
            search_results = search_results,
            skus = skus,
            urls= urls)
    else:
        return 'Not POST ... unsuccessful'











@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def result():
    upload_file = request.files['user_image']
    
    return render_template('results.html')



if __name__ == '__main__':
    
        
    app.run(host='0.0.0.0', port=8080, debug=True)