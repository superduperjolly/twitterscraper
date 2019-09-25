"""
Module to store some configuration for the Twitter scraper.
"""
import os


CONSUMER_KEY = os.getenv("CONSUMER_KEY", "XBxOau9zslm4SPufu2k1fBIhc")
CONSUMER_SECRET = os.getenv(
    "CONSUMER_SECRET", "uCpf8Hw25QWuCnXgy46pGwaKFxmacuW2kPuftqUXM4hPVy3p3K"
)
ACCESS_TOKEN = os.getenv(
    "ACCESS_TOKEN", "598146812-xKl8cwyH6QivL6UnRiPWbhb0gWNr3gWHM8iLlNF3"
)
ACCESS_TOKEN_SECRET = os.getenv(
    "ACCESS_TOKEN_SECRET", "0jrSuHO5PV9CNjrdw9q3QE7IVCsogofBKWOCGuQEkn2Vm"
)
