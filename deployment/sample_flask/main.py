from flask import Flask
import tensorflow as tf
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()


@app.get("/")
def home():
    return "Hello, World!"


@app.get("/check_gpu")
def check_gpu():
    gpu_status = tf.test.is_gpu_available()
    gpus = tf.config.list_physical_devices("GPU")

    return {"gpu_status": gpu_status, "gpus": [gpu.name for gpu in gpus]}


if __name__ == "__main__":
    app.run(port=8888)
