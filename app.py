from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            if file.filename == '':
                return jsonify({'error': 'No selected file'})
            
            # Save the file or perform processing
            upload_path = os.path.join('uploads', file.filename)
            file.save(upload_path)
            
            return jsonify({'message': 'File uploaded and saved successfully'})
        return jsonify({'error': 'No file uploaded'})
    
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Audio Processing App with Uppy</title>
        <!-- Include Uppy stylesheets -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/uppy@2.2.2/dist/uppy.min.css">
    </head>
    <body>
        <h1>Audio Processing App</h1>
        <form action="/" method="post" enctype="multipart/form-data">
            <div id="uppy-container"></div>
            <button type="submit">Upload</button>
        </form>

        <!-- Include Uppy script -->
        <script src="https://cdn.jsdelivr.net/npm/uppy@2.2.2/dist/uppy.min.js"></script>
        <script>
            document.addEventListener("DOMContentLoaded", function () {
                const uppy = Uppy.Core({
                    debug: true,
                    autoProceed: false,
                });

                // Add Dashboard plugin
                uppy.use(Uppy.Dashboard, {
                    target: '#uppy-container',
                    inline: true,
                    width: '100%',
                    height: 300,
                    proudlyDisplayPoweredByUppy: false,
                });
            });
        </script>
    </body>
    </html>
    """

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)  # Create uploads directory if not exist
    app.run(debug=True)
    
