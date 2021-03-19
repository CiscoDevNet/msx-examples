//
// Copyright (c) 2021 Cisco Systems, Inc
// All Rights reserved
//
import React, { useState, useEffect } from 'react';
import {constants, msxApiClient} from './config';
var MsxPlatformClient = require('msx-sdk');

/**
 * takes a token and fetches tenants
 * @param token
 * @returns {Promise<T>}
 */
const fetchTenants = (token) => {

    //setup api client to use token via Auth Header
    msxApiClient.defaultHeaders = {Authorization: 'Bearer ' + token};

    //init the tenants api with ApiClient
    const tenantsApi = new MsxPlatformClient.TenantsApi(msxApiClient);
    var page = 0;
    var pageSize = 10;
    var opts = {
        'showImage': true,
    };

    return tenantsApi.getTenantsPage(page, pageSize, opts);
};

export const Tenants = () => {
    const [tenants, setTenants] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        const token = localStorage.getItem(constants.ACCESS_TOKEN);
        if (token){
            fetchTenants(token).then(function(data){
                console.log('API called successfully. Returned data: ' + data);
                setTenants(data);
            }, function(error){
                console.error(error);
                setError(error);
            });
        }


        return () => {
        }
    }, [])

    /**
     * Shows tenants
     * @returns {JSX.Element}
     * @constructor
     */
    const DisplayTenants = () => {
        return (
            <div className="card text-white bg-success mb-3">
                <div className="card-body">
                    <h5 className="card-title">Tenants</h5>
                    <pre className="card-text">{JSON.stringify(tenants, undefined, 2)}</pre>
                </div>
            </div>
        )
    };

    /**
     * lets the user know they're unauthorized
     * @returns {JSX.Element}
     * @constructor
     */
    const UnAuthorized = () => {
        return (
            <div className="card text-white bg-danger mb-3">
                <div className="card-body">
                    <h5 className="card-title">You are NOT authenticated!</h5>
                </div>
            </div>
        )
    };

    /**
     * lets the user know they're unauthorized
     * @returns {JSX.Element}
     * @constructor
     */
    const Error = () => {
        return (
          <div className="card text-white bg-danger mb-3">
              <div className="card-body">
                  <h5 className="card-title">Error</h5>
                  <pre className="card-text">{JSON.stringify(error, undefined, 2)}</pre>
              </div>
          </div>
        )
    };

    return (
        <div className="container mt-3">
            { tenants ? <DisplayTenants /> : error ? <Error /> : <UnAuthorized /> }
        </div>
    );
}
