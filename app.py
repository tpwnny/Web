from flask import Flask, render_template, request

app = Flask(__name__)

# HTML template
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Audio Processing App</title>
    <style>
        /* Your CSS styles here */
    </style>
    <script>
        document.addEventListener("DOMContentLoaded", function () {
            const fileInput = document.querySelector("#audio_file");
            const uploadButton = document.querySelector("#upload_button");
            const submitButton = document.querySelector("#submit_button");

            uploadButton.addEventListener("click", function () {
                fileInput.click();
            });

            fileInput.addEventListener("change", function () {
                const fileName = fileInput.value.split("\\").pop();
                uploadButton.innerHTML = fileName ? fileName : "Choose a file";
            });

            uploadButton.addEventListener("touchstart", function (event) {
                event.preventDefault();
                fileInput.click();
            });

            submitButton.addEventListener("click", function () {
                if (fileInput.files.length === 0) {
                    alert("Please choose a file before submitting.");
                } else {
                    // Disable submit button to prevent multiple submissions
                    submitButton.disabled = true;
                    submitButton.innerHTML = "Uploading...";
                    
                    // Create FormData object to send the file
                    const formData = new FormData();
                    formData.append("audio_file", fileInput.files[0]);
                    
                    // Send the file using Fetch API or XMLHttpRequest
                    fetch("{{ url_for('upload') }}", {
                        method: "POST",
                        body: formData
                    })
                    .then(response => response.text())
                    .then(result => {
                        alert(result);
                        submitButton.disabled = false;
                        submitButton.innerHTML = "Upload";
                    })
                    .catch(error => {
                        alert("An error occurred: " + error.message);
                        submitButton.disabled = false;
                        submitButton.innerHTML = "Upload";
                    });
                }
            });
        });
    </script>
</head>
<body>
    <h1>Audio Processing App</h1>
    <form action="{{ url_for('upload') }}" method="post" enctype="multipart/form-data">
        <input type="file" id="audio_file" name="audio_file" accept=".wav, .mp3">
        <button type="button" id="upload_button">Choose a file</button>
        <button type="button" id="submit_button">Upload</button>
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
    
