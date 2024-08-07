# Run
You can now run this project with built image. The repo was old and some modification for building process was necessary. I made some changes and tested it. The web app have some problems that I have not resolved them yet. You can write a little and simple program to overcome this issue.

```bash
docker compose up -d
```

```bash
docker run -d --name darkweb-search-engine-onion-crawler --cpus="0.5" --restart=always --network=dark-web-crawler_default  dapperblondie/scraper_crawler_complete /opt/torscraper/scripts/start_onion_scrapy.sh

docker exec darkweb-search-engine-onion-crawler /opt/torscraper/scripts/elasticsearch_migrate.sh

docker exec -d darkweb-search-engine-onion-crawler /opt/torscraper/scripts/push_list.sh /opt/torscraper/onions_list/onions.txt
```
