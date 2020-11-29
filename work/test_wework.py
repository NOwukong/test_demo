import requests


class TestWeWork:
    token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    corpid = ''
    corpsecret = ''
    token = None

    def test_get_token(self):
        r = requests.get(
            self.token_url,
            params={
                "corpid": self.corpid,
                "corpsecret": self.corpsecret
            }
        )
        assert r.text
