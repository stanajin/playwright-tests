import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Project configuration settings."""
    BASE_URL = os.getenv("BASE_URL", "https://google.com")
    TIMEOUT = int(os.getenv("TIMEOUT", 10000))
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
    
    # Credentials (Example)
    USERNAME = os.getenv("USERNAME", "guest")
    PASSWORD = os.getenv("PASSWORD", "password123")
