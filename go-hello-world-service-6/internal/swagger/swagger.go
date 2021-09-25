//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package swagger

import (
	"github.com/CiscoDevNet/go-msx-swagger"
	"github.com/CiscoDevNet/msx-examples/go-hello-world-service-6/internal/config"
	"github.com/CiscoDevNet/msx-examples/go-hello-world-service-6/internal/consul"
	"github.com/CiscoDevNet/msx-examples/go-hello-world-service-6/internal/vault"
)

// Override configuration with values from Consul and Vault.
func UpdateConfig(c *config.Config, consul *consul.HelloWorldConsul, vault *vault.HelloWorldVault) error {
	c.Swagger.SsoURL, _ = consul.GetString(c.Consul.Prefix + "/defaultapplication/swagger.security.sso.baseUrl", c.Swagger.SsoURL)
	c.Swagger.ClientID, _ = consul.GetString(c.Consul.Prefix + "/helloworldservice/public.security.clientId", c.Swagger.ClientID)
	return nil
}

func NewSwagger(cfg *config.Config) (*msxswagger.MsxSwagger,error) {
	c := msxswagger.NewDefaultMsxSwaggerConfig()
	c.SwaggerJsonPath = cfg.Swagger.SwaggerJsonPath
	c.DocumentationConfig.RootPath = cfg.Swagger.RootPath
	c.DocumentationConfig.Security.Enabled = cfg.Swagger.Secure
	c.DocumentationConfig.Security.Sso.BaseUrl = cfg.Swagger.SsoURL
	c.DocumentationConfig.Security.Sso.ClientId = cfg.Swagger.ClientID
	c.DocumentationConfig.RootPath = "/helloworld"
	return msxswagger.NewMsxSwagger(c)
}