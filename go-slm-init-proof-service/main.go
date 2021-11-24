//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package main

import (
	"context"
	"log"

	"github.com/CiscoDevNet/msx-examples/go-slm-init-proof-service/internal/config"
	"github.com/CiscoDevNet/msx-examples/go-slm-init-proof-service/internal/consul"
	"github.com/CiscoDevNet/msx-examples/go-slm-init-proof-service/internal/datastore"
	"github.com/CiscoDevNet/msx-examples/go-slm-init-proof-service/internal/vault"

	openapi "github.com/CiscoDevNet/msx-examples/go-slm-init-proof-service/go"
)

func main() {
	// Read the configuration.
	config := config.ReadConfig()
	log.Printf("go-slm-init-proof-service Server started config=%#v", config)

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

	testDb(db)

	// Create the resource controllers.
	// ItemsApiController := openapi.NewItemsApiController(db)
	// LanguagesApiController := openapi.NewLanguagesApiController(db)
	// router := openapi.NewRouter(ItemsApiController, LanguagesApiController)
	// log.Fatal(http.ListenAndServe(":8081", router))
}

func testConsul(config *config.Config, consul *consul.HelloWorldConsul) {
	// Read our favourites from Consul and print them to the console.
	// Do not leak config in production as it is a security violation.

	// log.Printf("config.Consul=%#v", config.Consul)
	// log.Printf("consul=%#v", consul)

	log.Printf("config.Consul.Prefix=%s.", config.Consul.Prefix)
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

func testDb(db *datastore.Cockroach) {
	ctx := context.Background()

	result, err := db.GetLanguages(ctx)
	if err != nil {
		log.Printf("GetLanguages Error=%s", err.Error())
		return
	}

	log.Printf("GetLanguages Result Code=%d", result.Code)
	log.Printf("GetLanguages Result Body=%#v", result.Body)

	languages, ok := result.Body.([]openapi.Language)
	if ok && containsLanguage(languages, "French") {
		log.Printf("French already exists!")
		return
	}

	log.Printf("Lets add French!")

	language := openapi.Language{Name: "French", Description: "A Romance language of the Indo-European family"}
	result, err = db.CreateLanguage(ctx, language)
	if err != nil {
		log.Printf("CreateLanguage Error=%s", err.Error())
		return
	}

	language = result.Body.(openapi.Language)
	item := openapi.Item{LanguageId: language.Id, LanguageName: "French", Value: "Bonjour monde"}
	result, err = db.CreateItem(ctx, item)
	if err != nil {
		log.Printf("CreateItem Error=%s", err.Error())
		return
	}
}

func containsLanguage(languages []openapi.Language, name string) bool {
	for _, language := range languages {
		if language.Name == name {
			return true
		}
	}
	return false
}
