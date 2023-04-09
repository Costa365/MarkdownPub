# Markdown Publisher

Publish MarkDown documents.

- Write MarkDown
- Publish
  - URL is provided
- Share URL

## Backend

Backend is a Python FastAPI app. View API documentation at '/docs'. Documents are stored in MongoDB. The connection string should be defined in an environment variable. For example:

```bash
export MONGO_CONNECT="mongodb+srv://name:password@cluster0.mcdesr.mongodb.net/?retryWrites=true&w=majority"
```

### API Endpoints

doc - POST (MarkDOwn) - Returns ID to document
doc - GET (ID)

```bash
curl -X POST \
  'http://127.0.0.1:8000/doc' \
  --header 'Content-Type: application/json' \
  --data-raw '{"doc":"# Test 2\n- Four\n-Five\n-Six"}'
```

```bash
curl 'http://127.0.0.1:8000/doc/6428377ad8a75f3588dd8dc1'
```

### Run application

Docker and Docker Compose should be installed.

```
docker compose up
```

Access at http://127.0.0.1:8005
