/**
 * Created by johnmachahuay on 6/26/15.
 */

angular
    .module('app')
    .config(['$httpProvider', '$stateProvider', '$urlRouterProvider',
        '$interpolateProvider',
        function($httpProvider, $stateProvider, $urlRouterProvider, $interpolateProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
            $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');

        $stateProvider
            .state('campaign', {
                abstract: true,
                url: '/campaign',
                templateUrl: '../static/src/app/campaign/base.html'
            })
            .state('campaign.list', {
                url: '/list',
                templateUrl: '../static/src/app/campaign/list.html',
                controller: 'CampaignListCtrl'
            })
            .state('campaign.create', {
                url: '/create',
                templateUrl: '../static/src/app/campaign/create.html',
                controller: 'CampaignCreateCtrl'
            })
            .state('campaign.edit', {
                url: '/:campaignID/edit',
                templateUrl: '../static/src/app/campaign/edit.html',
                controller: 'CampaignEditCtrl'
            })

            .state('bd', {
                abstract: true,
                url: '/contact-list',
                templateUrl: '../static/src/app/bd/base.html'
            })
            .state('bd.list', {
                url: '/list',
                templateUrl: '../static/src/app/bd/list.html',
                controller: 'BDListCtrl'
            })
            .state('bd.create', {
                url: '/create',
                templateUrl: '../static/src/app/bd/create.html',
                controller: 'BDCreateCtrl'
            })
            .state('bd.edit', {
                url: '/:bdID/edit',
                templateUrl: '../static/src/app/bd/edit.html',
                controller: 'BDEditCtrl'
            })

            .state('template', {
                abstract: true,
                url: '/template',
                templateUrl: '../static/src/app/template/base.html'
            })
            .state('template.list', {
                url: '/list',
                templateUrl: '../static/src/app/template/list.html',
                controller: 'TemplateListCtrl'
            })
            .state('template.create', {
                url: '/create',
                templateUrl: '../static/src/app/template/create.html',
                controller: 'TemplateCreateCtrl'
            })
            .state('template.edit', {
                url: '/:templateID/edit',
                templateUrl: '../static/src/app/template/edit.html',
                controller: 'TemplateEditCtrl'
            })

            .state('statistics', {
                url: '/statistics/:campaignID/',
                templateUrl: '../static/src/app/statistics/main.html',
                controller: 'StatisticsCtrl'
            })

            .state('profile', {
                url: '/profile',
                templateUrl: '../static/src/app/profile/profile.html',
                controller: 'ClientCtrl'
            });
        //$urlRouterProvider.otherwise('/campaign/list');
    }]);