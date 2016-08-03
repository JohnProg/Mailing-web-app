/**
 * Created by johnmachahuay on 6/26/15.
 */
'use strict';

angular.module('app')
    .service('BD', function (Service, $q) {
        return {
            bd: {
                list_name: '',
                status: true,
                origin: 1,
                destination: 2,
                goodContacts: [],
                badContacts: []
            },
            bds: [],
            createModuleBDService: function (data) {
                var deferred = $q.defer();
                Service.createModuleBDService(data)
                    .then(function (response) {
                        deferred.resolve(response.data);
                    });
                return deferred.promise;
            },
            getModuleBDService: function (templateID) {
                var deferred = $q.defer();
                Service.getModuleBDService(templateID)
                    .then(function (response) {
                        deferred.resolve(response.data);
                    });
                return deferred.promise;
            },
            deleteModuleBDService: function (data) {
                var deferred = $q.defer();
                Service.deleteModuleBDService(data)
                    .then(function (response) {
                        deferred.resolve(response.data);
                    });
                return deferred.promise;
            },
            deleteContactsModuleBDService: function (id, data) {
                var deferred = $q.defer();
                Service.deleteContactsModuleBDService(id, data)
                    .then(function (response) {
                        deferred.resolve(response.data);
                    });
                return deferred.promise;
            },
            updateModuleBDService: function (data) {
                var deferred = $q.defer();
                Service.updateModuleBDService(data)
                    .then(function (response) {
                        deferred.resolve(response.data);
                    });
                return deferred.promise;
            },
            addContactToBDService: function (bdID, data) {
                var deferred = $q.defer();
                Service.addContactToBDService(bdID, data)
                    .then(function (response) {
                        deferred.resolve(response.data);
                    });
                return deferred.promise;
            },
            importEmails: function(data) {
                var deferred = $q.defer();
                Service.importContactToBDService(data)
                    .then(function (response) {
                        deferred.resolve(response.data);
                    });
                return deferred.promise;
            }
        }
    });