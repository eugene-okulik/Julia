from locust import task, HttpUser
import random

class ObjectUser(HttpUser):

    @task(1)
    def get_all_objects(self):
        self.client.get(
            url='/object',
            headers={'Content-Type': 'application/json'}
        )

    @task(3)
    def get_one_object(self):
        self.client.get(
            url=f'/object/{random.choice([2258, 2260, 2262, 4564])}',
            headers={'Content-Type': 'application/json'}
        )
