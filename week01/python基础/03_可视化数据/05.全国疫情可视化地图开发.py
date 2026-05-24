"""
演示全国疫情可视化地图开发
"""
import json
from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

# 读取数据文件
with open("D:/疫情.txt", "r", encoding="utf-8") as f:
    data = f.read()

data_dict = json.loads(data)

# 从字典中取出省份的数据
province_data_list = data_dict['areaTree'][0]['children']

# 组装每个省份和确诊人数为元组
data_list = []
for province_data in province_data_list:
    province_name = province_data['name']
    province_confirm = province_data['total']['confirm']

    # ---------------------- 核心修改：把简单补省字，升级为完整名称映射 ----------------------
    # 完整的名称映射表，覆盖所有省份、直辖市、自治区、特别行政区
    name_mapping = {
        "北京": "北京市", "天津": "天津市", "上海": "上海市", "重庆": "重庆市",
        "河北": "河北省", "山西": "山西省", "辽宁": "辽宁省", "吉林": "吉林省",
        "黑龙江": "黑龙江省", "江苏": "江苏省", "浙江": "浙江省", "安徽": "安徽省",
        "福建": "福建省", "江西": "江西省", "山东": "山东省", "河南": "河南省",
        "湖北": "湖北省", "湖南": "湖南省", "广东": "广东省", "海南": "海南省",
        "四川": "四川省", "贵州": "贵州省", "云南": "云南省", "陕西": "陕西省",
        "甘肃": "甘肃省", "青海": "青海省", "台湾": "台湾省",
        "内蒙古": "内蒙古自治区", "广西": "广西壮族自治区", "西藏": "西藏自治区",
        "宁夏": "宁夏回族自治区", "新疆": "新疆维吾尔自治区",
        "香港": "香港特别行政区", "澳门": "澳门特别行政区"
    }

    # 如果在映射表里，就用地图标准名；不在的话，保持原样
    if province_name in name_mapping:
        province_name = name_mapping[province_name]
    # ----------------------------------------------------------------------------------------

    data_list.append((province_name, province_confirm))

# 创建地图对象
map = Map()

# 添加数据
map.add("各省份疫情人数", data_list, "china")

# 设置全局配置（加上视觉映射组件，让地图有颜色渐变，更好看）
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图", pos_left="center"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,  # 分段显示
        pieces=[
            {"min": 1, "max": 99, "label": "1-99人", "color": "#FFFFCC"},
            {"min": 100, "max": 999, "label": "100-999人", "color": "#FFCC99"},
            {"min": 1000, "max": 9999, "label": "1000-9999人", "color": "#FF9966"},
            {"min": 10000, "max": 99999, "label": "10000-99999人", "color": "#CC3333"},
            {"min": 100000, "label": "100000人以上", "color": "#990033"}
        ]
    )
)

# 生成地图
map.render("全国疫情地图.html")
print("✅ 地图生成成功！请打开【全国疫情地图.html】查看，现在每个省份都能正常显示人数了！")