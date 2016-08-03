/**
 * Created by johnmachahuay on 6/27/15.
 */
'use strict';

angular.module('app')
    .controller('TemplateEditCtrl', function ($scope, Template, $state) {
        var templateID = $state.params.templateID;
        $scope.showLoaderForm = true;
        Template.getModuleTemplateService(templateID)
            .then(function (response) {
                $scope.showLoaderForm = false;
                $scope.template = response.module_template;
                $scope.template.name = response.module_template.template_name;
                $scope.template.status = response.module_template.status == 1 ? true : false;
                $scope.template.colors = $scope.template.colors ? JSON.parse($scope.template.colors) : Template.template.colors;
            });

        $scope.updateModuleTemplate = function() {
            $scope.showLoaderForm = true;
            $scope.template.colorsJSON = JSON.stringify($scope.template.colors);
            Template.updateModuleTemplateService($scope.template)
                .then(function(response) {
                    $scope.showLoaderForm = false;
                    if(response.success){
                        alert("Se actualizó con éxito");
                        $state.go("template.list");
                    }else {
                        alert("Hubo un problema al momento de actualizar.");
                    }
                });
        }
        angular.element("#name").focus();
    });
