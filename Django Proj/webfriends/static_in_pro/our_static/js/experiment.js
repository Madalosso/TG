// var csrftoken = $.cookie('csrftoken');
// function csrfSafeMethod(method) {
//     // these HTTP methods do not require CSRF protection
//     return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
// }

// $.ajaxSetup({
// 	data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
//     beforeSend: function(xhr, settings) {
//         if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//             xhr.setRequestHeader("X-CSRFToken", csrftoken);
//         }
//     }
// });

// function toggleFormWait(){
// 	$("#loadGif").toggle()
// 	$("#colForm").toggle()
// }

// function create_post(){
// 	$("#id_Algorithm").prop('disabled', false);	
// 	$("#id_opt").prop('disabled', false);
// 	toggleFormWait();
// 	$.ajax({
// 		url : "checkForm", //talvez tenha q ser experiments
// 		type : "POST",
// 		data : $('#form_exec').serialize(),
// 		 // {

// 			// opt : $('#id_opt').val(),
// 			// Algorithm : $('#id_Algorithm').val()
// 		// },
// 		//handle successful
// 		success : function(data){
// 			toggleFormWait();
// 	        if (!(data['success'])) {
// 	        	// $('#form_exec').replaceWith(data.form_html);
// 	        	$('#form_exec').replaceWith(data['form_html']);
// 	        	$('#form_exec').prepend('<input type="hidden" name="csrfmiddlewaretoken" value="'+csrftoken+'">');   
// 	        	$('#execute').click(function(){
// 					$('#form_exec').submit();
// 				});
// 				// setHandlers();
// 	            // console.log(data['form_html']);
// 	            // var formClear = data['form_html'];
// 	            // formClear = formClear.replace('<form  id="form_exec" method="post" >','')
// 	            // formClear = formClear.replace('</form>','')
// 	            // $('#formContent').replaceWith(formClear);
// 	        }
// 	        else {
// 	        	$('#form_exec').replaceWith(data['form_html']);
// 	        	$('#form_exec').prepend('<input type="hidden" name="csrfmiddlewaretoken" value="'+csrftoken+'">');   
// 	   //      	$('#form_exec').on('submit', function(event){
// 				//     event.preventDefault();
// 				//     console.log("form submitted!")  // sanity check
// 				//     create_post();
// 				// });
// 				$('#execute').click(function(){
// 					$('#form_exec').submit();
// 				});
// 	        	//provavelmente nunca vai chegar aqui pq vai ficar pensando
// 	            // Here you can show the user a success message or do whatever you need
// 	            // $('#form_exec').find('.success-message').show();
// 	        }
// 		},

// 		error : function(xhr,errmsg,err){
//         	toggleFormWait();
// 			console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
// 		}

// 	});
// };

// function setTriggers(){
// 	$('#form_exec').on('submit', function(event){
// 	    event.preventDefault();
// 	    console.log("form submitted!")  // sanity check
// 	    create_post();
// 	});


// 	$('#execute').click(function(){
// 		$('#form_exec').submit();
// 	});

// };

function setHandlers(){
	$('#id_PresetExecution').on("change", function(){
		var opcao = $('#id_PresetExecution').val();
		console.log(opcao);
		var algSelect = $('#id_PresetExecution option:selected').text();
		if(opcao){
			$("#id_Algorithm option").filter(function() {
		   		return $(this).text() == algSelect; 
			}).prop('selected', true);
			$("#id_opt").val('');
			$("#id_Algorithm").prop('disabled', true);	
			$("#id_opt").prop('disabled', true);
			$("#id_fileIn").prop('disabled', true);

		}else{
			$('select#id_Algorithm').prop('selectedIndex', 0);
			$("#id_opt").val('');	
			$("#id_Algorithm").prop('disabled', false);	
			$("#id_opt").prop('disabled', false);
			$("#id_fileIn").prop('disabled', false	);
		}
	});
};


setHandlers();
// setTriggers();