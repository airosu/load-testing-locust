from locust import TaskSet, task




class VisitorBehavior(TaskSet):
    @task(98)
    def visit_main_page(self):
        self.client.get('/')
    
    @task(2)
    def land_on_404(self):
        self.client.get('/404')



class SearchingUserBehavior(TaskSet):
    @task(3)
    def just_visiting(self):
        self.client.get('/')
    
    @task(27)
    def access_video_search(self):
        self.client.get('/videohp')
    
    @task(60)
    def access_image_search(self):
        self.client.get('/imghp')




