from src.app.presentation.__main__ import create_app


def run_dev(
        host: str = None,
        port: int = None
) -> None:
    """
    Runs a Flask dev server
    """
    host = "localhost" if host is None else host
    port = 5000 if port is None else port

    app = create_app()
    app.run(host=host, port=port)


if __name__ == "__main__":
    run_dev()
