python --version
Python 3.8.2

pip --version
pip 20.2.3


pip install -r requirements.txt
pip list

Run app
Python run_app.py

Run db
Python run_db.py

Run db with seed
Python run_db_seed.py

docker
docker build -t mypyimage .
docker run -d --name mypycontainer -p 8000:80 mypyimage

https://fastapi.tiangolo.com/tutorial/debugging/

Api Doc
http://127.0.0.1:8000/docs