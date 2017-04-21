import pandas as pd
import csv
import numpy

u_cols=['user_id','age','sex','occupation','zip_codes']
user=pd.read_csv('ml-100k/u.user',sep='|',names=u_cols,encoding='latin-1')
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols,encoding='latin-1')
i_cols = ['movie id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure','Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy','Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
items = pd.read_csv('ml-100k/u.item', sep='|', names=i_cols, encoding='latin-1')
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings_base = pd.read_csv('ml-100k/ua.base', sep='\t', names=r_cols, encoding='latin-1')
ratings_test = pd.read_csv('ml-100k/ua.test', sep='\t', names=r_cols, encoding='latin-1')
a=[]
a=items.head()

#def file_creation(self,name):
arr=items.loc[ (items["Western"]==1), ["movie title","release date"]].values
arr=arr.tolist()
arr1=[]
for i in arr:
	arr1.append([x.encode('UTF8') for x in i])
print arr1[:5]
#arr2=[['abhijeet','1994'],['anand','1997']]

with open("Western.csv", 'wb') as f:
	wr = csv.writer(f)
	wr.writerows(arr1)