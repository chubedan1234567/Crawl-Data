from bs4 import BeautifulSoup
import requests
import re

url = 'https://mobilecity.vn/dien-thoai'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# click vào xem thêm 
# for i in range(1, 5):
#     url = 'https://mobilecity.vn/dien-thoai?p=' + str(i)

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
list_thong_tin_chi_tiet = []
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
    # get thong tin chi tiet
    thong_tin_chi_tiet = soup.find('div', class_='product-info-content').text
    list_thong_tin_chi_tiet.append(thong_tin_chi_tiet)

# print(list_name)
# print(list_price)
# print(list_tinh_trang)
# print(list_thong_tin_chi_tiet)

# xóa ký \n trong list_thong_tin_chi_tiet
list_thong_tin_chi_tiet_1 = []
for i in list_thong_tin_chi_tiet:
    i = i.replace('\n', '')
    list_thong_tin_chi_tiet_1.append(i)
print(list_thong_tin_chi_tiet_1)

# # tạo dataframe
# import pandas as pd
# df = pd.DataFrame({'Tên sản phẩm': list_name,
#                      'Giá sản phẩm': list_price,
#                         'Tình trạng': list_tinh_trang,
#                         'Thông tin chi tiết': list_thong_tin_chi_tiet_1})
# print(df)

# # lưu file excel
# df.to_excel('mobilecity.xlsx', index=False)
    





    