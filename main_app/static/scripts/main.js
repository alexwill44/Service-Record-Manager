
console.log('! ! main.js loaded ! !');

$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
  })