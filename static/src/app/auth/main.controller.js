/**
 * Created by johnmachahuay on 6/26/15.
 */
'use strict';

angular.module('app')
    .controller('ClientCtrl', function (Client, $scope, CODE_ERRORS, CODE_SUCCESS) {
        $scope.client = {};

        $scope.loginClientUser = function () {
            $scope.showLoaderForm = true;
            Client.loginClientService($scope.client)
                .then(function (response) {
                    $scope.showLoaderForm = false;
                    response.success ? afterLoginSuccessResponse(response) : afterLoginErrorResponse(response);
                })
        };

        function afterLoginSuccessResponse(response) {
            alert(CODE_SUCCESS[100000].message);
            location.href = "/dashboard/#/campaign/create"
        }

        function afterLoginErrorResponse(response) {
            alert(CODE_ERRORS[response.errors[0]].message);
        }
    });
