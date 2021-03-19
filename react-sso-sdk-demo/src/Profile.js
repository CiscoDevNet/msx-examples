//
// Copyright (c) 2021 Cisco Systems, Inc
// All Rights reserved
//
import React, { useState, useEffect } from 'react';
import {constants} from "./config";

/**
 * takes a token and fetches user info from SSO server
 * @param token
 * @returns {Promise<T>}
 */
const fetchUserInfo = async (token) => {
    //get the endpoint from the authserver config that we initially saved when we logged in
    var authServer = JSON.parse(localStorage.getItem(constants.AUTH_SERVER_CONFIG));

    if (authServer && authServer.hasOwnProperty("userInfoEndpoint"))
    {
        return fetch(authServer.userInfoEndpoint, {
            headers: {
                authorization: `Bearer ${token}`
            }
        }).then(response =>{
            if (response.status === 200){
                return response.json().then((data) => {
                    console.log(data);
                    return data;
                }).catch((err) => {
                    console.log(err);
                })
            }else {
                return null;
            }
        });
    }

    return null;
};

export const Profile = () => {
    const [userInfo, setUserInfo] = useState(null);

    useEffect(() => {
        const token = localStorage.getItem(constants.ACCESS_TOKEN);
        if (token){
            fetchUserInfo(token)
              .then((resp) => {
                  if (resp != null){
                      console.log(resp);
                      setUserInfo(resp);
                  }
              });
        }

        return () => {
        }
    }, [])

    /**
     * Shows the users info
     * @returns {JSX.Element}
     * @constructor
     */
    const DisplayUserInfo = () => {
        return (
            <div className="card text-white bg-success mb-3">
                <div className="card-body">
                    <h5 className="card-title">Userinfo</h5>
                    <pre className="card-text">{JSON.stringify(userInfo, undefined, 2)}</pre>
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

    return (
        <div className="container mt-3">
            { userInfo ? <DisplayUserInfo /> : <UnAuthorized /> }
        </div>
    );
}
