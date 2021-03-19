//
// Copyright (c) 2021 Cisco Systems, Inc
// All Rights reserved
//
var MsxSdk = require('msx-sdk');

// customize this for development
const dev = {
  sso: {
    clientId: 'my-public-client',
    ssoBaseUrl: 'https://dev-plt-aio1.lab.ciscomsx.com/idm',
    redirectUrl: 'https://192.168.0.15:4200/reactSsoSdkDemo/callback',
    scope: 'openid email profile read write'
  },
  msxApi: {
    basePath: "https://dev-plt-aio1.lab.ciscomsx.com"
  }
};

// customize this for production
const prod = {
  sso: {
    clientId: 'my-public-client',
    ssoBaseUrl: window.location.protocol + "//" + window.location.hostname +  '/idm',
    redirectUrl: window.location.protocol + "//" + window.location.hostname + '/reactSsoSdkDemo/callback',
    scope: 'openid email profile read write'
  },
  msxApi: {
    basePath: window.location.protocol + "//" + window.location.hostname
  }
};

// select the config when in dev versus prod
const config = process.env.NODE_ENV === 'development' ? dev : prod;

// Do Not Touch: placeholders constants
const constants = {
  ACCESS_TOKEN: 'access_token',
  AUTH_SERVER_CONFIG: 'auth_server_config'
}

// Do Not Touch: bake the default msx api client for use throughout the application
var msxApiClient = new MsxSdk.ApiClient();
msxApiClient.basePath = config.msxApi.basePath;

export {config, constants, msxApiClient};
