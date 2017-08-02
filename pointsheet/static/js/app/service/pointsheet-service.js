// app/service/pointsheet-service.js

myServiceModule.service('PointsheetApi', ['$http', 'serverRoot', 'LoginApi', function($http, serverRoot, LoginApi){
	var globals = { pointsheetsUrl: serverRoot + 'v1/api/pointsheets/' };
	var _service = {};
	var _headers = LoginApi.GetHeader();
	/**
 	* API method GET for get all registers.
	* @type {Function}
	*/
	_service.Get = function () {
		return $http({ method: 'GET', url: globals.pointsheetsUrl, headers: _headers });
	};

	/**
	 * API method DELETE for delete an register
	 * @type {Function}
	 */
	_service.Delete = function (id) {
		return $http({ method: 'DELETE', url: globals.pointsheetsUrl + id + "/", data: { id: id }, headers: _headers });
	};

	/**
	 * API method PUT for update an exist register
	 * @type {Function}
	 */
	_service.Put = function (id, data) {
		return $http({ method: 'PUT', url: globals.pointsheetsUrl + id + "/", data: data, headers: _headers });
	};

	/**
	 * API method POST for insert new register
	 * @type {Function}
	 */
	_service.Post = function (data) {
		return $http({ method: 'POST', url:  globals.pointsheetsUrl, data: data, headers: _headers });
	}

    return _service;
}]);