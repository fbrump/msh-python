
myApp.controller('releasesCtrl', function ($scope, ReleaseApi, ReleaseFactory, PointsheetApi, $timeout) {
    $scope.messageModal = { type: '', messages: [] };
    $scope.data = {
        model: { error:false, message:'', is_submit_disabled: false },
        success: false,
        is_holiday: false
    }

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
            $scope.data.dayweek = getDayWeek($('#id_date'));
            var _ps = func_getPointsheetSelected($scope.data.pointsheet_id);
            if (_ps != null){
                $scope.data.pointsheet = _ps;
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
            else {
                func_messageModal(true, 'Pointsheet is required');
            }
        }
    };

    $scope.updateForm = function (item) {
        func_getPointsheets();
        $timeout(function () {
            func_fillForm(item);
            func_showModal();
        }, 1000)
    };

    $scope.showForm = function () {
        func_cleanForm();
        func_getPointsheets();
        func_showModal();
    };

    $scope.changePointsheetModal = function (item) {
        console.log(item);
        if (!angular.isUndefined(item))
        {
            _r = func_getPointsheetSelected(item);
            if (_r != null){
                _d = new Date(_r.year, _r.month, 1);
                $scope.data.date = formatDate(_d);
                $('#id_date').datepicker('setDate', $scope.data.date);
            }
        }else{
            console.log('Selected empty item (SELECT)');
        }
    };

    $scope.shwRemoveRelease = function (release) {
        
        func_fillForm(release);
        func_showModalDelete();

    };

    $scope.deleteRelease = function () {
        // body...
        func_disabledSubmitModal(true);
        func_removeRelease($scope.data);
    };

    var func_getPointsheetSelected = function (item) {
        _register = $scope.pointsheets.filter(function(el) {
            return el.id==item;
        });
        if (_register.length==0){
            _register = null;
            console.log('not exist')
        }else{
            _register = _register[0];
            console.log('exist')
        }
        console.log(_register);
        console.log('selcted one existent item');
        return _register;
    };

    var getReleases = function (){
        ReleaseApi.Get()
        .success(function(data, status, headers, config) {
            $scope.data.list = data;
        })
        .error(function(e) {
            console.error(e);
        });
    };

    var func_showModal = function () {
        func_messageModal(false, null);
        var _model = $('#modalFormRelease');
        _model.on('shown.bs.modal', function () {
            $("#id_pointsheet").focus();
        });
        _model.modal();
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
        $scope.data.pointsheet_id = item.pointsheet.id;
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
        $scope.data.pointsheet_id = undefined;
    };

    var func_addMessageModal = function (type, message) {
        if (type==1)
            $scope.messageModal.type = 'danger';
        else
            $scope.messageModal.type = 'success';
        $scope.messageModal.messages.push(message);
    };

    var func_getPointsheets = function (){
        PointsheetApi.Get()
        .success(function(data, status, headers, config) {
            $scope.pointsheets = data;
        })
        .error(function(e) {
            console.error(e);
        });
    };

    var func_messageModal = function(show, message){
        $scope.data.model.error = show;
        if (show == true){
            $scope.data.model.message = message;
            console.error(message);
        }
    };

    var func_showModalDelete = function () {
        func_messageModal(false, null);
        var _model = $('#modalDeleteRelease');
        _model.on('shown.bs.modal', function () {
            $("#id_pointsheet").focus();
        });
        _model.modal();
    };

    var func_closeModalDelete = function () {
        $('#modalDeleteRelease').modal('hide');
    };

    var func_disabledSubmitModal = function (disabled) {
        $scope.data.model.is_submit_disabled = disabled;
    };

    var func_removeRelease = function(release){
        ReleaseApi.Delete(release.id)
        .success(function(data, status, headers, config) {
            getReleases();
            $scope.data['success'] = true;
            func_closeModalDelete();
            func_disabledSubmitModal(false);
        })
        .error(function(data, status, headers, config) {
            console.error(data);
            $scope.data['success'] = false;
            func_disabledSubmitModal(false);
        });
    };

    // Load page
    getReleases();
});