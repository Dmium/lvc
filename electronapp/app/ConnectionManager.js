function ConnectionManager(host, port){
	this.host = host;
	this.port = port;

	this.makeRequest = function(requestEndpoint, cb){
		try{
			jQuery.get('http://' + this.host + ':' + this.port + '/' + requestEndpoint, function(r){
				cb($.parseJSON(r));
			});
		} catch(e) {
			cb(null);
		}
	};

	this.testConnection = function(cb){
		this.makeRequest('api/registerClient', cb);
	}

	this.getVersionedFiles = function(cb){
		this.makeRequest('api/getFileList', cb);
	}

	this.getNumberRevisions = function(fp, cb){
		this.makeRequest('api/getNumberRevisions/' + fp, cb);
	};

	this.getRevisionByIndex = function(index, fp, cb){
		this.makeRequest('api/getRevisionByIndex/' + index + '/' + fp, cb);
	}

	this.getLatestRevision = function(fp, cb){
		var latestRevisionIndexCb = function(response){
			var latestRevisionIndex = response.numRevisions - 1;

			this.getRevisionByIndex(latestRevisionIndex, fp, cb);
		}
		this.getNumberRevisions(fp, latestRevisionIndexCb);
	}

	return this;
}