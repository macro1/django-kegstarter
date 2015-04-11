import Ember from 'ember';
import config from './config/environment';

var Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {
  this.resource('beers', function() {});
  this.resource('beer', {
    path: '/beer/:pk'
  }, function() {});

  this.resource('kegs', function() {});
  this.resource('keg', {
    path: '/keg/:pk'
  }, function() {});

  this.resource('brewers', function() {});
  this.resource('brewer', {
    path: '/brewer/:pk'
  }, function() {});

  this.resource('ledgers', function() {});
  this.resource('ledger',{
    path: '/ledger/:pk'
  }, function() {
    this.resource('entry', {
      path: '/entry/:pk'
    }, function() {});
  });
});

export default Router;
