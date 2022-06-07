# Launch the docker for flask app

    docker image build -t breastcancer . 
>with this sentence, we will create the image necessary to contain the flask app; it is necessary to run everytime any change is deployed.

    docker run -p 3113:3113 -d breastcancer
>this is necessary for creating the container where the flask app will be launched


    pipenv install sqlalchemy psycopg2-binary

>in case sqlalchemy produces any error, run the previous instruction

    docker ps 
    docker stop ID
    docker rm   ID
>"necessary code to delete the container"

# Launch the docker for the database

    docker run --name breastcancerDB -p 5432:5432 -e POSTGRES_DB=dbbreastcancer 
    -e POSTGRES_PASSWORD=123 -d postgres
    docker-compose up
    
    pip freeze > requirements.txt

# Angular necessary information
    npm install -g @angular/cli@13.3.7 