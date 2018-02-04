'use strict';

app.module('careerInsightsApp')
	.constant("baseURL","http://localhost:3000/")
	.service('useFactory', ['$resource', 'baseURL', function($resource, baseURL){
		
		this.getUser = function(){
				return $resource(baseURL+"user/:id",null, {'update':{method:'POST'}});
			};
	}]);