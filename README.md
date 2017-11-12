# django-docker
Example project of a Dockerized Django app

To run the thing:
`docker-compose up -d --build && docker-compose ps`

## Notes
- To ease of testing the API, all views are `@csrf_exempt`
- Database is locally persisted in /tmp/postgres
- By default, local server runs on http://localhost:8000
- You can use the included postman collection for testing
