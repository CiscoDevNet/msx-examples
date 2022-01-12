//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
module github.com/CiscoDevNet/msx-examples/go-hello-world-service-8

go 1.13

require (
	github.com/CiscoDevNet/go-msx-security v1.0.1
	github.com/CiscoDevNet/go-msx-swagger v1.0.1
	github.com/google/uuid v1.2.0
	github.com/gorilla/mux v1.8.0
	github.com/hashicorp/consul/api v1.1.0
	github.com/hashicorp/vault/api v1.0.4
	github.com/jackc/pgx/v4 v4.10.1
	github.com/spf13/viper v1.7.1
)

replace github.com/CiscoDevNet/msx-examples/go-hello-world-service-8/go => ./go/
