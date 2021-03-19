//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package main

import (
	"github.com/CiscoDevNet/msx-examples/go-hello-world-service-5/internal/config"
	"github.com/CiscoDevNet/msx-examples/go-hello-world-service-5/internal/consul"
	"github.com/CiscoDevNet/msx-examples/go-hello-world-service-5/internal/datastore"
	"github.com/CiscoDevNet/msx-examples/go-hello-world-service-5/internal/vault"
	"log"
	"net/http"

	openapi "github.com/CiscoDevNet/msx-examples/go-hello-world-service-5/go"
)

func main() {
	// Read the configuration.
	config := config.ReadConfig()
	log.Printf("Server started")

	// Setup Consul.
	consul, err := consul.NewConsul(config)
	if err != nil {
		log.Printf("Could not initialize Consul: %s", err.Error())
	}
	testConsul(&consul)

	// Setup Vault.
	vault, err := vault.NewVault(config)
	if err != nil {
		log.Printf("Could not initialize Vault: %s", err.Error())
	}
	testVault(&vault)

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

	// Create the resource controllers.
	ItemsApiController := openapi.NewItemsApiController(db)
	LanguagesApiController := openapi.NewLanguagesApiController(db)

	router := openapi.NewRouter(ItemsApiController, LanguagesApiController)
	log.Fatal(http.ListenAndServe(":8080", router))
}

func testConsul(c *consul.HelloWorldConsul) {
	// Read our favourites from Consul and print them to the console.
	// Do not leak config in production as it is a security violation.
	favouriteColor, _:= c.GetString("thirdpartyservices/helloworldservice/favourite.color", "UNKNOWN")
	log.Printf("My favourite color is %s.", favouriteColor)
	favouriteFood, _ := c.GetString("thirdpartyservices/helloworldservice/favourite.food", "UNKNOWN")
	log.Printf("My favourite food is %s.", favouriteFood)
	favouriteDinosaur, _ := c.GetString("thirdpartyservices/helloworldservice/favourite.dinosaur", "UNKNOWN")
	log.Printf("My favourite dinosaur is %s.", favouriteDinosaur)
}

func testVault(v *vault.HelloWorldVault) {
	// Read a secret from Vault  and it to the console.
	// Do not leak secrets in production as it is a security violation.
	secretSquirrelLocation, _ := v.GetString("secret/thirdpartyservices/helloworldservice/", "secret.squirrel.location", "UNKNOWN")
	log.Printf("Where are the acorns buried?")
	log.Print(secretSquirrelLocation)
}