'use strict';

const mediaStreamConstraints = {
    video: true,
}

let constraints = {video: true, audio: false}

async function getMedia(constraints) {
    let stream = null;
    stream = await navigator.mediaDevices.getUserMedia(constraints);
    document.querySelector('video').srcObject = stream
  }

getMedia(constraints)


