var self = this;
$(document).ready(function(){
	var jsonDict = $.parseJSON(window.name);
	var host = jsonDict.host;
	var port = jsonDict.port;

	var connManager = ConnectionManager(host, port);

	var onFileClick = function(e){
		e.preventDefault();
		var fp = e.target.text;
		if(fp != null){
			var link = require('path').join(__dirname, 'revisions.html');
			jsonDict.fp = fp;
			window.name = JSON.stringify(jsonDict);
			window.location.assign(link);
		}
	};

	var versionedFileCb = function(response){
		var i = 0;

		for(file in response){
			$('#lvc-versioned-files').append(
				$('<tr />').append(
					$('<td />').append(
						$('<a />', {
							'text': file,
							'id': 'file-' + i
						})
					)
				).append(
					$('<td>' + response[file] + '<td />')
				)
			);
			$('#file-' + i).click(onFileClick);
			i++;
		}
	};

	connManager.getVersionedFiles(versionedFileCb);
});
