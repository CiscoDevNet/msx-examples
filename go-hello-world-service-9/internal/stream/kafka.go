package stream

import (
	"context"
	"crypto/tls"
	"crypto/x509"
	"fmt"
	"github.com/CiscoDevNet/msx-examples/go-hello-world-service-9/internal/config"
	"github.com/Shopify/sarama"
	"io/ioutil"
	"log"
	"strings"
)
type KafkaService interface {
	GetClient() *sarama.Client
	Produce(message string, topic string) error
	ConsumeTopicMessages(topic string) ([]string, error)
}
type kafkaServiceImpl struct {
	Client *sarama.Client
}

func brokerAddresses(kafkaConfig config.Kafka) []string {
	var results []string
	for _, broker := range kafkaConfig.Brokers {
		if !strings.Contains(broker, ":") {
			results = append(results, fmt.Sprintf("%s:%d", broker, kafkaConfig.Port))
		} else {
			results = append(results, broker)
		}
	}
	return results
}

func (k kafkaServiceImpl) GetClient() *sarama.Client {
	return k.Client
}
func (k kafkaServiceImpl) Produce(message string, topic string) (err error) {
	producer, err := sarama.NewSyncProducerFromClient(*(k.Client))
	if err != nil {
		return
	}
	msg := sarama.ProducerMessage{
		Topic: topic,
		Value: sarama.ByteEncoder(message),
	}
	_, _, err = producer.SendMessage(&msg)
	return
}
func  (k kafkaServiceImpl) ConsumeTopicMessages(topic string) (messages []string, error error) {
	consumer, err := sarama.NewConsumerFromClient(*(k.Client))
	if err != nil {
		log.Println("Error in sarama client ", err)
		return
	}

	defer func() {
		if err := consumer.Close(); err != nil {
			panic(err)
		}
	}()

	msg, consumerErrors := k.consume(topic, consumer)
	doneCh := make(chan struct{})
	go func() {
		for {
			select {
			case msg := <-msg:
				log.Println("Received messages on topic: ", topic, string(msg.Value))
				messages = append(messages, string(msg.Value))
			case consumerError := <-consumerErrors:
				log.Println("Received consumerError ", string(consumerError.Topic), string(consumerError.Partition), consumerError.Err)
				error = consumerError
				doneCh <- struct{}{}
			}
		}
	}()

	<-doneCh
	return
}

func  (k kafkaServiceImpl) consume(topic string, master sarama.Consumer) (chan *sarama.ConsumerMessage, chan *sarama.ConsumerError) {
	consumers := make(chan *sarama.ConsumerMessage)
	errors := make(chan *sarama.ConsumerError)
	partitions, _ := master.Partitions(topic)
	// this only consumes partition no 1, you would probably want to consume all partitions
	consumer, err := master.ConsumePartition(topic, partitions[0], sarama.OffsetNewest)
	if nil != err {
		log.Printf("Topic %v Partitions: %v", topic, partitions)
		panic(err)
	}
	go func(topic string, consumer sarama.PartitionConsumer) {
		for {
			select {
			case consumerError := <-consumer.Errors():
				errors <- consumerError
			case msg := <-consumer.Messages():
				consumers <- msg
			}
		}
	}(topic, consumer)
	return consumers, errors
}

func NewSaramaClient(cfg config.Kafka) (sarama.Client, error)  {
	saramaConfig := sarama.NewConfig()
	saramaConfig.Net.TLS.Enable = true
	certificate, err := tls.LoadX509KeyPair(cfg.TLS.ClientCertificate, cfg.TLS.ClientCertificateKey)
	if err != nil {
		return nil, err
	}
	caCert, err := ioutil.ReadFile(cfg.TLS.CaCert)
	if err != nil {
		log.Fatalln("Error Reading issuing certificate ", err)
		return nil, err
	}
	caCertPool := x509.NewCertPool()
	caCertPool.AppendCertsFromPEM(caCert)
	tlsConfig := tls.Config{}
	tlsConfig.RootCAs = caCertPool
	tlsConfig.Certificates = []tls.Certificate{certificate}
	tlsConfig.InsecureSkipVerify = true
	saramaConfig.Net.TLS.Config = &tlsConfig
	// set version
	saramaConfig.ClientID = cfg.ClientId + "-" + cfg.ClientIdSuffix
		for _, v := range sarama.SupportedVersions {
			if v.String() == cfg.Version {
				saramaConfig.Version = v
			}
		}
	saramaConfig.Producer.Return.Successes = true
	switch cfg.Partitioner {
	case "hash":
		saramaConfig.Producer.Partitioner = sarama.NewHashPartitioner
	case "roundrobin":
		saramaConfig.Producer.Partitioner = sarama.NewRoundRobinPartitioner
	case "random":
		saramaConfig.Producer.Partitioner = sarama.NewRandomPartitioner
	case "manual":
		saramaConfig.Producer.Partitioner = sarama.NewManualPartitioner
	}

	brokerAddresses := brokerAddresses(cfg)
	return sarama.NewClient(brokerAddresses, saramaConfig)
}


func NewKafkaService(ctx context.Context) (kafkaService KafkaService, err error) {
	kafkaService = kafkaServiceFromContext(ctx)
	config := config.ReadConfig()
	if kafkaService == nil {
		saramaClient, err := NewSaramaClient(config.Kafka)
		if err != nil {
			return nil, err
		}
		kafkaService = &kafkaServiceImpl{
			Client: &saramaClient,
		}
	}
	return
}