Profiles = new Meteor.Collection('Profiles');
	
var ProtonRouter = Backbone.Router.extend({
	routes: {
        "editProfile": "editProfile",
        "viewProfile": "viewProfile",
        "searchProfiles":"searchProfiles"
    },
    editProfile: function () {
        Session.set('page','editProfile');
    },
    viewProfile: function (){
        Session.set('page', 'viewProfile');
    },
    searchProfiles: function(){
        Session.set('page', 'searchProfiles');
    }
});


if (Meteor.isClient) {

  Template.base.pageIsEditProfile = function(){
    console.log(Session.get('page'));
	return Session.equals('page', 'editProfile');
  },

  Template.base.pageIsViewProfile = function(){
	console.log(Session.get('page'));
	return Session.equals('page', 'viewProfile');
  },

  Template.base.pageIsSearchProfiles = function(){
	console.log(Session.get('page'));
	return Session.equals('page', 'searchProfiles');
  },

  Template.base.events({
    'click #editProfile': function (evt, templ) {
	  //Session.set not these evaluation functions
	  console.log('Trying to set session to editProfile')
	  Session.set('page', 'editProfile');
	},
	'click #viewProfile': function (evt, templ) {
	  console.log('Trying to set session to viewProfile')
	  Session.set('page', 'viewProfile');
	},
	'click #searchProfiles': function (evt, templ){
      console.log('Trying to set session to searchProfiles')
	  Session.set('page', 'searchProfiles');
	}
  });

  Template.base.loggedIn = function () {
	  return Meteor.userId(); //if logged in, true.
  },

  Template.base.greeting = function () {
	return "Welcome to a fake dating site, Dummy Dating!"
  },

  Template.base.askForLogin = function () {
    return "Please login or create an account to view the profiles!"
  },

  Template.editProfile.hasMadeProfile = function () {
	  //Check to see if the user has ever made a profile.
	  return _.contains(this.userId, Meteor.userId());
  },

  Template.editProfile.greetingNewProfile = function () {
	  return "You have not yet made your profile!!!" 
  },

  Template.editProfile.greeting2 = function () {
      return "Please edit the fields below and click 'Update My Profile' to save your changes."
  },
  
  Template.editProfile.events({
    'click #createProfile': function (evt, templ) {
		Profiles.insert({
			userId: Meteor.userId(),
		    name: templ.find("#name").value,
			gender: templ.find("#gender").value,
			age: templ.find("#age").value,
			build: templ.find("#build").value,
			aboutMe: templ.find("#aboutMe").value,
			turnOns: templ.find("#turnOns").value,
			turnOffs: templ.find("#turnOffs").value,
		    profileViews: []});
	}
  });
 
}

if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
  });
}
