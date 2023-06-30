from quay.io/prometheuscommunity/postgres-exporter

podman run -d --network dbnet --net=monitor --name postgres-exporter -e DATA_SOURCE_NAME="postgresql://postgres:password@pgsql:5432/postgres?sslmode=disable" quay.io/prometheuscommunity/postgres-exporter
