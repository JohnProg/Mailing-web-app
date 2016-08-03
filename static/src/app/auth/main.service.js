/**
 * Created by johnmachahuay on 6/26/15.
 */
'use strict';

angular.module('app')
    .service('Client', function (Service, $q) {
        return {
            user: {},
            loginClientService: function (data) {
                var deferred = $q.defer();
                Service.loginClientService(data)
                    .then(function (response) {
                        deferred.resolve(response.data);
                    });
                return deferred.promise;
            },
            logOutClientService: function () {
                var deferred = $q.defer();
                Service.logOutClientService()
                    .then(function (response) {
                        deferred.resolve(response.data);
                    });
                return deferred.promise;
            }
        }
    });