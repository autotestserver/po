import os,sys
sys.path.append(os.getcwd())

from base.base_action import BaseAction
import page
class SearchPage(BaseAction):
    #初始化方法
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    # 点击搜索按钮
    def click_search_btn(self):
        self.click_element(page.search_btn)

    #2向接收着输入框里面输入内容
    def input_search_edit(self,content):
        self.input_edit_content(page.search_edit,content)



