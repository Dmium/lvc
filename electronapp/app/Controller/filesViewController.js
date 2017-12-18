var self = this;
$(document).ready(function(){
	var jsonDict = $.parseJSON(window.name);
	var host = jsonDict.host;
	var port = jsonDict.port;

	var connManager = ConnectionManager(host, port);

	var versionedFileCb = function(response){
		var i = 0;

		for(file in response){
			$('#lvc-versioned-files').append(
				$('<tr />').append(
					$('<td />').append(
						$('<a>' + file + '</a>', {
							'id': 'file-' + i
						})
					)
				).append(
					$('<td>' + response[file] + '<td />')
				)
			);
			i++;
		}
	};

	connManager.getVersionedFiles(versionedFileCb);
});