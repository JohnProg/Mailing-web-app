'use strict';

angular
    .module('app', ['ngCookies', 'ui.router', 'ngTable'])
    .run(function ($http, $cookies, $rootScope, $state, $stateParams) {
        $http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
        $rootScope.$state = $state;
        $rootScope.$stateParams = $stateParams;
    })
    .constant('API_SERVER', location.origin);
