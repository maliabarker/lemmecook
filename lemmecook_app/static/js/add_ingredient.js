$("#add-ingredient").on('click', function(event){
    $.ajax({
        url: "{{ url_for('main.new_recipe') }}",
        type : "POST",
        //dataType : 'json', // data type
        data : $("#new-recipe-form").serialize(),
        success : function(result) {
            console.log(result);
            $("#form-ingredients").html(result);
        },
        error: function(xhr, resp, text) {
            console.log(xhr, resp, text);
        }
    });
    event.preventDefault();
});