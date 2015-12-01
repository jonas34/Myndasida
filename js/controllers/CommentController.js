app.controller('CommentController', ['$scope', 'photos','comments', '$routeParams', function($scope, photos, comments, $routeParams) {
  photos.success(function(data) {
    console.log($routeParams.id);
    $scope.mynd  = data[$routeParams.id].fields;
    $scope.photoId = $routeParams.id;
    document.body.style.background = "#ffffff";
  });
  comments.success(function(data) {
    $scope.comments = [];
    for (var i = 0; i < data.length; i++) {
      if(data[i].fields.photo==$routeParams.id){
        console.log(data[i]);
        $scope.comments.push(data[i]);
      }
    }
  });
}]);
