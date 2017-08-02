// app/service/pointsheet-service.js

myServiceModule.service('LoginApi', ['$http', 'serverRoot', function($http, serverRoot){
	var globals = { url: serverRoot + 'v1/api/api-token-auth/' };
	var _service = {};

	var _make_base_auth = function (user, password) {
	  var tok = user + ':' + password;
	  var hash = btoa(tok);
	  return "Basic " + hash;
	}

	/**
	 * API method POST for insert new register
	 * @type {Function}
	 */
	_service.Post = function (data) {
		sessionStorage.setItem('user', _make_base_auth(data.username, data.password));
		return $http({ method: 'POST', url: globals.url, data: data });
	}

	_service.SetHeader = function (data) {
		sessionStorage.setItem('token-user', JSON.stringify(data));
	};

	_service.GetHeader = function () {
		var _token = JSON.parse(sessionStorage.getItem('token-user'));
		var _user = sessionStorage.getItem('user');
		return {
			'Authorization': _user
		};
	};

    return _service;
}]);