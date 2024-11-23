def number_to_chinese():
    chinese_numbers=['零','一','二','三','四','五','六','七','八','九']
    user_input=input().strip()
    if  user_input== "h":
            print("输入错误，请重新输入")
    else:
        try:
            num=int(user_input)

            print(chinese_numbers[num])

        except IndexError:
            print('输入超出范围')
        except ValueError:
            print('输入类型错误，请输入整数')
        except Exception:
            print("输入错误，请重新输入")

if __name__=='__main__':

    number_to_chinese()