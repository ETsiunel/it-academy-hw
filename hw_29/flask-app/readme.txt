Build image
    docker build -t my-cats-app .
Run container
    docker run -p 8866:8866 --name cats-container my-cats-app
View app
    http://localhost:8866