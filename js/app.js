angular.module('myLogin', [].config(['$routeProvider','$locationProvider',
  function($routeProvider, $locationProvider) {
      $routeProvider
      .when('/login', {
        templateUrl: 'login.html',
        controller: 'LoginController'
      })
      .when('/register', {
        templateUrl: 'register.html',
        controller: 'RegisterController'
      })
      .otherwise({
        redirectTo: '/login'
      });
  }]);
