import requests

# Server URL
url = "http://127.0.0.1:5000/getspeech"

# Text to be converted to speech
payload = {
    "text": "pulkit"
}

# Send POST request
response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})

if response.status_code == 200:
    # Save the received audio file to local storage
    with open("received_speech.wav", "wb") as f:
        f.write(response.content)
    print("Audio file saved as 'received_speech.wav'")
else:
    print(f"Failed to convert text to speech. Status code: {response.status_code}")
