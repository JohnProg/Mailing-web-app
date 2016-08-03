/**
 * Created by johnmachahuay on 6/26/15.
 */
'use strict';

angular.module('app')
    .service('Campaign', function (Service, $q) {
        return {
            campaign: {
                campaign_name: "demo1",
                from_name: "john@mailinator.com",
                reply_email: "john@mailinator.com",
                subject: "Test!",
                link_redirect_to: "https://play.spotify.com/album/2yNaksHgeMQM9Quse463b5",
                titile: "",
                subtitle: "",
                body_section1: "",
                body_section2: ""
            },
            campaigns: [],
            createModuleCampaignService: function (data) {
                var deferred = $q.defer();
                Service.createModuleCampaignService(data)
                    .then(function (response) {
                        deferred.resolve(response.data);
                    });
                return deferred.promise;
            },
            getModuleCampaignService: function (templateID) {
                var deferred = $q.defer();
                Service.getModuleCampaignService(templateID)
                    .then(function (response) {
                        deferred.resolve(response.data);
                    });
                return deferred.promise;
            },
            deleteModuleCampaignService: function (data) {
                var deferred = $q.defer();
                Service.deleteModuleCampaignService(data)
                    .then(function (response) {
                        deferred.resolve(response.data);
                    });
                return deferred.promise;
            },
            updateModuleCampaignService: function (data) {
                var deferred = $q.defer();
                Service.updateModuleCampaignService(data)
                    .then(function (response) {
                        deferred.resolve(response.data);
                    });
                return deferred.promise;
            }
        }
    });