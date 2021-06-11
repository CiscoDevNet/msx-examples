//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package main

import (
	"github.com/CiscoDevNet/msx-examples/go-hello-world-service-3/internal/config"
	"github.com/CiscoDevNet/msx-examples/go-hello-world-service-3/internal/consul"
	"log"
	"net/http"

	openapi "github.com/CiscoDevNet/msx-examples/go-hello-world-service-3/go"
)

func main() {
	// Read the configuration.
	config := config.ReadConfig()
	log.Printf("Server started")
	log.Printf("config.host=" + config.Consul.Host)
	log.Printf("config.port=" + config.Consul.Port)

	// Setup Consul.
	consul, err := consul.NewConsul(config)
	if err != nil {
		log.Printf("Could not initialize Consul: %s", err.Error())
	}
	testConsul(&consul)

	ItemsApiService := openapi.NewItemsApiService()
	ItemsApiController := openapi.NewItemsApiController(ItemsApiService)

	LanguagesApiService := openapi.NewLanguagesApiService()
	LanguagesApiController := openapi.NewLanguagesApiController(LanguagesApiService)

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