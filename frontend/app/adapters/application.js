import Ember from 'ember';
import DRFAdapter from './drf';

export default DRFAdapter.extend({
  pathForType: function(type) {
    return Ember.String.camelize(type);
  }
});
