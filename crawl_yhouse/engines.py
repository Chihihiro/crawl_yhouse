from sqlalchemy import create_engine
import socket

hostname = socket.gethostname()

def get_engine(hostname):

    if hostname in ('wx09', 'wx01', 'wx02', 'wx03', 'wx04', 'wx05', 'wx06', 'wx07', 'wx08'):
        engine = create_engine(
            "mysql+pymysql://{}:{}@{}:{}/{}".format('yhouse', 'GHLs9X8q@QWkjo6#ZX4f', '10.10.209.30', 3306,
                                                    'test', ), connect_args={"charset": "utf8"}, echo=True, )
    else:
        # engine = create_engine(
        #     "mysql+pymysql://{}:{}@{}:{}/{}".format('spider_dev', 'csQXEMw9udrC4f*4JB6WnGiv2MKZRn', 'localhost', 13306,
        #                                             'test', ), connect_args={"charset": "utf8"}, echo=True, )
        engine = create_engine(
            "mysql+pymysql://{}:{}@{}:{}/{}".format('yhouse', 'GHLs9X8q@QWkjo6#ZX4f', 'localhost', 10002,
                                                    'test', ), connect_args={"charset": "utf8"}, echo=True, )
    return engine


choise_engine = get_engine(hostname)


