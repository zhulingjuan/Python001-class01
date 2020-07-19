import pandas as pd
import numpy as np



   
# 1. SELECT * FROM data;
group = ['x','y','z','x','y','z','x','y','z','x','y','z','x','y','z']
data1 = pd.DataFrame(group)
#print(data1)

 
#2. SELECT * FROM data LIMIT 10;
data2 = data1.iloc[0:10]
#print(data2)
 
#3. SELECT id FROM data;  //id 是 data 表的特定一列
df2 = pd.DataFrame([
                     [1, 30], 
                     [1, 30], 
                     [2, 80], 
                     [2, 100], 
                     [10, 120]
                    ])
df2.columns= ['id', 'age']
#print(df2['id'])

 
#4. SELECT COUNT(id) FROM data;
#print(df2['id'].count())

 
#5. SELECT * FROM data WHERE id<1000 AND age>30;
#print(df2[(df2['id'] < 1000) & (df2['age'] > 30)])

 
#6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
df2.columns= ['id', 'order_id']
#subDf = df2.groupby('id').nunique('order_id')

#print(subDf)
 
#7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
df3 = pd.DataFrame([
                     [1, 30], 
                     [4, 30], 
                     [2, 80], 
                     [3, 100], 
                     [10, 120]
                    ])
df3.columns= ['id', 'haha']
data7 = pd.merge(df3, df2, on='id', how='inner')
print(data7)

 
#8. SELECT * FROM table1 UNION SELECT * FROM table2;
data8 = pd.concat([df3, df2])
#print(data8)

 
#9. DELETE FROM table1 WHERE id=10;
data3 = df2.drop(df2[(df2['id'] == 10)].index)
#print(data3)

 
#10. ALTER TABLE table1 DROP COLUMN column_name;
data4 = df2.drop(axis = 1, columns= 'order_id')
#print(data4)