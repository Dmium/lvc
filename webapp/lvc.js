var self = this;

$(document).ready(function(){
	if(window.location.pathname.substring(1, 10) == 'revisions'){
		getRevisions();
	} else {
		initIndex();
	}
});

function getRevisions(){
	var fp = window.location.pathname.substring(11)
	fp = encodeURIComponent(fp);
	jQuery.get('/api/getRevisions/' + fp, function(r){
		var json = $.parseJSON(r);
		if(json.length == 0){
			$('#lvc-revisions-container').html('<p>No revisions found for this file.</p>');
		} else {
			self.revisions = json;
			for(revision in json){
				console.log(json[revision]);
				$('#lvc-revisions-container').html('<p>' + json[revision].content + '</p>');
			}

			$('#lvc-commit-slider').slider({
				value: self.revisions.length - 1,
				min: 0,
				max: self.revisions.length - 1,
				step: 1,
				slide: function(event, ui){
					var current_point = ui.value;
					console.log(current_point);
					$('#lvc-revisions-container').html('<p>'+json[current_point].content + '</p>');
				}
			})
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
