function ConnectionManager(host, port){
	this.host = host;
	this.port = port;

	this.makeRequest = function(requestEndpoint){
		jQuery.get('http://' + this.host + ':' + this.port + '/' + requestEndpoint, function(r){
			return $.parseJSON(r);
		});
	};

	this.testConnection = function(cb){
		var response = this.makeRequest('api/registerClient');
		return response.success || false;
	}

	this.getVersionedFiles = function(cb){
		return this.makeRequest('api/getFileList');
	}

	this.getNumberRevisions = function(fp){
		var response = this.makeRequest('api/getNumberRevisions/' + fp);
		return response.numRevisions;
	};

	this.getRevisionByIndex = function(index, fp, cb){
		var response = this.makeRequest('api/getRevisionByIndex/' + index + '/' + fp);
		return response.content;
	}

	this.getLatestRevision = function(fp, cb){
		var latestRevisionIndex = this.getNumberRevisions(fp) - 1;
		var response = this.getRevisionByIndex(latestRevisionIndex, fp);
		return response.content;
	}

	return this;
}