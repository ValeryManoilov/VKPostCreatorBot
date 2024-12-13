import requests
import csv

class Dataset:

    def __init__(self):
        self.api_key = "43e7ef0443e7ef0443e7ef043940c1f96b443e743e7ef0424bfd463f653a46bcdde41b4"

    def get_data_from_wall(self, domain, count_of_posts):
        response = requests.get('https://api.vk.com/method/wall.get',
                                        params={
                                            'access_token': self.api_key,
                                            'v': "5.103",
                                            'domain': domain,
                                            'count': count_of_posts,
                                            'offset': 0
                                        })
        return response.json()
    
    def get_all_data(self):
        domains = ["molodyeiskinfo", "life4e", "ftlyceum", "hacktrip", 
                   "knizhnyi_dvorik_ekb", "pso_pnv", "koteoganezov", "verasergeeva116", 
                   "spottykit"]
        texts = []
        count_posts = 30
        for domain in range(len(domains)):
            for count in range(count_posts):
                texts.append([self.get_data_from_wall(domains[domain], count_posts)["response"]["items"][count]["text"]])
        return texts
    
    def create_dataset(self):
        texts = self.get_all_data()
        with open("dataset.csv", "w", encoding='utf8', newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter="|")
            writer.writerows(texts)

dataset = Dataset()
print(dataset.get_all_data())