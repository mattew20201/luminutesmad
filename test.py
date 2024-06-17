TOKEN='6579196085:AAHPWo16Q_scDH5m_A4iQlz4O7REfmokMws'
CHAT_ID='7284568121'

import requests
import re

message="something we don't see everyday"

url=f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
requests.get(url)