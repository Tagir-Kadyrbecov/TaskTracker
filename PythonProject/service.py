from data import data_task
import datetime
class Service:
    @staticmethod
    def create_expense(id: int, name: str, description: str, status: str) -> dict:
        localBase = data_task.copy()
        localBase["id"] = id
        localBase["name"] = name
        localBase["description"] = description
        localBase["status"] = status
        localBase["created_at"] = datetime.datetime.now().isoformat()
        localBase["updated_at"] = datetime.datetime.now().isoformat()
        return localBase
