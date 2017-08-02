// app/service/pointsheet-service.js

myServiceModule.service('PointsheetApi', ['$http', 'serverRoot', function($http, serverRoot){
	var globals = { pointsheetsUrl: serverRoot + 'v1/api/pointsheets/' };
	var _service = {};

	/**
 	* API method GET for get all registers.
	* @type {Function}
	*/
	_service.Get = function () {
		return $http({ method: 'GET', url: globals.pointsheetsUrl });
	};

	/**
	 * API method DELETE for delete an register
	 * @type {Function}
	 */
	_service.Delete = function (id) {
		return $http({ method: 'DELETE', url: globals.pointsheetsUrl + id + "/", data: { id: id } });
	};

	/**
	 * API method PUT for update an exist register
	 * @type {Function}
	 */
	_service.Put = function (id, data) {
		return $http({ method: 'PUT', url: globals.pointsheetsUrl + id + "/", data: data });
	};

	/**
	 * API method POST for insert new register
	 * @type {Function}
	 */
	_service.Post = function (data) {
		return $http({ method: 'POST', url: 'v1/api//pointsheets/', data: data });
	}

    return _service;
}]);