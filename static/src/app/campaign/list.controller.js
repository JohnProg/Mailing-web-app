'use strict';

angular.module('app')
    .controller('CampaignListCtrl', function ($rootScope, $scope, $filter, Campaign, ngTableParams, dataService, END_POINT) {
        $scope.search = "";
        $scope.status = false;

        $scope.$watch("status", function (newvalue, oldvalue) {
            $scope.tableParams ? $scope.tableParams.reload() : '';
        });
        $scope.$watch("search", function (newvalue, oldvalue) {
            $scope.tableParams ? $scope.tableParams.reload() : '';
        });
        dataService.all(END_POINT.getListModuleCampaign)
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
                        total: results.campaigns.length,
                        getData: function ($defer, params) {
                            $scope.campaigns = results.campaigns;
                            var orderedData = params.sorting() ? $filter('orderBy')(results.campaigns, params.orderBy()) : results.campaigns;
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
            Campaign.deleteModuleCampaignService($scope.tmpItemToRemove)
                .then(function(response) {
                    $scope.showLoaderForm = false;
                    $rootScope.$broadcast('closeModal');
                    if(response.success){
                        alert("Se eliminó con éxito");
                        deleteCampaign();
                    }else {
                        alert("Hubo un problema al momento de eliminar.");
                    }
                });
        };
        function deleteCampaign() {
             for (var i in $scope.campaigns) {
                 var item = $scope.campaigns[i];
                 if(item.id == $scope.tmpItemToRemove.id) {
                     $scope.campaigns.splice(i, 1);
                     $scope.tableParams.reload();
                     break;
                 }
             }
         }
        angular.element("#search").focus();
    });
