from app import start_socketio_server
import os
from dotenv import load_dotenv
load_dotenv()  # This loads the variables from .env

if __name__ == "__main__":
    # cds_helper_ddx.run({"transcript": "hello world"}, callbacks=None)
    print("[main] Running server thread")
    start_socketio_server()
