from flask import Flask, request, jsonify
from tempfile import NamedTemporaryFile
import openai
import os

app = Flask(__name__)

openai.api_key = "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"

@app.route('/transcribe', methods=['POST'])
def transcribe_route():
    try:
        language = request.form['language']
        audio_file = request.files['audio']

        # Save the uploaded audio file temporarily
        temp_audio_file = NamedTemporaryFile(delete=False)
        audio_file.save(temp_audio_file.name)

        transcript = transcribe_audio(temp_audio_file.name, language)

        # Remove the temporary file
        os.unlink(temp_audio_file.name)

        return jsonify({"transcription": transcript}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def transcribe_audio(audio_path, language):
    with open(audio_path, "rb") as file:
        transcript = openai.Audio.transcribe(
            file=file,
            model="whisper-1",
            response_format="text",
            language=language
        )
        return transcript

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
