//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package com.cisco.msx.passwordgrantdemo;

import com.cisco.msx.platform.ApiClient;
import com.cisco.msx.platform.ApiException;
import com.cisco.msx.platform.client.SecurityApi;
import com.cisco.msx.platform.client.TenantsApi;
import com.cisco.msx.platform.model.TenantsPage;

import java.util.Base64;

public class Main {
    public static final String MY_SERVER_URL = "https://dev-plt-aio1.lab.ciscomsx.com";
    public static final String MY_CLIENT_ID = "my-test-private-client";
    public static final String MY_CLIENT_SECRET = "there-are-no-secrets-that-time-does-not-reveal";
    public static final String MY_USERNAME = "jeff";
    public static final String MY_PASSWORD = "Password@1";

    public static void main(String[] args) {
        try {
            // Create an MSX SDK client.
            ApiClient client = new ApiClient().setBasePath(MY_SERVER_URL);
            client.setVerifyingSsl(false);

            // Get an access token using the password grant.
            SecurityApi securityApi = new SecurityApi(client);
            String basicToken = MY_CLIENT_ID + ":" + MY_CLIENT_SECRET;
            String basicAuthorization = "Basic " + Base64.getEncoder().encodeToString(basicToken.getBytes());
            String accessToken = securityApi.getAccessToken(basicAuthorization, "password", MY_USERNAME, MY_PASSWORD,
                    null, null, null, null, null, null)
                    .getAccessToken();
            System.out.println("Access Token:");
            System.out.println(accessToken);

            // Add the access token header to the client.
            client.addDefaultHeader("Authorization", "Bearer " + accessToken);

            // Get a page of tenants and display the names.
            TenantsApi tenantsApi = new TenantsApi(client);
            TenantsPage tenantsPage = tenantsApi.getTenantsPage(0, 10, null, false, null, null);
            tenantsPage.getContents().forEach(x -> System.out.println(x.getName()));
        }
        catch (ApiException e) {
            System.err.println(e.toString());
        }
    }
}
