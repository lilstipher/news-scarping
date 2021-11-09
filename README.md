# news-scarping
full news scarping pipeline

## Setup
For run everything just run the `bootstrap.sh` script.
However, here are the steps to start the project:
- Go in db folder then run
 ```bash 
  docker-compose up -d 
```
- In news-scraper folder, there is a README.md file, follow all instructions in.
- In news-api folder, there is a README.md file, follow all instructions in.
You can found the api at http://localhost:8000/docs (default port)

## Shutdown 
```bash
cd db  
docker-compose down
kill -9 $(pgrep -f uvicorn) #Stop api server
````

## Limit
- There is no authentication 
- No data persistence
- The scraper should use kafka in production

