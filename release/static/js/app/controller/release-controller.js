
myApp.controller('releasesCtrl', function ($scope, ReleaseApi, ReleaseFactory) {
    $scope.data = { success: false };
    $scope.messageModal = { type: '', messages: [] };

    $scope.removeRelease = function(release){
        ReleaseApi.Delete(release.id)
        .success(function(data, status, headers, config) {
            var index = $scope.data.releases.indexOf(release);
            if (index != -1) {
                $scope.data.releases.splice(index, 1);
            }
        })
        .error(function(data, status, headers, config) {
            console.error(data);
        });
    };
 
    $scope.updateRelease = function() {
        if (!angular.isUndefined($scope.data.id))
        {
            ReleaseApi.Put($scope.data.id, ReleaseFactory.ConstructorModel($scope.data))
            .success(function(data, status, headers, config) {
                $scope.data['success'] = true;
                getReleases();
                func_closeModal();
            })
            .error(function(data, status, headers, config) {
                $scope.data['success'] = false;
                console.error(data);
            });

        } else {
            // REMOVED LATER
            $scope.data.dayweek = 'THU';
            $scope.data.is_holiday = false;
            $scope.data.pointsheet = { id: 11, year:2017, month: 1 }; // POINTSHEET
            ReleaseApi.Post(ReleaseFactory.ConstructorModel($scope.data))
            .success(function(data, status, headers, config) {
                $scope.data['success'] = true;
                getReleases();
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

    function getReleases(){
        ReleaseApi.Get()
        .success(function(data, status, headers, config) {
            $scope.data.list = data;
        })
        .error(function(e) {
            console.error(e);
        });
    };

    var func_showModal = function () {
        $('#modalFormRelease').on('shown.bs.modal', function () {
            $('#id_year').focus();
        });
        $('#modalFormRelease').modal();
    };

    var func_closeModal = function () {
        $('#modalFormRelease').modal('hide');
    };

    var func_fillForm = function (item) {
        $scope.data.id = item.id;
        $scope.data.date = item.date;
        $scope.data.dayweek = item.dayweek;
        $scope.data.checkin = item.checkin;
        $scope.data.checkout_lunch = item.checkout_lunch;
        $scope.data.checkin_lunch = item.checkin_lunch;
        $scope.data.checkout = item.checkout;
        $scope.data.is_holiday = item.is_holiday;
        $scope.data.type_absence = item.type_absence;
        $scope.data.checkin_absence = item.checkin_absence;
        $scope.data.checkout_absence = item.checkout_absence;
        $scope.data.justification_absence = item.justification_absence;
        $scope.data.file_link = item.file_link;
        $scope.data.pointsheet = item.pointsheet;
    };

    var func_cleanForm = function () {
        $scope.data.id = undefined;
        $scope.data.date = '';
        $scope.data.dayweek = '';
        $scope.data.checkin = '';
        $scope.data.checkout_lunch = '';
        $scope.data.checkin_lunch = '';
        $scope.data.checkout = '';
        $scope.data.is_holiday = '';
        $scope.data.type_absence = '';
        $scope.data.checkin_absence = '';
        $scope.data.checkout_absence = '';
        $scope.data.justification_absence = '';
        $scope.data.file_link = '';
        $scope.data.pointsheet = '';
    };

    var func_addMessageModal = function (type, message) {
        if (type==1)
            $scope.messageModal.type = 'danger';
        else
            $scope.messageModal.type = 'success';
        $scope.messageModal.messages.push(message);
    };

    // Load page
    getReleases();
});