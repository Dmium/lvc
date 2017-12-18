var self = this;

$(document).ready(function(){
	initIndex();
});

function getRevisions(fp){
	fp = encodeURIComponent(fp);
	jQuery.get('http://localhost:8080/api/getRevisions/' + fp, function(r){
		var json = $.parseJSON(r);
		if(json.length == 0){
			$('#lvc-revisions-container').html('No revisions found for this file.');
		} else {
			self.revisions = json;

			for(revision in json){
				$('#lvc-revisions-container').html(json[revision].content);
			}

			$('#lvc-commit-slider').slider({
				value: self.revisions.length - 1,
				min: 0,
				max: self.revisions.length - 1,
				step: 1,
				slide: function(event, ui){
					var current_point = ui.value;
					$('#lvc-revisions-container').html(json[current_point].content);
				}
			})
		}
	});
}

function initIndex(){
	jQuery.get('http://localhost:8080/api/getFileList', function(r){
		var json = $.parseJSON(r);
		for(file in json){
			var rowId = file.replace('/', '-');
			rowId = rowId.replace('.', '-') + '-row';

			console.log(rowId);
			$('#lvc-versioned-files').append(
				jQuery('<tr />', {
					'id': rowId
				}).append(
					jQuery('<td />').append(
						jQuery('<a>' + file + '</a>', {
							'href': '/revisions/' + file 
						})
					)
				).append(
					jQuery('<td>' + json[file] + '</td>')
				)
			);
		}
	});

	$('#add-file-btn').click(function(e){
		e.preventDefault();
		$('#add-file').trigger('click');
	});

	$('#add-file').change(function(e){
		console.log($(this).val());
		/*$.post('/api/addFile', {filename: $(this).val()}, function(data){
			if(data !== 'success'){
				console.log('ERROR in file submission');
			}
		});*/
	});
}
