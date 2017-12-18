var self = this;
$(document).ready(function(){
	$('#connectBtn').click(function(e){
		e.preventDefault();
		var host = $('#hostname').val();
		var port = $('#port').val();
		
		var testConnectionCb = function(response){
			if(response.success == true){
				var link = require('path').join(__dirname, 'files.html');
				var persistDict = {'host': host, 'port': port};
				window.name = JSON.stringify(persistDict);
				window.location.assign(link);
			}
		}
		
		ConnectionManager(host, port).testConnection(testConnectionCb);
	});
});