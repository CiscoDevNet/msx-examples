//
// Copyright (c) 2021 Cisco Systems, Inc
// All Rights reserved
//
import React, {useEffect, useState} from 'react';
import {
    TokenRequest,
    BaseTokenRequestHandler,
    GRANT_TYPE_AUTHORIZATION_CODE,
    AuthorizationServiceConfiguration,
    RedirectRequestHandler,
    AuthorizationNotifier,
    FetchRequestor, LocalStorageBackend, DefaultCrypto
} from '@openid/appauth';
import {config, constants} from "./config";
import {NoHashQueryStringUtils} from './utils/noHashQueryStringUtils';

/**
 * The callback is caught when the sso server redirects back to the client application.
 *
 * In this example we're simply completing the handshake from the SSO server, reqesting a token
 * and then storing the token to localStorage.
 *
 * @param props
 * @returns {JSX.Element}
 * @constructor
 */
export const Callback = (props) => {

    const [error, setError] = useState(null);
    const [code, setCode] = useState(null);
    const [loading, setLoading] = useState(null);

    useEffect(function () {
        ///////////////////////////
        setLoading(true);
        const tokenHandler = new BaseTokenRequestHandler(new FetchRequestor());
        const authorizationHandler = new RedirectRequestHandler(new LocalStorageBackend(), new NoHashQueryStringUtils(), window.location, new DefaultCrypto());
        const notifier = new AuthorizationNotifier();
        authorizationHandler.setAuthorizationNotifier(notifier);
        notifier.setAuthorizationListener((request, response, error) => {
            console.log('Authorization request complete ', request, response, error);
            if (response) {
                console.log(`Authorization Code  ${response.code}`);

                let extras = null;
                if (request && request.internal) {
                    extras = {};
                    extras.code_verifier = request.internal.code_verifier;
                }

                const tokenRequest = new TokenRequest({
                    client_id: config.sso.clientId,
                    redirect_uri: config.sso.redirectUrl,
                    grant_type: GRANT_TYPE_AUTHORIZATION_CODE,
                    code: response.code,
                    refresh_token: undefined,
                    extras
                });

                AuthorizationServiceConfiguration.fetchFromIssuer(config.sso.ssoBaseUrl, new FetchRequestor())
                    .then((oResponse) => {
                        const configuration = oResponse;
                        return tokenHandler.performTokenRequest(configuration, tokenRequest);
                    })
                    .then((oResponse) => {
                        console.log("authenticated with token " + oResponse.accessToken +  " redirecting...");
                        localStorage.setItem(constants.ACCESS_TOKEN, oResponse.accessToken);
                        props.history.push('/profile');
                    })
                    .catch(oError => {
                        setLoading(false);
                        console.log(oError);
                        setError(JSON.stringify(oError, undefined, 2));
                    });
            }
        });

        //////////////////////////
        const params = new URLSearchParams(props.location.search);
        setCode(params.get('code'));

        if (!code) {
            setError('Unable to get authorization code');
            return;
        }
        authorizationHandler.completeAuthorizationRequestIfPossible();
    }, [code, props]);

    /**
     * error jsx
     * @returns {JSX.Element}
     * @constructor
     */
    const Error = () => {
        return (
          <div className="card-body bg-danger">
              <div className="card-body">
                  <pre className="card-text">{error}</pre>
              </div>
          </div>
        )
    };

    /**
     *
     * @returns {JSX.Element}
     * @constructor
     */
    const Loading = () => {
        return (
          <div className="card-body">
              <h5 className="card-title">Loading... Well, talking to SSO server really.</h5>
          </div>
        )
    };



    return (
        <div className="container-fluid" style={{marginTop: '10px'}}>
            <div className="card">
                { loading ? <Loading/> : <Error/> }
            </div>
        </div>
    );
}
