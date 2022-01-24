//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package consul

import (
	"fmt"
	"log"
	"net/url"

	"github.com/CiscoDevNet/msx-examples/go-slm-init-proof-service/internal/config"
	"github.com/hashicorp/consul/api"
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
	log.Printf("Consul GetString  key=%s", key)
	value, error := p.GetValue(key)
	if error == nil {
		log.Printf("Consul GetString value=%s", value)
		return string(value), error
	}
	log.Printf("Consul failed to GetString Error=%s, defaultValue=%s", error.Error(), defaultValue)
	return defaultValue, error
}

func (p *HelloWorldConsul) FindPrefix() string {
	_, err := p.GetString("thirdpartycomponents/defaultapplication/swagger.security.sso.baseUrl", "")
	if err == nil {
		return "thirdpartycomponents"
	} else {
		return "thirdpartyservices"
	}
}

func NewConsul(cfg *config.Config) (HelloWorldConsul, error) {
	ic := HelloWorldConsul{
		Config: cfg.Consul,
	}
	err := ic.Connect()
	if err != nil {
		log.Printf("NewConsul Failed to connect ic=%#v", ic)
		log.Printf("NewConsul Failed to connect cfg=%#v", cfg)
		log.Printf("NewConsul Connection Error=%s", err.Error())
		// log.Fatal("NewConsul Failed to connect")
		return ic, err
	}
	return ic, nil
}