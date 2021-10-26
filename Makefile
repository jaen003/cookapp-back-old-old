.PHONY: run
run :
	@echo "Running balancer architecture"
	@docker-compose up --remove-orphans

.PHONY: stop
stop :
	@echo "Stopping balancer architecture"
	@docker-compose stop