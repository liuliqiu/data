from urllib import parse
import json

import requests

url = "http://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData"


def get_data(code):
    params = {"symbol": code, "scale": 240, "ma": "no", "datalen": 3000}
    resp = requests.get(url, params)
    with open(f"data/{code}.json", "w") as f:
        f.write(json.dumps(resp.json()))


get_data("sz000001")
