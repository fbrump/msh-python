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
    $scope.messageModal = { type: '', messages: [] };
 
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
        var _form = { year: $scope.data['year'], month: $scope.data['month'] };
        if (!angular.isUndefined($scope.data.id))
        {
            $http({ method: 'PUT', url: globals.pointsheetsUrl + $scope.data.id + "/", data: _form })
            .success(function(data, status, headers, config) {
                $scope.data['success'] = true;
                getPointsheets();
                func_closeModal();
            })
            .error(function(data, status, headers, config) {
                $scope.data['success'] = false;
                console.error(data);
            });

        } else {
            $http({method: 'POST', url: globals.pointsheetsUrl, data: _form})
            .success(function(data, status, headers, config) {
                $scope.data['success'] = true;
                getPointsheets();
                func_closeModal();
            })
            .error(function(data, status, headers, config) {
                console.error(data);
                $scope.data['success'] = false;
            });
        }
    };

    $scope.updateForm = function (item) {
        func_fillForm(item);
        func_showModal();
    };

    $scope.showForm = function () {
        func_showModal();
    };

    var func_showModal = function () {
        console.log('show modal form');
        $('#modalFormPointsheet').on('shown.bs.modal', function () {
            $('#id_year').focus();
        });
        $('#modalFormPointsheet').modal();
    };

    var func_closeModal = function () {
        $('#modalFormPointsheet').modal('hide');
    };

    var func_fillForm = function (item) {
        $scope.data.id = item.id;
        $scope.data.year = item.year;
        $scope.data.month = item.month;
    };

    var func_cleanForm = function () {
        $scope.data.id = "";
        $scope.data.year = "";
        $scope.data.month = "";
    };

    var func_addMessageModal = function (type, message) {
        if (type==1)
            $scope.messageModal.type = 'danger';
        else
            $scope.messageModal.type = 'success';
        $scope.messageModal.messages.push(message);
    }

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