# Usage: locust -f locustfile.py --headless --users 10 --spawn-rate 1 -H http://localhost:8000
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task(1)
    def healthcheck(self):
        self.client.get("/healthcheck")
