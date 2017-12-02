var self = this;

$(document).ready(function(){
	if(window.location.pathname.substring(1, 10) == 'revisions'){
		getRevisions();
	} else {
		initIndex();
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

function initIndex(){
	$('#add-file-btn').click(function(e){
		e.preventDefault();
		$('#add-file').trigger('click');
	});

	$('#add-file').change(function(e){
		$.post('/api/addFile', {filename: $(this).val()}, function(data){
			if(data !== 'success'){
				console.log('ERROR in file submission');
			}
		});
	});
}
