import requests

class PatentSearcher:
    def __init__(self, api_key, api_secret):
        self.base_url = "https://api.patsnap.com" # 示例地址
        self.token = self._get_token(api_key, api_secret)

    def _get_token(self, k, s):
        # 实现 OAuth2 鉴权逻辑获取 Access Token
        pass

    def execute_search(self, keywords, ipc_codes):
        # 构建检索表达式：(TTL:(关键词) OR AB:(关键词)) AND IPC:(分类号)
        query = f"TTL:({keywords}) AND IPC:({ipc_codes}) AND LS:(有效 OR 审中)"
        
        endpoint = f"{self.base_url}/v1/patent/search"
        params = {
            "q": query,
            "fields": "pn,title,abstract,claims,ipc",
            "size": 20 # 先取前20条近似度最高的
        }
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(endpoint, params=params, headers=headers)
        return response.json().get("data", [])