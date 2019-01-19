###多元分段函数
1. 右键MultivarFunc.feature添加新run configuration， Glue为MyStepdefs.java的位置即com.cucumber
2. 然后点击Run执行测试用例

###Restfult API
1. 连接本地MySQL，在MySQL控制台执行以下命令
source <createTable.sql的路径>
2. 启动restful服务：在IDEA里运行文件StartRestfulService.py
3. 执行测试文件：需安装cucumber for java插件在IDEA中， 右键CalculatorAPI.feature添加新run configuration，Glue需指定为com.intuit.karate，然后Run