'use strict';

angular.module('careerInsightsApp')
		
		.controller('LoginController', ['$scope', function($scope){
			
			$scope.tab = 1;
			$scope.isLogin = true;
			
			$scope.user = {email:"", pwd:""};
			$scope.secPwd = "";
			$scope.signupForm = {email:"", pwd:"", secPwd:""};
			
			// tab control functions
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
			
			// sign up functions
			$scope.samePwd = function(){
				return ($scope.user.pwd === $scope.secPwd);
			}
		}]);