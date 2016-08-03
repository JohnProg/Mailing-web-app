'use strict';

angular.module('app')
    .controller('TemplateListCtrl', function ($scope, $rootScope, $state, $filter, Template, ngTableParams, dataService, END_POINT) {
        $scope.search = "";
        $scope.status = false;
        $scope.showLoaderForm = true;

        $scope.$watch("status", function (newvalue, oldvalue) {
            $scope.tableParams ? $scope.tableParams.reload() : '';
        });
        $scope.$watch("search", function (newvalue, oldvalue) {
            $scope.tableParams ? $scope.tableParams.reload() : '';
        });
        init();
        function init () {
            dataService.all(END_POINT.getListModuleTemplate)
            .then(function (results) {
                $scope.tableParams = new ngTableParams({
                        page: 1,
                        count: 5,
                        sorting: {
                            name: 'asc'
                        },
                        filter: {}
                    },
                    {
                        total: results.module_templates.length,
                        getData: function ($defer, params) {
                            $scope.showLoaderForm = false;
                            $scope.templates = results.module_templates;
                            var orderedData = params.sorting() ? $filter('orderBy')(results.module_templates, params.orderBy()) : results.module_templates;
                            orderedData = $filter('filterStatus')(orderedData, $scope.status);
                            orderedData = $filter('filterMatchingAttribute')(orderedData, $scope.search);

                            params.total(orderedData.length);
                            $defer.resolve(orderedData.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                        }
                    });
            });
        }
        $scope.removeItem = function (item) {
            $scope.tmpItemToRemove = item;
        }
        $scope.acceptConfirmation = function () {
            $scope.showLoaderForm = true;
            Template.deleteModuleTemplateService($scope.tmpItemToRemove)
                .then(function(response) {
                    $scope.showLoaderForm = false;
                    $rootScope.$broadcast('closeModal');
                    if(response.success){
                        alert("Se eliminó con éxito");
                        deleteTemplate();
                    }else {
                        alert("Hubo un problema al momento de eliminar.");
                    }
                });
        };
         function deleteTemplate() {
             for (var i in $scope.templates) {
                 var item = $scope.templates[i];
                 if(item.id == $scope.tmpItemToRemove.id) {
                     $scope.templates.splice(i, 1);
                     $scope.tableParams.reload();
                     break;
                 }
             }
         }
        angular.element("#search").focus();
    });
