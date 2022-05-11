//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package main

import (
	"context"
	"crypto/tls"
	"encoding/base64"
	"fmt"
	"net/http"
	"os"

	msxsdk "github.com/CiscoDevNet/go-msx-sdk"
	"github.com/google/uuid"
)

func main() {
	// TODO - Replace these with values from your test MSX environment.
	const (
		myHostName     = "rtp-msxlite-10.lab.ciscomsx.com"
		myClientId     = "my-test-private-client"
		myClientSecret = "make-up-a-private-client-secret-and-keep-it-safe"
		myUsername     = "superuser"
		myPassword     = "4b=@TNydSshIuT$farMA^9alXT56Sb3."
	)

	var (
		config             = msxsdk.NewConfiguration()
		ctx                = context.Background()
		client             = msxsdk.NewAPIClient(config)
		customTransport    = http.DefaultTransport.(*http.Transport).Clone()
		basicToken         = fmt.Sprintf("%s:%s", myClientId, myClientSecret)
		basicAuthorization = fmt.Sprintf("Basic %s", base64.StdEncoding.EncodeToString([]byte(basicToken)))
	)

	// <DANGER> Do not defeat the SSL certificate in production.
	customTransport.TLSClientConfig = &tls.Config{InsecureSkipVerify: true}
	// </DANGER>

	// Create the MSX SDK client.
	config.Scheme = "https"
	config.Host = myHostName
	config.HTTPClient = &http.Client{Transport: customTransport}

	// Make the authorization token to pass to MSX.

	// Call GetAccessToken with a username and credentials.
	accessToken, _, _ := client.SecurityApi.
		GetAccessToken(ctx).
		Authorization(basicAuthorization).
		GrantType("password").
		Username(myUsername).
		Password(myPassword).
		Execute()

	// Add Access Token Header in the Request
	if token := accessToken.GetAccessToken(); token != "" {
		bearer := fmt.Sprintf("Bearer %s", token)
		config.AddDefaultHeader("Authorization", bearer)
		fmt.Printf("Access Token: %s\n\n", token)
	}

	// Create a new Tenant
	tenantCreate := *msxsdk.NewTenantCreate("GoSDKTestTenant_" + uuid.New().String())

	createResp, _, _ := client.TenantsApi.
		CreateTenant(ctx).
		TenantCreate(tenantCreate).
		Execute()

	// Get list of tenant pages
	pageResp, _, err := client.TenantsApi.
		GetTenantsPage(ctx).
		Page(0).
		PageSize(100).
		Execute()

	if err != nil {
		fmt.Printf("Something went wrong.\n%s\n", err.Error())
		os.Exit(1)
	}

	fmt.Println("Create tenant:")
	fmt.Printf("\tId : %s \n", *createResp.Id)
	fmt.Printf("\tName : %s\n\n", createResp.Name)

	fmt.Println("List of tenants:")
	for _, v := range pageResp.GetContents() {
		fmt.Printf("\tId : %s\n", *v.Id)
		fmt.Printf("\tName : %s\n\n", v.Name)
	}

	// Delete previously created tenant
	client.TenantsApi.
		DeleteTenant(ctx, *createResp.Id).
		Execute()

	fmt.Println("Delete tenant:")
	fmt.Printf("\tId : %s \n", *createResp.Id)
	fmt.Printf("\tName : %s\n\n", createResp.Name)

}
