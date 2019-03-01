# Setting up the environment
* virtualenv -p /usr/bin/python3 ~/Downloads/blog_env
* source blog_env/bin/activate
* pip install -r requirements.txt
* deactivate  # 退出虚拟环境
* python manage.py makemigrations
* python manage.py migrate
* python manage.py sqlmigrate blog 0001
* python manage.py createsuperuser
    >username: xuyuanzhe
    
    >password: ************

# run server
python manage.py runserver
