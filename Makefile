.PHONY: setup run-backend run-frontend run-celery run-valkey

setup:
	@echo "Setting up backend..."
	python -m venv venv && ./venv/bin/pip install -r server/requirements.txt
	@echo "Setting up frontend..."
	cd client && npm install

run-valkey:
	sudo systemctl start valkey

run-backend:
	./venv/bin/python -m server.run

run-celery:
	./venv/bin/celery -A server.make_celery:celery_app worker --loglevel=info

run-celery-beat:
	./venv/bin/celery -A server.make_celery:celery_app beat --loglevel=info

run-frontend:
	cd client && npm run dev
