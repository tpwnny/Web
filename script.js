const recordButton = document.getElementById('recordButton');
const audioPreview = document.getElementById('audioPreview');

let mediaRecorder;
let audioChunks = [];

const handleDataAvailable = event => {
    if (event.data.size > 0) {
        audioChunks.push(event.data);
    }
};

const startRecording = async () => {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);
        mediaRecorder.ondataavailable = handleDataAvailable;
        mediaRecorder.start();
        recordButton.disabled = true;
    } catch (error) {
        console.error('Error accessing microphone:', error);
    }
};

const stopRecording = () => {
    if (mediaRecorder && mediaRecorder.state !== 'inactive') {
        mediaRecorder.stop();
        recordButton.disabled = false;
    }
};

recordButton.addEventListener('click', startRecording);
mediaRecorder.addEventListener('stop', () => {
    const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
    audioChunks = [];
    const audioUrl = URL.createObjectURL(audioBlob);
    audioPreview.src = audioUrl;

    // Send audioBlob to the server
    sendAudioToServer(audioBlob);
});

function sendAudioToServer(blob) {
    const formData = new FormData();
    formData.append('audio', blob);

    fetch('upload.php', {
        method: 'POST',
        body: formData
    }).then(response => {
        // Handle the server's response if needed
    }).catch(error => {
        console.error('Error uploading audio:', error);
    });
}
