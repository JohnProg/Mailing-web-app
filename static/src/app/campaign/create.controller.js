/**
 * Created by johnmachahuay on 6/27/15.
 */
'use strict';

angular.module('app')
    .controller('CampaignCreateCtrl', function ($rootScope, $state, $scope, utils, Campaign, dataService, $filter, BD, ngTableParams, END_POINT) {
        $scope.campaign = Campaign.campaign;
        $scope.search = "";
        $scope.dbs = [];
        $scope.goToStep = function(step) {
            $scope.step = step;
            angular.element(".collapsible-body").stop(true, true).slideUp({duration: 350, queue: !1});
            angular.element(".btn-collapsible").addClass("active");

            angular.element(".collapsible-body").eq(step-1).stop(true, true).slideDown({duration: 350, queue: !1});
            angular.element(".btn-collapsible").eq(step-1).removeClass("active");
        };

        $scope.isInValidateStep1 = function() {
            return !($scope.campaign.from_name &&
                    $scope.campaign.reply_email &&
                    $scope.campaign.subject &&
                    $scope.campaign.link_redirect_to &&
                    utils.isEmail($scope.campaign.from_name) &&
                    utils.isEmail($scope.campaign.reply_email));
        }
        $scope.isInValidateStep2 = function() {
            return $scope.getQuantityOfSelectedItems($scope.checkboxes.items) == 0;
        }
        $scope.isInValidateStep3 = function() {
            for(var i in $scope.templates){
                if($scope.templates[i].selected) return false;
            }
            return true;
        }
        $scope.isInValidateStep4 = function() {
            return !($scope.campaign.title &&
                    $scope.campaign.subtitle &&
                    $scope.campaign.body_section1);
        }
        $scope.getQuantityOfSelectedItems = function(list) {
            var newList = [];
            for(var i in Object.keys(list)){
                if(list[Object.keys(list)[i]]) newList.push(Object.keys(list)[i]);
            }
            return newList.length
        }

        dataService.all(END_POINT.getListModuleBD)
            .then(function (results) {
                $scope.tableParams = new ngTableParams({
                        page: 1,
                        count: 4,
                        filter: {}
                    },
                    {
                        total: getActiveItemsDBS(results.module_dbs).length,
                        getData: function ($defer, params) {
                            $scope.showLoaderForm = false;
                            $scope.dbs = getActiveItemsDBS(results.module_dbs);
                            $scope.orderedData = params.sorting() ? $filter('orderBy')(getActiveItemsDBS(results.module_dbs), params.orderBy()) : getActiveItemsDBS(results.module_dbs);
                            params.total($scope.orderedData.length);
                            $defer.resolve($scope.orderedData.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                        }
                    });
            });
        dataService.all(END_POINT.getListModuleTemplate)
            .then(function (results) {
                $scope.templates = getActiveItems(results.module_templates);
            });
        function getActiveItems(list) {
            var newList = [];
            for(var i in list) {
                if(list[i].status == 1) newList.push(list[i])
            }
            return newList;
        }
        function getActiveItemsDBS(list) {
            var newList = [];
            for(var i in list) {
                if(list[i].status == 1 && (list[i].good_contacts + list[i].bad_contacts) > 0) newList.push(list[i])
            }
            return newList;
        }

        $scope.checkboxes = { 'checked': false, items: {} };

        // watch for check all checkbox
        $scope.$watch('checkboxes.checked', function(value) {
            angular.forEach($scope.orderedData, function(item) {
                if (angular.isDefined(item.id)) {
                    $scope.checkboxes.items[item.id] = value;
                }
            });
        });

        // watch for data checkboxes
        $scope.$watch('checkboxes.items', function(values) {
            if ($scope.dbs.length == 0) {
                return;
            }
            var checked = 0, unchecked = 0,
                total = $scope.dbs.length;
            angular.forEach($scope.dbs, function(item) {
                checked   +=  ($scope.checkboxes.items[item.id]) || 0;
                unchecked += (!$scope.checkboxes.items[item.id]) || 0;
            });
            if ((unchecked == 0) || (checked == 0)) {
                $scope.checkboxes.checked = (checked == total);
            }
            // grayed checkbox
            angular.element(document.getElementById("select_all")).prop("indeterminate", (checked != 0 && unchecked != 0));
        }, true);

        $scope.selectTemplate = function(template) {
            for(var i in $scope.templates) {
                $scope.templates[i].selected = false;
            }
            template.selected = true;
            $scope.currentTemplate = template;
        }
        function getIdsDB(list) {
            var newList = [];
            for(var i in Object.keys(list)){
                if(list[Object.keys(list)[i]]) newList.push(Object.keys(list)[i]);
            }
            return newList;
        }
        $scope.saveCampaign = function (type) {
            $scope.showLoaderForm = true;
            var data = angular.copy($scope.campaign);
                data.type = type;
                data.template_id = $scope.currentTemplate.id;
                data.db_ids = getIdsDB($scope.checkboxes.items);
            Campaign.createModuleCampaignService(data)
                .then(function(response) {
                    $scope.showLoaderForm = false;
                    if(response.success){
                        alert("Se guardó con éxito");
                        $state.go("campaign.list");
                    }else {
                        alert("Hubo un problema al momento de crear.");
                    }
                });
        }
    });
