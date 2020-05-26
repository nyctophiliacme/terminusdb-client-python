# idParser.py


class IDParser:
    def __init__(self):
        pass

    def _valid_url(self, input):
        if input is not None:
            if (input[:7] == "http://") or (input[:8] == "https://"):
                return True
        return False

    def _valid_id_string(self, input, _=None):
        if type(input) != str:
            return False
        if (":" in input) or (" " in input) or ("/" in input):
            return False
        return True

    def parse_server_url(self, url):
        if not self._valid_url(url):
            return False
        if url[-1] != "/":
            url += "/"
        return url

    def parse_dbid(self, dbid):
        if self._valid_id_string(dbid, "db"):
            return dbid
        return False

    def parse_account(self, account):
        if self._valid_id_string(account, "account"):
            return account
        return False

    def parse_branch(self, bid):
        if self._valid_id_string(bid, "branch"):
            return bid
        return False

    def parse_jwt(self, jwt):
        return jwt

    def parse_key(self, key):
        return key
