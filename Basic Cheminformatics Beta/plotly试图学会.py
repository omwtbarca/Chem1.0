#尝试未果



import pandas as pd
import numpy as np
import plotly.express as px  # 或 import plotly.express as px
import matplotlib.pyplot as plt

# 柱状图     指定选取国家：Switzerland
gapminder =px.data.gapminder()
gapminder.head()
Switzerland  = gapminder[gapminder["country"] == "Switzerland"]
Switzerland   # 数据显示如下
print("Switzerland",Switzerland)  # 数据显示如下
fig=px.bar(Switzerland,  # 上面指定的数据
       x="year",  # 横坐标
       y="pop",  # 纵坐标
       color="pop")  # 颜色取值
fig.show()
#散点图
#先选取绘图需要的数据：

# 写法1
# gapminder_2002 = gapminder.query("year==2002")

# 写法2
gapminder_2002 = gapminder[gapminder["year"] == 2002]
gapminder_2002
fig=px.scatter(gapminder_2002,   # 传入的数据集
           x="gdpPercap",  # 横坐标是人均GDP
           y="lifeExp",  # 纵坐标是平均寿命
           color="continent"  # 颜色取值：根据洲的值来取
          )
fig.show()
#冒泡散点图
fig=px.scatter(gapminder_2002,x="gdpPercap",y="lifeExp",color="continent",size="pop",size_max=60)
fig.show()
'''鸢尾花数据集
著名的鸢尾花数据集，包含字段：

萼片长sepal_length
萼片宽sepal_width
花瓣长petal_length
花瓣宽petal_width
花的种类species
种类所属编号species_id'''
iris=px.data.iris()
iris.head()
print("iris",iris)  # 数据显示如下
#散点矩阵图
fig=px.scatter_matrix(iris,dimensions=["sepal_width","sepal_length","petal_width","petal_length"],color="species")  # 颜色取值
fig.show()


import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
fig.show()

import pandas as pd
import numpy as np
import plotly.express as px  # 或 import plotly.express as px
# 柱状图     指定选取国家：Switzerland

'''鸢尾花数据集
著名的鸢尾花数据集，包含字段：

萼片长sepal_length
萼片宽sepal_width
花瓣长petal_length
花瓣宽petal_width
花的种类species
种类所属编号species_id'''
iris=px.data.iris()
iris.head()
print("iris",iris)  # 数据显示如下
#散点矩阵图
fig=px.scatter_matrix(iris,  # 传入绘图数据
                  dimensions=["sepal_width","sepal_length","petal_width","petal_length"],  # 维度设置
                  color="species")  # 颜色取值
fig.show()