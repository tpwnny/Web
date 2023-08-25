from flask import Flask, render_template, request, jsonify
import os
import multiprocessing

app = Flask(__name__)

def process_audio(audio_path):
    # Simulate background processing
    # Replace this with your actual processing logic
    print(f"Processing audio: {audio_path}")
    # Your processing logic here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400

    audio_file = request.files['audio']
    if audio_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the uploaded audio file
    audio_path = os.path.join('uploads', audio_file.filename)
    audio_file.save(audio_path)

    # Start background processing
    background_process = multiprocessing.Process(target=process_audio, args=(audio_path,))
    background_process.start()

    return jsonify({'message': 'Audio uploaded and processing started'}), 200

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
  
