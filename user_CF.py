import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

articles = pd.read_csv("C:/Users/youjeong/Downloads/articles.csv/articles.csv")
transactions = pd.read_csv("C:/Users/youjeong/Downloads/transactions_train.csv/transactions_train.csv")

editedArticles = articles[['article_id',"product_type_name","product_group_name","graphical_appearance_name",
    "colour_group_name","perceived_colour_value_name","department_name","index_name",
    "index_group_name","section_name","garment_group_name"]]

transactions.drop(labels = "price", axis =1)

transactions['t_dat'] = pd.to_datetime(transactions['t_dat'])

transactions_2019_10_01 = transactions[transactions['t_dat'].str.startswith('2019')]
transactions_2019_10_01_dupliate = transactions_2019_10_01.duplicated() #중복된 행 true 반환,series
transactions_2019_10_01_dupliate_to_f=transactions_2019_10_01_dupliate.to_frame()

transactions_2019_10_01['is_duplicate'] = transactions_2019_10_01_dupliate_to_f[0]
transactions_2019_10_01

#중복행 제거
transactions_2019_10_01 = transactions_2019_10_01[transactions_2019_10_01.is_duplicate != True]
transactions_2019_10_01['sales_channel_id'] = 1

###pivot만들기

transactions_2019_10_01_pivot = pd.pivot_table(transactions_2019_10_01, index = 'customer_id',columns = 'article_id', values = 'sales_channel_id')

transactions_2019_10_01_pivot = transactions_2019_10_01_pivot.fillna(0)

transactions_2019_10_01_pivot_T = transactions_2019_10_01_pivot.transpose()
transactions_2019_10_01_pivot_T

from sklearn.metrics.pairwise import cosine_similarity

item_sim = cosine_similarity(transactions_2019_10_01_pivot, transactions_2019_10_01_pivot)

# cosine_similarity()값 DataFrame으로 변환

item_sim_df = pd.DataFrame(data=item_sim, index=transactions_2019_10_01_pivot.index,
                          columns=transactions_2019_10_01_pivot.index)

##0006사용자와의 유사도 계산
sim_custom = item_sim_df['0006d1fc72f81261e70e74249ab2c348e21a093ba40f2af6e90f4337a9736af2'].sort_values(ascending=False)[:10]
sim_custom = sim_custom.to_frame()#시리즈
sim_custom

###여러달꺼 랜덤추출하기*************

sim_cus_10 = transactions_2019_10_01_pivot.loc[(sim_custom.index)]

a = sim_cus_10.iloc[[0], :] * sim_custom.iloc[0,0]

for i in range(1,10) :
  b = sim_cus_10.iloc[[i], :] * sim_custom.iloc[i,0]
  a = pd.concat([a,b],axis = 0)

a_sum = a.sum()
a_sum_top3=a_sum.sort_values(ascending=False)[:3].to_frame()

from PIL import Image
img_name = str(a_sum_top3.index[2]) + ".png"
img_name_file = "0"+img_name[:2]
file_name = "C:/Users/youjeong/Downloads/Khuda3차/초기자료/images/" + img_name_file + "/"+"0"+img_name
image = Image.open(file_name)

image.show()