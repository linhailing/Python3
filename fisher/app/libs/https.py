# https requests
import requests


class HTTPS:

    @staticmethod
    def get(url,return_json=True):
        """
        requests get
        :param return_json:
        :return:
        """
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text()

