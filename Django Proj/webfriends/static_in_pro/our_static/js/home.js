$("#run").click( function() {
    $.post( "." /*"your_python_script_url"*/, {}, function () {
        // What to do when request successfully completed
    });
});

// function getParameterByName(name) {
//     name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
//     var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
//         results = regex.exec(location.search);
//     return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
// }

// function setPaginator(){
// 	page = getParameterByName("page")
// 	if(page==1 || page==""){
// 		$('#first').addClass("active")
// 		$('#etc1').remove();
// 		$('#n-2').remove();
// 		$('#n-1').remove();
// 		$('#n').remove();
// 	}
// 	$('#np').find('a').attr("href", "?page="+(parseInt(page)+1));
// 	$('#np').find('a').html(parseInt(page)+1);
// 	$('#npp').find('a').attr("href", "?page="+(parseInt(page)+2));
// 	$('#npp').find('a').html(parseInt(page)+2);
	
// }

// $( document ).ready(setPaginator());