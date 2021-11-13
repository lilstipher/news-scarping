
echo "Setup python virtual env"
python -m venv .venv
source $(pwd)/.venv/bin/activate

echo "Setting up mongodb" 
 
 cd db && docker-compose up -d && cd ..
 #-f $(pwd)/db/docker-compose.yml
 echo "Current Path: $(pwd)"

while ! docker exec -d mongodb pgrep mongodb; do sleep 1;echo " waiting for mongo..." ;done

 echo "Mongo is ok"

echo "Setting up projects requirements" 
pip install -U pip setuptools setuptools_scm tox

echo "Install projects deps.."
cd news-api && pip install -e . && cd ..
cd news-scraper && pip install -e . && cd ..
echo "Current Path: $(pwd)"

echo "Run scraper"
cd news-scraper &&   python -m news_scraper.run -v && cd ..


echo "Run the api"
cd news-api &&   uvicorn main:app   --app-dir src/news_api  &
