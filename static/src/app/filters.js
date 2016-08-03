/**
 * Created by johnmachahuay on 6/27/15.
 */
'use strict';

angular.module('app')
    .filter("filterStatus", function () {
        return function (list, status) {
            if (!status)
                return list;
            else if (typeof list !== "undefined") {
                var listCopy = [];
                angular.forEach(list, function (queryInfo, index) {
                    if (queryInfo.status)
                        listCopy.push(queryInfo);
                });
                return listCopy;
            }
            return list;
        };
    })
    .filter("filterMatchingAttribute", function () {
        return function (list, substring) {
            if ((typeof substring === "undefined") || (substring == ""))
                return list;
            else if (typeof list !== "undefined") {
                var listCopy = [];
                angular.forEach(list, function (object, index) {
                    for (var property in object) {
                        if (object.hasOwnProperty(property)) {
                            if (object[property] && object[property].toString().toLowerCase().indexOf(substring.toLowerCase()) != -1) {
                                listCopy.push(object);
                                break;
                            }
                        }
                    }
                });
                return listCopy;
            }
            else
                return list;
        };
    });