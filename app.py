from flask import Flask, render_template, Response
from time import sleep
import os

#makeFlaskInstance
app=Flask(__name__, static_folder='./templates/images')

IMAGE_DIR="./templates/images"

def get_image(filename):
    with open(f"{IMAGE_DIR}/{filename}", "rb") as f:
        image = f.read()
    return image
    
    mtime = os.path.getmtime(f"{IMAGE_DIR}/{filename}")
    
    if mtime != last_mtime:
        last_mtime = mtime
        image = get_image(filename)
        
    return image
    

#showOnBrowser
@app.route('/')
def index():
    return render_template("test.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8080, threaded=True)
