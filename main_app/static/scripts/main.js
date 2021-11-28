
console.log('! ! main.js loaded ! !');

$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
  })

/* background style effect */
let c = 45;

function draw(){
  document.documentElement.style.setProperty('--direction', c++ + 'deg');
  requestAnimationFrame(draw);
}

requestAnimationFrame(draw);
