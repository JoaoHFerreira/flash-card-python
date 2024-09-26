test-get-all:
	curl http://0.0.0.0:8000/learning_topic/

test-get-by-id:
	curl http://0.0.0.0:8000/learning_topic/1

test-post:
	curl -X POST http://0.0.0.0:8000/learning_topic/ \
	-H 'Content-Type: application/json' \
	-d '{"subject": "Mathematics"}'

test-put:
	curl -X PUT http://0.0.0.0:8000/learning_topic/1 \
	-H 'Content-Type: application/json' \
	-d '{"subject": "Advanced Mathematics"}'

test-delete:
	curl -X DELETE http://0.0.0.0:8000/learning_topic/1