//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
module github.com/CiscoDevNet/msx-examples/go-hello-world-service-6

go 1.13

replace github.com/CiscoDevNet/msx-examples/go-hello-world-service-6/go => ./go/

require (
	cloud.google.com/go/datastore v1.1.0 // indirect
	cloud.google.com/go/pubsub v1.3.1 // indirect
	github.com/CiscoDevNet/go-msx-swagger v1.0.1
	github.com/coreos/go-systemd v0.0.0-20190719114852-fd7a80b32e1f // indirect
	github.com/google/btree v1.0.0 // indirect
	github.com/google/uuid v1.3.0
	github.com/gorilla/mux v1.8.0
	github.com/hashicorp/consul/api v1.12.0
	github.com/hashicorp/vault/api v1.5.0
	github.com/jackc/pgx/v4 v4.15.0
	github.com/konsorten/go-windows-terminal-sequences v1.0.2 // indirect
	github.com/spf13/viper v1.11.0
	github.com/stretchr/objx v0.2.0 // indirect
	golang.org/x/exp v0.0.0-20200224162631-6cc2880d07d6 // indirect
)
