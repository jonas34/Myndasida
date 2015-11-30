app.factory('photos', ['$http', function($http) {
  return $http.get('http://localhost:8000/myndir/photos/')
            .success(function(data) {
              return data;
            })
            .error(function(err) {
              return err;
            });
}]);
