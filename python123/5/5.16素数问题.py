
def question_judge(question):
    """接收一个字符串为参数，根据参数值判断问题类型，调用合适的函数进行操作。"""
    if question == '素数':       # 如果输入”素数“，再输入一个正整数n，输出不大于n的所有素数
        n = int(input())
        output_prime(n)         # 输出素数
    elif question == '回文素数':
        n = int(input())
        palindromic_prime(n)   # 输出回文素数
    elif question == '反素数':
        n = int(input())
        reverse_prime(n)  # 输出反素数
    elif question == '哥德巴赫猜想':
        n = int(input())
        goldbach_conjecture(n)
    else:
        print('输入错误')



def is_prime(n):
    """判断素数的函数,接收一个正整数为参数，参数是素数时返回True，否则返回False
    一个整数若可以进行因数分解，那么分解时得到的两个数一定是一个小于等于sqrt(n)，一个大于等于sqrt(n)，
    所以对于每个数n，并不需要从2判断到n-1，只需要遍历到sqrt(n)即可。因为若sqrt(n)左侧找不到因数，
    那么右侧也一定找不到因数,这样可以显著提升算法的效率。减小判定区间，减少循环次数，提升效率"""

    if n<=1:
        return False
    if n<=3:
        return True
    if n%2==0 or n%3==0:
        return False
    for i in range(5, int(n**0.5)+1, 6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True



def output_prime(number):
    """接收一个正整数为参数，遍历从0到number之间的所有整数
    在一行中输出不大于number的所有素数，函数无返回值"""
    for i in range(2, number + 1):
        if is_prime(i):
            print(i, end=' ')



def palindromic(num):
    """接收一个数字为参数，判定其是否为回文数，返回布尔值。"""
    return str(num) == str(num)[::-1]


def palindromic_prime(number):
    """接收一个正整数参数number，遍历从0到number之间的所有整数，
    若某个数是素数，且转为字符串后是回文字符串，则称其为回文素数
    找出并在同一行中从小到大输出小于number的所有回文素数，各数字间用一个空格分隔，
    函数无返回值"""
    for i in range(2, number + 1):
        if is_prime(i) and palindromic(i):
            print(i, end=' ')



def reverse_num(num):
    """接收一个整数，返回其逆序字符串对应的整数"""
    return int(str(num)[::-1])


def reverse_prime(number):
    """接收一个正整数参数，找出并在同一行内输出所有小于number的反素数，数字间用一个空格分隔。
    反素数指某数i及其逆序数都是素数，但数i对应的字符串不是回文字符串
    函数无返回值"""
    for i in range(2, number + 1):
        if is_prime(i) and is_prime(reverse_num(i)) and not palindromic(i):
            print(i, end=' ')



def goldbach_conjecture(num):
    """ 哥德巴赫猜想, 接收一个不小于4的正整数为参数。
    当参数为不小于4的偶数时，将其分解为两个素数的加和，按小数+数的格式输出。
    有多种组合时全部输出，但不输出重复的组合，例如输出8=3+5，不输出8=5+3。
    参数为奇数或小于4时，输出'Data error!'
    """
    if num<4 and num%2!=0:
        print('Data error!')
        return
    pairs=set()
    for i in range(2, num//2+1):
        if is_prime(i) and is_prime(num-i):
            pair=(i,num-i)
            if pair not in pairs:
                pairs.add(pair)
                print(f"{num}={i}+{num-i}")






if __name__ == '__main__':
    problems = input()
    question_judge(problems)