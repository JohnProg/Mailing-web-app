/**
 * Created by johnmachahuay on 6/27/15.
 */
'use strict';

angular.module('app')
    .controller('BDEditCtrl', function ($rootScope, $scope, $filter, $state, BD, utils, ngTableParams) {
        var bdID = $state.params.bdID;
        $scope.showLoaderForm = true;
        $scope.currentContactData = {};
        $scope.bd = BD.bd;

        $scope.$watch("search", function (newvalue, oldvalue) {
            $scope.tableParams ? $scope.tableParams.reload() : '';
            $scope.tableParams2 ? $scope.tableParams2.reload() : '';
        });

        $rootScope.$on('writeText', function(e, data) {
            if(data.module == "db" && data.file.type == "text/csv") {
                data.text = JSON.stringify(utils.getNoRepeatedItems(null, utils.csvJSON(data.text)));
                importEmailsToContactListDB(data);
            }
        });
        function importEmailsToContactListDB (data) {
            $scope.contactListDBTMP = angular.copy($scope.bd);
            $scope.contactListDBTMP.file_name = data.filePath;
            $scope.contactListDBTMP.file = data.file;

            $scope.showLoaderForm = true;
            BD.importEmails($scope.contactListDBTMP)
                .then(function (response) {
                if(response.success){
                    alert("Se importaron los contactos correctamente");
                    BD.getModuleBDService(bdID)
                    .then(function (response) {
                        $scope.showLoaderForm = false;
                        $scope.bd = response.module_db;
                        $scope.bd.status = response.module_db.status == 1 ? true : false;
                        $scope.bd.goodContacts = response.module_db.good_contacts;
                        $scope.bd.badContacts = response.module_db.bad_contacts;

                        setTimeout(function() {
                            $scope.tableParams.reload();
                            $scope.tableParams2.reload();
                        }, 1000)
                        jQuery('#import-db').val("");
                    });

                }else {
                    $scope.showLoaderForm = false;
                    if(response.errors.length == 0) alert("Se guardaron correctamente");
                }
            });
        };


        initData();
        function initData() {
            BD.getModuleBDService(bdID)
            .then(function (response) {
                $scope.showLoaderForm = false;
                $scope.bd = response.module_db;
                $scope.bd.status = response.module_db.status == 1 ? true : false;
                $scope.bd.goodContacts = response.module_db.good_contacts;
                $scope.bd.badContacts = response.module_db.bad_contacts;

                setDataInTables();
            });
        }

        function setDataInTables () {
            $scope.tableParams = new ngTableParams({
                page: 1,
                count: 5,
                sorting: {
                    name: 'asc'
                },
                filter: {}
            }, {
                total: $scope.bd.goodContacts.length,
                getData: function ($defer, params) {
                    $scope.orderedData = params.sorting() ? $filter('orderBy')($scope.bd.goodContacts, params.orderBy()) : $scope.bd.goodContacts;
                    $scope.orderedData = $filter('filterMatchingAttribute')($scope.orderedData, $scope.search);

                    params.total($scope.orderedData.length);
                    $defer.resolve($scope.orderedData.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                }
            });
            $scope.tableParams2 = new ngTableParams({
                page: 1,
                count: 5,
                sorting: {
                    name: 'asc'
                },
                filter: {}
            }, {
                total: $scope.bd.badContacts.length,
                getData: function ($defer, params) {
                    $scope.orderedData2 = params.sorting() ? $filter('orderBy')($scope.bd.badContacts, params.orderBy()) : $scope.bd.badContacts;
                    $scope.orderedData2 = $filter('filterMatchingAttribute')($scope.orderedData2, $scope.search);

                    params.total($scope.orderedData2.length);
                    $defer.resolve($scope.orderedData2.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                }
            })
        }

        $scope.updateModuleBD = function() {
            $scope.showLoaderForm = true;
            BD.updateModuleBDService($scope.bd)
                .then(function(response) {
                    $scope.showLoaderForm = false;
                    if(response.success){
                        alert("Se actualizó con éxito");
                        $state.go("bd.list");
                    }else {
                        alert("Hubo un problema al momento de actualizar.");
                    }
                });
        };
        $scope.cancelToAddNewContactData = function() {
            $scope.currentContactData = {};
        }
        $scope.addNewContactData = function (data) {
            $scope.showLoaderForm = true;
            BD.addContactToBDService(bdID, data)
                .then(function(response) {
                    $scope.showLoaderForm = false;
                    if(response.success){
                        alert("Se agregó un contacto con éxito");
                        data = {};
                        $rootScope.$broadcast('closeModal');

                        BD.getModuleBDService(bdID)
                            .then(function (response) {
                                $scope.showLoaderForm = false;
                                $scope.bd = response.module_db;
                                $scope.bd.status = response.module_db.status == 1 ? true : false;
                                $scope.bd.goodContacts = response.module_db.good_contacts;
                                $scope.bd.badContacts = response.module_db.bad_contacts;

                                $scope.tableParams.reload();
                                $scope.tableParams2.reload();
                            });
                    }else {
                        if(response.errors[0] == "630400") alert("Ya se encuentra registrado el contacto.");
                        else alert("Hubo un problema al momento de agregar un contacto.");
                    }
                });
        }
        angular.element("#name").focus();

        $scope.isEmail = function(email) {
            return utils.isEmail(email);
        }
        $scope.focusModal = function() {
           setTimeout(function () {
                $("#contact_name").focus();
           }, 500)
        }

        $scope.checkboxes = { 'checked': false, items: {} };
        $scope.checkboxes2 = { 'checked': false, items: {} };

        // watch for check all checkbox
        $scope.$watch('checkboxes.checked', function(value) {
            angular.forEach($scope.orderedData, function(item) {
                if (angular.isDefined(item.id)) {
                    $scope.checkboxes.items[item.id] = value;
                }
            });
        });
        $scope.$watch('checkboxes2.checked', function(value) {
            angular.forEach($scope.orderedData2, function(item) {
                if (angular.isDefined(item.id)) {
                    $scope.checkboxes2.items[item.id] = value;
                }
            });
        });

        // watch for data checkboxes
        $scope.$watch('checkboxes.items', function(values) {
            if ($scope.bd.goodContacts.length == 0) {
                return;
            }
            var checked = 0, unchecked = 0,
                total = $scope.bd.goodContacts.length;
            angular.forEach($scope.bd.goodContacts, function(item) {
                checked   +=  ($scope.checkboxes.items[item.id]) || 0;
                unchecked += (!$scope.checkboxes.items[item.id]) || 0;
            });
            if ((unchecked == 0) || (checked == 0)) {
                $scope.checkboxes.checked = (checked == total);
            }
            // grayed checkbox
            angular.element(document.getElementById("select_all")).prop("indeterminate", (checked != 0 && unchecked != 0));
        }, true);
        $scope.$watch('checkboxes2.items', function(values) {
            if ($scope.bd.badContacts.length == 0) {
                return;
            }
            var checked = 0, unchecked = 0,
                total = $scope.bd.badContacts.length;
            angular.forEach($scope.bd.badContacts, function(item) {
                checked   +=  ($scope.checkboxes2.items[item.id]) || 0;
                unchecked += (!$scope.checkboxes2.items[item.id]) || 0;
            });
            if ((unchecked == 0) || (checked == 0)) {
                $scope.checkboxes2.checked = (checked == total);
            }
            // grayed checkbox
            angular.element(document.getElementById("select_all2")).prop("indeterminate", (checked != 0 && unchecked != 0));
        }, true);


        $scope.getQuantityOfSelectedItems = function(list) {
            var newList = [];
            for(var i in Object.keys(list)){
                if(list[Object.keys(list)[i]]) newList.push(Object.keys(list)[i]);
            }
            return newList.length
        }

        $scope.removeItems = function (list) {
            $scope.tmpItemsToRemove = [];
            for(var i in Object.keys(list)){
                if(list[Object.keys(list)[i]]) $scope.tmpItemsToRemove.push(Object.keys(list)[i]);
            }
        }
        $scope.acceptConfirmation = function () {
            $scope.showLoaderForm = true;
            var data = {
                list: $scope.tmpItemsToRemove
            }
            BD.deleteContactsModuleBDService(bdID, data)
                .then(function(response) {
                    $rootScope.$broadcast('closeModal');
                    if(response.success){
                        alert("Se eliminó con éxito");
                        BD.getModuleBDService(bdID)
                            .then(function (response) {
                                $scope.showLoaderForm = false;
                                $scope.bd = response.module_db;
                                $scope.bd.status = response.module_db.status == 1 ? true : false;
                                $scope.bd.goodContacts = response.module_db.good_contacts;
                                $scope.bd.badContacts = response.module_db.bad_contacts;

                                $scope.tableParams.reload();
                                $scope.tableParams2.reload();
                                $scope.checkboxes = { 'checked': false, items: {} };
                                $scope.checkboxes2 = { 'checked': false, items: {} };
                            });
                    }else {
                        $scope.showLoaderForm = false;
                        alert("Hubo un problema al momento de eliminar.");
                    }
                });
        };
    });
