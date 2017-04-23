var myApp = angular.module('mshApp', ['MyServices', 'MyFactories']);
 
myApp.config(['$httpProvider', '$interpolateProvider',
    function($httpProvider, $interpolateProvider) {
    /* for compatibility with django teplate engine */
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
    /* csrf */
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
}]);

myApp.filter('formatHour', function () {
    return function function_name(input) {
        var _time_formated = '';
        if (angular.isUndefined(input) || input == null)
            return null;
        else{
            var _arr = input.split(':');
            _time_formated = _arr[0] + ':' + _arr[1]
        }
        return _time_formated;
    }
});

// FACTORY MODULE
var myFactoryModule = angular.module('MyFactories', []);
// SERVICE MODULE
var myServiceModule = angular.module('MyServices', []);

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
//var csrftoken = getCookie('csrftoken');

function formatDate(date) {
    var d = new Date(date),
        month = '' + (d.getMonth()),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2) month = '0' + month;
    if (day.length < 2) day = '0' + day;

    return [year, month, day].join('-');
};

/**
 * Method that retorn of Day of week from datepicker.
 * @param  {Datepicker element} element Date element (with datepicker)
 * @return {String}         Key of day of week.
 */
function getDayWeek(element) {
    var date = $(element).datepicker('getDate');
    var dayOfWeek = date.getUTCDay();
    if (dayOfWeek == 1)
        return 'MON';
    else if (dayweek == 2)
        return 'TUE';
    else if (dayweek == 3)
        return 'WED';
    else if (dayweek == 4)
        return 'THU';
    else if (dayweek == 5)
        return 'FRI';
    else if (dayweek == 6)
        return 'SAT';
    else //if (dayweek == 7)
        return 'SUN';
}