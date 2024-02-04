from sqlalchemy import create_engine, Column, Integer, String

from sqlalchemy.orm import sessionmaker, declarative_base
from config import Config

# 替换"your_username", "your_password", "your_host", "your_port", "your_database"为你的MySQL数据库信息
# 例如："mysql+pymysql://username:password@host:port/database"
database_url = Config.SQLALCHEMY_DATABASE_URI

engine = create_engine(database_url)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

user = None


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(60), nullable=False)


def calculate_bmi():
    global user
    if not user:
        print("请先登录")
        print("是否立即登录？(y/n)")
        choice = input()
        if choice == 'y':
            login()
        else:
            main()
    # 添加计算BMI的逻辑
    height = float(input("请输入身高（米）: "))
    weight = float(input("请输入体重（千克）: "))

    bmi = weight / ((height / 100) ** 2)
    print(f"你的BMI是: {bmi}")
    print("是否返回(y/n)")
    choice = input()
    if choice == 'y':
        main()
    else:
        calculate_bmi()


def login():
    global user
    # 添加登录逻辑
    username = input("请输入用户名: ")
    password = input("请输入密码: ")

    user = session.query(User).filter_by(username=username).first()

    if user and user.password == password:

        print("登录成功!")
        print(f"欢迎回来，{username},是否立即计算BMI？(y/n)")
        choice = input()
        if choice == 'y':
            calculate_bmi()
        else:
            main()
    else:
        print("登录失败，用户名或密码不正确.输入1进行返回")
        choice = input()
        if choice == '1':
            main()
        else:
            print("无效的选择\n")
            login()


def register():
    # 添加注册逻辑
    username = input("请输入用户名: ")
    password = input("请输入密码: ")

    user = User(username=username, password=password)
    session.add(user)
    session.commit()
    print("注册成功!")
    choice = input("是否立即登录？(y/n)")
    if choice == 'y':
        login()
    elif choice == 'n':
        # 用户选择不登录，直接返回
        main()


def main():
    # 用户选择功能
    choice = input("请选择功能：\n1. 计算BMI\n2. 登录\n3. 注册\n")
    if choice == '1':
        calculate_bmi()
    elif choice == '2':
        login()
    elif choice == '3':
        register()
    else:
        print("无效的选择")
        main()


try:
    main()
except Exception as e:
    print(f"An error occurred: {e}")
    session.rollback()

finally:
    session.close()
