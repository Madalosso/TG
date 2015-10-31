var check = false;

//select/unselect all rows in the table
$("#checkHeader").click(function(){
	check = !check;
	$("#tableExp").find("input:checkbox").prop( "checked", check );
});

//get selected rows from table and remove
$("#btExcluir").click(function(){
	var listIds =  $("#tableExp").find("input:checkbox:checked");
	var asd=[];
	console.log(listIds.length);
	for (var i = 0; i < listIds.length; i++) {
    	asd.push(listIds[i].value);
	}
	console.log(asd);
	var data = {
		'dic': asd,
	}
});

$("#formRemove").submit(function(){
	var listIds =  $("#tableExp").find("input:checkbox:checked");
	var asd=[];
	console.log(listIds.length);
	for (var i = 0; i < listIds.length; i++) {
    	asd.push(listIds[i].value);
	}
	console.log(asd);

	$(this).append($('<input>', {
            type: 'hidden',
            name: "data",
            value: asd
        }))
});