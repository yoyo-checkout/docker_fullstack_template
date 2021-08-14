```bash
docker-compose build
sudo docker-compose run backend python manage.py makemigrations --skip-checks MainApp
sudo docker-compose run backend python manage.py migrate MainApp
docker-compose up
```