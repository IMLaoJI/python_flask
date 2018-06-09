# -*- coding: utf-8 -*-
'''
SDK for alidayu
requires: python3.x, requests
@author: raptor.zh@gmail.com
'''

import requests
import hashlib
from time import time
import logging

logger = logging.getLogger(__name__)


class RestApi(object):
    def __init__(self, key, secret, url='https://eco.taobao.com/router/rest', partner_id=""):
        self.key = key
        self.secret = secret
        self.url = url
        self.partner_id = partner_id

    def sign(self, params):
        # params可以接收字典和字符串两种方式
        if isinstance(params, dict):
            params = "".join(["%s%s" % (k,v) for k,v in sorted(params.items())])
            params = "".join([self.secret, params, self.secret])
        sign = hashlib.md5(params.encode("utf-8")).hexdigest().upper()
        return sign

    def get_api_params(self):
        params = {}
        try:
            [params.__setitem__(k, getattr(self, k)) for k in self.get_param_names()]
        except AttributeError:
            raise Exception("Some parameters is needed for this api call")
        [params.__setitem__(k, getattr(self, k)) for k in self.get_option_names() if hasattr(self, k)]
        return params

    def getResponse(self, authorize=None):
        sys_params = {
                "method": self.get_api_name(),
                "app_key": self.key,
                "timestamp": str(int(time() * 1000)),
                "format": "json",
                "v": "2.0",
                "partner_id": self.partner_id,
                "sign_method": "md5",
                }
        if authorize is not None:
            sys_params['session'] = authorize
        params = self.get_api_params()
        sign_params = sys_params.copy()
        sign_params.update(params)
        print('='*40)
        print(sign_params)
        print('='*40)
        sys_params['sign'] = self.sign(sign_params)
        headers = {
                 'Content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                 "Cache-Control": "no-cache",
                 "Connection": "Keep-Alive",
        }
        sys_params.update(params)
        r = requests.post(self.url, params=sys_params, headers=headers)
        print('='*30)
        print(r.url)
        print('='*30)
        r.raise_for_status()
        return r.json()


class AlibabaAliqinFcSmsNumSendRequest(RestApi):
    def get_api_name(self):
        return "alibaba.aliqin.fc.sms.num.send"

    def get_param_names(self):
        return ['sms_type', 'sms_free_sign_name', 'rec_num', 'sms_template_code']

    def get_option_names(self):
        return ['extend', 'sms_param']