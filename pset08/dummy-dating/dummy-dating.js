Profile = function (doc) {
  _.extend(this, doc);
};

_.extend(Profile.prototype, {
  getValues: function () {
  return {name: this.name, gender: this.gender, age: this.age, build: this.build, aboutMe: this.aboutMe, turnOns: this.turnOns, turnOffs: this.turnOffs}
  }
});


Profiles = new Meteor.Collection('Profiles', {
  transform: function (doc) { return new Profile(doc); }
});
	
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

  Template.base.pageIsEditProfile = function() {
    console.log(Session.get('page'));
	  return Session.equals('page', 'editProfile');
  },

  Template.base.pageIsViewMyProfile = function() {
	  console.log(Session.get('page'));
		console.log(Session.get('profile'));
	  return Session.equals('page', 'viewProfile') && Session.equals('profile', Meteor.userId());
  },

  Template.base.pageIsSearchProfiles = function() {
	  console.log(Session.get('page'));
	  return Session.equals('page', 'searchProfiles');
  },

  Template.base.events({
    'click #editProfile': function (evt, templ) {
	    console.log('Trying to set session to editProfile')
	    Session.set('page', 'editProfile');
	  },
	  
	  'click .viewProfile': function (evt, templ) {
	    console.log("Trying to set 'page' to viewProfile and 'id' to " + evt.id)
		  Session.set('profile', evt.id);
	    Session.set('page', 'viewProfile');
	  },

	  'click #viewMyProfile': function (evt, templ) {
			console.log("Trying to view user's own profile")
		  Session.set('profile', Meteor.userId());
	    Session.set('page', 'viewProfile');
		},
	   
    // In order to have a viewProfile template that accepts
	  // parameters, such as userId, to serve up pages based
	  // on user ID, would I set another value 'profileId' such as:
	  //      Session.set('profileId', Meteor.userId())
	  // In order to view the user's own profile for instance?

	  'click #searchProfiles': function (evt, templ) {
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

	//True if the user has made a profile, false if they have not
  Template.editProfile.hasMadeProfile = function () { 
	  if (Profiles.findOne({userId: Meteor.userId()})) {
	    return true;
	  }
	  else {
	    return false;
	  }
  },

  Template.editProfile.greetingNew = function () {
	  return "You have not yet made your profile!!! Please edit the fields and click 'Create My Profile' to save your changes" 
  },

  Template.editProfile.greetingOld = function () {
      return "Please edit the fields below and click 'Update My Profile' to save your changes."
  },
  
  //Insert a profile if the user has not made one, or update an
  //existing profile.
  Template.editProfile.events({
    'click #updateProfile': function (evt, templ) {
		  var this_profile = Profiles.findOne({userId: Meteor.userId()}); 
			Profiles.update(this_profile._id, {$set: {
				userId: Meteor.userId(),
		    name: templ.find("#name").value,
			  gender: templ.find("#gender").value,
			  age: templ.find("#age").value,
			  build: templ.find("#build").value,
			  aboutMe: templ.find("#aboutMe").value,
			  turnOns: templ.find("#turnOns").value,
			  turnOffs: templ.find("#turnOffs").value
			}});
		  console.log("Updating profile...")
		},

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
        profileViews: []
			});
		  console.log("Creating new profile...")
		}
	});
  
	//values for displaying a profile for the given userId
  Template.viewProfile.value = function () {
	  return Profiles.findOne({userId: Session.get('profile')}) 
  }
	
}

if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
  });
}
