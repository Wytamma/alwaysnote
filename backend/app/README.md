Create a `.env` file with the following
```
SECRET_KEY=""  
PASSWORD=""  
BACKEND_CORS_ORIGINS=""  
DATABASE_URL=""
```

alias pg_start='pg_ctl -D /usr/local/var/postgres start'
alias pg_stop='pg_ctl -D /usr/local/var/postgres stop'

git push heroku master

git subtree push --prefix backend/app heroku master

https://www.geekality.net/2019/03/13/heroku-deploy-sub-directory/
