/**
 * Created by johnmachahuay on 7/1/15.
 */
angular.module('app')
    .factory('utils', function () {
        return {
            isEmail: function isValidEmail(email) {
                if (email != undefined) {
                    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
                    re = re.test(email);
                    if (re) return true;
                    else return false;
                } else return false;
            },
            csvJSON: function (csv) {
                var lines = csv.split("\n"),
                    result = [];
                var headers = ["name", "email"];

                for (var i = 0, l = lines.length; i < l; ++i) {
                    var obj = {};
                    if (lines[i] !== "") {
                        var currentLine = lines[i].split(",");
                        for (var j = 0, l2 = headers.length; j < l2; ++j) {
                            obj[headers[j]] = JSON.parse(currentLine[j].toLowerCase());
                        }
                        result.push(obj);
                    }
                }
                return result;
            },
            getNoRepeatedItems: function (attr, list) {
                var u = {}, a = [];
                for (var i = 0, l = list.length; i < l; ++i) {
                    if (u.hasOwnProperty(list[i].email)) {
                        continue;
                    }
                    a.push(list[i]);
                    u[list[i].email] = 1;
                }
                return a;
            }
        };
    })
    .factory("fileReader", function ($q, $log) {

        var onLoad = function(reader, deferred, scope) {
            return function () {
                scope.$apply(function () {
                    deferred.resolve(reader.result);
                });
            };
        };

        var onError = function (reader, deferred, scope) {
            return function () {
                scope.$apply(function () {
                    deferred.reject(reader.result);
                });
            };
        };

        var onProgress = function(reader, scope) {
            return function (event) {
                scope.$broadcast("fileProgress",
                    {
                        total: event.total,
                        loaded: event.loaded
                    });
            };
        };

        var getReader = function(deferred, scope) {
            var reader = new FileReader();
            reader.onload = onLoad(reader, deferred, scope);
            reader.onerror = onError(reader, deferred, scope);
            reader.onprogress = onProgress(reader, scope);
            return reader;
        };

        var readAsDataURL = function (file, scope) {
            var deferred = $q.defer();

            var reader = getReader(deferred, scope);
            reader.readAsDataURL(file);

            return deferred.promise;
        };

        var readAsText = function (file, scope) {
            var deferred = $q.defer();

            var reader = getReader(deferred, scope);
            reader.readAsText(file);

            return deferred.promise;
        };

        return {
            readAsDataUrl: readAsDataURL,
            readAsText: readAsText
        };
    });