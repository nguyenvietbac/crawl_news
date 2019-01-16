#! /usr/bin/python

import smtplib
import os
import json
#######################################
# file_data = []
# #############################################
# file_temp = []
# if os.stat("dantri.json").st_size != 0 :
# 	with open('dantri.json', encoding="utf-8") as f:
# 		file_dantri = json.load(f)
# tab = []
# for x in range(len(file_dantri)):
# 	if file_dantri[x]["tab"] not in tab:
# 		tab.append(file_dantri[x]["tab"])
# print(tab)


# a = [
# {"source": "vneconomy.vn", "description": ["&lt;a href=&quot;http://vneconomy.vn/gia-vang-mieng-giam-them-gia-usd-tu-do-tang-20190116111213802.htm&quot;&gt;&lt;img src=&quot;https://vneconomy.mediacdn.vn/zoom/80_50/2019/1/16/1-1547611865136264559935-crop-15476118712321162896236.jpg&quot; /&gt;&lt;/a&gt;Tuy nhi&#234;n, gi&#225; v&#224;ng thế giới vẫn đang được hỗ trợ bởi những bất ổn to&#224;n cầu"], "tab": "tai chinh", "title": ["Gi&#225; v&#224;ng miếng giảm th&#234;m, gi&#225; USD tự do tăng"], "date": ["Wed, 16 Jan 2019 11:31:00 GMT+7"], "link": ["http://vneconomy.vn/gia-vang-mieng-giam-them-gia-usd-tu-do-tang-20190116111213802.htm"]},
# {"source": "vneconomy.vn", "description": ["&lt;a href=&quot;http://vneconomy.vn/ty-le-no-cong-cua-viet-nam-ngay-cang-giam-manh-20190115132753951.htm&quot;&gt;&lt;img src=&quot;https://vneconomy.mediacdn.vn/zoom/80_50/2019/1/15/no-cong-15475335485351277149275-crop-1547533557631605710634.jpg&quot; /&gt;&lt;/a&gt;Tỷ lệ nợ c&#244;ng giảm từ mức cuối năm 2016 l&#224; 63,7% GDP xuống c&#242;n 61,4% GDP cuối năm 2017"], "tab": "tai chinh", "title": ["Tỷ lệ nợ c&#244;ng của Việt Nam ng&#224;y c&#224;ng giảm mạnh"], "date": ["Tue, 15 Jan 2019 23:14:00 GMT+7"], "link": ["http://vneconomy.vn/ty-le-no-cong-cua-viet-nam-ngay-cang-giam-manh-20190115132753951.htm"]},
# {"source": "vneconomy.vn", "description": ["&lt;a href=&quot;http://vneconomy.vn/gia-vang-mieng-sjc-giam-nhe-dang-re-hon-vang-9999-2019011510291746.htm&quot;&gt;&lt;img src=&quot;https://vneconomy.mediacdn.vn/zoom/80_50/2019/1/15/1-1547522929514104305086-crop-15475229343841271589651.jpg&quot; /&gt;&lt;/a&gt;Gi&#225; USD tự do giảm th&#234;m, trong khi gi&#225; USD ng&#226;n h&#224;ng đi ngang"], "tab": "tai chinh", "title": ["Gi&#225; v&#224;ng miếng SJC giảm nhẹ, đang rẻ hơn v&#224;ng 999,9"], "date": ["Tue, 15 Jan 2019 11:13:00 GMT+7"], "link": ["http://vneconomy.vn/gia-vang-mieng-sjc-giam-nhe-dang-re-hon-vang-9999-2019011510291746.htm"]},
# {"source": "vneconomy.vn", "description": ["&lt;a href=&quot;http://vneconomy.vn/sau-dong-tac-that-ngan-hang-nha-nuoc-don-dap-mua-rong-ngoai-te-20190115090326309.htm&quot;&gt;&lt;img src=&quot;https://vneconomy.mediacdn.vn/zoom/80_50/2019/1/15/0-1547517711041998362458-crop-1547517738584200357139.jpg&quot; /&gt;&lt;/a&gt;Lượng mua r&#242;ng đến đầu tuần n&#224;y đ&#227; khoảng 1,3 tỷ USD, l&#227;i suất li&#234;n ng&#226;n h&#224;ng giảm mạnh"], "tab": "tai chinh", "title": ["Sau động t&#225;c thật, Ng&#226;n h&#224;ng Nh&#224; nước dồn dập mua r&#242;ng ngoại tệ"], "date": ["Tue, 15 Jan 2019 09:31:00 GMT+7"], "link": ["http://vneconomy.vn/sau-dong-tac-that-ngan-hang-nha-nuoc-don-dap-mua-rong-ngoai-te-20190115090326309.htm"]},
# {"source": "vneconomy.vn", "description": ["&lt;a href=&quot;http://vneconomy.vn/thong-doc-ngan-hang-can-co-trach-nhiem-truoc-tin-dung-den-20190114205714865.htm&quot;&gt;&lt;img src=&quot;https://vneconomy.mediacdn.vn/zoom/80_50/2019/1/14/0-15474741653391752820026-crop-1547474178575916014033.jpg&quot; /&gt;&lt;/a&gt;Thống đốc Ng&#226;n h&#224;ng Nh&#224; nước n&#243;i về hướng giải ph&#225;p tham gia xử l&#253; t&#236;nh trạng t&#237;n dụng đen hiện nay"], "tab": "tai chinh", "title": ["Thống đốc: “Ng&#226;n h&#224;ng cần c&#243; tr&#225;ch nhiệm trước t&#237;n dụng đen”"], "date": ["Mon, 14 Jan 2019 21:16:00 GMT+7"], "link": ["http://vneconomy.vn/thong-doc-ngan-hang-can-co-trach-nhiem-truoc-tin-dung-den-20190114205714865.htm"]},
# {"source": "vneconomy.vn", "description": ["&lt;a href=&quot;http://vneconomy.vn/loi-nhuan-cua-ngan-hang-quan-doi-duoc-du-bao-vuot-7000-ty-dong-20190114120612903.htm&quot;&gt;&lt;img src=&quot;https://vneconomy.mediacdn.vn/zoom/80_50/2019/1/14/anh-21-15474420332541457233698-crop-15474420438891417856215.jpg&quot; /&gt;&lt;/a&gt;Kết th&#250;c năm 2018, MB đạt mức lợi nhuận trước thuế lũy kế tr&#234;n 7.000 tỷ VND, tăng 31% so với c&#249;ng kỳ, vượt 8% so với kế hoạch"], "tab": "tai chinh", "title": ["Lợi nhuận của Ng&#226;n h&#224;ng Qu&#226;n đội được dự b&#225;o vượt 7.000 tỷ đồng"], "date": ["Mon, 14 Jan 2019 12:10:00 GMT+7"], "link": ["http://vneconomy.vn/loi-nhuan-cua-ngan-hang-quan-doi-duoc-du-bao-vuot-7000-ty-dong-20190114120612903.htm"]},
# {"source": "vneconomy.vn", "description": ["&lt;a href=&quot;http://vneconomy.vn/vang-mieng-tang-gia-nhe-usd-tu-do-giam-manh-20190114115615778.htm&quot;&gt;&lt;img src=&quot;https://vneconomy.mediacdn.vn/zoom/80_50/2019/1/14/1-1547441732801549804957-crop-15474417377321704582374.jpg&quot; /&gt;&lt;/a&gt;C&#225;c sản phẩm v&#224;ng 999,9 đang giữ xu hướng tăng nhanh, thậm ch&#237; đ&#227; vượt gi&#225; v&#224;ng miếng SJC ở chiều b&#225;n ra"], "tab": "tai chinh", "title": ["V&#224;ng miếng tăng gi&#225; nhẹ, USD tự do giảm mạnh"], "date": ["Mon, 14 Jan 2019 11:59:00 GMT+7"], "link": ["http://vneconomy.vn/vang-mieng-tang-gia-nhe-usd-tu-do-giam-manh-20190114115615778.htm"]},
# {"source": "vneconomy.vn", "description": ["&lt;a href=&quot;http://vneconomy.vn/techcombank-mien-phi-moi-giao-dich-truc-tuyen-fst-ebank-cho-doanh-nghiep-20190113205355589.htm&quot;&gt;&lt;img src=&quot;https://vneconomy.mediacdn.vn/zoom/80_50/2019/1/13/hinh-techcombank-154738752368312828122-crop-1547387535692265360806.png&quot; /&gt;&lt;/a&gt;Theo đ&#243;, doanh nghiệp sẽ được ho&#224;n to&#224;n miễn ph&#237; chuyển khoản trong v&#224; ngo&#224;i hệ thống Techcombank khi sử dụng ng&#226;n h&#224;ng điện tử F@st Ebank"], "tab": "tai chinh", "title": ["Techcombank miễn ph&#237; mọi giao dịch trực tuyến F@st Ebank cho doanh nghiệp"], "date": ["Mon, 14 Jan 2019 09:00:00 GMT+7"], "link": ["http://vneconomy.vn/techcombank-mien-phi-moi-giao-dich-truc-tuyen-fst-ebank-cho-doanh-nghiep-20190113205355589.htm"]},
# ]

a = ["1" ,"2", "3" ,"4", "1"]

for x in range(len(a)):
	for y in range(len(a)):
		if x != y and a[x] == a[y]:
			del a[y]





