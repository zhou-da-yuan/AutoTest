### 框架架构
```
common 封装公共方法
	case_yaml.py 测试用例yaml文件读取模块
	env.py 环境配置文件操作模块
	faker_data.py 模拟数据生成模块
	log.py 日志管理模块
	login.py 公共登录接口
	request.py 接口请求封装模块
	
Test_case 测试用例函数
  conftest.py 测试固件
  test_console.py 测试用例
  test_console_user.py 测试用例
  
casedata 测试用例数据
  case.yaml 测试数据
  case_console_user 测试数据
  
config 配置文件
  env.yaml 环境配置文件
  
allure-report 测试报告生成
allure-report 测试结果生成

logs 日志文件

pytest.ini pytest配置文件

run.py 运行函数

```
