### Bring up the postgres DB

```bash
docker-compose up -d
```

### Open postgres shell

```bash
docker-compose exec pg-db psql -U <user> -d <db_name>
```
