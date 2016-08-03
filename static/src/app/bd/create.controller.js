/**
 * Created by johnmachahuay on 6/27/15.
 */
'use strict';

angular.module('app')
    .controller('BDCreateCtrl', function (BD, $scope, $state) {
        $scope.bd = BD.bd;

        $scope.createModuleBD = function () {
            $scope.showLoaderForm = true;
            BD.createModuleBDService($scope.bd)
                .then(function(response) {
                    $scope.showLoaderForm = false;
                    if(response.success){
                        alert("Se guardó con éxito");
                        $state.go("bd.edit", {bdID: response.data.id});
                    }else {
                        alert("Hubo un problema al momento de crear.");
                    }
                });
        }
        setTimeout(function() {
            angular.element("#name").val("");
            angular.element("#name").focus();
        }, 200);
    });
