import pyttsx3
from flask import Flask, request, send_file

app = Flask(__name__)

text_to_speech = pyttsx3.init()

@app.route("/getspeech", methods=['POST'])
def speech():
    data = request.get_json()
    if not data or 'text' not in data:
        return {'error': 'No text provided'}, 400
    
    text = data['text']
    audio_file_path = "output.wav"
    
    # Generate speech and save to file
    text_to_speech.save_to_file(text, audio_file_path)
    text_to_speech.runAndWait()

    # Send the audio file as a response
    return send_file(audio_file_path, as_attachment=True, download_name='speech.wav')

if __name__ == '__main__':
    app.run( debug=True)