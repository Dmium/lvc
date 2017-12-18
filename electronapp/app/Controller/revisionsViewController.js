var self = this;
$(document).ready(function(){
	var jsonDict = $.parseJSON(window.name);
	var host = jsonDict.host;
	var port = jsonDict.port;
	var fp = jsonDict.fp;

	var connManager = ConnectionManager(host, port);

	var receivedRevisionCb = function(response){
		$('#lvc-revisions-container').html(response.content);
	};

	var totalRevisionsCb = function(response){
		$('#lvc-commit-slider').slider({
			value: response.numRevisions - 1,
			min: 0,
			max: response.numRevisions - 1,
			step: 1,
			slide: function(event, ui){
				var revIndex = ui.value;
				connManager.getRevisionByIndex(revIndex, fp, receivedRevisionCb);
			}
		});
	}

	connManager.getLatestRevision(fp, receivedRevisionCb);

	$(window).on('load', function(){
		connManager.getNumberRevisions(fp, totalRevisionsCb);
	});
});