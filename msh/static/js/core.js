var profileEditApp = angular.module('pointsheetApp', []);
 
profileEditApp.config(['$httpProvider', '$interpolateProvider',
    function($httpProvider, $interpolateProvider) {
    /* for compatibility with django teplate engine */
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
    /* csrf */
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
}]);
 
profileEditApp.controller('pointsheetsCtrl', function ($scope, $http) {
    $scope.data = { success: false, teste:"pinzi" };
 
    function getPointsheets(){
        $http({ method: 'GET', url: globals.pointsheetsUrl })
        .success(function(data, status, headers, config) {
            console.log('oi')
            $scope.data.pointsheets = data;
        })
        .error(function(e) {
            console.error(e);
        });
    };
 
    getPointsheets();
 
    $scope.removePointsheet = function(pointsheet){
        $http({ method: 'DELETE', url: globals.pointsheetsUrl + pointsheet.id + "/", data: { id: pointsheet.id } })
        .success(function(data, status, headers, config) {
            var index = $scope.data.pointsheets.indexOf(pointsheet);
            if (index != -1) {
                $scope.data.pointsheets.splice(index, 1);
            }
        })
        .error(function(data, status, headers, config) {
            console.error(data);
        });
    };
 
    $scope.updatePointsheet = function() {
        $http({method: 'POST', url: globals.pointsheetsUrl, data: { year: $scope.data['year'], month: $scope.data['month'] }}).
        success(function(data, status, headers, config) {
            $scope.data['success'] = true;
            getPointsheets();
        }).
        error(function(data, status, headers, config) {
            console.error(data);
            $scope.data['success'] = false;
        });
    };

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
});