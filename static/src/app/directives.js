/**
 * Created by johnmachahuay on 6/27/15.
 */
'use strict';

angular.module('app')
    .directive('openModal', function ($rootScope) {
        return {
            restrict: 'A',
            link: function postLink(scope, element, attrs) {
                function setModalTargetFromController(modalTarget) {
                    showModal(modalTarget);
                }

                function setModalTargetAfterClick(e, modalTarget) {
                    var modal = modalTarget === undefined ? jQuery(this).data("target") : modalTarget;
                    showModal(modal);
                }

                function showModal(modal) {
                    var options = {
                        keyboard: false,
                        backdrop: 'static',
                        show: true
                    };
                    jQuery(modal).modal(options);
                }

                function hideModal(modalTarget) {
                    var modal = modalTarget == undefined ? ".modal" : modalTarget;
                    jQuery(modal).modal("hide");
                }

                element.bind('click', setModalTargetAfterClick);

                $rootScope.$on("openModal", function (e, modalTarget) {
                    setModalTargetFromController(modalTarget);
                });

                $rootScope.$on("closeModal", function (e, modalTarget) {
                    hideModal(modalTarget);
                });
            }
        };
    })
    .directive('collapsible', function () {
        return {
            restrict: 'A',
            link: function postLink(scope, element, attrs) {
                element.find('.btn-collapsible').bind('click', showOrHideCollapsibleBody);
                function showOrHideCollapsibleBody(event) {
                    event.preventDefault();
                    var a = jQuery(this);
                    if (a.hasClass("active")) {
                        a.parent().siblings(".collapsible-body").stop(true, true).slideDown({duration: 350, queue: !1});
                        a.removeClass("active");
                    } else {
                        a.parent().siblings(".collapsible-body").stop(true, true).slideUp({duration: 350, queue: !1});
                        a.addClass("active");
                    }
                }
            }
        };
    })
    .directive('ngFileSelect', function ($rootScope, fileReader) {
        return {
            link: function ($scope, el, attrs) {
                //READ TEXT
                function readText() {
                    fileReader.readAsText($scope.fileToRead, $scope)
                        .then(function (result) {
                            var data = {
                                text: result,
                                file: $scope.fileToRead,
                                module: $scope.module,
                                filePath: el.val()
                            };
                            $rootScope.$emit('writeText', data);
                        });
                }
                // READ ANY FILE
                function readAnyFile() {
                    var data = {file: $scope.fileToRead, module: $scope.module};
                    $rootScope.$emit('anyFile', data);
                }
                function eventTrigger(evt) {
                    angular.element(el).trigger('click');
                }
                function inputFileChanged(evt) {
                    $scope.fileToRead = (evt.srcElement || evt.target).files[0];
                    $scope.module = attrs.module;
                    $scope.fileType = attrs.filetype;

                    // Check for the various File API support.
                    if (window.FileReader) {
                        if ($scope.fileType == 'txt') readText();
                        if ($scope.fileType == 'any') readAnyFile();
                    } else {
                        alert('FileReader are not supported in this browser.');
                    }
                }

                if (attrs.parent) {
                    el.parents(attrs.parent).find(".btn-trigger").on("click", eventTrigger);
                    angular.element(el).on("change", inputFileChanged);
                }
            }
        };
    })
.directive('pieChart', function ($timeout) {
        return {
            restrict: 'A',
            scope: {
                data: "="
            },
            link: function postLink($scope, element, attrs) {

                $scope.$watch('data', handleViewModelUpdate, true);

                function handleViewModelUpdate() {
                    var options = {
                        bindto: '.chart',
                        size: {
                            height: 300,
                            width: 300
                        },
                        data: {
                            order: 'asc',
                            columns: [
                                ['Correos rechazados', $scope.data["rejected"]],
                                ['Correos recibidos', $scope.data["received"]]
                            ],
                            type: 'pie',
                            colors: {
                                "Correos recibidos": '#3FDBC2',
                                "Correos rechazados": 'rgba(99, 135, 166, 1)'
                            },
                            color: function (color, d) {
                                // d will be 'id' when called for legends
                                return d.id && d.id === 'data3' ? d3.rgb(color).darker(d.value / 150) : color;
                            },
                            onclick: function (d, i) {
                                alert("onclick" + d + "  " + i);
                            },
                            onmouseover: function (d, i) {
                            },
                            onmouseout: function (d, i) {
                            }

                        },
                        legend: {
                            position: 'bottom',
                            show: true
                        },
                        tooltip: {
                            show: true,
                            grouped: true
                        }
                    };

                    $timeout(function () {
                        var chart = c3.generate(options);
                        jQuery('.c3 .c3-chart-arc').eq(1).find("text").attr("transform", "translate(5.13279266711413, 10.235437791419702)");
                        //$('.c3 .c3-chart-arc').eq(1).find("text").attr("transform", "translate(5.13279266711413, 10.235437791419702)");
                    }, 50);
                }
            }
        }
    });