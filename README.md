# CNPJ Scrapper


## Instalação

### Criar network
```shell
docker network create scrapper
```

### Subir o docker
```shell
docker-compose up -d
```

## Iniciando

### Rodando o Seed
```
docker-compose run --rm app seed.py
```

### Rodando o Scrapper
```
docker-compose run --rm app app.py
```