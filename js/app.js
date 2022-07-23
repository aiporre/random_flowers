const colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF', '#FF00FF'];

const btn = document.querySelector('#generate');
const color = document.querySelector('.color');

btn.addEventListener('click', function() {
    // get a random number between 0 and lenght of colors 
    const random = Math.floor(Math.random() * colors.length);
    document.body.style.backgroundColor = colors[random];
    color.textContent = colors[random];
    console.log(random);
});