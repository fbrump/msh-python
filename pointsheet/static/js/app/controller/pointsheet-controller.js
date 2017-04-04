
myApp.controller('pointsheetsCtrl', function ($scope, PointsheetApi, PointsheetFactory) {
    $scope.data = { success: false };
    $scope.messageModal = { type: '', messages: [] };

    $scope.removePointsheet = function(pointsheet){
        PointsheetApi.Delete(pointsheet.id)
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
        if (!angular.isUndefined($scope.data.id))
        {
            PointsheetApi.Put($scope.data.id, PointsheetFactory.ConstructorModel($scope.data))
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
            PointsheetApi.Post(PointsheetFactory.ConstructorModel($scope.data))
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
        func_cleanForm();
        func_showModal();
    };

    function getPointsheets(){
        PointsheetApi.Get()
        .success(function(data, status, headers, config) {
            $scope.data.pointsheets = data;
        })
        .error(function(e) {
            console.error(e);
        });
    };

    var func_showModal = function () {
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
    };

    // Load page
    getPointsheets();
});