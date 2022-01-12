//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package vault

import (
	"errors"

	"github.com/CiscoDevNet/msx-examples/go-hello-world-service-8/internal/config"
	"github.com/hashicorp/vault/api"
)

type HelloWorldVault struct {
	Client *api.Client
	Config config.Vault
}

func (v *HelloWorldVault) Connect() error {
	c := api.DefaultConfig()
	c.Address = v.Config.Scheme + "://" + v.Config.Host + ":" + v.Config.Port

	if v.Config.Scheme == "https" {
		t := api.TLSConfig{
			CACert:   v.Config.CACert,
			Insecure: v.Config.Insecure,
		}
		err := c.ConfigureTLS(&t)
		if err != nil {
			return err
		}
	}
	client, err := api.NewClient(c)
	if err != nil {
		return err
	}
	client.SetToken(v.Config.Token)
	v.Client = client
	return nil
}

func (v *HelloWorldVault) GetSecret(s string) (*api.Secret, error) {
	result, err := v.Client.Logical().Read(s)
	return result, err
}

func (v *HelloWorldVault) getValue(secret string, key string) (interface{}, error) {
	s, err := v.GetSecret(secret)
	if err != nil {
		return nil, err
	}
	if s == nil {
		e := errors.New("Value " + secret + " not found.")
		return nil, e
	}
	for k, v := range s.Data {
		if k == key {
			return v, nil
		}
	}
	// It is possible that this is a versioned secret so look just in case.
	if s.Data["data"] != nil {
		for k, v := range s.Data["data"].(map[string]interface{}) {
			if k == key {
				return v, nil
			}
		}
	}
	e := errors.New("Value not found.")
	return nil, e
}

func (v *HelloWorldVault) GetString(secret string, key string, defaultValue string) (string, error) {
	value, error := v.getValue(secret, key)
	if error == nil {
		return value.(string), error
	}
	return defaultValue, error
}

func NewVault(c *config.Config) (HelloWorldVault, error) {
	pv := HelloWorldVault{
		Config: c.Vault,
	}
	err := pv.Connect()
	if err != nil {
		return pv, err
	}
	return pv, nil
}
