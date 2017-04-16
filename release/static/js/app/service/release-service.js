// app/service/release-service.js

myServiceModule.service('ReleaseApi', ['$http', function($http){
	var globals = { URL: '/api/releases/' };
	var _service = {};

	/**
 	* API method GET for get all registers.
	* @type {Function}
	*/
	_service.Get = function () {
		return $http({ method: 'GET', url: globals.URL });
	};

	/**
	 * API method DELETE for delete an register
	 * @type {Function}
	 */
	_service.Delete = function (id) {
		return $http({ method: 'DELETE', url: globals.URL + id + "/", data: { id: id } });
	};

	/**
	 * API method PUT for update an exist register
	 * @type {Function}
	 */
	_service.Put = function (id, data) {
		return $http({ method: 'PUT', url: globals.URL + id + "/", data: data });
	};

	/**
	 * API method POST for insert new register
	 * @type {Function}
	 */
	_service.Post = function (data) {
		return $http({ method: 'POST', url: '/api/releases/', data: data });
	}

    return _service;
}]);