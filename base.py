import json
import requests


class BaseFile(object):


    def send_request(self, url, method, body=None, headers=None, files=None, token=None):
        if body:
            body = json.dumps(body) 
        if not headers:
            headers = {}
        headers['Content-Type'] = 'application/json'

        if token:
            headers['Authorization'] = f'Bearer {token}'

        match method:
            case "GET":
                return self.send_get_request(url, body, headers, files)
            case "POST":
                return self.send_post_request(url, body, headers, files)
            case "PUT":
                return self.send_put_request(url, body, headers, files)
            case "DELETE":
                return self.send_delete_request(url, body, headers, files)
            
    def send_get_request(self, url, body,  headers, files):
        response = requests.get(url=url, data=body, headers=headers, files=files)
        return response
    
    def send_post_request(self, url, body, headers, files):
        response = requests.post(url=url, data=body, headers=headers, files=files)
        return response
    
    def send_put_request(self, url, body, headers, files):
        response = requests.put(url=url, data=body, headers=headers, files=files)
        return response
    
    def send_delete_request(self, url, body, headers, files):
        response = requests.delete(url=url, data=body, headers=headers, files=files)
        return response




