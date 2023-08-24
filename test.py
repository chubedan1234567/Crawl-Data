# Get all links
links = soup.find_all('p', class_='name')
list_link = []
for link in links:
    url = link.a['href']
    list_link.append(url)
print(list_link)
# truy cập tung link để lấy thông tin
list_name = []
list_price = []
list_tinh_trang = []
list_tinh_trang_tam_thoi = []
for link in links:
    url = link.a['href']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Get name
    name = soup.find('h1', class_='title').text
    list_name.append(name)
    # Get price
    price = soup.find('p', class_='price').text
    list_price.append(price)
    # get tinh trang
    tinh_trang = soup.find('span', class_='status_instook')
    list_tinh_trang_tam_thoi.append(tinh_trang)
    for i in list_tinh_trang_tam_thoi:
        if i == None:
            i = 'Còn hàng'
        else:
            i = 'Hết hàng'
    list_tinh_trang.append(i)

print(list_name)
print(list_price)
print(list_tinh_trang)