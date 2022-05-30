//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package security

import (
	"fmt"
	"net/http"

	msxsecurity "github.com/CiscoDevNet/go-msx-security"
	openapi "github.com/CiscoDevNet/msx-examples/go-hello-world-service-8/go"
	"github.com/CiscoDevNet/msx-examples/go-hello-world-service-8/internal/config"
	"github.com/CiscoDevNet/msx-examples/go-hello-world-service-8/internal/consul"
	"github.com/CiscoDevNet/msx-examples/go-hello-world-service-8/internal/vault"
	"github.com/gorilla/mux"
)

// The Security global will represent the Security validator provided by msx-security.
var Security = &msxsecurity.MsxSecurity{}

// EnsureAuth will wrap http handle funcs that require auth.
type EnsureAuth struct {
	permission string
	handler    http.Handler
}

// Override configuration with values from Consul and Vault.
func UpdateConfig(c *config.Config, consul *consul.HelloWorldConsul, vault *vault.HelloWorldVault) error {
	c.Security.SsoURL, _ = consul.GetString(c.Consul.Prefix+"/defaultapplication/swagger.security.sso.baseUrl", c.Security.SsoURL)
	c.Security.ClientID, _ = consul.GetString(c.Consul.Prefix+"/helloworldservice/integration.security.clientId", c.Security.ClientID)
	c.Security.ClientSecret, _ = vault.GetString(c.Vault.Prefix+"/helloworldservice", "integration.security.clientSecret", c.Security.ClientSecret)

	// 20220524 - Temporary workaround for key issue.
	if c.Security.ClientID == "" {
		c.Security.ClientID, _ = consul.GetString(c.Consul.Prefix+"/helloworldservice/integration.security.client.clientId", c.Security.ClientID)
	}
	if c.Security.ClientSecret == "" {
		c.Security.ClientSecret, _ = vault.GetString(c.Vault.Prefix+"/helloworldservice", "integration.security.client.clientSecret", c.Security.ClientSecret)
	}
	return nil
}

// ServeHTTP will perform the auth on behalf of the embedded handlerfunc.
func (ea *EnsureAuth) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	permitted, _ := Security.HasPermission(r, ea.permission)
	if permitted {
		ea.handler.ServeHTTP(w, r)
	} else {
		w.WriteHeader(http.StatusForbidden)
		fmt.Fprint(w, "Access denied")
	}
}

// NewEnsureAuth will be used to generate an auth wrapper.
func NewEnsureAuth(handlerToWrap http.Handler, permission string) http.Handler {

	return &EnsureAuth{
		permission: permission,
		handler:    handlerToWrap,
	}
}

// Sets up a new Security handler.
func NewSecurity(cfg *config.Config) error {
	c := msxsecurity.DefaultMsxSecurityConfig()
	c.SsoURL = cfg.Security.SsoURL
	c.ClientID = cfg.Security.ClientID
	c.ClientSecret = cfg.Security.ClientSecret
	Security = msxsecurity.NewMsxSecurity(c)
	return nil
}

// NewSecureRouter creates a new router for any number of api routers.
// Routes are secured using our ensure auth wrapper.
func NewSecureRouter(routers ...openapi.Router) *mux.Router {
	router := mux.NewRouter().StrictSlash(true)
	for _, api := range routers {
		for _, route := range api.Routes() {
			var handler http.Handler
			handler = route.HandlerFunc
			handler = openapi.Logger(handler, route.Name)
			handler = NewEnsureAuth(handler, route.Permission)

			router.
				Methods(route.Method).
				Path(route.Pattern).
				Name(route.Name).
				Handler(handler)
		}
	}

	return router
}

// AddSecureRoutes adds api routes to an existing router.
func AddSecureRoutes(router *mux.Router, routers ...openapi.Router) *mux.Router {
	for _, api := range routers {
		for _, route := range api.Routes() {
			var handler http.Handler
			handler = route.HandlerFunc
			handler = openapi.Logger(handler, route.Name)
			handler = NewEnsureAuth(handler, route.Permission)

			router.
				Methods(route.Method).
				Path(route.Pattern).
				Name(route.Name).
				Handler(handler)
		}
	}

	return router
}
