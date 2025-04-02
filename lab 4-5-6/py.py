from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Рандомная задержка между запросами

    @task
    def load_test(self):
        self.client.get("/")  # Тестируемый URL