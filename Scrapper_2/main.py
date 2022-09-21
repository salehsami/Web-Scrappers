from datetime import datetime
import requests
from bs4 import BeautifulSoup
from pony import orm

db = orm.Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)


class Price(db.Entity):
    name = orm.Required(str)
    price = orm.Required(float)
    date_created = orm.Required(datetime)


# creates the table
db.generate_mapping(create_tables=True)

# web scraping functions


def gear4(session):
    url = "https://www.gear4music.com/Recording-and-Computers/Shure-SM7B-Dynamic-Studio-Microphone/G6X"
    resp = session.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    data = (
        "gear4music",
        float(soup.select_one("span.info-row-price span.c-val").text),
    )
    return data


# def ubuy(session):
#     url = "https://www.ubuy.com.pk/en/product/217KVF8-shure-sm7b-cardioid-dynamic-microphone"
#     resp = session.get(url)
#     soup = BeautifulSoup(resp.text, "html.parser")
#     data = (
#         "ubuy",
#         float(soup.select_one(
#             "div.price-wrapper del.product-old-price ml-2").text))
#     return data


def thomann(session):
    url = "https://www.thomann.de/gb/shure_sm_7b_studiomikro.htm"
    resp = session.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    data = (
        "thomann",
        float(soup.select_one(
            "div.price-wrapper div.price").text.replace("£", "").strip()),
    )
    return data


def main():

    # # set user agent header
    # headers =
    # use a session
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 '
                      'Safari/537.36'})

    data = [
        (gear4(session)),
        # (ubuy(session)),
        (thomann(session)),
    ]
    with orm.db_session:
        for item in data:
            Price(name=item[0], price=item[1], date_created=datetime.now())
        # export_data_to_csv()

    # print(data)


if __name__ == '__main__':
    main()
