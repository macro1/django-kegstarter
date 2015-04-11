import DS from 'ember-data';

export default DS.Model.extend({
  url: DS.attr(),
  name: DS.attr(),
  abv: DS.attr(),
  brewer: DS.belongsTo('brewer')
});
