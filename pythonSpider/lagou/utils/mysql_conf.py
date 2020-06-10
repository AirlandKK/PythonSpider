from pymysql import *


class pysql(object):
    """
    docstring for pysql
    代码的高内聚低耦合：
    - 内聚：是从功能角度来度量模块内的联系，一个好的内聚模块应当恰好做一件事，
    它描述的是模块内的功能联系；
    - 耦合：是软件结构中各模块之间相互连接的一种度量，耦合强弱取决于模块间接口的复杂程度、
    进入或访问一个模块的点以及通过接口的数据。
    """

    def __init__(self):
        # 建立连接
        self.conn = connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='root',
            database='lagou',
            charset='utf8'
        )
        # 获取游标
        self.cursor = self.conn.cursor()

    def execute_sql(self, sql_cmd):
        """执行方法，执行sql"""

        self.cursor.execute(sql_cmd)

    def select_sql(self, sql_cmd):
        """查询"""
        sql = sql_cmd

        self.execute_sql(sql)
        # 返回1个结果fetchone 返回所有个结果集fetchall
        # res = self.cursor.fetchone()
        res = self.cursor.fetchall()
        print('select_sql: ', res)
        return res

    def insert_sql(self, sql_cmd):
        """插入"""
        sql = sql_cmd
        # print(sql)

        self.execute_sql(sql)
        # 提交执行成功的代码
        self.conn.commit()
        print('Done...%s' % sql)

    def update_sql(self, sql_cmd):
        """更新"""
        sql = sql_cmd
        self.execute_sql(sql)
        # 提交执行成功的代码
        self.conn.commit()
        print('Done...%s' % sql)

    def create_sql(self, sql_cmd):
        """创建表"""
        sql = sql_cmd
        self.execute_sql(sql)
        print('Done...%s' % sql)

    def __del__(self):
        # 关闭游标
        self.cursor.close()
        # 关闭连接
        self.conn.close()

# def main():
#     pysql1 = pysql()
#     # pysql1.select_sql()
#     sql_cmd = ''
#     pysql1.insert_sql(sql_cmd)
#     # pysql1.update_sql()
#
#
# if __name__ == '__main__':
#     # main()
#     pass
