from flask import Flask, url_for, send_from_directory, request
import face_detection2_2
import face_recognition
import logging, os
import base64
from io import BytesIO
from StringIO import StringIO
from werkzeug import secure_filename
from PIL import Image
import cStringIO

app = Flask(__name__)
file_handler = logging.FileHandler('server.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

#picture=Image.open("/home/sidcloud/Downloads/lol.jpeg")

#picturefinal=Image.open(BytesIO(base64.decode(picture)))
#plain import base64 image = open('/home/sidcloud/Downloads/lol.jpeg', 'rb')
#image_64_encode = base64.encodestring(image_read)

#encoded = base64.b64encode(face_detection2_2.face_recognition(i))
PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def create_new_folder(local_dir):
    newpath = local_dir
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath

@app.route('/server', methods = ['GET','POST'])
def api_root():
    app.logger.info(PROJECT_HOME)
    if request.method == 'POST' and request.form['image_path']:
        app.logger.info(app.config['UPLOAD_FOLDER'])
        img = request.form['image_name']
        im = request.form['image_path']
        finalim = Image.open(BytesIO(base64.b64decode(im)))
        finalim.save("/home/shamshu/Desktop/facial_recognition/facerec/"+img+".jpg")
	boximg=face_detection2_2.face_recognition1(finalim,img)
	buffer = cStringIO.StringIO()
	boximg.save(buffer, format="JPEG")
	encoded = base64.b64encode(buffer.getvalue())
	#encoded=base64.b64encode(boximg)
        #img_name = secure_filename(img)
        #create_new_folder(app.config['UPLOAD_FOLDER'])
        #saved_path = os.path.join(app.config['UPLOAD_FOLDER'], img_name)
        #print saved_path
        #app.logger.info("saving {}".format(saved_path))
        #img.save(saved_path)
        #return send_from_directory(app.config['UPLOAD_FOLDER'],img_name, as_attachment=True)
        #return "Success"
        return encoded
    # else:

        #return "Where is the image?"


if __name__ == '__main__':
