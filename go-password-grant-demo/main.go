//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package main

import (
	"crypto/tls"
	"encoding/base64"
	"fmt"
	"github.com/CiscoDevNet/go-msx-sdk"
	"net/http"
)

func main() {
    // TODO - Replace these with values from your test MSX environment.
	const myHostName = "dev-plt-aio1.lab.ciscomsx.com"
	const myClientId = "my-private-client"
	const myClientSecret = "there-are-no-secrets-that-time-does-not-reveal"
	const myUsername = "jeff"
	const myPassword = "Password@1"

	// <DANGER> Do not defeat the SSL certificate in production.
	customTransport := http.DefaultTransport.(*http.Transport).Clone()
	customTransport.TLSClientConfig = &tls.Config{InsecureSkipVerify: true}
	// </DANGER>

    // Create the MSX SDK client.
	var config = msxsdk.NewConfiguration()
	config.Scheme = "https"
	config.Host = myHostName
	config.HTTPClient = &http.Client{Transport: customTransport}
	var client = msxsdk.NewAPIClient(config)

    // Make the authorization token to pass to MSX.
	var basicToken = myClientId + ":" + myClientSecret
	var basicAuthorization = "Basic " + base64.StdEncoding.EncodeToString([]byte(basicToken))

    // Call GetAccessToken with a username and credentials.
	response, _, err := client.SecurityApi.GetAccessToken(nil).Authorization(basicAuthorization).GrantType("password").Username(myUsername).Password(myPassword).Execute()

    // Print the user details and access token.
	if err == nil || err.Error() == "" {
		fmt.Printf("First Name: " + *response.FirstName + "\n")
		fmt.Printf("Last Name: " + *response.LastName + "\n")
		fmt.Printf("Email: " + *response.Email + "\n")
		fmt.Printf("Access Token:\n" + *response.AccessToken + "\n")
	} else {
		fmt.Printf("Something went wrong.\n")
		fmt.Printf(err.Error())
	}
}