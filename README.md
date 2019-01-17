### 请使用BDD开发流程，选择上述[“测试开发语言”](### 测试开发语言)，实现多元分段函数:
1. 函数的输入: 两个浮点数: x和y,
2. 函数的值: 当x和y满足下面条件时函数值为true：x位于4和6之间(不包含边界)、并且y位于3和7之间(不包含边界)；否则，函数值为false
> 选择cucumber＋java的组合进行开发与测试， 相关依赖请查看pom.xml
> 测试用例请查看<src/test/resources/cucumberTest/MultivarFunc.feature>
> step定义请查看<src/test/java/com/cucumber/MyStepdefs.java>
> 被测源码请查看<src/main/java/com/cucumber/action/MultivarFunc.java>
> 相关测试结果请查看<Test Results - Feature__MultivarFunc.html>

### 请使用BDD开发流程，选择上述[“测试开发语言”](### 测试开发语言)，熟悉的RESTful API框架，通过RESTful API提供以下服务:
1. 用户执行加法运算
2. 用户可以查询自己运算的次数和结果的总和，为了简单起见，系统用IP地址作为用户账户的ID
### 在上一题的技术框架的基础上，实现三个整数的加法和减法的任意组合。用户的输入中，只允许使用0-9、+/-及空格。
> 选择python作为开发语言，karate测试框架, 相关依赖请查看pom.xml和requiment.txt
> 测试用例设计思路是连接验证，计算验证，无效输入验证以及数据库查询验证（计算前和计算后）
> 测试用例请查看<src/test/resources/cucumberTest/CalculatorAPI.feature>
> 被测源码请查看<src/main/resources/StartRestfulService.py>
> 相关测试结果请查看<Test Results - Feature__CalculatorAPI.html>
