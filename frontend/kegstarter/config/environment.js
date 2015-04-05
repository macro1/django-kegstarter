/* jshint node: true */

module.exports = function(environment) {
  var ENV = {
    modulePrefix: 'kegstarter',
    environment: environment,
    baseURL: '/',
    locationType: 'auto',
    EmberENV: {
      FEATURES: {
        // Here you can enable experimental features on an ember canary build
        // e.g. 'with-controller': true
      }
    },

    APP: {
      // Here you can pass flags/options to your application instance
      // when it is created
    }
  };

  if (environment === 'development') {
    ENV.APP.contentSecurityPolicy = {
      'default-src': "'self' 192.168.59.103:8080",
      'script-src': "'self' 192.168.59.103:8080",
      'font-src': "'self' 192.168.59.103:8080",
      'connect-src': "'self' 192.168.59.103:8080",
      'img-src': "'self' 192.168.59.103:8080",
      'style-src': "'self' 192.168.59.103:8080",
      'frame-src': "'self' 192.168.59.103:8080"
    }
    ENV.APP.API_HOST = 'http://192.168.59.103:8080'
    // ENV.APP.LOG_RESOLVER = true;
    // ENV.APP.LOG_ACTIVE_GENERATION = true;
    // ENV.APP.LOG_TRANSITIONS = true;
    // ENV.APP.LOG_TRANSITIONS_INTERNAL = true;
    // ENV.APP.LOG_VIEW_LOOKUPS = true;
  }

  if (environment === 'test') {
    // Testem prefers this...
    ENV.baseURL = '/';
    ENV.locationType = 'none';

    // keep test console output quieter
    ENV.APP.LOG_ACTIVE_GENERATION = false;
    ENV.APP.LOG_VIEW_LOOKUPS = false;

    ENV.APP.rootElement = '#ember-testing';
  }

  if (environment === 'production') {

  }

  return ENV;
};
