'use strict';

angular.module('app')
    .controller('BDListCtrl', function ($rootScope, $scope, $filter, BD, ngTableParams, dataService, END_POINT) {
        $scope.search = "";
        $scope.status = false;
        $scope.showLoaderForm = true;

        $scope.$watch("status", function (newvalue, oldvalue) {
            $scope.tableParams ? $scope.tableParams.reload() : '';
        });
        $scope.$watch("search", function (newvalue, oldvalue) {
            $scope.tableParams ? $scope.tableParams.reload() : '';
        });

        dataService.all(END_POINT.getListModuleBD)
            .then(function (results) {
                $scope.tableParams = new ngTableParams({
                        page: 1,
                        count: 10,
                        sorting: {
                            name: 'asc'
                        },
                        filter: {}
                    },
                    {
                        total: results.module_dbs.length,
                        getData: function ($defer, params) {
                            $scope.showLoaderForm = false;
                            $scope.dbs = results.module_dbs;
                            var orderedData = params.sorting() ? $filter('orderBy')(results.module_dbs, params.orderBy()) : results.module_dbs;
                            orderedData = $filter('filterStatus')(orderedData, $scope.status);
                            orderedData = $filter('filterMatchingAttribute')(orderedData, $scope.search);

                            params.total(orderedData.length);
                            $defer.resolve(orderedData.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                        }
                    });
            });
        $scope.removeItem = function (item) {
            $scope.tmpItemToRemove = item;
        }
        $scope.acceptConfirmation = function () {
            $scope.showLoaderForm = true;
            BD.deleteModuleBDService($scope.tmpItemToRemove)
                .then(function(response) {
                    $scope.showLoaderForm = false;
                    $rootScope.$broadcast('closeModal');
                    if(response.success){
                        alert("Se eliminó con éxito");
                        deleteBD();
                    }else {
                        alert("Hubo un problema al momento de eliminar.");
                    }
                });
        };
         function deleteBD() {
             for (var i in $scope.dbs) {
                 var item = $scope.dbs[i];
                 if(item.id == $scope.tmpItemToRemove.id) {
                     $scope.dbs.splice(i, 1);
                     $scope.tableParams.reload();
                     break;
                 }
             }
         }
        angular.element("#search").focus();
    });
