# khuda_recsys_hm


H&M 소비 데이터 기반 추천 시스템



## 📑 프로젝트 소개
전세계 5000여개 이상의 매장을 보유하고 있는 대표적인 spa 브랜드 H&M에서 제공하는 소비 데이터를 통해 고객에게 옷을 추천해주는 시스템을 만들고자 한다. 
의류 추천 시스템을 개발하는 것은 고객 맞춤 최적화를 통해 고객 만족도를 높일 뿐만 아니라 소비 트렌드를 알 수 있는 척도이기도 하다. 또한 재고 확보를 최적화할 수 있다는 장점이 있다.

kaggle에서 제공하는 데이터를 통해서 판매 경향성을 알아보고, 사용자 기반 협업 필터링, 아이템 기반 협업 필터링, ALS 모델을 활용한 방식으로 고객에게 의류를 추천해주느 시스템을 구현하고자 한다. 




## 👏 팀 소개 

도유정
<br>서지은  https://github.com/zal-eun
<br>
최보경  https://github.com/B0gyeong



## 🔎 핵심 기능 구현
### 1. EDA
#### article.csv
해당 데이터를 통해 제품의 종류,색상,무늬 등을 알 수 있음

![image](https://github.com/zal-eun/khuda_recsys_hm/assets/122002700/0e50a9ad-1ffb-479c-a1ec-1e04c683daf1)
<br><br>
![image](https://github.com/zal-eun/khuda_recsys_hm/assets/122002700/d6495f60-4636-41b9-9573-97081c6a08df)
<br><br>
![image](https://github.com/zal-eun/khuda_recsys_hm/assets/122002700/7b0396b1-0281-4120-a3bb-e909e8fd4392)
<br><br>
![image](https://github.com/zal-eun/khuda_recsys_hm/assets/122002700/daab2519-ca96-44d9-af26-be1c29c76af1)
<br><br>
#### customer.csv
<br><br>
![image](https://github.com/zal-eun/khuda_recsys_hm/assets/122002700/eb4c80fc-0893-4037-9648-7a8b450bd569)
<br><br>
![image](https://github.com/zal-eun/khuda_recsys_hm/assets/122002700/22c6eb20-d833-40d3-991d-7de13a876d3e)
<br><br>
## 2. modeling
### 사용자 기반 협업 필터링
- 고객 데이터 중 패션관심이 평균보다 높은 소비자들의 구매 데이터 이용

- 구매자 id를 기준으로 구매했으면 1, 아니면 0값을 가지는 pivot table 생성
- cos 유사도를 이용해 각 사용자간 유사도를 계산해 표 생성

- 추천해줄 사용자에 대한 타 사용자의 유사도와 transactions 데이터를 곱해준 후 제품별로 다 더해줌

- 더한 값이 가장 큰 제품 상위 3개를 추천


![image](https://github.com/zal-eun/khuda_recsys_hm/assets/122002700/fb338f65-2836-4346-9a3e-31f10b49011f)

![image](https://github.com/zal-eun/khuda_recsys_hm/assets/122002700/28d94607-2f95-40a0-b863-cfc8b29a0466)


### 아이템 기반 협업 필터링


- transactions 데이터 "article_id" 
열의 값들을 세어서 가장 많이 등장한 
상위 1500개의 값들을 추출

- transactions의 customer_id와 
- 	article_id을 사용하여 pivot_table을 만듦
 아이템을 기준으로 행간 유사도 측정
	cosine_similarity 사용

- 유사도 순서를 나열하여 
아이템 추천


![image](https://github.com/zal-eun/khuda_recsys_hm/assets/122002700/f8d63c50-2dfa-483d-8a05-c9ff0b71f33a)

![image](https://github.com/zal-eun/khuda_recsys_hm/assets/122002700/7bcf1fd9-11f2-433b-a55d-4612b1e44aab)


### ALS 모델 활용한 MF 기법

- pyspark에서 지원하는 ALS 모델
- 사용자 행렬과 제품 행렬을 각각 그룹화하고 모든 블록의 벡터값을 복사하여 활용하는 기존 방식과 차별화
- 해당 특징이 유사한 경우에만 기능 벡터 값을 황용함(일부 값을 차단시켜 데이터 집합에 대한 공동의 필터링 진행)
  <br>
![image](https://github.com/zal-eun/khuda_recsys_hm/assets/122002700/160324ba-02f4-4f2c-8bc9-9e5b26cdeb68)
![image](https://github.com/zal-eun/khuda_recsys_hm/assets/122002700/f731e0fb-23a0-4f87-88dd-88f331644aed)



## 📄 Reference

- [데이터](https://github.com/khuda-3rd](https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations)https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations)
- [코드](https://www.kaggle.com/code/hanifansari93/starter-als-using-pyspark/notebook)
