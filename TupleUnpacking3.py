# Demonstration of Tuple Unpacking

url = 'https://www.amazon.com.au/War-Art-Steven-Pressfield-ebook/dp/B007A4SDCG'
list_of_items_from_url = url.split('/')
print(list_of_items_from_url)

# Output : ['https:', '', 'www.amazon.com.au', 'War-Art-Steven-Pressfield-ebook', 'dp', 'B007A4SDCG']
list_of_items_from_url = url.split('/')[2:]

domain, asin, *rest = url.split('/')[2:]
print(domain)
print(asin)
print(*rest)
