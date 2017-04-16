// app/controller/pointsheet-factory.js

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