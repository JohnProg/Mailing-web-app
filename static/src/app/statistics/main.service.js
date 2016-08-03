/**
 * Created by johnmachahuay on 6/26/15.
 */
'use strict';

angular.module('app')
    .service('Statistics', function (Service, $q) {
        return {
            statistic: {},
            statistics: [],
            getBDS: function (data) {
                var deferred = $q.defer();
                Service.loginClientService(data)
                    .then(function (response) {
                        deferred.resolve(response.data);
                    });
                return deferred.promise;
            },
            getStatistics: function(campaignId) {
                var deferred = $q.defer();
                Service.getStatisticsCampaignsService(campaignId)
                .then(function(response){
                    deferred.resolve(response.data);
                });
                return deferred.promise;
            }
        }
    });