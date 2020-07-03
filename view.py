from pyecharts.charts import Line,Bar
import pandas as pd
import pyecharts.options as opts

data=pd.read_csv('./data/stock/000001.SZ_平安银行_银行.csv')

data['trade_date']= data['trade_date'].astype('str')
data['trade_date']=pd.to_datetime(data['trade_date'])
(
    Line()
    .set_global_opts(
        tooltip_opts=opts.TooltipOpts(is_show=False),
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
    .add_xaxis(xaxis_data=data['trade_date'])
    .add_yaxis(
        series_name='收盘价',
        y_axis=data['close'],
        symbol="emptyCircle",
        is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .render("./view/平安银行.html")
)