app.controller('CommentController', ['$scope', 'photos', '$routeParams', function($scope, photos, $routeParams) {
  photos.success(function(data) {
    console.log(data);
    $scope.mynd  = data.fields[$routeParams.id];
    $scope.photoId = $routeParams.id + 1;
    document.body.style.background = "#ffffff";
  });
}]);
