pipenv install sqlalchemy psycopg2-binary

docker image build -t breastcancer . --> every change, build again
docker run -p 3113:3113 -d breastcancer


docker ps 
docker stop ID
docker rm   ID



docker run --name breastcancerDB -p 5432:5432 -e POSTGRES_DB=dbbreastcancer -e POSTGRES_PASSWORD=123 -d postgres

docker-compose up
 pip freeze > requirements.txt




npm install -g @angular/cli@13.3.7 