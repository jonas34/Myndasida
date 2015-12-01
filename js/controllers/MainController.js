app.controller('MainController', ['$scope', 'photos', function($scope, photos) {
  photos.success(function(data) {
    console.log(data);
    $scope.myndir = data;
    document.body.style.background = "#c3dfef";
  });
}]);
