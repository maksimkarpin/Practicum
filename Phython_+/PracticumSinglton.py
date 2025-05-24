from abc import abstractmethod
import asyncio
import numpy as np
import pandas as pd
import requests
from io import BytesIO
import datetime
import concurrent.futures


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

    def start(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=30) as pool:
            pool.map(self.export_bathc, np.array_split(range(0, 100_000), 1000))



    def export_bathc(self, categories):
        asyncio.set_event_loop(asyncio.new_event_loop())
        return asyncio.get_event_loop().run_until_complete(asyncio.gather(*[
            asyncio.ensure_future(self.export_data(category))
            for category in categories
        ]))

    async def export_data(self, category):
        for skip in range(0, 99_999, 100):
            if self.download(category, skip) == False: break

        return None

    def download(self, skip, category):
        url = self.url + f"?skip={skip}&price_min=0&price_max=1060225&up_vy_min=0&up_vy_max=108682515&up_vy_pr_min=0&up_vy_pr_max=2900&sum_min=1000&sum_max=82432725&feedbacks_min=0&feedbacks_max=32767&trend=false&sort=sum_sale&sort_dir=-1&id_cat={category}"
        response = requests.get(url)
        df = pd.read_excel(BytesIO(response.content), engine='openpyxl')
        #if df.empty: return False # с этой строчкой не начинает считывать.
        df['category_id'], df['download_date'] = category, datetime.datetime.now()
        #print( requests.get(url), response.content)
        print(df)



if __name__ == '__main__':
    loader = Loader()
    #skip = 100
    #categories = np.array_split(range(100, 120), 10)
    """df_result = asyncio.get_event_loop() \
        .run_until_complete(
        asyncio.gather(*list(map(lambda x: asyncio.ensure_future(loader.download(skip, categories)), categories)))
    )
    print(df_result)"""
    loader.start()
    # Программа работает, но не понимаю: цикл, либо бесконечный, либо там очень много данных.


