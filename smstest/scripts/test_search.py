import os,sys
sys.path.append(os.getcwd())
import pytest

from page.search_page import SearchPage

from base.init_driver import get_driver
# from page.sms_page import SmsPage
from base.read_yaml import read_yaml_data
import page

#读取sms_send.yaml的数据
def get_data():
    data =  read_yaml_data("search.yaml")
    #{'send_data':['1','2','3']}
    return  data.get("send_data")

class TestSearch:

    def setup_class(self):
        #1.初始化driver
        self.driver = get_driver(page.setting_app_package,page.setting_app_activity)
        #2.初始化searchpage类
        self.searchpage = SearchPage(self.driver)
    def teardown_class(self):
        # 1 退出driver
        self.driver.quit()

    def test_click_search_btn(self):
        self.searchpage.click_search_btn()

    # @pytest.mark.parametrize("content", ['aaa', 'bbb', 'ccc'])
    @pytest.mark.parametrize("content",get_data())
    def test_input_search_edit(self,content):
        #1.实现发送内容
        self.searchpage.input_search_edit(content)






