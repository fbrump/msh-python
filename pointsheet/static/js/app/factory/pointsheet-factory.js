var myFactoryModule = angular.module('MyFactories', []);

myFactoryModule.factory('PointsheetFactory', [function () {

	var _ConstructorModel = function (form) {
		return {
			year: form['year'],
			month: form['month']
		};
	}
	return {
		ConstructorModel: _ConstructorModel
	};
}]);