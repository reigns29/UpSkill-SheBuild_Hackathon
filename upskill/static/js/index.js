var i = 0;
var txt = 'Providing one step solution for impossible military problems...'; /* The text */
var speed = 60; /* The speed/duration of the effect in milliseconds */
typeWriter();
function typeWriter() {
  if (i < txt.length) {
    document.getElementById("type").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}