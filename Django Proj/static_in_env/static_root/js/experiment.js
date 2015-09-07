var csrftoken = $.cookie('csrftoken');



function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function create_post(){
	console.log("create post is working!")
	$('#form_exec').hide();
	$.ajax({
		url : "checkForm", //talvez tenha q ser experiments
		type : "POST",
		data : $('#form_exec').serialize(),
		 // {

			// opt : $('#id_opt').val(),
			// Algorithm : $('#id_Algorithm').val()
		// },
		//handle successful
		success : function(data){
            $('#form_exec').show();
	        if (!(data['success'])) {
	            // Here we replace the form, for the
	            $('#form_exec').replaceWith(data['form_html']);
	        }
	        else {
	        	//provavelmente nunca vai chegar aqui pq vai ficar pensando
	            // Here you can show the user a success message or do whatever you need
	            // $('#form_exec').find('.success-message').show();
	        }
		},

		error : function(xhr,errmsg,err){
            $('#form_exec').show();
			console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
		}

	});
};


$('#form_exec').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post();
});


$('#execute').click(function(){
	$('#form_exec').submit();
});
