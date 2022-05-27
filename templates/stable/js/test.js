
// // Get the webcam stream
// navigator.mediaDevices.getUserMedia({video: true, audio: false}).then(random_func)

// // The above requires a function, and it automatically passes in a stream (in the below case, the stream is called 'random_var')
// function random_func(random_var){
//     document.querySelector('video').srcObject = random_var
// }

'use strict';

let constraints = {video: true, audio: false}

async function getMedia(constraints) {
    let stream = null;
    stream = await navigator.mediaDevices.getUserMedia(constraints);
    document.querySelector('video').srcObject = stream
  }

getMedia(constraints)