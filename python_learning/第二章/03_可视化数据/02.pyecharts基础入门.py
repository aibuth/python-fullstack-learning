from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 创建折线图对象
line = Line()

# 给折线图添加x轴数据
line.add_xaxis(["美国", "日本", "印度"])

# 给折线图添加y轴数据
line.add_yaxis("GDP展示", [30, 20, 10])

# 设置全局配置项（修正拼写错误）
line.set_global_opts(
    title_opts=TitleOpts("GDP展示", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),  # 这里是 toolbox，不是 toobox
    visualmap_opts=VisualMapOpts(is_show=True)
)

# 生成图表
line.render()
print("✅ 图表生成成功！打开项目根目录的 render.html 查看")