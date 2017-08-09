myFactoryModule.factory('LoginFactory', [function () {

	var _ConstructorModel = function (form) {
		return {
			username: _TreatEmpty(form['username']),
			password: _TreatEmpty(form['password'])
		};
	}

	/**
	 * Method that treat property when is allow NULL value.
	 * @param  {String} text value/data/text
	 * @return {Object}      null or text;
	 */
	var _TreatEmpty = function (text) {
		if (text === null || text === undefined || text === '' || text === 0 || text === false){
			return null;
		}
		else{
			return text;
		}
	};

	return {
		ConstructorModel: _ConstructorModel
	};
}]);