const colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF', '#FF00FF'];

const btn = document.querySelector('#generate');
const color = document.querySelector('.color');

btn.addEventListener('click', function() {
    // const random = Math.floor(Math.random() * colors.length);
    // get random number berewe 0 and 3
    // harcoder value of random number
    const random = 2;
    document.body.style.backgroundColor = colors[random];
    color.textContent = colors[random];
    console.log(random);
});