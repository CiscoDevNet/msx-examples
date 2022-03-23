//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
module github.com/CiscoDevNet/msx-examples/go-hello-world-service-3

go 1.13

require (
	github.com/gorilla/mux v1.7.3
	github.com/hashicorp/consul/api v1.8.1
	github.com/spf13/viper v1.7.1
)

replace github.com/CiscoDevNet/msx-examples/go-hello-world-service-3/go => ./go/
