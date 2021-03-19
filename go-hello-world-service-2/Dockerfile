#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All Rights reserved
#
FROM golang:alpine as builder
RUN apk update && apk add ca-certificates upx git
COPY go/ /go/src/github.com/CiscoDevNet/msx-examples/go-hello-world-service-2/go
COPY go.mod go.sum main.go /go/src/github.com/CiscoDevNet/msx-examples/go-hello-world-service-2/
WORKDIR /go/src/github.com/CiscoDevNet/msx-examples/go-hello-world-service-2
RUN go mod vendor \
  && go build -ldflags="-s -w" -o helloworld main.go \
  && upx helloworld
# Create appuser.
ENV USER=helloworld
ENV UID=10001
# See https://stackoverflow.com/a/55757473/12429735RUN
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    "${USER}"
RUN chown helloworld:helloworld /go/src/github.com/CiscoDevNet/msx-examples/go-hello-world-service-2/helloworld

FROM scratch
COPY --from=builder /go/src/github.com/CiscoDevNet/msx-examples/go-hello-world-service-2/helloworld /
COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /etc/group /etc/group
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /lib/ld-musl-x86_64.so.1 /lib/ld-musl-x86_64.so.1
USER helloworld:helloworld
ENTRYPOINT ["/helloworld"]
