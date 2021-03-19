//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package consul

import (
	"github.com/CiscoDevNet/msx-examples/go-hello-world-service-5/internal/config"
	"fmt"
	"github.com/hashicorp/consul/api"
	"net/url"
)

type HelloWorldConsul struct {
	Client  *api.Client
	Service api.AgentServiceRegistration
	Config  config.Consul
}

func (p *HelloWorldConsul) Connect() error {
	conf := api.DefaultConfig()
	u, err := url.Parse(p.Config.Host + ":" + p.Config.Port)
	if err != nil {
		return err
	}
	conf.Address = u.Host
	conf.Scheme = u.Scheme
	conf.Token = p.Config.Token
	if u.Scheme == "https" {
		conf.TLSConfig = api.TLSConfig{
			CAFile:             p.Config.CACert,
			InsecureSkipVerify: p.Config.Insecure,
		}
	}
	client, err := api.NewClient(conf)
	p.Client = client
	return err
}

func (p *HelloWorldConsul) RegisterService() error {
	return p.Client.Agent().ServiceRegister(&p.Service)
}

func (p *HelloWorldConsul) DeregisterService() error {
	return p.Client.Agent().ServiceDeregister(p.Service.ID)
}

func (p *HelloWorldConsul) GetValue(key string) ([]byte, error) {
	kv, _, err := p.Client.KV().Get(key, nil)
	if kv != nil {
		return kv.Value, err
	}
	return []byte{}, fmt.Errorf("key not found")
}

func (p *HelloWorldConsul) GetString(key string, defaultValue string) (string, error) {
	value, error := p.GetValue(key)
	if error == nil {
		return string(value), error
	}
	return defaultValue, error
}

func NewConsul(cfg *config.Config) (HelloWorldConsul, error) {
	ic := HelloWorldConsul{
		Config: cfg.Consul,
	}
	err := ic.Connect()
	if err != nil {
		return ic, err
	}
	return ic, nil
}