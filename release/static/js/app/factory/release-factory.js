// app/controller/release-factory.js

myFactoryModule.factory('ReleaseFactory', [function () {

	var _ConstructorModel = function (form) {
		return {
			date: form['date'],
			dayweek: form['dayweek'],
			checkin: form['checkin'],
			checkout_lunch: _TreatEmpty(form['checkout_lunch']),
			checkin_lunch: _TreatEmpty(form['checkin_lunch']),
			checkout: form['checkout'],
			is_holiday: _TreatBoolean(form['is_holiday']),
			type_absence: form['type_absence'],
			checkin_absence: form['checkin_absence'],
			checkout_absence: form['checkout_absence'],
			justification_absence: form['justification_absence'],
			file_link: form['file_link'],
			pointsheet: form['pointsheet']
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

	var _TreatBoolean = function (check) {
		if (check === null || check === undefined || check === '' || check === 0 || check === false){
			return false;
		}
		else{
			return check;
		}
	};

	return {
		ConstructorModel: _ConstructorModel
	};
}]);