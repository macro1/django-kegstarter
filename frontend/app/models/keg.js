import DS from 'ember-data';

export default DS.Model.extend({
  beer: DS.belongsTo('beer'),
  gallons: DS.attr(),
  purchase_date: DS.attr('datetime'),

});
