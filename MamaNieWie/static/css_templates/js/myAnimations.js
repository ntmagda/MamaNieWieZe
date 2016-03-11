/**
 * Created by ntmagda on 3/8/2016.
 */
var z = 0;
function colo()
{
    document.getElementById("text").style.color = "rgb(0,0,"+z+")";
    z = Math.round(255 * Math.random());
    setTimeout("colo()", 500);
}


function changeColors() {
    document.getElementById("text").style.color = "red";
}

var canvas = null;

function colorCircle(centerX, centerY) {
    canvas = document.getElementById('kolo');
    canvas.style.left = '10px';
    canvas.style.position= 'relative';
    var context = canvas.getContext('2d');
    var centerX = canvas.width / 2;
    var centerY = canvas.height / 2;
    var radius = 70;

    context.beginPath();
    context.arc(centerX, centerY, radius, 0, 2 * Math.PI, false);
    context.fillStyle = 'green';
    context.fill();
    context.lineWidth = 5;
    context.strokeStyle = '#003300';
    context.stroke();
}

function moveCircle(){
   canvas = document.getElementById('kolo');
   canvas.style.left = parseInt(canvas.style.left) + 10 + 'px';
   canvas.getContext('2d').fillStyle = 'red';
   canvas.getContext('2d').fill();
   canvas.getContext('2d')
   window.onload = colorCircle
}
