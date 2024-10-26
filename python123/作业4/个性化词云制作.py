import jieba
import wordcloud
import imageio.v2 as imageio


def random_color(word,font_size,position,orientation,font_path,random_state):
    return f"rgb(255,125,78)"
with open("习近平讲话.txt", "r", encoding="gbk") as f:
    t=f.read()

exwords=['的','和']
for word in exwords:
    t=t.replace(word,'')
ls = jieba.lcut(t)
txt = " ".join(ls)
mask=imageio.imread("img.png")
w = wordcloud.WordCloud(mask=mask,color_func=random_color,
                        font_path=r"C:\Windows\Fonts\msyh.ttc",
                        width = 1000, height = 700, background_color = "white",
                        )
w.generate(txt)
w.to_file("习近平讲话2.png")
