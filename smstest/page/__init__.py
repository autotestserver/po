# 快速复制  ctrl + d   删除 ctrl + y
from selenium.webdriver.common.by import By

#启动应用的包名和启动名
setting_app_package = "com.android.settings"
setting_app_activity = ".Settings"

search_btn = By.ID,'com.android.settings:id/search'
search_edit = By.ID,'android:id/search_src_text'