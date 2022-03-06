//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package config

import (
	"log"
	"strings"

	"github.com/spf13/viper"
)

// HelloWorld config options.
type Config struct {
	Consul    Consul
	Vault     Vault
	Cockroach Cockroach
	Swagger   Swagger
	Security  Security
	Kafka 	  Kafka
}

// Security config options.
type Security struct {
	SsoURL       string
	ClientID     string
	ClientSecret string
}

// Swagger config options.
type Swagger struct {
	Secure          bool
	SsoURL          string
	SwaggerJsonPath string
	RootPath        string
	ClientID        string
}

// Cockroach config options.
type Cockroach struct {
	Host         string
	Port         string
	Username     string
	Password     string
	DatabaseName string
	CACert       string
	SSLMode      string
}

// Vault represents Vault config options.
type Vault struct {
	Scheme   string
	Host     string
	Port     string
	Token    string
	CACert   string
	Insecure bool
	Prefix   string
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
type TLSConfig struct {
	ClientCertificate 	   string   `config:"/etc/ssl/certs/kafka-client.cert"`
	ClientCertificateKey   string   `config:"/etc/ssl/certs/kafka-client.key"`
	CaCert 				   string   `config:"/etc/ssl/certs/issuing-cert.cert"`
}

type KafkaTopics struct {
	Consume []string
	Produce []string
}

type Kafka struct {
	Brokers                []string `config:"default=localhost"`
	Port			       int      `config:"default=9093"`
	RequiredAcks           int      `config:"default=1"`
	Version                string   `config:"default=2.0.0"`
	ClientId               string   `config:"default=${spring.application.name}"`
	ClientIdSuffix         string   `config:"default=${spring.application.instance}"`
	Partitioner            string   `config:"default=hash"`
	Topics				   KafkaTopics
	TLS                    TLSConfig
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
		log.Printf("%s", err.Error())
		if _, ok := err.(viper.ConfigFileNotFoundError); ok {
			log.Print("No config found.")
		} else {
			log.Printf("Error reading config: %s", err.Error())
		}
	}

	// Bind config to environment based on expected injections.
	bindConfig(v, "Consul.Host", "SPRING_CLOUD_CONSUL_HOST")
	bindConfig(v, "Consul.Port", "SPRING_CLOUD_CONSUL_PORT")
	bindConfig(v, "Consul.Token", "SPRING_CLOUD_CONSUL_CONFIG_ACLTOKEN")
	bindConfig(v, "Vault.Scheme", "SPRING_CLOUD_VAULT_SCHEME")
	bindConfig(v, "Vault.Host", "SPRING_CLOUD_VAULT_HOST")
	bindConfig(v, "Vault.Port", "SPRING_CLOUD_VAULT_PORT")
	bindConfig(v, "Vault.Token", "SPRING_CLOUD_VAULT_TOKEN")
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
