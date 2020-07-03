# StockAnalysis
股票数据爬虫，挖掘建模，历史数据离线分析

## Config
config.conf 
变量配置
参数配置

## scrapy.py数据爬虫
api|说明
--|--
tushare|获取全部股票名称和代码
http://tool.cnfunny.cn/api/stock/list|获取股票历史数据


支持`追加爬取`和`全量爬取`，可设置`日期区间`和`迭代次数`两种组建时间周期方式。


![数据图片](https://github.com/SuiMingYang/StockAnalysis/tree/master/temp/stock.png)

## merge.py 文件合并
爬取的全部数据文件合成一个，便于分组汇总做数据分析。

## xgb.py xgboost拟合涨跌值

## group.py 分组汇总统计

## kmeans.py 聚类分析

## view.py pyecharts展示

## lstm.py 时间序列预测


