# pyhton data scrapper
# scrappes data from an HTML website and saves it in CSV file

# pip install requests-html (install it to get requests_html running)

# from requests_html import HTMLSession  # HTML sessoins are used to make request

# s = HTMLSession()

# url = 'https://themes.woocommerce.com/storefront/product-category/clothing/page/3'

# r = s.get(url)

# # print(r.status_code)  # if 200 then good other wise 300 means page redirect and 400 means server doesn't exists

# # print(r.text)  # to check all the html of a page

# # print(r.html.find('ul.products')) # find always return list so ull find square brackets with the recquired element

# # print(r.html.find('ul.products', first=True)) # this will show us the first element

# # we need list not main produxts so we call all lists
# # now this will show us all of the lists in product UL
# # print(r.html.find('ul.products li'))

# products = r.html.find('ul.products li')

# for item in products:
#     # print(item) # show all iems in a loop
#     # print(item.find('a'))  # will show all a tags in a list
#     # print(item.find('a').attrs('href'))  # this will give an error which is [AttributeError: 'list' object has no attribute 'attrs']
#     # print(item.find('a', first=True).attrs['href'])  # will show all href/links

# know create a functoin to call all pages meas whole website in a loop not one by one
# so
import csv
from requests_html import HTMLSession  # HTML sessoins are used to make request

s = HTMLSession()


def get_product_links(page_num):
    url = f'https://themes.woocommerce.com/storefront/product-category/clothing/page/{page_num}'
    r = s.get(url)
    links = []  # empty list to get all the links
    products = r.html.find('ul.products li')
    for item in products:
        # links will be appended in links list
        links.append(item.find('a', first=True).attrs['href'])
    return (links)


# # page1 = get_product_links(1) # we can see any page links from here
# # print(page1)

# test_link = 'https://themes.woocommerce.com/storefront/product/ninja-silhouette-2/'

# r = s.get(test_link)
# # this will return the heading tag
# # print(r.html.find('h1.product_title.entry-title', first=True).text)
# # print(r.html.find('h1.product_title.entry-title', first=True).text).strip() # we use strip to strip off white space or can use replace to replace sapce with no space
# title = r.html.find('h1.product_title.entry-title', first=True).text
# price = r.html.find('p.price', first=True).text
# # print(price)
# sku = r.html.find('span.sku_wrapper', first=True).text
# # print(sku)
# category = r.html.find('span.posted_in', first=True).text
# print(category)

# now we can call this in function
# so

def parse_product(url):
    r = s.get(url)
    title = r.html.find('h1.product_title.entry-title',
                        first=True).text.strip()
    price = r.html.find('p.price', first=True).text.strip().replace('\n', ' ')
    cat = r.html.find('span.posted_in', first=True).text.strip()
    try:
        sku = r.html.find('span.sku_wrapper', first=True).text.strip()
    except AttributeError as err:
        sku = 'None'
        # print(err)
    product = {
        'title': title,
        'price': price,
        'cat': cat,
        'sku': sku,
    }
    return product

# print(parse_product('https://themes.woocommerce.com/storefront/product/ninja-silhouette-2/'))

# now we have got the result from all pages now we will save teh results in csv file as it is core python so we jsut import csv


def save_csv(results):
    keys = results[0].keys()
    with open('products.csv', 'w') as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(results)


def main():
    results = []
    for x in range(1, 6):
        print("Getting page: ", x)
        urls = get_product_links(x)
        for url in urls:
            results.append(parse_product(url))
        print('Total results: ', len(results))
        save_csv(results)
    # print('Showimg results: \n', results)


if __name__ == '__main__':
    main()
