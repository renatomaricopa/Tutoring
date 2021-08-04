from flask import Flask, render_template, request
import boto3
app = Flask(__name__)
from werkzeug.utils import secure_filename

ACCESS_KEY = "AKIA5PIVZRYKTVTLPCHD"
SECRET_KEY = "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"
s3 = boto3.client('s3',
                    aws_access_key_id=ACCESS_KEY,
                    aws_secret_access_key= SECRET_KEY,
                    region_name='us-east-1'
                     )

BUCKET_NAME='fileproject1'

@app.route('/')  
def home():
    return render_template("file_upload_to_s3.html")

@app.route('/upload',methods=['post'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
                filename = secure_filename(img.filename)
                img.save(filename)
                s3.upload_file(
                    Bucket = BUCKET_NAME,
                    Filename=filename,
                    Key = filename
                )
                msg = "Upload Done ! "

    return render_template("file_upload_to_s3.html",msg =msg)




if __name__ == "__main__":
    
    app.run(debug=True)