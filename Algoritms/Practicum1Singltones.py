from abc import abstractmethod
import requests
class Method:
    url = 'https://analitika.woysa.club/images/panel/json/download/niches.php'
    def __init__(self,skip, category):
        self.skip = skip
        self.category = category
    @abstractmethod
    def download(self, skip, category):
        ...


class Loader(Method):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.obj = range(0, 10_000_000_000)
            cls.instance = super(Loader, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        ...

    def download(self, skip, category):
        url = self.url + f"?skip = {skip}&price_min=0&price_max=1060225&up_vy_min=0&up_vy_max=108682515&up_vy_pr_min=0&up_vy_pr_max=2900&sum_min=1000&sum_max=82432725&feedbacks_min=0&feedbacks_max=32767&trend=false&sort=sum_sale&sort_dir=-1&id_cat={category}"
        response = requests.get(url)
        return requests.get(url), response.content


if __name__ == '__main__':
    loader = Loader()
    print(loader.download(100, 1000))

