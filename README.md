# Markdown Publisher

[![GitHub Super-Linter](https://github.com/costa365/MarkdownPub/actions/workflows/lint.yml/badge.svg)](https://github.com/marketplace/actions/super-linter)
[![Pytest](https://github.com/costa365/MarkdownPub/actions/workflows/tests.yml/badge.svg)](https://github.com/marketplace/actions/run-pytest)


Publish Markdown documents.

- Write Markdown
- Publish
  - URL is provided
- Share URL

## Backend

Backend is a Python FastAPI app. View API documentation at '/docs'. Documents are stored in MongoDB. The connection string should be defined in an environment variable. For example:

```bash
export MONGO_CONNECT="mongodb+srv://name:password@cluster0.mcdesr.mongodb.net/?retryWrites=true&w=majority"
```

### API Endpoints

doc - POST (Markdown) - Returns ID to document
doc - GET (ID)

```bash
curl \
  'http://127.0.0.1:8000/doc' \
  -H 'Content-Type: application/json' \
  -d '{"doc":"# Test 2\n- Test1\n- Test2\n- Test3"}'
```

```bash
curl 'http://127.0.0.1:8000/doc/6428377ad8a75f3588dd8dc1'
```

### Run application

Docker and Docker Compose should be installed.

```bash
docker compose up
```

Access at [http://127.0.0.1:8005](http://127.0.0.1:8005)


### Linter

We use the GitHub Super-Linter. Run it locally:

```bash
docker pull github/super-linter:slim-v4
docker run -e RUN_LOCAL=true -v $PWD:/tmp/lint -w /tmp/lint github/super-linter
```
