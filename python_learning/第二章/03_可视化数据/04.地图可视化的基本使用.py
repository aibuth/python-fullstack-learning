from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()

data = [
    ("山西省",9),
    ("陕西省",59),
    ("河北省",109),
    ("河南省",159),
    ("台湾省",209)
]

map.add("测试地图", data, "china")

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces = [
            {"min": 1, "max": 75, "label": "1-9人", "color": "#CCFFFF"},
            {"min": 76, "max": 150, "label": "76-150人", "color": "#FF9966"},
            {"min": 151, "max": 250, "label": "151-250人", "color": "#990033"}
        ]
    )
)

map.render()