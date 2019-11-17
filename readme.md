**Running Locally with Docker**
    
    docker-compose run web python manage.py migrate
    docker-compose up -d --build
    
**Upload news from news.ycombinator.com**

    docker-compose run web python manage.py uploadposts

