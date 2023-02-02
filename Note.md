## pandas中的for循环使用
### 1.直接使用for循环df
```
df = pd.DataFrame({'age': [24, 42], 'state': ['NY', 'CA'], 'point': [64, 92]},
index=['Alice', 'Bob'])
```
```
for i in df:
    print(i)
    print(type(i))

# <class 'str'>
# age
# <class 'str'>
# state
# <class 'str'>
# point
```
- 直接循环df，得到的是df的列名。
- 实际上是调用了pandas内部的__iter__()方法
- 直接调用并没有多大的意义，所以想要循环df，得用pandas内部的方法

### 2. 逐列检索 DataFrame.iteritems()
```
for column_name, item in df.iteritems():
    print(type(item))
    print(item)
# <class 'pandas.core.series.Series'>
# Alice    24
# Bob      42
# <class 'pandas.core.series.Series'>
# Alice    NY
# Bob      CA
```
- 逐列索引相当于将每一列单独提取出来
- 每一列还是series类型，符合series的特性
- 返回值有两个，一个是列名，一个是列数据

### 3. 逐行索引 DataFrame.iterrows()
- DataFrame.iterrows()
```
for index_name, rows for df.iterrows():
    print(type(rows))
    print(rows)
    
# <class 'pandas.core.series.Series'>
# age      24
# state    NY
# point    64
```
- 1. 逐行索引相当于把每一行的数据拿出来
- 2. 每一行也是series，符合series的特征
- 3. 返回值有两个，一个是行名字，一个一行数据


- DataFrame.itertuples()
```
for row in df.itertuples():
    print(type(row))
    print(row)
    
# <class 'pandas.core.frame.Pandas'>
# Pandas(Index='Alice', age=24, state='NY', point=64)
```
- itertuples()方法只有一个返回值，就是返回每一行的数据
- 每一行的数据仍然符合dataframe的特性

## pandas中处理文本类数据
- ### 1. 简单的字符串类型处理
    - 字符串拆分
      ```
      data_movie["country"] = data_movie["country"].apply(lambda x: x.split(" "))
      ```
      - 拆分之后会转化为列表，如果在split（）中加上expend=Ture，则会拆分为几列，需要提前设置空列供他使用
    - 字符串去空格
      ```
      data_movie["country"] = data_movie["country"].apply(lambda x: x.strip())
      ```
    - 字符串的替换
      ```
      data_movie["country"] = data_movie["country"].apply(lambda x: x.replace("/", ""))
      ```
    - 字符串大小写转换
- ### 2. 简单的列表类型处理
- ### 3. 使用正则表达式处理需要的字符串
    ```
    data_movie["runtime"] = data_movie["runtime"].apply(lambda x: int(re.search(r'\d+', (x[0])).group()))
    ```
    - re.search(正则表达式, data).group() 只显示结果