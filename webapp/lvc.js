var self = this;

$(document).ready(function(){
	if(window.location.pathname.substring(1, 10) == 'revisions'){
		getRevisions();
	}
});

function getRevisions(){
	jQuery.get('/api/getRevisions', function(r){
		var json = $.parseJSON(r);
		for(revision in json){
			console.log(json[revision]);
			$('#lvc-revisions-container').html('<p>' + json[revision].content + '</p>');
		}
	});
}
