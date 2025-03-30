from locust import HttpUser, task, between

class LoadTestUser(HttpUser):
    wait_time = between(1, 3) 

    @task
    def test_endpoint(self):
        self.client.get("/") 

