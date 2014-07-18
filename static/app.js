var resumizeApp = angular.module('resumizeApp', ['ngSanitize']);

resumizeApp.factory('resumizeFactory', ['$http', function ($http) {
    var urlBase = '/';
    var resumizeFactory = {};

    resumizeFactory.submit = function (data) {
        console.log(data);
    };

    return resumizeFactory;
}]);

resumizeApp.controller('resumizeController', function ($scope, $sce, resumizeFactory) {
    init();
    function init() {
        // Initialize the editor with a JSON schema
        editor = new JSONEditor(document.getElementById('editor_holder'),{
        schema: {
          type: "object",
          title: "Resume",
          properties: {
            name: {
              type: "string"
            },
            gender: {
              type: "string",
              enum: ["male", "female"]
            },
            year: {
              type: "integer",
              enum: [
                1995,1996,1997,1998,1999,
                2000,2001,2002,2003,2004,
                2005,2006,2007,2008,2009,
                2010,2011,2012,2013,2014
              ],
              default: 1990
            },
            education: {
              type: "string"
            }
          }
        }
        });
    }

    $scope.submit = function () {
        resumizeFactory.submit(editor.getValue());
    };

});
