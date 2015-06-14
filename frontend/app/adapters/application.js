import Ember from 'ember';
import DRFAdapter from './drf';

export default DRFAdapter.extend({
  namespace: "api/v1",
  pathForType: function(type) {
    return Ember.String.camelize(type);
  }
});
