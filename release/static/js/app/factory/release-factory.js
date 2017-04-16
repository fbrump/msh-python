// app/controller/release-factory.js

myFactoryModule.factory('ReleaseFactory', [function () {

	var _ConstructorModel = function (form) {
		return {
			date: form['date'],
			dayweek: form['dayweek'],
			checkin: form['checkin'],
			checkout_lunch: form['checkout_lunch'],
			checkin_lunch: form['checkin_lunch'],
			checkout: form['checkout'],
			is_holiday: form['is_holiday'],
			type_absence: form['type_absence'],
			checkin_absence: form['checkin_absence'],
			checkout_absence: form['checkout_absence'],
			justification_absence: form['justification_absence'],
			file_link: form['file_link'],
			pointsheet: form['pointsheet']
		};
	}
	return {
		ConstructorModel: _ConstructorModel
	};
}]);