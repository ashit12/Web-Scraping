import requests
from requests import get
from bs4 import BeautifulSoup
names = ['Name']
urls = ['URL']
prices = ['Price']
avg_ratings = ['Average rating']
authors = ['Author']
num_ratings = ['Number of ratings']
url = 'https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_1?ie=UTF8&pg='
for l in range(0, 5):
    response = get(url + str(l+1))
    html_soup = BeautifulSoup(response.text, 'html.parser')
    book_containers = html_soup.find_all('div', class_='zg_itemWrapper')
    for book in book_containers:

        name = ((book.find(
            'div', class_='p13n-sc-truncate p13n-sc-line-clamp-1').text).encode('utf-8')).strip()
        names.append(name)

        author = book.find('a', class_='a-size-small a-link-child')
        if author is not None:
            author = ((book.find(
                'a', class_='a-size-small a-link-child').get_text()).encode('utf-8')).strip()
        else:
            author = "Not available"
        authors.append(author)

        price = book.find('span', class_='p13n-sc-price')
        if price is not None:
            price = (
                (book.find('span', class_='p13n-sc-price').get_text()).encode('utf-8')).strip()
            prices.append(price)
        else:
            price = "Not available"
            prices.append(price)

        num_rating = book.find('a', class_='a-size-small a-link-normal')
        if num_rating is not None:
            num_rating = (
                (book.find('a', class_='a-size-small a-link-normal').text).encode('utf-8')).strip()
        else:
            num_rating = "Not available"
        num_ratings.append(num_rating)

        avg_rating = book.find('span', class_='a-icon-alt')
        if avg_rating is not None and "Prime":
            avg_rating = (
                (book.find('span', class_='a-icon-alt').text).encode('utf-8')).strip()
        else:
            avg_rating = "Not available"
        avg_ratings.append(avg_rating)

        lol = book.find_next('a', class_='a-link-normal')
        if lol is not None:
            urls.append(((lol.get('href')).encode('utf-8')).strip())
        else:
            urls.append("Not available")

file = open("in_book.csv", "w")
length = len(names)
for i in range(0, length):
    file.write(names[i]+";"+urls[i]+";"+authors[i]+";" +
               prices[i]+";"+num_ratings[i]+";"+avg_ratings[i])
    file.write("\n")
file.close()
