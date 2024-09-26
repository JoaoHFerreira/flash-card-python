# Easy Python Docker - Quick Development Setup

Follow these steps to quickly set up a Python development environment using Docker.

1. **Navigate to the Docker directory:**
   ```bash
   cd docker
   ```

2. **Optional: Edit the Dockerfile**
   If needed, modify the `Dockerfile` located at:
   ```
   python_easy_docker_compose/docker/Dockerfile
   ```

3. **Add your required libraries:**
   Specify any additional Python libraries in:
   ```
   python_easy_docker_compose/docker/requirements
   ```

4. **Build the Docker image:**
   ```bash
   docker-compose build python-service
   ```

5. **Run the container:**
   Launch the container with:
   ```bash
   docker-compose run --rm -it python-service bash
   ```

6. Run  Database
docker-compose exec db psql -U user -d python_flash_db



# Testing

Certainly, let's organize the cURL commands into a list based on their HTTP methods:

**GET**

```bash
# Get all learning topics
curl http://0.0.0.0:8000/learning_topic/

# Get a specific learning topic by ID
curl http://0.0.0.0:8000/learning_topic/1 
```

**POST**

```bash
# Create a new learning topic
curl -X POST http://0.0.0.0:8000/learning_topic/ \
-H 'Content-Type: application/json' \
-d '{"subject": "Mathematics"}'
```

**PUT**

```bash
# Update a learning topic
curl -X PUT http://0.0.0.0:8000/learning_topic/1 \
-H 'Content-Type: application/json' \
-d '{"subject": "Advanced Mathematics"}'
```

**DELETE**

```bash
# Delete a learning topic
curl -X DELETE http://0.0.0.0:8000/learning_topic/1
```

Feel free to request any further adjustments or additions to the list!
