var slider = document.getElementById("customRange1");
var output = document.getElementById("time");
output.innerHTML = slider.value + "s"; // Display the default slider value

var httpRequest;

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
    output.innerHTML = this.value + " s";
}

function getTime(){
    var sec = document.getElementById("customRange1").value;

    httpRequest = new XMLHttpRequest();
    if(!httpRequest) {
        alert('Giving Up! Cannot send an XMLHTTO request.');
    }

    httpRequest.open('POST', 'http://192.168.37.69:50001/time');
    var data = JSON.stringify({"time": sec});
    
    httpRequest.send(data);
    localStorage.setItem('globalTime', sec);
    console.log(sec);
} 