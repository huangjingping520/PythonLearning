import jieba

from pyecharts import options as opts
from pyecharts.charts import WordCloud

story = '''
实打实打算阿斯顿阿三爱上倒是都i阿松嗲送i的厚爱收到安抚和速度放缓阿斯顿法海速度回复哎u收到饭后阿萨的哈佛i啊u是和覅u送达和覅u阿斯顿哈佛i撒旦和覅说的话弗兰克世界大会风口浪尖撒旦和李开复盛大开放哈桑了艰苦奋斗
'''

words = jieba.lcut(story)
counts = {}
for w in words:
    if len(w) == 1:
        continue
    else:
        counts[w] = counts.get(w, 0) + 1
items = list(counts.items())

words = [(k, v) for (k, v) in items]

(
    WordCloud()
    .add(series_name="MyLove", data_pair=words, word_size_range=[6, 66])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="MyLove", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("MyLove.html")
)