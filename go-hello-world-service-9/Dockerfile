FROM golang:alpine as builder
RUN apk update && apk add ca-certificates upx git
COPY go/ /go/src/github.com/CiscoDevNet/msx-examples/go-hello-world-service-9/go
COPY go.mod go.sum main.go /go/src/github.com/CiscoDevNet/msx-examples/go-hello-world-service-9/
COPY internal/ /go/src/github.com/CiscoDevNet/msx-examples/go-hello-world-service-9/internal
COPY HelloWorldService-1.json /
WORKDIR /go/src/github.com/CiscoDevNet/msx-examples/go-hello-world-service-9
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
RUN chown helloworld:helloworld /go/src/github.com/CiscoDevNet/msx-examples/go-hello-world-service-9/helloworld
RUN chown helloworld:helloworld /HelloWorldService-1.json

FROM alpine:latest
COPY --from=builder /go/src/github.com/CiscoDevNet/msx-examples/go-hello-world-service-9/helloworld /
COPY --from=builder /HelloWorldService-1.json /
COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /etc/group /etc/group

COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
COPY --from=builder /lib/ld-musl-x86_64.so.1 /lib/ld-musl-x86_64.so.1
ENTRYPOINT ["/helloworld"]