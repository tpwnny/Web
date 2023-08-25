from flask import Flask, render_template, request

app = Flask(__name__)

# HTML template
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Audio Processing App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: #f5f5f5;
        }
        h1 {
            text-align: center;
            margin-bottom: 20px;
        }
        form {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        input[type="file"] {
            display: none;
        }
        #upload_button {
            background-color: #007bff;
            color: #ffffff;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
        }
    </style>
    <script>
        document.addEventListener("DOMContentLoaded", function () {
    const fileInput = document.querySelector("#audio_file");
    const uploadButton = document.querySelector("#upload_button");

    uploadButton.addEventListener("click", function () {
        fileInput.click();
    });

    fileInput.addEventListener("change", function () {
        const fileName = fileInput.value.split("\\").pop();
        uploadButton.innerHTML = fileName ? fileName : "Choose a file";
    });

    // Handle touch events for mobile devices
    uploadButton.addEventListener("touchstart", function (event) {
        event.preventDefault();
        fileInput.click();
    });
});

    </script>
</head>
<body>
    <h1>Audio Processing App</h1>
    <form action="{{ url_for('upload') }}" method="post" enctype="multipart/form-data">
        <input type="file" id="audio_file" name="audio_file" accept=".wav, .mp3">
        <button type="button" id="upload_button">Choose a file</button>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
"""

@app.route('/')
def index():
    return html_template

@app.route('/upload', methods=['POST'])
def upload():
    if 'audio_file' not in request.files:
        return "No file part"
    
    file = request.files['audio_file']
    
    if file.filename == '':
        return "No selected file"
    
    # Process the uploaded file, e.g., save it, perform actions, etc.
    # Add your processing logic here
    
    return "File uploaded and processed successfully!"

if __name__ == '__main__':
    app.run(debug=True)
    
