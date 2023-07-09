import requests
import time


def get_questions_number(start_date, end_date):
    url = "https://api.stackexchange.com/questions"
    params = {
        "fromdate": start_date,
        "todate": end_date,
        "order": "desc", "sort": "activity",
        "tagged": "Python", "site": "stackoverflow"
    }
    response = requests.get(url, params=params).json()
    print(f"В период с '{time.ctime(start_date)}' по '{time.ctime(end_date)}' на сайте stackoverflow было задано "
          f"{len(response['items'])} вопросов с тегом Python: ")
    for id, topic in enumerate(response['items']):
        print(f"{id + 1}: {topic['title']}")


if __name__ == '__main__':
    two_days_seconds = 172800
    get_questions_number(int(time.time()) - two_days_seconds, int(time.time()))
