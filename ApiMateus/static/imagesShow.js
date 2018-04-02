$(function() {
    // Multiple images preview in browser
    var imagesPreview = function(input, placeToInsertImagePreview) {

        if (input.files) {
            var filesAmount = input.files.length;

            for (i = 0; i < filesAmount; i++) {
                var reader = new FileReader();

                reader.onload = function(event) {
                    $($.parseHTML('<img>')).attr(
                            {
                                src: event.target.result,
                                class: "Size-image"
                            }
                    ).appendTo(placeToInsertImagePreview);
                    $('<div class="buttons">' +
                            '<button type ="button" class="btn buttons position-btn btn-success">Enviar</button>' +
                            '<button type ="button" class="btn buttons position-btn btn-danger">Apagar</button>' +
                    '</div>').appendTo(placeToInsertImagePreview)
                    /*$('<button type ="button" class="btn position-btn btn-success">Enviar</button>').appendTo(placeToInsertImagePreview)
                    $('<button type ="button" class="btn position-btn btn-danger">Apagar</button>').appendTo(placeToInsertImagePreview)*/

                }
                reader.readAsDataURL(input.files[i]);
            }
        }

    };

    $('#FormImageFile').on('change', function() {
        imagesPreview(this, 'div.gallery');
    });
});