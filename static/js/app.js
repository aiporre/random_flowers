const URL="localhost";
const PORT="8000";

images = ["static/img/background_color/complement_9BA0BC.png", 
          "static/img/background_color/complement_699CCD.png",
          "static/img/background_color/complement_88918D.png", 
          "static/img/background_color/complement_AFA7DD.png",
          "static/img/background_color/complement_B4AFB2.png",
          "static/img/background_color/complement_BBBEC8.png"];

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
const flowername = document.querySelector("#flowername");

// btn.addEventListener('click', function() {
    // get a random number between 0 and lenght of colors 
    // const random = Math.floor(Math.random() * colors.length);
    // document.body.style.backgroundColor = colors[random];
    // flower.src = images[random]; 
    // color.textContent = colors[random];
    // console.log(random);
    // console.log(flower.src)
// });

btn.addEventListener('click', async function() {
    // get a random number between 0 and lenght of colors A
    const random = Math.floor(Math.random() * 1000);
    let res = await fetch(`generate/${random}`);
    console.log('the response is: ', res);
    if (res.ok) {
        let data = await res.json();
        document.body.style.backgroundColor = data.color;
        flower.src = data.img; 
        flower.alt = `flower${random}`
        color.textContent = data.description;
        flowername.textContent = data.name;
        console.log(flower.src)
    } else{
        console.log('error while generating flower')
    }
});