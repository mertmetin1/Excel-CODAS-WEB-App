import os
from flask import Flask, render_template, request
import pandas as pd
from CODAS import codas_method  # your_module, kodunuzun bulunduğu dosyanın adıdır

# Ensure the 'uploads' directory exists
uploads_dir = os.path.join(os.getcwd(), 'uploads')
os.makedirs(uploads_dir, exist_ok=True)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['input_excel']
        if file:
            file_path = os.path.join(uploads_dir, file.filename)
            file.save(file_path)
            result = codas_method(file_path)
            # Read uploaded Excel file
            df_uploaded = pd.read_excel(file_path)
            # Convert DataFrame to HTML table
            html_table = df_uploaded.to_html()
            return render_template('index.html', result=result, html_table=html_table)
    return render_template('index.html', error="File upload failed.")

if __name__ == '__main__':
    app.run(debug=True)