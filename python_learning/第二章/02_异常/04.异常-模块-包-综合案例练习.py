import 第二章.my_utils.str_util
from 第二章.my_utils import file_util,str_util
print(str_util.str_reverse("77556613"))
print(str_util.substr("77556613",2,5))

file_util.append_to_file("D:/abc.txt","追加内容")
file_util.print_file_info("D:/abc.txt")

