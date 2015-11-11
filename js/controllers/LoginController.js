app.controller('LoginController', ['$scope','login',
function($scope, login) {
  login.success(function(data) {
    $scope.login = data;

    $scope.Submit = function(){
      alert("hallo");
    }
  });
}]);
