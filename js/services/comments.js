app.factory('comments', ['$http', function($http) {
  return $http.get('http://localhost:8000/myndir/comments/')
            .success(function(data) {
              return data;
            })
            .error(function(err) {
              console.log(err);
              return err;
            });
}]);
