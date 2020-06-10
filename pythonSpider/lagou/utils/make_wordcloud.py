from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy as np
import jieba
import matplotlib.pyplot as plt
import sqlite3
"""stopwords """

def get_wordcloud(word=None, in_image_name=None, out_image_name=None):
    # 获取文本信息，复制到' '内或者读取文本文件均可
    # if word:
    #     word = word
    # else:
    #     word = 'words that you would like to show, you can copy it here or read a file.不会因为虚度年华而悔恨。'
    # text_list = jieba.cut(word, cut_all=True)
    # text = ' '.join(text_list)
    text = word
    print('1.生成jieba分词完成...')
    # 获取词云轮廓形状图
    if in_image_name:
        shape_image = np.array(Image.open(in_image_name))
    else:
        shape_image = np.array(Image.open('1.jpg'))
    print('2.读取输入图片完成...')
    # shape_image = np.array(Image.open('C:\\Users\\Administrator\\Desktop\\1.jpeg'))

    # 设置生成词云的颜色，如去掉这两行则字体为默认颜色
    image_color = ImageColorGenerator(shape_image)
    # 生成词云图，此处默认为随机染色，当文本数量较少（看处理效果）时，将repeat设置为True
    word_cloud = WordCloud(background_color='white', font_path='simhei.ttf', repeat=True,
                           mask=shape_image, min_font_size=1)
    word_cloud.generate(text)
    word_cloud.recolor(color_func=image_color)
    print('3.生成图片中...')

    # 保存图像
    if out_image_name:
        word_cloud.to_file('../static/images/{}.png'.format(out_image_name))
        print('4.保存图片成功，可以打开 {} 进行查看'.format(out_image_name+'.png'))
    else:
        word_cloud.to_file('../static/images/wordcloud.png')
        print('4.保存图片成功,可以打开进行查看--> {}'.format('wordcloud.png'))

    # 显示图像
    print('5.展示成果...')
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


def get_skill():
    db = '../db.sqlite3'
    table = 'pyjobs_pythonjob'
    conn = sqlite3.connect(db)
    c = conn.cursor()
    sql = 'select skillLables from pyjobs_pythonjob'
    data = c.execute(sql)
    words = ''
    for i in data:
        words += ' '.join(i)
        # print(i)
    # print(words)
        # break
    get_wordcloud(words, in_image_name='1.jpg', out_image_name='skill_wordcloud')

def get_city():
    db = '../db.sqlite3'
    table = 'pyjobs_pythonjob'
    conn = sqlite3.connect(db)
    c = conn.cursor()
    sql = 'select address from pyjobs_pythonjob'
    data = c.execute(sql)
    words = ''
    for i in data:
        words += ' %s' %i

        # print(i)
    # print(words)
        # break
    get_wordcloud(words, in_image_name='2.png', out_image_name='city_wordcloud')


if __name__ == '__main__':
    # pass
    get_skill()
    # get_city()