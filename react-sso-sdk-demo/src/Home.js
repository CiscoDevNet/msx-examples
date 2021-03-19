//
// Copyright (c) 2021 Cisco Systems, Inc
// All Rights reserved
//
import React, {useState} from 'react';
import {
  AuthorizationServiceConfiguration,
  AuthorizationRequest, RedirectRequestHandler,
  FetchRequestor, LocalStorageBackend, DefaultCrypto
} from '@openid/appauth';
import {NoHashQueryStringUtils} from './utils/noHashQueryStringUtils';
import {config, constants} from "./config";

/**
 *
 * @returns {JSX.Element}
 * @constructor
 */
export const Home = () => {
  const [error, setError] = useState(null);
  const authorizationHandler = new RedirectRequestHandler(new LocalStorageBackend(), new NoHashQueryStringUtils(), window.location, new DefaultCrypto());
  const redirect = () => {
    AuthorizationServiceConfiguration.fetchFromIssuer(config.sso.ssoBaseUrl, new FetchRequestor())
      .then((response) => {
        const authRequest = new AuthorizationRequest({
          client_id: config.sso.clientId,
          redirect_uri: config.sso.redirectUrl,
          scope: config.sso.scope,
          response_type: AuthorizationRequest.RESPONSE_TYPE_CODE,
          state: undefined
        });
        localStorage.setItem(constants.AUTH_SERVER_CONFIG, JSON.stringify(response));
        authorizationHandler.performAuthorizationRequest(response, authRequest);
      })
      .catch(error => {
        console.log(error);
        setError("Error Message: " + error.toString() + " -> Failed to fetch openId configuration. Usually this is a certificate error. Do you trust the SSO cert from: " + config.sso.ssoBaseUrl+ "? Does it have an openId Configuration?");
      });
  };

  return (
    <div className="container-fluid mt-3">
      {
        error && <div className="card text-white bg-danger mb-3">
          <div className="card-body bg-danger">
            <div className="card-body">
              <h5 className="card-text">Error</h5>
              <p>{error}</p>
            </div>
          </div>
        </div>
      }

      <div className="card">
        <div className="card-body">
          <h5 className="card-title">Welcome !!!</h5>
          <p className="card-text">MSX-SSO React Demo Application using &nbsp;
            <a href="https://github.com/openid/AppAuth-JS" rel="noopener noreferrer"
              target="_blank">
              App Auth JS
            </a>
          </p>
          <p>This app is an example on how to sign in via SSO and protect routed pages.</p>
          <button type="button" className="btn btn-primary" onClick={redirect}>Sign In</button>
        </div>
      </div>
    </div>
  )
};
