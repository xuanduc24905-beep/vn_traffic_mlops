"""Cấu hình chung: đọc từ biến môi trường, hoặc từ file .env khi chạy trên WSL."""
import os

from dotenv import load_dotenv

load_dotenv()  # biến đã đặt sẵn (ví dụ trong Docker) được ưu tiên hơn giá trị trong .env

MINIO_ENDPOINT = os.environ["MINIO_ENDPOINT"]
MINIO_ACCESS_KEY = os.environ["MINIO_ACCESS_KEY"]
MINIO_SECRET_KEY = os.environ["MINIO_SECRET_KEY"]
MINIO_BUCKET = os.getenv("MINIO_BUCKET", "vn-traffic")
MLFLOW_TRACKING_URI = os.environ["MLFLOW_TRACKING_URI"]
EXPERIMENT_PREFIX = os.getenv("MLFLOW_EXPERIMENT_PREFIX", "vn-traffic")
