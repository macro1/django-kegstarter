import {
  moduleForModel,
  test
} from 'ember-qunit';

moduleForModel('brewer', {
  // Specify the other units that are required for this test.
  needs: [
    'model:beer',
  ]
});

test('it exists', function(assert) {
  var model = this.subject();
  // var store = this.store();
  assert.ok(!!model);
});
