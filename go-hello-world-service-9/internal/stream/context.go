package stream

import (
	"context"
)

type contextKey int

const (
	contextKeyKafkaService contextKey = iota
)

func contextWithService(ctx context.Context, service KafkaService) context.Context {
	return context.WithValue(ctx, contextKeyKafkaService, service)
}

func kafkaServiceFromContext(ctx context.Context) KafkaService {
	value, _ := ctx.Value(contextKeyKafkaService).(KafkaService)
	return value
}