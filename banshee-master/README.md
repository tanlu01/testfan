# Banshee

Banshee 是一个BDD形式的，主要用于接口自动化的测试框架。

## Features

1. 自然语言关键字编排自动化，功能测试用例即是自动化用例
2. 串联接口组成业务场景自动化
3. 支持grpc接口
4. 支持webdriver测试UI层
5. (根据业务场景/业务流量对接口进行容量测试)
6. 语言支持：Feature层Gherkin语法/自然语言，Step层支持Python,Java,Ruby,JS,C#

## Usage

    conda create -y --name banshee python==3.7
    conda install --file requirements_conda.txt
    conda activate banshee
OR

    virtualenv banshee && cd banshee
    source bin/activate
    pip install -r requirements_pip3.txt

然后运行测试

    gauge run specs

OR

    gauge run -t root001

功能测试报告

    reports/html-report/index.html

压测报告

    reports/load-testing

生产测试用例

    gauge docs spectacle specs
    docs/html/index.html

### Troubleshooting

---
peewee导出语句:

    python -m pwiz -e mysql -H mysql_host -p 3306 -u username -P database_name > database_name.py
