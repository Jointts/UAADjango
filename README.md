# Sample UAA integration in Django

## Launching local UAA server
Download and start local UAA server
```
git clone git://github.com/cloudfoundry/uaa.git
cd uaa
./gradlew run
```

Install UAA CLI
```
sudo apt install rubygems
gem install cf-uaac
```

Set UAA server uri
```
uaac target http://localhost:8080/uaa
```

Login as default admin
```
uaac token client get admin -s adminsecret
```

Add test client
```
uaac client add testclient -s testclientsecret --name TestClient --scope openid,profile,email,address,phone --authorized_grant_types authorization_code,refresh_token,client_credentials,password --authorities uaa.resource --redirect_uri http://localhost:8081/login/oauth2/code/uaa
```

Add new test user
```
uaac user add testuser -p testpassword --emails test@test.com
```

Later you can authenticate in django with
```
username: testuser
password: testpassword
```
Groups can be added with
```
uaac group add resource.read
```
Groups can be attached to users with
```
 uaac member add resource.read testuser
```

## Launching the application
Create new virtualenv
```
python3 -m venv ./venv
```
Activate virtualenv
```
source venv/bin/activate 
(Optional) Configure "Project Interpreter" from Pycharm settings
```
Install dependencies
```
pip install -r requirements
```
Apply database migrations (needed for Django to start)
```
python manage.py migrate
```
Run server with the following command
```
python manage.py runserver 8000
```

UAA connection parameters can be changed in UAA/settings.py, the defaults are
```
UAA_ISSUER_URI = 'http://localhost:8080/uaa/oauth/token'
UAA_CLIENT_ID = 'testclient'
UAA_CLIENT_SECRET = 'testclientsecret'
```

Login can be accessed at http://127.0.0.1:8000/accounts/login (requires local UAA server to be running)