from base import BaseFile
from config import TestData


class FAST(BaseFile):

    def create_task(self, content, user_id, task_id, is_done=0):
        url = f'{TestData.BASE_URL}/create-task'
        method = 'PUT'
        body = {"user_id":user_id,"content": content, "task_id":task_id, "is_done":is_done}
        return self.send_request(url=url, method=method, body=body)
    
    def update_task(self, content, user_id, task_id, is_done=0):
        url = f'{TestData.BASE_URL}/update-task'
        method = 'PUT'
        body = {"user_id":user_id,"content": content, "task_id":task_id, "is_done":is_done}
        return self.send_request(url=url, method=method, body=body)
    
    def get_task_by_id(self, task_id):
        url = f'{TestData.BASE_URL}/get-task/{task_id}'
        method = 'GET'
        return self.send_request(url=url, method=method)
    
    def list_tasks(self, user_id):
        url = f'{TestData.BASE_URL}/list-tasks/{user_id}'
        method = 'GET'
        return self.send_request(url=url, method=method)
    
    def delete_tasks(self, task_id):
        url = f'{TestData.BASE_URL}/delete-task/{task_id}'
        method = 'DELETE'
        return self.send_request(url=url, method=method)