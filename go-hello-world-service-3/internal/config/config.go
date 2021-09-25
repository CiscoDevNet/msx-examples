//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package config

import (
	"github.com/spf13/viper"
	"log"
	"strings"
)


// Config represents the complete helloworldservice config options.
type Config struct {
	Consul     Consul
}

// Consul represent the Consul config options.
type Consul struct {
	Host     string
	Port     string
	CACert   string
	Insecure bool
	Token    string
	Prefix   string
}

func ReadConfig() *Config {
	v := viper.New()
	v.SetConfigName("helloworld")
	v.AddConfigPath("/etc/helloworld/")
	v.AddConfigPath(".")
	v.SetEnvPrefix("helloworld")
	v.SetEnvKeyReplacer(strings.NewReplacer(".", "_"))
	v.AutomaticEnv()
	if err := v.ReadInConfig(); err != nil {
		log.Printf("%s",err.Error())
		if _, ok := err.(viper.ConfigFileNotFoundError); ok {
			log.Print("No config found.")
		} else {
			log.Printf("Error reading config: %s", err.Error())
		}
	}

	// Bind config to environment based on expected injections.
	bindConfig(v,"Consul.Host", "SPRING_CLOUD_CONSUL_HOST")
	bindConfig(v,"Consul.Port", "SPRING_CLOUD_CONSUL_PORT")

	var c Config
	v.Unmarshal(&c)
	return &c
}

func bindConfig(v *viper.Viper, keyName string, envName string) {
	err := v.BindEnv(keyName, envName)
	if err != nil {
		log.Printf("Could not bind env vars: %s", err.Error())
	}
}