from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "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"

@app.route('/transcribe', methods=['POST'])
def transcribe_route():
    try:
        language = request.form['language']
        audio_file = request.files['audio']

        transcript = transcribe_audio(audio_file, language)

        return jsonify({"transcription": transcript}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def transcribe_audio(audio_file, language):
    with open(audio_file, "rb") as file:
        transcript = openai.Audio.transcribe(
            file=file,
            model="whisper-1",
            response_format="text",
            language=language
        )
        return transcript

if __name__ == '__main__':
    app.run(debug=True)
  
