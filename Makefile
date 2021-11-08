.PHONY: run
run :
	@echo "Running balancer architecture"
	@docker-compose up --remove-orphans

.PHONY: stop
stop :
	@echo "Stopping balancer architecture"
	@docker-compose stop

.PHONY: test
test :
	@echo "Starting cookapp suite tests"
	@docker-compose up --remove-orphans backoffice_backend_test