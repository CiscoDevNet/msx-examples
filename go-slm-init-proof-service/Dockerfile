#
# Copyright (c) 2021 Cisco Systems, Inc and its affiliates
# All Rights reserved
#
FROM golang:alpine as builder
RUN apk update && apk add ca-certificates upx git
COPY go/ /go/src/github.com/CiscoDevNet/msx-examples/go-slm-init-proof-service/go
COPY go.mod go.sum main.go /go/src/github.com/CiscoDevNet/msx-examples/go-slm-init-proof-service/
# REGION BOOTSTRAP FILES
COPY internal/ /go/src/github.com/CiscoDevNet/msx-examples/go-slm-init-proof-service/internal
# ENDREGION BOOTSTRAP FILES
WORKDIR /go/src/github.com/CiscoDevNet/msx-examples/go-slm-init-proof-service
RUN go mod vendor \
  && go build -ldflags="-s -w" -o slminitproof main.go \
  && upx slminitproof
# Create appuser.
ENV USER=slminitproof
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
RUN chown slminitproof:slminitproof /go/src/github.com/CiscoDevNet/msx-examples/go-slm-init-proof-service/slminitproof


FROM scratch
COPY --from=builder /go/src/github.com/CiscoDevNet/msx-examples/go-slm-init-proof-service/slminitproof /
COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /etc/group /etc/group
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /lib/ld-musl-x86_64.so.1 /lib/ld-musl-x86_64.so.1
USER slminitproof:slminitproof
ENTRYPOINT ["/slminitproof"]
