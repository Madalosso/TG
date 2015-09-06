
function create_post(){
	console.log("create post is working!")
	$.ajax({
		url : ".", //talvez tenha q ser experiments
		type : "POST",
		data : { opt : $('#id_opt').val() },

		//handle successful
		sucess : function(json){
			$('#id_opt').val('BEEI')
			console.log(json)
			console.log("sucess")
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