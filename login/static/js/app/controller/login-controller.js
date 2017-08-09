
myApp.controller('loginCtrl', function ($scope, LoginApi, LoginFactory, $timeout, $location) {
    $scope.model = {
        username: '',
        password: '',
        message: '',
        is_valid: true,
        is_processing: false
    };

    $scope.submitLogin = function () {
        $scope.model.is_processing = true;
        console.log('submit - login');
        var _login = LoginFactory.ConstructorModel($scope.model);
        console.log(_login);
        if (_login.username == null || _login.password == null)
        {
            $scope.model.message= 'Username and password are required!';
            $scope.model.is_valid= false;
            $scope.model.is_processing = false;
        }
        else
        {
            console.log('Realizar o login');
            func_logar(_login);
        }
    };

    $scope.closeAlert = function () {
        // body...
        $scope.model.is_valid=true;
    };

    var func_logar = function (login) {
        LoginApi.Post(login)
        .success(function(data, status, headers, config) {
            console.info('Success');
            console.log(data);
            LoginApi.SetHeader(data);
            $scope.model.is_processing = false;
            $location.path("/pointsheet"); 
        })
        .error(function(data, status, headers, config) {
            console.info('Error');
            console.error(data);
            $scope.model.is_processing = false;
        });
    }

});