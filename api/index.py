# -*- coding: UTF-8 -*-
import requests
import re
from http.server import BaseHTTPRequestHandler
import json

def list_split(items, n):
    return [items[i:i + n] for i in range(0, len(items), n)]

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 2024-03-15 规范接口的传参方式 https://github.com/Zfour/python_github_calendar_api/issues/20#issuecomment-1999115747
        # path = self.path
        # spl=path.split('?')[1:]
        # for kv in spl:
        #     key,user=kv.split("=")
        #     if key=="user": break
        # 把getdata(user)改为自己的用户名写死就好了
        data = 'icewolf-li'
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return
