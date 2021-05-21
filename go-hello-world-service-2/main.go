//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package main

import (
	"log"
	"net/http"

	openapi "github.com/CiscoDevNet/msx-examples/go-hello-world-service-2/go"
)

func main() {
	log.Printf("Hello World - Server Started")

	ItemsApiService := openapi.NewItemsApiService()
	ItemsApiController := openapi.NewItemsApiController(ItemsApiService)

	LanguagesApiService := openapi.NewLanguagesApiService()
	LanguagesApiController := openapi.NewLanguagesApiController(LanguagesApiService)

	router := openapi.NewRouter(ItemsApiController, LanguagesApiController)

	log.Fatal(http.ListenAndServe(":8080", router))
}
