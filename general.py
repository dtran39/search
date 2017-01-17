from urllib2 import urlopen
from link_finder2 import LinkFinder

# Set for faster processing, file for saving data
queued_links = set()

# Append to a file
def append_to_file(path, data):
    with open(path, "a") as file:
        file.write(data + '\n')


# Get links from webpage
def get_page_links(base_url, page_url):
    response = urlopen(base_url)
    html_string = ''
    if 'text/html' in dict(response.info())['content-type']:
        html_response = response.read()
        html_string = html_response.decode("utf-8")
    link_finder = LinkFinder(base_url, page_url)
    link_finder.feed(html_string)
    return link_finder.get_page_links()


# Add a set of links to the queue
def add_links_to_list(base_url, page_url):
    open('queue.txt', 'w').close()
    for url in get_page_links(base_url, page_url):
        if url not in queued_links:
            append_to_file('queue.txt', url)
            queued_links.add(url)

links = [
    'https://www.peterbe.com/plog/python-new-style-classes-and-super',
    'http://www.bongda.com.vn/'
]
add_links_to_list(links[0], 'https://thenewboston.com/')
