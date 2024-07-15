## Coffee manager project

### Development
Language | Framework | Database
--- | --- | ---|
Python3 | Django5 | Sqlite3

### Documentation
* [UI/UX documentation](https://app.diagrams.net/#G1cHqEa9rIB-vwxNpvU5EfxVBAak23uPxW#%7B%22pageId%22%3A%22Ya_B0YewmzJZYzgCy9wD%22%7D)
* [Database documentation](https://app.diagrams.net/#G1cHqEa9rIB-vwxNpvU5EfxVBAak23uPxW#%7B%22pageId%22%3A%22n3Fa2zsxcn-xMpsse4Qi%22%7D)

### Start project
* Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

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
