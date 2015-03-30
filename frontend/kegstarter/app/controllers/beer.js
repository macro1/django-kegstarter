import Ember from "ember";

export default Ember.ObjectController.extend({
  setupController: function(controller, beers){
    controller.set('model', beer.get('beer'));
  }
});
