'use strict';

const mediaStreamConstraints = {
    video: true,
}

// // Initializes media stream 
// navigator.mediaDevices.getUserMedia(mediaStreamConstraints).then(gotLocalMediaStream)

// // Adds the video stream to webpage video element
// function gotLocalMediaStream(mediaStream){
//     document.querySelector('video').srcObject = mediaStream;
// }

// REWRITE BY YOU. GOOOD BOY!!!

let constraints = {video: true, audio: false}

async function getMedia(constraints) {
    let stream = null;
    stream = await navigator.mediaDevices.getUserMedia(constraints);
    document.querySelector('video').srcObject = stream
  }

getMedia(constraints)


