/**
 * Created by johnmachahuay on 6/26/15.
 */
angular.module('app')
    .controller('NavBarCtrl', function (Client, $scope, CODE_ERRORS) {

        function afterLogOutSuccessResponse() {
            location.href = "/"
        }

        function afterLogOutErrorResponse(response) {
            alert(CODE_ERRORS[response.errors[0]].message);
        }

        $scope.acceptConfirmation = function () {
            $scope.showLoaderForm = true;
            Client.logOutClientService()
                .then(function (response) {
                    $scope.showLoaderForm = false;
                    response.success ? afterLogOutSuccessResponse() : afterLogOutErrorResponse(response);
                })
        };
    });