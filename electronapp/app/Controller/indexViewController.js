var self = this;
$(document).ready(function(){
	$('#connectBtn').click(function(e){
		e.preventDefault();
		var host = $('#hostname').val();
		var port = $('#port').val();

		console.log(ConnectionManager(host, port).testConnection());
	});
})