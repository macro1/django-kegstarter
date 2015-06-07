import DS from 'ember-data';

export default DS.Model.extend({
  url: DS.attr(),
  username: DS.attr(),
  firstName: DS.attr(),
  lastName: DS.attr(),
  dateJoined: DS.attr('date')
});
