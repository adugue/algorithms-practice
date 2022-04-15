cache = {"facebook.com": "<html>hello</html>"}

def get_page(url):
    data = cache.get(url)
    if data:
        return data
    else:
        # data = get_data_from_server(url)  # get data that is not cached
        # cache[url] = data  # store retrieved data in cache
        # return data  # return data
        return "no data"
