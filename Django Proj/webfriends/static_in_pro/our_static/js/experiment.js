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
	$('#form_exec').hide()
	$.ajax({
		url : ".", //talvez tenha q ser experiments
		type : "POST",
		data : {
			opt : $('#id_opt').val(),
			Algorithm : $('#id_Algorithm').val()
		},

		//handle successful
		success : function(json){
			$('#id_opt').val('')
			console.log(json.resposta)
			console.log("success")
		},

		error : function(xhr,errmsg,err){
			console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
		}

	});
};


$('#form_exec').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post();
});