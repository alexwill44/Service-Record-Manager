
console.log(' main.js loaded javaScript w/ jQuery');

$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
  })

/* Downdown logic */
$('.dropdown-menu').on('show.bs.dropdown', function () {
  console.log('clicked it -> we are listening ');
})