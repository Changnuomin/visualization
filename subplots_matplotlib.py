x = ['1.12', '1.13', '1.14', '1.15', '1.16', '1.17', '1.18']
y1 = list(range(1,8))
y2 = list(range(8,15))
y3 = list(range(15,22))

# subplots的结构是1*3，一行三列
# figsize, 是每个子图的大小（高，宽）
fig, axs = plt.subplots(1, 3, figsize=(12,5))

# label 是legend
axs[0].plot(x, y1, label='y1')

# 子图的title
axs[0].set_title("titile_1")

# ticks 的设置，x轴，旋转45度
axs[0].tick_params(axis='x', labelrotation=45)
# 显示子图的legend
axs[0].legend()

axs[1].plot(x, y2, label='y1')
axs[1].set_title("title_2")
axs[1].tick_params(axis='x', labelrotation=45)
axs[1].legend()

axs[2].plot(x, y3,label='y2')
axs[2].set_title("title_3")
axs[2].tick_params(axis='x', labelrotation=45)
axs[2].legend()

# 0图和1图 share y轴
axs[0].sharey(axs[1])
axs[1].sharey(axs[2])


# plt.show()
fig.tight_layout()
plt.savefig('plt.png',dpi=300)