$("#run").click( function() {
    $.post( "." /*"your_python_script_url"*/, {}, function () {
        // What to do when request successfully completed
    });
});