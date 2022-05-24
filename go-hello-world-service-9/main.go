//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package main

import (
	"context"
	openapi "github.com/CiscoDevNet/msx-examples/go-hello-world-service-9/go"
	"github.com/CiscoDevNet/msx-examples/go-hello-world-service-9/internal/config"
	"github.com/CiscoDevNet/msx-examples/go-hello-world-service-9/internal/consul"
	"github.com/CiscoDevNet/msx-examples/go-hello-world-service-9/internal/datastore"
	"github.com/CiscoDevNet/msx-examples/go-hello-world-service-9/internal/stream"
	"github.com/CiscoDevNet/msx-examples/go-hello-world-service-9/internal/swagger"
	"github.com/CiscoDevNet/msx-examples/go-hello-world-service-9/internal/vault"
	"log"
	"net/http"
)

func main() {
	// Read the configuration.
	config := config.ReadConfig()
	log.Printf("Service started")

	// Setup Consul.
	consul, err := consul.NewConsul(config)
	if err != nil {
		log.Printf("Could not initialize Consul: %s", err.Error())
	}
	config.Consul.Prefix = consul.FindPrefix()
	config.Vault.Prefix = "secret/" + config.Consul.Prefix
	testConsul(config, &consul)

	// Setup Vault.
	vault, err := vault.NewVault(config)
	if err != nil {
		log.Printf("Could not initialize Vault: %s", err.Error())
	}
	testVault(config, &vault)

	// Setup CockroachDB
	datastore.UpdateConfig(config, &consul, &vault)
	db, err := datastore.NewCockroachDB(config)
	if err != nil {
		log.Fatal("FATAL: Could not connect to DB: %s", err.Error())
	}
	err = db.BuildSchema()
	if err != nil {
		log.Fatal("FATAL: Could not build DB schema: %s", err.Error())
	}

	// Setup Swagger.
	swagger.UpdateConfig(config, &consul, &vault)
	swagger, err := swagger.NewSwagger(config)
	if err != nil {
		log.Fatalf("Could not setup Swagger: %s", err.Error())
	}

	// Setup Controllers
	ItemsApiController := openapi.NewItemsApiController(db)
	LanguagesApiController := openapi.NewLanguagesApiController(db)

	// Add insecure routes for Items and Languages.
	router := openapi.NewRouter(ItemsApiController, LanguagesApiController)

	// Add route for Swagger.
	router.PathPrefix("/helloworld/swagger").HandlerFunc(swagger.SwaggerRoutes)
	listenToTopics(*config)
	log.Fatal(http.ListenAndServe(":8080", router))
}
func listenToTopics(config config.Config) {
	kafkaClient, error := stream.NewKafkaService(context.Background())
	if error != nil {
		log.Printf("Error opening a connection to kafka, could not listen to topics %s", error)
	} else {
		for _, topic := range config.Kafka.Topics.Consume {
			log.Println("Kicking off consumer for topic ", topic)
			go kafkaClient.ConsumeTopicMessages(topic)
		}
	}
}

func testConsul(config *config.Config, consul *consul.HelloWorldConsul) {
	// Read our favourites from Consul and print them to the console.
	// Do not leak config in production as it is a security violation.
	favouriteColor, _ := consul.GetString(config.Consul.Prefix+"/helloworldservice/favourite.color", "UNKNOWN")
	log.Printf("My favourite color is %s.", favouriteColor)
	favouriteFood, _ := consul.GetString(config.Consul.Prefix+"/helloworldservice/favourite.food", "UNKNOWN")
	log.Printf("My favourite food is %s.", favouriteFood)
	favouriteDinosaur, _ := consul.GetString(config.Consul.Prefix+"/helloworldservice/favourite.dinosaur", "UNKNOWN")
	log.Printf("My favourite dinosaur is %s.", favouriteDinosaur)
}

func testVault(config *config.Config, vault *vault.HelloWorldVault) {
	// Read a secret from Vault and it to the console.
	// Do not leak secrets in production as it is a security violation.
	secretSquirrelLocation, _ := vault.GetString(config.Vault.Prefix+"/helloworldservice/", "secret.squirrel.location", "UNKNOWN")
	log.Printf("Where are the acorns buried?")
	log.Print(secretSquirrelLocation)
}