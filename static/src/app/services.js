/**
 * Created by johnmachahuay on 6/26/15.
 */
angular.module('app')
    .service('Service', function ($http, END_POINT, API_SERVER) {
        return {
            loginClientService: function (data) {
                var url = API_SERVER + END_POINT.loginClient;
                return $http.post(url, data);
            },
            logOutClientService: function () {
                var url = API_SERVER + END_POINT.logoutClient;
                return $http.get(url);
            },

            getListGeneralTemplateService: function () {
                var url = API_SERVER + END_POINT.getListGeneralTemplate;
                return $http.get(url);
            },
            createModuleTemplateService: function (data) {
                var url = API_SERVER + END_POINT.createModuleTemplate;
                return $http.post(url, data);
            },
            updateModuleTemplateService: function (data) {
                var url = API_SERVER + END_POINT.updateModuleTemplate.replace('module_template_id', data.id);
                return $http.post(url, data);
            },
            getModuleTemplateService: function (templateID) {
                var url = API_SERVER + END_POINT.getModuleTemplate.replace('module_template_id', templateID);
                return $http.get(url);
            },
            deleteModuleTemplateService: function (data) {
                var url = API_SERVER + END_POINT.deleteModuleTemplate.replace('module_template_id', data.id);
                return $http.delete(url, data);
            },

            createModuleCampaignService: function (data) {
                var url = API_SERVER + END_POINT.createModuleCampaign;
                return $http.post(url, data);
            },
            updateModuleCampaignService: function (data) {
                var url = API_SERVER + END_POINT.updateModuleCampaign.replace('mailing_id', data.id);
                return $http.post(url, data);
            },
            getModuleCampaignService: function (mailingID) {
                var url = API_SERVER + END_POINT.getModuleCampaign.replace('mailing_id', mailingID);
                return $http.get(url);
            },
            deleteModuleCampaignService: function (data) {
                var url = API_SERVER + END_POINT.deleteModuleCampaign.replace('mailing_id', data.id);
                return $http.delete(url, data);
            },

            createModuleBDService: function (data) {
                var url = API_SERVER + END_POINT.createModuleBD;
                return $http.post(url, data);
            },
            updateModuleBDService: function (data) {
                var url = API_SERVER + END_POINT.updateModuleBD.replace('module_db_id', data.id);
                return $http.post(url, data);
            },
            getModuleBDService: function (templateID) {
                var url = API_SERVER + END_POINT.getModuleBD.replace('module_db_id', templateID);
                return $http.get(url);
            },
            getStatisticsCampaignsService: function (mailingID) {
                var url = API_SERVER + END_POINT.getStatisticsModuleCampaign.replace('mailing_id', mailingID);
                return $http.get(url);
            },
            deleteModuleBDService: function (data) {
                var url = API_SERVER + END_POINT.deleteModuleBD.replace('module_db_id', data.id);
                return $http.delete(url, data);
            },
            deleteContactsModuleBDService: function (id, data) {
                var url = API_SERVER + END_POINT.deleteContactsModuleBD.replace('module_db_id', id);
                return $http.post(url, data);
            },

            addContactToBDService: function (bdID, data) {
                var url = API_SERVER + END_POINT.addContactToBD.replace('module_db_id', bdID);
                return $http.post(url, data);
            },
            importContactToBDService: function (data) {
                var url = API_SERVER + END_POINT.importContactToBD.replace("module_db_id", data.id);

                var fd = new FormData();
                fd.append("file", data.file);
                fd.append("file_name", data.file_name);

                return $http.post(url, fd, {
                    transformRequest: angular.identity,
                    headers: {'Content-Type': undefined}
                });
            }
        }
    })
    .service('dataService', ['$http', '$q', function ($http, $q) {
        return {
            all: function (url) {
                var deferred = $q.defer();
                $http.get(url)
                    .success(function (data, status, headers, config) {
                        deferred.resolve(data, status, headers, config);
                    })
                    .error(function (data, status, headers, config) {
                        deferred.reject(data, status, headers, config);
                    });
                return deferred.promise;
            }
        };
    }]);