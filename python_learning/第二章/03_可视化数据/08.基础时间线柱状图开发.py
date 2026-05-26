from pyecharts.charts import Bar,Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

bar1 = Bar()
bar1.add_xaxis(["中国","美国","英国"])
bar1.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right"))
# 反转X轴和Y轴
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国","美国","英国"])
bar2.add_yaxis("GDP",[50,35,20],label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国","美国","英国"])
bar3.add_yaxis("GDP",[80,60,35],label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

# 创建时间线并设置主题
timeline = Timeline(
    {"theme": ThemeType.LIGHT}
)

timeline.add(bar1,"1")
timeline.add(bar2,"2")
timeline.add(bar3,"3")

# 自动播放设置
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

timeline.render("基础时间柱状图.html")