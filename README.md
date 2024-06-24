## Coffee manager project

### Development
Language | Framework | Database
--- | --- | ---|
Python3 | Django5 | Sqlite3

### Start project
* Copy environment variables file
    ```bash
    cp .env.example .env
    ```

* Change directory to source folder
    ```bash
    cd src/
    ```

* Run server
    ```bash
    python manage.py runserver 0.0.0.0:80
    ```
    > Note: 0.0.0.0 is public host to any network. 80 is the port of server
