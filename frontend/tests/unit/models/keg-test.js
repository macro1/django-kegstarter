import {
  moduleForModel,
  test
} from 'ember-qunit';

moduleForModel('keg', {
  // Specify the other units that are required for this test.
  needs: [
    'model:beer',
    'model:brewer',
  ]
});

test('it exists', function(assert) {
  var model = this.subject();
  // var store = this.store();
  assert.ok(!!model);
});
