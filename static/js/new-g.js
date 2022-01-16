
var h5 = document.getElementsByTagName('h5')[0];
// var start = document.getElementById('strt');
// var stop = document.getElementById('stp');
// var reset = document.getElementById('rst');

var score = 0;
var elScore = document.getElementById('score');


var sec = localStorage.getItem('globalTime');
var min = 0;
var hrs = 0;
var t;

function tick(){
   
    if( sec > 0){
        sec--;
        if(sec == 0){
            sec = 0;
            min = 0;
            hrs = 0; 
            ress = confirm("This part is finished! YOU SCORE IS:" + score + "Do you want to spot it again?");
            if(ress){
                window.location.href = "http://127.0.0.1:5000/rules";
            }
            else{
                window.location.href = "http://127.0.0.1:5000/";
            } 
            
        } 
   
    }
}


function add() {
    tick();
    h5.textContent = (hrs > 9 ? hrs : "0" + hrs) 
            + ":" + (min > 9 ? min : "0" + min)
            + ":" + (sec > 9 ? sec : "0" + sec);
    timer();
}

function timer() {
    t = setTimeout(add, 1000);
}

timer();
// start.onclick = timer;
// stop.onclick = function() {
//     clearTimeout(t);
// }
// reset.onclick = function() {
//     h5.textContent = "00:00:00";
//     seconds = 0; minutes = 0; hours = 0;
// }

var httpRequest;

   // document.getElementById('clickme').onclick = 


// var card1 = document.getElementById('clickme');
// var card2 = document.getElementById('card2');
// var card3 = document.getElementById('card3');
// var card4 = document.getElementById('card4');



var card1 = document.getElementById('clickme');
var card2 = document.getElementById('card2');
var card3 = document.getElementById('card3');
var card4 = document.getElementById('card4');

            
function clickEvent(e) {
    // e = Mouse click event.
    var rect = e.target.getBoundingClientRect();
    var x = e.clientX - rect.left; //x position within the element.
    var y = e.clientY - rect.top;  //y position within the element.

    // localStorage.setItem('xPosition', x);
    // localStorage.setItem('yPosition', y);
     


    //console.log("OK");
    httpRequest = new XMLHttpRequest();

    if(!httpRequest) {
        alert('Giving Up! Cannot send an XMLHTTO request.');
    }

    httpRequest.open('POST', 'http://127.0.0.1:5000/apitest');
    //console.log("OK");
    var data = JSON.stringify({X: x});
    //console.log("OK");
    httpRequest.send(data);
    //console.log("OK");
    //console.log(data) 
    
    console.log("Left? : " + x + " ; Top? : " + y + ".");
    

    if( x >= 161 && x <= 219 && y >= 50 && y <= 67  ){

            score++;
            elScore.textContent = score;
            ress = confirm("GOOD You win :) DO YOU WANT TO PLAY AGAIN ?");
      
            if(ress){
           

                card1.style.display = "none";
                card2.style.display = "block";
                card3.style.display = "none";
                card4.style.display = "block";
                sec = localStorage.getItem('globalTime');
            }
            else{
                window.location.href = "http://127.0.0.1:5000/";
            } 
    }  

    // var xhr = new XMLHttpRequest();
    // xhr.open("POST", yourUrl, true);
    // xhr.setRequestHeader('Content-Type', 'application/json');
    // xhr.send(JSON.stringify({
    //     x: x,
    //     y: y
    // }))
}

function restartGame() {
    window.location.href = "http://127.0.0.1:5000/rules";
}



function clickEvent2(e) {
  
    var rect = e.target.getBoundingClientRect();
    var x = e.clientX - rect.left; 
    var y = e.clientY - rect.top;  

    httpRequest = new XMLHttpRequest();

    if(!httpRequest) {
        alert('Giving Up! Cannot send an XMLHTTO request.');
    }
    httpRequest.open('POST', 'http://127.0.0.1:5000/apitest');
    var data = JSON.stringify({X: x});
    httpRequest.send(data);
    console.log("Left? : " + x + " ; Top? : " + y + ".");
    if( x >= 126 && x <= 218 && y >= 26 && y <= 276  ){
            score++;
            elScore.textContent = score;
            ress = confirm("GOOD You win :) DO YOU WANT TO PLAY AGAIN ?");
      
            if(ress){
                sec = localStorage.getItem('globalTime');
            }
            else{
                window.location.href = "http://127.0.0.1:5000/";
            } 
    }  

    // var xhr = new XMLHttpRequest();
    // xhr.open("POST", yourUrl, true);
    // xhr.setRequestHeader('Content-Type', 'application/json');
    // xhr.send(JSON.stringify({
    //     x: x,
    //     y: y
    // }))
}



























// // Diaporamaa : --------------------------------------

// var diaporama = 1;
// affichage(diaporama);

// function boutons(n) {
// affichage(diaporama += n);
// }

// function actifIndic(n) {
// affichage(diaporama = n);
// }

// function affichage(n) {
// var i;
// var diapoImg = document.getElementsByClassName("diapo");

// if (n > diapoImg.length) {diaporama = 1}    
// if (n < 1) {diaporama = diapoImg.length}
// for (i = 0; i < diapoImg.length; i++) {
    
//     diapoImg[i].style.opacity = "0";
// }
// diapoImg[diaporama-1].style.opacity = "1";    

// }