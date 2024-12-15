import logging
import os

from dotenv import load_dotenv
from connectors.binance import BinanceClient
from connectors.bitmex import BitmexClient

load_dotenv()
from interface.root_component import Root

# Load API keys in a single step to avoid repeated calls to os.getenv()
binance_public_key = os.getenv('BINANCE_PUBLIC_KEY')
binance_private_key = os.getenv('BINANCE_PRIVATE_KEY')
bitmex_public_key = os.getenv('BITMEX_PUBLIC_KEY')
bitmex_private_key = os.getenv('BITMEX_PRIVATE_KEY')

# Create and configure the logger object

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':  # Execute the following code only when executing main.py (not when importing it)

    binance = BinanceClient(binance_public_key,
                            binance_private_key,
                            testnet=True, futures=True)
    bitmex = BitmexClient(bitmex_public_key, 
                          bitmex_private_key,
                          testnet=True)

    root = Root(binance, bitmex)
    root.mainloop()


