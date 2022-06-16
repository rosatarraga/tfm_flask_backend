# Launch the docker for flask app

    docker image build -t breastcancer . 
>with this sentence, we will create the image necessary to contain the flask app; it is necessary to run everytime any change is deployed.

    docker run --name breastcancer -p 3113:3113 -d breastcancer
>this is necessary for creating the container where the flask app will be launched

    docker ps 
    docker stop ID
    docker rm   ID
>"necessary code to delete the container"


# Launch the docker for angular app
    docker build -t breast-cancer-angular .
    docker run  --name breast-cancer-angular -p 8000:80 -d breast-cancer-angular 
>go to the angular_app folder and build the angular docker


# Angular necessary information
    npm install -g @angular/cli@13.3.7 
