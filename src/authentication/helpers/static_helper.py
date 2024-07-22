class StaticHelper:
    def __init__(self) -> None:
        pass

    def get_avtar_url(self, key: str) -> str:
        return f'http://localhost/static/{key}'
