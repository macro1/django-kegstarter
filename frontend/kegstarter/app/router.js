import Ember from 'ember';
import config from './config/environment';

var Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {
//  this.resource('beer', function() {});
  this.resource('beer');
});

export default Router;
