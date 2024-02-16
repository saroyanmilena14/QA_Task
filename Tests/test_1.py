import pytest
from APIs.fast_apis import FAST
from test_data import TestData
from dataclasses import dataclass

@dataclass
class Task:
    user_id: str
    content: str
    is_done: bool
    created_time: int
    task_id: str
    ttl: int

obj=FAST()

def test_create_task():
    errors=[]
    create_task=obj.create_task(TestData.user_id, TestData.content, TestData.task_id, is_done=0)
    #Verify that the staus code is 200
    assert create_task.status_code==200
    data=create_task.json()
    assert "task" in data
    task_data = data.get("task")
    assert task_data is not None
    task = Task(**task_data)
    assert isinstance(task.user_id, str)
    assert isinstance(task.content, str)
    assert isinstance(task.is_done, bool)
    assert isinstance(task.created_time, int)
    assert isinstance(task.task_id, str)
    assert isinstance(task.ttl, int)

def test_update_task():
    errors=[]
    #create task for updating
    create=obj.create_task(TestData.user_id, TestData.content, TestData.task_id, is_done=0)
    #getting task_id from response to update that task 
    data=create.json()
    task_id_from_response = data.get('task', {}).get('task_id')
    update_task=obj.update_task(TestData.user_id_update, TestData.content_update, task_id_from_response, is_done=0)
    #Verify that the staus code is 200
    assert update_task.status_code==200
    #Verify that the response body is correct
    data2=update_task.json()
    updated_taskid=data2.get('updated_task_id')
    assert updated_taskid==task_id_from_response


def test_get_by_id():
    create=obj.create_task(TestData.user_id, TestData.content, TestData.task_id, is_done=0)
    data=create.json()
    task_id_from_response = data.get('task', {}).get('task_id')
    get_by_id=obj.get_task_by_id(task_id_from_response)
    #Verify that the staus code is 200
    assert get_by_id.status_code == 200
    #Verify that the response body is correct
    data=get_by_id.json()
    assert data is not None
    task = Task(**data)
    assert isinstance(task.user_id, str)
    assert isinstance(task.content, str)
    assert isinstance(task.is_done, bool)
    assert isinstance(task.created_time, int)
    assert isinstance(task.task_id, str)
    assert isinstance(task.ttl, int)

@pytest.mark.parametrize("content", [TestData.content1,TestData.content2])
@pytest.mark.parametrize("task_id", [TestData.task_id1,TestData.task_id2,])
@pytest.mark.parametrize("user_id", [TestData.user_id,TestData.user_id,])
def test_create_task(content,user_id,task_id,is_done=0):
    errors = []
    create_mutiple = obj.create_task(content,user_id,task_id,is_done)
    #Verify that the staus code is 200
    assert create_mutiple.status_code == 200
    #Verify that the response body is correct
    data=create_mutiple.json()
    assert "task" in data
    task_data = data.get("task")
    assert task_data is not None
    task = Task(**task_data)
    assert isinstance(task.user_id, str)
    assert isinstance(task.content, str)
    assert isinstance(task.is_done, bool)
    assert isinstance(task.created_time, int)
    assert isinstance(task.task_id, str)
    assert isinstance(task.ttl, int)

def test_list_tasks():
    create1=obj.create_task(TestData.user_id, TestData.content, TestData.task_id, is_done=0)
    data=create1.json()
    user_id_from_response = data.get('task', {}).get('user_id')
    print(user_id_from_response)
    list_taskss=obj.list_tasks(user_id_from_response)
    #Verify that the staus code is 200
    assert list_taskss.status_code == 200

@pytest.mark.parametrize("user_id", [TestData.user_id,TestData.user_id_update])
def test_delete_tasks(user_id):
    list_tasks_response = obj.list_tasks(user_id)
    #Verify that the staus code is 200
    assert list_tasks_response.status_code == 200
    response_data = list_tasks_response.json()
    assert "tasks" in response_data
    tasks_list = response_data.get("tasks")
    for task in tasks_list:
        task_id = task.get("task_id")
        delete_tasks_response = obj.delete_tasks(task_id)
        assert delete_tasks_response.status_code == 200

   