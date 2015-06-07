import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr('string'),
  beerSet: DS.hasMany('beer', {async: true})
});
