/**
 * Created by johnmachahuay on 6/26/15.
 */
'use strict';

angular.module('app')
    .service('Template', function (Service, $q) {
        return {
            template: {
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
            },
            templates: [],
            getListGeneralTemplate: function () {
                var deferred = $q.defer();
                Service.getListGeneralTemplateService()
                    .then(function (response) {
                        deferred.resolve(response.data);
                    });
                return deferred.promise;
            },
            createModuleTemplateService: function (data) {
                var deferred = $q.defer();
                Service.createModuleTemplateService(data)
                    .then(function (response) {
                        deferred.resolve(response.data);
                    });
                return deferred.promise;
            },
            getModuleTemplateService: function (templateID) {
                var deferred = $q.defer();
                Service.getModuleTemplateService(templateID)
                    .then(function (response) {
                        deferred.resolve(response.data);
                    });
                return deferred.promise;
            },
            deleteModuleTemplateService: function (data) {
                var deferred = $q.defer();
                Service.deleteModuleTemplateService(data)
                    .then(function (response) {
                        deferred.resolve(response.data);
                    });
                return deferred.promise;
            },
            updateModuleTemplateService: function (data) {
                var deferred = $q.defer();
                Service.updateModuleTemplateService(data)
                    .then(function (response) {
                        deferred.resolve(response.data);
                    });
                return deferred.promise;
            }
        }
    });