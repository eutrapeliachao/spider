# coding=utf-8
import re
from retrying import retry
import requests


class Neihan:

    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}
        self.start_url = "http://neihanshequ.com/"
        self.pattern = re.compile(r"<a target=\"_blank\" class=\"image share_url\" href=\"(.*?)\".*?<p>(.*?)</p>", re.S)

    @retry(stop_max_attempt_number=3)
    def _parse_url(self, url):
        response = requests.get(url, headers=self.headers, timeout=5)
        assert response.status_code == 200
        return response.content.decode()

    def get_content_list(self, html_rul):
        content_list = self.pattern.findall(html_rul)
        return content_list

    def parse_url(self, url):
        try:
            html_str = self._parse_url(url)
        except Exception as e:
            print(e)
            html_str = None
        return html_str

    def save_content_list(self, content_list):
        with open("neihan.txt", "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(content[0])
                f.write("\n")
                f.write(content[1])
                f.write("\n")

    def run(self):
        html_str = self.parse_url(self.start_url)
        content_list = self.get_content_list(html_str)
        self.save_content_list(content_list)

if __name__ == '__main__':
    neihan = Neihan()
    neihan.run()
