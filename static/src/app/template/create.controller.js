/**
 * Created by johnmachahuay on 6/27/15.
 */
'use strict';

angular.module('app')
    .controller('TemplateCreateCtrl', function ($scope, Template, $state) {
        $scope.template = {};
        Template.getListGeneralTemplate()
            .then(function (response) {
                $scope.generalTemplates = response.templates;
                setTimeout(function() {
                    angular.element("#name").val("");
                    angular.element("#name").focus();
                    $scope.template = {
                        name: "",
                        status: true,
                        colors: {
                            color1 : '#ffffff',
                            color2 : '#ffffff',
                            color3 : '#ffffff',
                            color4 : '#ffffff',
                            color5 : '#ffffff',
                            color6 : '#ffffff',
                            color7 : '#ffffff',
                            color8 : '#ffffff',
                            color9 : '#ffffff'
                        }
                    }
                }, 200)

            });



        $scope.createModuleTemplate = function() {
            $scope.showLoaderForm = true;
            $scope.template.colorsJSON = JSON.stringify($scope.template.colors);
            Template.createModuleTemplateService($scope.template)
                .then(function(response) {
                    $scope.showLoaderForm = false;
                    if(response.success){
                        alert("Se guardó con éxito");
                        $state.go("template.list");
                    }else {
                        alert("Hubo un problema al momento de crear.");
                    }
                });
        }
    });
