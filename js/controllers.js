'use strict';

angular.module('careerInsightsApp')
		
		.controller('LoginController', ['$scope', function($scope){
			
			$scope.tab = 1;
			$scope.show = false;
			$scope.isLogin = true;
			
			$scope.select = function(setTab) {
				console.log("current tab is "+setTab);
				$scope.tab = setTab;
				if (setTab === 1){
					$scope.isLogin = true;
				} else {
					$scope.isLogin = false;
				}
			}
			
			$scope.isSelected = function(checkTab) {
				return ($scope.tab === checkTab);
			}
		}]);