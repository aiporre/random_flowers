URL="localhost"
PORT="8000"

localhost
images = ["complement_9BA0BC.png", 
          "complement_699CCD.png",
          "complement_88918D.png", 
          "complement_AFA7DD.png",
          "complement_B4AFB2.png",
          "complement_BBBEC8.png"];

colors = [
          "#9BA0BC", 
          "#699CCD",
          "#88918D", 
          "#AFA7DD",
          "#B4AFB2",
          "#BBBEC8"];
const btn = document.querySelector('#generate');
const color = document.querySelector('.color');
const flower = document.querySelector('.flower');

btn.addEventListener('click', function() {
    // get a random number between 0 and lenght of colors 
    const random = Math.floor(Math.random() * colors.length);
    document.body.style.backgroundColor = colors[random];
    flower.src = `${URL}:${PORT}/static/img/background_color/${images[random]}`; 
    color.textContent = colors[random];
    console.log(random);
    console.log(flower.src)
});