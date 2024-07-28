## Task manager project
### Development
Language | Framework | Database
--- | --- | ---|
Python3 | Django5 | Sqlite3


### Documentation
* [UI/UX documentation](https://app.diagrams.net/#G1cHqEa9rIB-vwxNpvU5EfxVBAak23uPxW#%7B%22pageId%22%3A%22Ya_B0YewmzJZYzgCy9wD%22%7D)
* [Database documentation](https://app.diagrams.net/#G1cHqEa9rIB-vwxNpvU5EfxVBAak23uPxW#%7B%22pageId%22%3A%22n3Fa2zsxcn-xMpsse4Qi%22%7D)

<br>

## Prepare for project
* Download and install `Python3`
    Offical website | Windows store | Mac brew
    --- | --- | --- |
    [python.org](https://www.python.org/) | [apps.microsoft.com](https://apps.microsoft.com/search?query=python) | [docs.brew.sh](https://docs.brew.sh/Homebrew-and-Python)

* Copy `.env.example` to `.env` file
    ```bash
    cp .env.example .env
    ```

<br>

## Build and run project
### Build project with Windows batch
* Run this command or double click to `run_server.bat`
    ```bash
    run_server.bat
    ```


### Build project with docker-compose
* Change directory to source folder
    ```bash
    cd docker/
    ```

* Copy `.env.example` to `.env` file
    ```bash
    cp .env.example .env
    ```

* Create network
    ```bash
    docker network create task_manager_network
    ```

* Start server

    ```bash
    docker-compose up --build -d
    ```

* Shutdown server
    ```bash
    docker-compose down
    ```


### Build project manual
* Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

* Change directory to source folder
    ```bash
    cd src/
    ```

* Migrate database
    ```bash
    python .\manage.py migrate
    ```
    ```bash
    python .\manage.py migrate --database authentication
    ```
    ```bash
    python .\manage.py migrate --database session
    ```

* Run server
    ```bash
    python manage.py runserver 0.0.0.0:80
    ```
    > Note: 0.0.0.0 is public host to any network. 80 is the port of server
