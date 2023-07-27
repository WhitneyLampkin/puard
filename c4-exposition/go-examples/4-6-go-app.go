package main

import (
	"log"
	"net/http"

	// "github.com/prometheus/client_golang/prometheus"
	// "github.com/prometheus/client_golang/prometheus/promauto"
	// "github.com/prometheus/client_golang/prometheus/promhttp"
	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promauto"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

var (
	requests = promauto.NewCounter(
		prometheus.CounterOpts{
			Name: "hello_worlds_total",
			Help: "Hello Worlds requested.",
		})
)

func handler(w http.ResponseWriter, r *http.Request) {
	requests.Inc()
	w.Write([]byte("Hello World"))
}

func main() {
	http.HandleFunc("/", handler)
	// Is this the exposition of the metrics piece the chapter is centered around?
	http.Handle("/metrics", promhttp.Handler())
	log.Fatal(http.ListenAndServe(":8081", nil))
}
