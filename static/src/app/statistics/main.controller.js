'use strict';

angular.module('app')
    .controller('StatisticsCtrl', function ($scope, $state, Statistics) {
        var campaignID = $state.params.campaignID;
        Statistics.getStatistics(campaignID)
            .then(function(response){
                setStatisticsGraphics(response.data);
            });
         function setStatisticsGraphics(data) {
            if(data) {
                $scope.data = {
                    rejected: data.hard_bounces,
                    received: (data.sent - data.hard_bounces),
                    opens: data.opens,
                    unique_opens: parseInt(data.unique_opens * 100/data.sent),
                    unique_clicks: parseInt(data.unique_clicks * 100/data.sent),
                    clicks: data.clicks
                }
            } else {
                $scope.data = {
                    rejected: 0,
                    received: 0,
                    opens: 0,
                    unique_opens: 0,
                    unique_clicks: 0,
                    clicks: 0
                };
            }
        }
    });
