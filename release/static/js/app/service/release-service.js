// app/service/release-service.js

myServiceModule.service('ReleaseApi', ['$http', 'serverRoot', 'LoginApi', function($http, serverRoot, LoginApi){
	var globals = { URL: serverRoot + 'v1/api/releases/' };
	var _service = {};
	var _headers = LoginApi.GetHeader();
	
	/**
 	* API method GET for get all registers.
	* @type {Function}
	*/
	_service.Get = function () {
		return $http({ method: 'GET', url: globals.URL , headers: _headers});
	};

	/**
	 * API method DELETE for delete an register
	 * @type {Function}
	 */
	_service.Delete = function (id) {
	 	return $http({ method: 'DELETE', url: globals.URL + id + "/", data: { id: id }, headers: _headers });
	};

	/**
	 * API method PUT for update an exist register
	 * @type {Function}
	 */
	_service.Put = function (id, data) {
		return $http({ method: 'PUT', url: globals.URL + id + "/", data: data, headers: _headers });
	};

	/**
	 * API method POST for insert new register
	 * @type {Function}
	 */
	_service.Post = function (data) {
		return $http({ method: 'POST', url: globals.URL, data: data, headers: _headers });
	}

    return _service;
}]);