
console.log(' main.js loaded javaScript w/ jQuery');

$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
  })


// text editor


/* tinymce.init({
  selector: 'textarea',
  menubar: false,
  content_css: 'default',
}); */