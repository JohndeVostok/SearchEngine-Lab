# 搜索引擎性能评价

计54 马子轩 2015012283 计65 尹思程 2016011354

## 分组信息

马子轩 尹思程

## 构建查询样例集合

| 类型   | 关键词      | 信息需求                     |
| ------ | ----------- | ---------------------------- |
| 导航类 | 携程        | www.ctrip.com                |
| 导航类 | 清华大学    | www.tsinghua.edu.cn          |
| 信息类 | 土屋圭市    | 关于土屋圭市本人的介绍       |
| 信息类 | 英雄联盟    | 关于英雄联盟游戏的资讯与介绍 |
| 信息类 | golang      | 介绍GO语言、教程或技巧       |
| 信息类 | 北京        | 介绍北京城市信息             |
| 信息类 | 拉格朗日    | 介绍Lagrange的经历与工作     |
| 事务类 | 订机票      | 能够订机票的网站             |
| 事务类 | gdb设置断点 | gdb设置断点的方法            |
| 事务类 | word画表格  | 怎么在word里画表格           |

## 构建Pooling

### 携程

#### 百度

| 编号 | 摘要                                                      | 网址                | 标注 |
| ---- | --------------------------------------------------------- | ------------------- | ---- |
| 0    | 携程-酒店、机票、车票、门票、线路低价订……当季特惠!        | www.ctrip.com       | 1    |
| 1    | 携程网订酒店 机票 车票 汽车票 门票有多重豪礼              | www.ctrip.com       | 1    |
| 2    | 携程旅行网官网:酒店预订,机票预订查询,旅游度假,商...       | www.ctrip.com       | 1    |
| 3    | 【携程酒店】酒店预订,酒店价格查询,宾馆住宿推荐,网上订酒店 | hotels.ctrip.com    | 0    |
| 4    | 携程                                                      | vacations.ctrip.com | 0    |
| 5    | 携程旅游攻略,自助游,自驾游,出游,游玩攻略指南【携程攻略】  | you.ctrip.com       | 0    |
| 6    | 携程旅游信息技术(上海)有限公司_企业信息                   | xin.baidu.com       | 0    |
| 7    | 携程_百度百科                                             | baike.baidu.com     | 0    |
| 8    | 携程- DoNews.com                                          | DoNews.com          | 0    |
| 9    | 携程的最新相关信息                                        | www.baidu.com       | 0    |

#### 360好搜

| 编号 | 摘要                                                       | 网址                | 标注 |
| ---- | ---------------------------------------------------------- | ------------------- | ---- |
| 0    | 携程网:专业订机票、酒店、车票、门票、线路，假期出行提早订! | www.ctrip.com       | 1    |
| 1    | 携程(xiecheng)官网只此一家,服务有保障!  官网               | www.ctrip.com       | 1    |
| 2    | 携程旅行网官网:酒店预订,机票预订查询,旅游度假,商旅管理     | www.ctrip.com       | 1    |
| 3    | 携程旅行网官网:酒店预订,机票预订查询,旅游度假,商旅管理     | www.ctrip.com       | 1    |
| 4    | 【携程机票】飞机票查询,机票预订,机票价格查询,打折特价机票  | flights.ctrip.com   | 0    |
| 5    | 携程旅行网_客服电话                                        | pages.ctrip.com     | 0    |
| 6    | 携程_360百科                                               | baike.so.com/doc/   | 0    |
| 7    | 【携程酒店】酒店预订,酒店价格查询,宾馆住宿推荐,网上订酒店  | hotels.ctrip.com    | 0    |
| 8    | 酒店管理系统_酒店管理软件_PMS_酒店收益管理_携程酒店预订_.. | ebooking.ctrip.com  | 0    |
| 9    | 携程[CTRP]美股实时行情_东方财富网                          | quote.eastmoney.com | 1    |

#### 搜狗

| 编号 | 摘要                                                         | 网址                | 标注 |
| ---- | ------------------------------------------------------------ | ------------------- | ---- |
| 0    | 携程网:专业订机票、酒店、车票、门票、线路，假期出行提早订!   | www.ctrip.com       | 1    |
| 1    | 携程网订酒店_机票,车票,汽车票_门票享多重好礼                 | www.ctrip.com       | 1    |
| 2    | 机票预订_网上预订_来携程网!携程低价机票1折起                 | flights.ctrip.com   | 0    |
| 3    | 【携程机票】飞机票查询,机票预订,机票价格查询,打折特价机票    | flights.ctrip.com   | 0    |
| 4    | 携程旅行网[CTRP]_美股实时行情_新浪财经                       | finance.sina.com.cn | 0    |
| 5    | 携程的最新相关信息                                           | news.sogou.com/     | 0    |
| 6    | 携程 - 搜狗百科                                              | baike.sogou.com     | 0    |
| 7    | 【携程酒店】酒店预订,酒店价格查询,宾馆住宿推荐,网上订酒店    | hotels.ctrip.com    | 0    |
| 8    | 携程旅行-酒店预订,机票预订查询,旅游度假,商旅管理-携程无线官网 | m.ctrip.com         | 0    |
| 9    | 旅游团_旅游线路_自驾游_跟团游_自由行_周边游_..._邮轮【携...  | vacations.ctrip.com | 0    |

### 清华大学

#### 百度

| 编号 | 摘要                                     | 网址                      | 标注 |
| ---- | ---------------------------------------- | ------------------------- | ---- |
| 0    | 清华大学                                 | www.tsinghua.edu.cn       | 1    |
| 1    | 清华大学_百度百科                        | baike.baidu.com           | 0    |
| 2    | 清华大学高考分数线_招生信息_中国教育在线 | gkcx.eol.cn               | 0    |
| 3    | 清华大学-医学院                          | www.med.tsinghua.edu.cn   | 0    |
| 4    | 清华大学本科招生网                       | www.join-tsinghua.edu.cn/ | 0    |
| 5    | 清华大学研究生招生网                     | yz.tsinghua.edu.cn/       | 0    |
| 6    | 清华大学的最新相关信息                   | www.baidu.com             | 0    |
| 7    | 清华大学吧_百度贴吧                      | tieba.baidu.com           | 0    |
| 8    | 清华大学 - Tsinghua University           | www.tsinghua.edu.cn       | 1    |
| 9    | 清华大学_百度地图                        | map.baidu.com             | 0    |

#### 360搜索

| 编号 | 摘要                                         | 网址                | 标注 |
| ---- | -------------------------------------------- | ------------------- | ---- |
| 0    | 清华大学                                     | www.tsinghua.edu.cn | 1    |
| 1    | 中国教育在线提供清华大学高考分数线           | gkcx.eol.cn         | 0    |
| 2    | 清华大学                                     | baike.so.com        | 0    |
| 3    | 清华大学_360地图                             | ditu.so.com         | 0    |
| 4    | 清华大学_360图片                             | image.so.com        | 0    |
| 5    | 清华大学- Tsinghua University                | www.tsinghua.edu.cn | 1    |
| 6    | 清华大学的最新相关消息                       | news.so.com         | 0    |
| 7    | 清华大学相关资讯！有些人还不知道，赶快来看！ | sh.qihoo.com        | 0    |
| 8    | 清华大学高考招生——高考志愿填报参考系统       | gkcx.eol.cn         | 0    |
| 9    | 清华大学历任校长_360问答                     | wenda.so.com        | 0    |

#### 搜狗

| 编号 | 摘要                                 | 网址                    | 标注 |
| ---- | ------------------------------------ | ----------------------- | ---- |
| 0    | 清华大学                             | www.tsinghua.edu.cn     | 1    |
| 1    | 清华大学_分数线_阿凡题高考           | gaokao.afanti100.com    | 0    |
| 2    | 清华大学的最新相关信息               | news.sogou.com          | 0    |
| 3    | 清华大学 - 搜狗百科                  | baike.sogou.com         | 0    |
| 4    | 清华大学本科招生网                   | www.tsinghua.edu.cn     | 1    |
| 5    | 清华大学旅游_最佳旅游线路 - 去哪儿网 | dujia.qunar.com         | 0    |
| 6    | 清华大学的最新相关信息               | news.sogou.com          | 0    |
| 7    | 清华大学图书馆                       | www.lib.tsinghua.edu.cn | 0    |
| 8    | 清华大学-医学院                      | www.med.tsinghua.edu.cn | 0    |
| 9    | 清华大学_搜狗图片                    | pic.sogou.com           | 0    |

### 土屋圭市

#### 百度

| 编号 | 摘要                                                         | 网址                    | 标注 |
| ---- | ------------------------------------------------------------ | ----------------------- | ---- |
| 0    | 土屋圭市_百度百科                                            | baike.baidu.com         | 1    |
| 1    | 「图文」漂神土屋圭市 一位漂移王者的养成经历_爱卡汽车         | http://info.xcar.com.cn | 1    |
| 2    | 藤原文太_百度百科                                            | baike.baidu.com         | 0    |
| 3    | 一路尖叫不断 坐土屋圭市的车感受漂移_视频_汽车之家            | v.autohome.com.cn       | 0    |
| 4    | 土屋圭市是谁?藤原拓海原型开AE86单挑GTR,原来电影里是真..._... | www.iqiyi.com           | 1    |
| 5    | 土屋圭市的座驾!这台"战神"R32又将沦为拍卖品!_易车号_易车网    | news.bitauto.com        | 0    |
| 6    | 【图】东京改装展:土屋圭市漂移座驾AE86亮相_汽车之家           | www.autohome.com        | 0    |
| 7    | 在中国被奉为漂移之神的土屋圭市,在日本却是个路人?             | www.sohu.com            | 0    |
| 8    | 话说这人是土屋圭市吗                                         | tieba.baidu.com         | 0    |
| 9    | 约战赛道丨《头文字D》原型土屋圭市驾到!_搜狐汽车_搜狐网       | www.sohu.com            | 1    |

#### 360搜索

| 编号 | 摘要                                                         | 网址                       | 标注 |
| ---- | ------------------------------------------------------------ | -------------------------- | ---- |
| 0    | 土屋圭市_360百科                                             | baike.so.com               | 1    |
| 1    | 土屋圭市的最新相关消息                                       | www.so.com                 | 0    |
| 2    | 土屋圭市（约396个相关视频）高清在线观看_360视频              | video.360kan.com           | 1    |
| 3    | 土屋圭市30年花500万改装AE86,在中国早就给你 黄标 报废了!_搜狐... | www.sohu.com               | 0    |
| 4    | 「图文」漂神土屋圭市一位漂移王者的养成经历_爱卡汽车          | Info.xcar.com.cn           | 1    |
| 5    | 土屋圭市的这段AE86漂移是什么水平? - 步行街主干道- 虎扑社区   | bbs.hupu.com               | 0    |
| 6    | 一路尖叫不断坐土屋圭市的车感受漂移_视频_汽车之家             | v.autohome.com.cn          | 0    |
| 7    | 土屋圭市オフィシャルサイト - K1 PLANNING –                   | http://www.k1planning.com/ | 1    |
| 8    | 土屋圭市_360图片                                             | Image.so.com               | 1    |
| 9    | 为什么土屋圭市要花31 万改装那台丰田AE86?_【快资讯】          | sh.qihoo.com               | 0    |

#### 搜狗

| 编号 | 摘要                                                         | 网址             | 标注 |
| ---- | ------------------------------------------------------------ | ---------------- | ---- |
| 0    | 土屋圭市 - 搜狗百科                                          | baike.sogou.com  | 1    |
| 1    | 土屋圭市在线观看-搜狗视频                                    | v.sogou.com      | 1    |
| 2    | 土屋圭市AE86山路教学演示-汽车-高清正版视频在线观看–爱奇艺    | www.iqiyi.com    | 0    |
| 3    | 土屋圭市_搜狗图片                                            | my.tv.sohu.com   | 1    |
| 4    | 【图】东京改装展：土屋圭市漂移座驾AE86亮相_汽车之家          | www.autohome.com | 0    |
| 5    | 土屋圭市的车技究竟高到什么程度?_知乎                         | www.zhihu.com    | 1    |
| 6    | 土屋圭市 早期成名作 峠开AE86 LEVIN 漂移下山-汽车-高清正版视频在... | www.iqiyi.com    | 1    |
| 7    | 土屋圭市的相关内容_微信                                      | weixin.sogou.com | 0    |
| 8    | 「图文」漂神土屋圭市 一位漂移王者的养成经历_爱卡汽车         | Info.xcar.com    | 1    |
| 9    | 藤原文太 - 搜狗百科                                          | baike.sogou.com  | 0    |

### 英雄联盟

#### 百度

| 编号 | 摘要                                                         | 网址               | 标注 |
| ---- | ------------------------------------------------------------ | ------------------ | ---- |
| 0    | 英雄联盟全新官方网站-腾讯游戏                                | lol.qq.com         | 1    |
| 1    | 英雄联盟LOL_LOL官网合作专区_英雄联盟视频_多玩游戏网          | lol.duowan.com     | 1    |
| 2    | 英雄联盟_百度百科                                            | baike.baidu.com    | 1    |
| 3    | 英雄联盟赛事官网-腾讯游戏                                    | lpl.qq.com         | 1    |
| 4    | 英雄联盟吧_百度贴吧                                          | tieba.baidu.com    | 0    |
| 5    | 英雄联盟的最新相关信息                                       | www.baidu.com      | 0    |
| 6    | 高校教师巧用英雄联盟讲授机械制图                             | www.techweb.com.cn | 0    |
| 7    | 硬核教师!用《英雄联盟》讲机械制图,老师你把你大号..._手机网易网 | 3g.163.com         | 0    |
| 8    | 下载中心-英雄联盟官方网站-腾讯游戏                           | lol.qq.com         | 1    |
| 9    | 领取中心-英雄联盟官方网站-腾讯游戏                           | lol.qq.com         | 1    |

#### 360搜索

| 编号 | 摘要                                                         | 网址             | 标注 |
| ---- | ------------------------------------------------------------ | ---------------- | ---- |
| 0    | 英雄联盟全新官方网站-腾讯游戏                                | lol.qq.com       | 1    |
| 1    | 英雄联盟_客服电话                                            | kf.qq.com        | 0    |
| 2    | 英雄联盟_分集剧情/大结局全集剧情                             | www.tvsou.com    | 0    |
| 3    | 英雄联盟_360百科                                             | baike.so.com     | 1    |
| 4    | 英雄联盟（约469000个相关视频）高清在线观看_360视频           | video.360kan.com | 1    |
| 5    | 英雄联盟的最新相关消息                                       | www.so.com       | 1    |
| 6    | 英雄联盟手游官网_英雄联盟手游下载_英雄联盟手游攻略_小皮手游网 | sj.xiaopi.com    | 0    |
| 7    | 英雄联盟：无极剑圣 在线免费试读-亚马逊Kindle电子书           | www.amazon.cn    | 0    |
| 8    | 英雄联盟相关资讯！这才是你想看的！                           | sh.qihoo.com     | 1    |
| 9    | 下载中心-英雄联盟官方网站-腾讯游戏                           | lol.qq.com       | 1    |

#### 搜狗

| 编号 | 摘要                                                    | 网址             | 标注 |
| ---- | ------------------------------------------------------- | ---------------- | ---- |
| 0    | 英雄联盟全新官方网站-腾讯游戏官网                       | lol.qq.com       | 1    |
| 1    | 英雄联盟（LOL）S9新赛季-游戏合作专区-S9最新天赋出装大全 | iwan.sogou.com   | 1    |
| 2    | 英雄联盟 - 搜狗百科                                     | baike.sogou.com  | 1    |
| 3    | 下载英雄联盟,英雄联盟下载 - 桔梗下载站                  | soft.jiegeng.com | 1    |
| 4    | lol,英雄联盟,lol官网,lol英雄联盟攻略 - 178lol英雄联盟   | lol.178.com      | 1    |
| 5    | 英雄联盟吧-百度贴吧                                     | tieba.baidu.com  | 0    |
| 6    | 英雄联盟的最新相关信息                                  | news.sogou.com   | 1    |
| 7    | 英雄联盟_搜狗图片                                       | pic.sogou.com    | 0    |
| 8    | 英雄联盟客服电话                                        | kf.qq.com        | 0    |
| 9    | 英雄联盟_英雄联盟游戏资料库_腾讯网                      | games.qq.com     | 1    |

### golang

#### 百度

| 编号 | 摘要                                                 | 网址              | 标注 |
| ---- | :--------------------------------------------------- | ----------------- | ---- |
| 0    | 首页- Go语言中文网 - Golang中文社区                  | studygolang.com   | 1    |
| 1    | 首页- Golang中国                                     | www.golangtc.com  | 1    |
| 2    | golang官网 - The Go Programming Language             | golang.google.com | 1    |
| 3    | Go 语言教程\|菜鸟教程                                | www.runoob.com    | 1    |
| 4    | Golang_百度百科                                      | baike.baidu.com   | 1    |
| 5    | 为什么现在 Golang 的工作这么难找? - V2EX             | lax.v2ex.com      | 0    |
| 6    | Golang心得 - Go语言中文网 - Golang中文社区           | studygolang.com   | 1    |
| 7    | Go语言标准库文档中文版\|Go语言中文网\|Golang中文社区 | studygolang.com   | 1    |
| 8    | Golang就业前景_非零无限2019年Golang招聘工资-BOSS直聘 | www.zhipin.com    | 0    |
| 9    | 说说Golang的使用心得 - 011 - 博客园                  | www.cnblogs.com   | 0    |

#### 360搜索

| 编号 | 摘要                                                 | 网址              | 标注 |
| ---- | ---------------------------------------------------- | ----------------- | ---- |
| 0    | [充电节]2019-51CTOgolang培训中心                     | edu.51cto.com     | 0    |
| 1    | 首页- Go语言中文网- Golang中文社区                   | studygolang.com   | 1    |
| 2    | Golang_360百科                                       | baike.so.com      | 1    |
| 3    | 首页- Golang中国                                     | www.golangtc.com  | 1    |
| 4    | Golang心得- Go语言中文网- Golang中文社区             | studygolang.com   | 1    |
| 5    | golang环境搭建- Go语言中文网- Golang中文社区         | studygolang.com   | 1    |
| 6    | The Go Programming Language                          | golang.google.com | 1    |
| 7    | 资源索引- Go语言中文网- Golang中文社区               | studygolang.com   | 1    |
| 8    | Go语言标准库文档中文版\|Go语言中文网\|Golang中文社区 | studygolang.com   | 1    |
| 9    | golang info                                          | golang.info       | 1    |

#### 搜狗

| 编号 | 摘要                                          | 网址             | 标注 |
| ---- | --------------------------------------------- | ---------------- | ---- |
| 0    | Golang                                        | golang.org       | 1    |
| 1    | Golang - 搜狗百科                             | baike.sogou.com  | 1    |
| 2    | Go (programming language) - Wikipedia         | en.wikipedia.org | 1    |
| 3    | golang 最佳实践_热门回答_知乎                 | www.zhihu.com    | 0    |
| 4    | 首页 - Go语言中文网 - Golang中文社区          | studygolang.com  | 1    |
| 5    | Why I Love Golang – Sagi Serge Nadir – Medium | medium.com       | 0    |
| 6    | 首页 - Golang中国                             | www.golangtc.com | 1    |
| 7    | golang的相关内容_微信                         | weixin.sogou.com | 0    |
| 8    | Go 语言教程\|菜鸟教程                         | www.runoob.com   | 1    |
| 9    | Golang Go                                     | golanggo.com     | 1    |

### 北京

#### 百度

| 编号 | 摘要                                                         | 网址                                                | 标注 |
| ---- | ------------------------------------------------------------ | --------------------------------------------------- | ---- |
| 0    | 北京_百度百科                                                | https://baike.baidu.com/item/北京/128981?fr=aladdin | 1    |
| 1    | 北京市地图_百度地图                                          | map.baidu.com                                       | 1    |
| 2    | 首都之窗-北京市政务门户网站                                  | http://www.beijing.gov.cn                           | 1    |
| 3    | 北京天气预报_一周天气预报_中国天气网                         | http://www.weather.com.cn/weather/101010100.shtml   | 1    |
| 4    | 2019北京旅游攻略,北京自由行攻略,马蜂窝北京出游攻略游记 - 马蜂窝 | http://www.mafengwo.cn/                             | 1    |
| 5    | 北京_百度图片                                                | https://image.baidu.com/                            | 1    |
| 6    | 北京人事考试服务频道_北京市人力资源和社会保障局              | www.bjrbj.gov.cn                                    | 1    |
| 7    | 北京二手房_北京租房_北京房产网(北京链家网)                   | bj.lianjia.com                                      | 1    |
| 8    | 北京市公安局                                                 | http://www.bjgaj.gov.cn/web/                        | 1    |
| 9    | 中国国际贸易促进委员会北京市分会                             | www.ccpitbj.org                                     | 1    |

#### 360好搜

| 编号 | 摘要                                             | 网址                                                         | 标注 |
| ---- | ------------------------------------------------ | ------------------------------------------------------------ | ---- |
| 0    | 北京_360百科                                     | https://baike.so.com/doc/2510451-2652822.html                | 1    |
| 1    | 首都之窗-北京市政务门户网站                      | http://www.beijing.gov.cn                                    | 1    |
| 2    | 北京旅游攻略                                     | http://u.ctrip.com/place/beijing1.html                       | 1    |
| 3    | 北京天气预报_近日天气预报                        | https://tianqi.so.com/weather/101010100                      | 1    |
| 4    | 北京_360地图                                     | https://ditu.so.com/?t=map&src=onebox&new=1&k=北京市&c=北京  | 1    |
| 5    | 北京北京_分集剧情/大结局全集剧情                 | https://www.tvsou.com/show/9ac984e1/                         | 0    |
| 6    | 【北京PM2.5实时查询】空气质量指数查询_全国天气网 | https://tianqi.so.com/air/101010100                          | 1    |
| 7    | 北京_360图片                                     | http://image.so.com/i?src=360pic_normal&z=1&i=0&cmg=ce9d2a9b7b083c0079850f897927b14c&q=北京 | 1    |
| 8    | 北京@北京_小区二手房_租房_详情介绍_房价_房天下   | www.fang.com                                                 | 1    |
| 9    | 北京相关资讯！有些人还不知道，赶快来看！         | http://sh.qihoo.com                                          | 1    |

#### 搜狗

| 编号 | 摘要                                                         | 网址                                                         | 标注 |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- |
| 0    | 北京 - 搜狗百科                                              | https://baike.sogou.com/v4412.htm?fromTitle=北京             | 1    |
| 1    | 北京的最新相关信息（搜狗新闻）                               | http://news.sogou.com/news?mode=1&sort=0&fixrank=1&query=%B1%B1%BE%A9&shid=djt1 | 1    |
| 2    | 北京市地图_搜狗地图                                          | http://map.sogou.com/#c=12956000,4824875,9&lq=北京市&originurltype=PC_VR_City | 1    |
| 3    | 北京旅游_最佳线路_攻略_热门景点_去哪儿网                     | https://dujia.qunar.com/compositecard/index?sightId=27005&tf=sg_jd_title&ex_track=auto_547eb7ca | 1    |
| 4    | 首都之窗-北京市政务门户网站                                  | http://www.beijing.gov.cn                                    | 1    |
| 5    | 【北京天气】北京天气预报,蓝天,蓝天预报,雾霾,雾霾消散,天...（中国天气网） | http://www.weather.com.cn/weather/101010100.shtml            | 1    |
| 6    | 北京_热门回答_知乎                                           | https://www.zhihu.com/topic/19550828/top-answers             | 1    |
| 7    | 北京_搜狗图片                                                | http://pic.sogou.com/pics?query=%B1%B1%BE%A9&p=40230500&st=255&mode=255 | 1    |
| 8    | 北京市预约挂号统一平台                                       | www.bjguahao.gov.cn                                          | 1    |
| 9    | 北京天气预报_一周天气预报_中国天气网                         | www.weather.com.cn                                           | 1    |

### 拉格朗日

#### 百度

| 编号 | 摘要                                                         | 网址                                                         | 标注 |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- |
| 0    | 拉格朗日_百度百科                                            | https://baike.baidu.com/item/约瑟夫·拉格朗日/3224655?fromtitle=拉格朗日&fromid=383115&fr=aladdin | 1    |
| 1    | 拉格朗日定理_百度百科                                        | https://baike.baidu.com/item/拉格朗日定理/7217921            | 0    |
| 2    | 拉格朗日中值定理_百度百科                                    | https://baike.baidu.com/item/拉格朗日中值定理/1876030        | 0    |
| 3    | 高等数学：拉格朗日中值定理？_百度经验                        | https://jingyan.baidu.com/article/15622f2426064efdfcbea5a2.html | 0    |
| 4    | 远超四大“装逼天王”,装逼界的始祖——拉格朗日                    | http://baijiahao.baidu.com/s?id=1581223247698431174&wfr=spider&for=pc | 1    |
| 5    | 深入理解拉格朗日乘子法(Lagrange Multiplier) 和KKT条件..._博客园 | https://www.cnblogs.com/sddai/p/5728195.html                 | 0    |
| 6    | 拉格朗日_百度文库                                            | https://wenku.baidu.com/search?word=%E6%8B%89%E6%A0%BC%E6%9C%97%E6%97%A5&ie=utf-8&lm=0&od=0 | 1    |
| 7    | 拉格朗日点(平面圆型限制性三体问题的5个特解)_百度百科         | https://baike.baidu.com/item/%E6%8B%89%E6%A0%BC%E6%9C%97%E6%97%A5%E7%82%B9/731078 | 0    |
| 8    | 拉格朗日乘子法如何理解? - 知乎                               | https://baike.baidu.com/item/%E6%8B%89%E6%A0%BC%E6%9C%97%E6%97%A5%E6%96%B9%E7%A8%8B/1948406 | 0    |
| 9    | 拉格朗日乘数法_百度百科                                      | https://baike.baidu.com/item/%E6%8B%89%E6%A0%BC%E6%9C%97%E6%97%A5%E4%B9%98%E6%95%B0%E6%B3%95/8550443 | 0    |

#### 360好搜

| 编号 | 摘要                                                         | 网址                                                         | 标注 |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- |
| 0    | 拉格朗日_360百科                                             | https://baike.so.com/doc/5812482-6025289.html                | 1    |
| 1    | 拉格朗日中值定理_百度百科                                    | https://baike.baidu.com/item/拉格朗日中值定理/1876030        | 0    |
| 2    | 拉格朗日方法_360百科                                         | https://baike.so.com/doc/9363479-9701518.html                | 0    |
| 3    | 高等数学：拉格朗日中值定理？_百度经验                        | https://jingyan.baidu.com/article/15622f2426064efdfcbea5a2.html | 0    |
| 4    | 拉格朗日方程,拉格朗日体系,你一定听过                         | https://www.sohu.com/a/167657053_479097                      | 0    |
| 5    | 拉格朗日函数- 百度文库                                       | https://wenku.baidu.com/view/03d36fc4d5bbfd0a79567318.html   | 0    |
| 6    | 拉格朗日_360图片                                             | http://image.so.com/i?src=360pic_normal&z=1&i=0&cmg=ce9d2a9b7b083c0079850f897927b14c&q=拉格朗日 | 1    |
| 7    | 斯坦福大学公开课:机器人学_拉格朗日方程_网易公开课            | https://open.163.com/movie/2008/11/H/M/M6TN5NEEU_M6TN7TCHM.html | 0    |
| 8    | 轮回的拉格朗日-第1季-更新更全更受欢迎的影视网站-在线观看     | https://www.360kan.com/ct/PU4ncMPdMoazDT.html                | 0    |
| 9    | 拉格朗日L2点:神秘的“地月平动点”\|拉格朗日\|央视网\|飞行_新浪新闻 | http://news.sina.com.cn/w/2018-05-21/doc-ihawmaua0336675.shtml | 0    |

#### 搜狗

| 编号 | 摘要                                                         | 网址                                                         | 标注 |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- |
| 0    | 拉格朗日 - 搜狗百科                                          | https://baike.sogou.com/v548631.htm?fromTitle=拉格朗日       | 1    |
| 1    | 【拉格朗日】拉格朗日拉格朗日中值定理_拉格朗日点_人物_历史上的... | http://www.todayonhistory.com/people/201512/12131.html       | 1    |
| 2    | 拉格朗日插值法（图文详解） - Angel_Kitty - 博客园            | http://www.cnblogs.com/ECJTUACM-873284962/p/6833391.html     | 0    |
| 3    | 高等数学:拉格朗日中值定理_百度经验                           | https://jingyan.baidu.com/article/15622f2426064efdfcbea5a2.html | 0    |
| 4    | 拉格朗日_搜狗图片                                            | http://pic.sogou.com/pics?query=%C0%AD%B8%F1%C0%CA%C8%D5&p=40230500&st=255&mode=255 | 1    |
| 5    | 拉格朗日定理与罗尔定理,柯西定理啥关系?_知乎                  | https://www.zhihu.com/question/26803653#answer-41991300      | 0    |
| 6    | 拉格朗日的相关内容_微信                                      | http://weixin.sogou.com/weixin?query=拉格朗日&ie=utf8&type=2&sourceid=weixinvr | 1    |
| 7    | 拉格朗日中值定理_百度百科                                    | https://baike.baidu.com/item/拉格朗日中值定理/1876030        | 0    |
| 8    | 拉格朗日L2点:神秘的“地月平动点”\|拉格朗日\|央视网\|飞行_新浪新闻 | http://news.sina.com.cn/w/2018-05-21/doc-ihawmaua0336675.shtml | 0    |
| 9    | 拉格朗日力学_百度百科                                        | https://baike.baidu.com/item/%E6%8B%89%E6%A0%BC%E6%9C%97%E6%97%A5%E5%8A%9B%E5%AD%A6/4054316 | 0    |

### 订机票

#### 百度

| 编号 | 摘要                                                         | 网址                      | 标注 |
| ---- | ------------------------------------------------------------ | ------------------------- | ---- |
| 0    | 订机票-携程订机票低价\_机票预订\_超低折扣                    | http://flights.ctrip.com/ | 1    |
| 1    | 【天猫】-天猫机票预订_大牌"惠"聚_理想生活上天猫              | https://www.tmall.com/    | 1    |
| 2    | 携程飞机票网上订票_机票查询_机票预订_携程网出行更简          | https://flights.ctrip.com | 1    |
| 3    | 【海南航空】3月大促2折起_尊享特价_唤醒春风艳阳天             | http://www.hnair.com      | 1    |
| 4    | 订 机票-中国南方航空 机票2折起                               | https://www.csair.com     | 1    |
| 5    | 国内国际特价机票查询及在线预订_百度机票                      | http://flights.ctrip.com/ | 1    |
| 6    | 【去哪儿网】机票查询,特价机票,打折飞机票-去哪儿网Qunar.com   | https://flight.qunar.com  | 1    |
| 7    | 携程旅行网官网:酒店预订,机票预订查询,旅游度假,商旅管理       | http://www.ctrip.com      | 0    |
| 8    | 【艺龙旅行网】酒店预订\_机票查询\_酒店团购\_电话4009-333-333 | http://www.elong.com      | 0    |
| 9    | 天巡网 - 廉价航空、国际机票、特价机票查询预订、Skyscanner中国 | https://www.tianxun.com   | 1    |

#### 360好搜

| 编号 | 摘要                                                       | 网址                                                      | 标注 |
| ---- | ---------------------------------------------------------- | --------------------------------------------------------- | ---- |
| 0    | 订机票-机票预订 预订机票 订机票 携程网                     | http://flights.ctrip.com/booking/bjs-beijing-flights.html | 1    |
| 1    | 订机票 打折机票 上途牛网 低至1折                           | http://www.tuniu.com/                                     | 1    |
| 2    | 订机票 机票查询 携程机票超值优惠                           | http://flights.ctrip.com                                  | 1    |
| 3    | 关于订机票，为您推荐更多优质结果>>                         | e.360.cn                                                  | 0    |
| 4    | 飞机订票(AirAsia)-亚洲航空官方网站                         | e.so.com/go                                               | 1    |
| 5    | 北京出发机票查询_打折/特价机票_机票预定及票价查询_携程机票 | www.ctrip.com                                             | 1    |
| 6    | 【去哪儿网】机票查询,特价机票,打折飞机票-去哪儿网Qunar.com | https://flight.qunar.com                                  | 1    |
| 7    | 【携程机票】飞机票查询,机票预订,机票价格查询,打折特价机票  | http://flights.ctrip.com                                  | 1    |
| 8    | 机票预订_机票预订查询_机票预订网_2-7折_同程旅游            | www.ly.com                                                | 1    |
| 9    | 网上订机票_360百科                                         | baike.so.com                                              | 0    |

#### 搜狗

| 编号 | 摘要                                                         | 网址                      | 标注 |
| ---- | ------------------------------------------------------------ | ------------------------- | ---- |
| 0    | 订机票_机票查询预订_即刻预订_说走就走!                       | http://www.ctrip.com/     | 1    |
| 1    | 订机票:上携程官网订机票                                      | http://flights.ctrip.com/ | 1    |
| 2    | 订机票抢便宜日本机票_就在全日空预订享超值特价                | www.ana.co.jp             | 1    |
| 3    | 亚洲航空(AirAsia)亚洲航空官方网站                            | www.AirAsia.com           | 1    |
| 4    | 淘宝订机票_尽在淘宝                                          | re.taobao.com             | 0    |
| 5    | 国内机票查询及机票在线预订_携程旅行网提供                    | http://flights.ctrip.com  | 1    |
| 6    | 飞机票预订官网_特价酒店预订_旅游度假去哪好_逍遥行旅行网      | www.feijipiao.cn          | 1    |
| 7    | 天巡网 - 廉价航空、国际机票、特价机票查询预订、Skyscanner中国 | https://www.tianxun.com   | 1    |
| 8    | 如何订机票最划算?_知乎                                       | www.zhihu.com/            | 0    |
| 9    | 【去哪儿网】机票查询,特价机票,打折飞机票-去哪儿网Qunar.com   | https://flight.qunar.com  | 1    |

### gdb设置断点

#### 百度

| 编号 | 摘要                                              | 网址                                                         | 标注 |
| ---- | ------------------------------------------------- | ------------------------------------------------------------ | ---- |
| 0    | gdb几种设置断点的方式 - 波波诸葛伟 - CSDN博客     | https://blog.csdn.net/wojiuguowei/article/details/82386567   | 1    |
| 1    | GDB(设置断点) - 华秋实的专栏 - CSDN博客           | https://blog.csdn.net/yockie/article/details/79166713        | 1    |
| 2    | linux c之gdb常用断点调试总结 - CSDN博客           | https://blog.csdn.net/u011068702/article/details/53931648    | 1    |
| 3    | linux gdb的详细用法 运行与断点(一) - CSDN博客     | https://blog.csdn.net/Z_Dream_ST/article/details/77840733    | 1    |
| 4    | GDB断点设置与调试 - jasononline - 博客园          | https://www.cnblogs.com/jason2013/articles/4331486.html      | 1    |
| 5    | gdb几种设置断点的方式 - 惡盈好謙 - 博客园         | https://www.cnblogs.com/northhurricane/p/3860393.html        | 1    |
| 6    | Linux gdb设置和管理断点 - blacet的专栏 - CSDN博客 | https://blog.csdn.net/blacet/article/details/52397261        | 1    |
| 7    | Linux编程基础——GDB(设置断点) - 天方 - 博客园      | https://www.cnblogs.com/TianFang/archive/2013/01/20/2868889.html | 1    |
| 8    | gdb在文件行号上打断点 - taolusi的博客 - CSDN      | https://blog.csdn.net/taolusi/article/details/81072226       | 0    |
| 9    | GDB——GDB的断点调试 - 食梦者 - CSDN博客            | https://blog.csdn.net/small_prince_/article/details/80681684 | 1    |

#### 360好搜

| 编号 | 摘要                                                         | 网址                                                         | 标注 |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- |
| 0    | gdb break 断点设置(一) - 杨重选的专栏- CSDN博客              | https://blog.csdn.net/yangzhongxuan/article/details/6897968  | 1    |
| 1    | Linux编程基础——GDB(设置断点) - 天方 - 博客园                 | https://www.cnblogs.com/TianFang/archive/2013/01/20/2868889.html | 1    |
| 2    | linux c之gdb常用断点调试总结- No talent - CSDN博客           | https://blog.csdn.net/u011068702/article/details/53931648    | 1    |
| 3    | gdb几种设置断点的方式 - 惡盈好謙 - 博客园                    | https://www.cnblogs.com/northhurricane/p/3860393.html        | 1    |
| 4    | Linux编程基础——GDB(设置断点)-做最好的自己-51CTO博客          | https://blog.51cto.com/qiaopeng688/2065145                   | 1    |
| 5    | GDB设置断点- Linux编程基础详细教程_Linux编程_Linux公社-Linux... | https://www.linuxidc.com/Linux/2017-12/149081p2.htm          | 1    |
| 6    | gdb设置断点的时候总是显示No line 19 in file.-CSDN论坛        | https://bbs.csdn.net/topics/390287983                        | 0    |
| 7    | linux下使用gdb的断点设置- enmmmm - 博客园                    | http://www.cnblogs.com/xxjb/p/9942863.html                   | 1    |
| 8    | 请教一下,GDB条件断点设置问题- C/C++-ChinaUnix.net            | http://bbs.chinaunix.net/thread-1881637-1-1.html             | 0    |
| 9    | gdb中设置断点_wfdgd_新浪博客                                 | http://blog.sina.com.cn/s/blog_418d92e601009h3z.html         | 1    |

#### 搜狗

| 编号 | 摘要                                               | 网址                                                         | 标注 |
| :--- | -------------------------------------------------- | ------------------------------------------------------------ | ---- |
| 0    | gdb break 断点设置（一） - CSDN博客                | https://blog.csdn.net/yangzhongxuan/article/details/6897968  | 1    |
| 1    | linux c之gdb常用断点调试总结- No talent - CSDN博客 | https://blog.csdn.net/u011068702/article/details/53931648    | 1    |
| 2    | Linux编程基础——GDB(设置断点) - 天方 - 博客园       | https://www.cnblogs.com/TianFang/archive/2013/01/20/2868889.html | 1    |
| 3    | GDB——GDB的断点调试 - 食梦者 - CSDN博客             | https://blog.csdn.net/small_prince_/article/details/80681684 | 1    |
| 4    | gdb几种设置断点的方式 - 惡盈好謙 - 博客园          | https://www.cnblogs.com/northhurricane/p/3860393.html        | 1    |
| 5    | gdb中设置断点 - zangcf的专栏 - CSDN博客            | https://blog.csdn.net/zangcf/article/details/8590145         | 1    |
| 6    | [原创]GDB调试指南-断点设置 - 守望先生 - 博客园     | https://www.cnblogs.com/bianchengzhuji/p/10445882.html       | 1    |
| 7    | GDB调试指南-断点设置                               | https://mp.weixin.qq.com/                                    | 1    |
| 8    | gdb如何保存和读取断点_百度经验                     | jingyan.baidu.com                                            | 0    |
| 9    | gdb调试的断点设置方法_kid_寂寞空虚冷_新浪博客      | http://blog.sina.com.cn/s/blog_b849fc610101a5pz.html         | 1    |

### word画表格

#### 百度

| 编号 | 摘要                                         | 网址                                                         | 标注 |
| ---- | -------------------------------------------- | ------------------------------------------------------------ | ---- |
| 0    | word如何制作表格_百度经验                    | https://jingyan.baidu.com/article/49711c61334757fa441b7c97.html | 1    |
| 1    | 用word怎么画表格?怎么在word中画表格_百度经验 | https://jingyan.baidu.com/article/495ba841e0a63838b30eded9.html | 1    |
| 2    | Word2010怎么绘制表格_百度经验                | https://jingyan.baidu.com/article/0aa223751a7d1d88cc0d649b.html | 1    |
| 3    | word文档怎么用绘制表格划线\_百度知道         | https://zhidao.baidu.com/question/1113672777662167019.html   | 1    |
| 4    | 详解如何用Word绘制表格和表格调整             | http://baijiahao.baidu.com/s?id=1599942907935934694&wfr=spider&for=pc | 1    |
| 5    | 怎么在WORD里画表格_百度知道                  | https://zhidao.baidu.com/question/355817708.html             | 1    |
| 6    | Word文档如何绘制表格_百度经验                | https://jingyan.baidu.com/article/63acb44a02df9261fdc17e60.html | 1    |
| 7    | 如何在Word中绘制表格_百度经验                | https://jingyan.baidu.com/article/3c343ff7a0db5d0d377963c4.html | 1    |
| 8    | word画表格_百度图片                          | https://image.baidu.com                                      | 0    |
| 9    | wps word如何画表格_百度经验                  | https://jingyan.baidu.com/article/1709ad804448a54634c4f092.html | 1    |

#### 360好搜

| 编号 | 摘要                                                   | 网址                                                         | 标注 |
| ---- | ------------------------------------------------------ | ------------------------------------------------------------ | ---- |
| 0    | 制作Word表格的最基本方法:绘制与插入_天极网             | http://soft.yesky.com/office/356/2585356.shtml               | 1    |
| 1    | 如何在word 中绘制表格_百度经验                         | https://jingyan.baidu.com/article/925f8cb80dd07fc0dce05660.html | 1    |
| 2    | word如何制作表格_360新知                               | http://xinzhi.wenda.so.com/a/1523980252614879                | 1    |
| 3    | 怎样在Word2007文档中绘制表格\_百度经验                 | https://jingyan.baidu.com/article/4d58d541ec3f8c9dd4e9c0c4.html | 1    |
| 4    | 用Word怎么画表格?\_360问答                             | https://wenda.so.com/q/1363986391064895?src=180              | 1    |
| 5    | 用Word怎么画表格?怎么在Word中画表格                    | http://www.geren-jianli.com/n16433c34.aspx?jdfwkey=tnqd72    | 1    |
| 6    | word文档怎么用绘制表格划线\_360问答                    | https://wenda.so.com/q/1483906324721576                      | 1    |
| 7    | word文档中怎么画表格_360问答                           | https://wenda.so.com/q/1534024226211058                      | 1    |
| 8    | 怎么在WORD里画表格_360问答                             | https://wenda.so.com/q/1463589490724891                      | 1    |
| 9    | Word画表格的笔在哪里\_Word2010怎么绘制表格\_最火下载站 | http://www.veryhuo.com/a/view/117556.html                    | 1    |

#### 搜狗

| 编号 | 摘要                                         | 网址                                                         | 标注 |
| ---- | -------------------------------------------- | ------------------------------------------------------------ | ---- |
| 0    | 简历怎么写_个人简历模板尽在拉勾              | https://www.lagou.com/lp/html/common.html?utm_source=m_cf_cpc_sogou_pc&m_kw=sogou_cpc_bj_2a9bf2_4dd26e_word%E6%80%8E%E4%B9%88%E5%81%9A%E8%A1%A8%E6%A0%BC | 0    |
| 1    | WORD中绘制表格_百度文库                      | https://wenku.baidu.com/view/707abcd6195f312b3169a563.html   | 1    |
| 2    | 用word怎么制作自己想要的表格_搜狗指南        | https://zhinan.sogou.com/guide/detail/?id=1610010307         | 1    |
| 3    | word如何制作表格_百度经验                    | https://jingyan.baidu.com/article/49711c61334757fa441b7c97.html | 1    |
| 4    | Word2003中自己手工绘制表格技巧_Word联盟      | http://www.wordlm.com/html/2692.html                         | 1    |
| 5    | word画表格的相关内容_微信                    | https://weixin.sogou.com/weixin?query=word%E7%94%BB%E8%A1%A8%E6%A0%BC&ie=utf8&type=2&sourceid=weixinvr | 0    |
| 6    | word画表格_搜狗知识（全部约50998条结果）     | https://www.sogou.com/sogou?query=word%E7%94%BB%E8%A1%A8%E6%A0%BC&ie=utf8&pid=sogou-wsse-926c11cc055de9b8&interation=196636&jhdid=3c28af542f2d49f7-c53fd3988c057bf5-a0a46ac725159a5916bb74dabc14ef69 | 1    |
| 7    | word中表格绘制如何绘制表格线间断点?\_知乎    | https://www.zhihu.com/question/34878321#answer-19509290      | 1    |
| 8    | 制作Word表格的最基本方法:绘制与插入_天极网   | http://soft.yesky.com/office/356/2585356.shtml               | 1    |
| 9    | 用word怎么画表格?怎么在word中画表格_百度经验 | https://jingyan.baidu.com/article/495ba841e0a63838b30eded9.html | 1    |

## 性能评价

### 导航类

#### 携程

| 评价指标 | 百度 | 360好搜 | 搜狗 |
| -------- | ---- | ------- | ---- |
| AP       | 0.63 | 0.75    | 0.49 |
| RR       | 1.0  | 1.0     | 1.0  |

#### 清华大学

| 评价指标 | 百度 | 360好搜 | 搜狗 |
| -------- | ---- | ------- | ---- |
| AP       | 0.31 | 0.36    | 0.38 |
| RR       | 1.0  | 1.0     | 1.0  |

### 信息类

#### 土屋圭市

| 评价指标 | 百度 | 360好搜 | 搜狗 |
| -------- | ---- | ------- | ---- |
| AP       | 0.58 | 0.58    | 0.73 |
| P@5      | 0.6  | 0.6     | 0.6  |
| P@10     | 0.4  | 0.5     | 0.6  |
| RR       | 1.0  | 1,0     | 1.0  |

#### 英雄联盟

| 评价指标 | 百度 | 360好搜 | 搜狗 |
| -------- | ---- | ------- | ---- |
| AP       | 0.76 | 0.58    | 0.88 |
| P@5      | 0.8  | 0.6     | 1.0  |
| P@10     | 0.5  | 0.6     | 0.7  |
| RR       | 1.0  | 1.0     | 1.0  |

#### golang

| 评价指标 | 百度 | 360好搜 | 搜狗 |
| -------- | ---- | ------- | ---- |
| AP       | 0.88 | 0.71    | 0.79 |
| P@5      | 1.0  | 0.8     | 0.8  |
| P@10     | 0.7  | 0.9     | 0.7  |
| RR       | 1.0  | 0.5     | 1.0  |

#### 北京

| 评价指标 | 百度 | 360好搜 | 搜狗 |
| -------- | ---- | ------- | ---- |
| AP       | 1.00 | 0.93    | 1.00 |
| P@5      | 1.0  | 1.0     | 1.0  |
| P@10     | 1.0  | 0.9     | 1.0  |
| RR       | 1.0  | 1.0     | 1.0  |

#### 拉格朗日

| 评价指标 | 百度 | 360好搜 | 搜狗 |
| -------- | ---- | ------- | ---- |
| AP       | 0.43 | 0.34    | 0.62 |
| P@5      | 0.4  | 0.2     | 0.6  |
| P@10     | 0.3  | 0.2     | 0.4  |
| RR       | 1.0  | 1.0     | 1.0  |

### 事务类

#### 订机票

| 评价指标 | 百度 | 360好搜 | 搜狗 |
| -------- | ---- | ------- | ---- |
| AP       | 0.95 | 0.88    | 0.89 |
| S@5      | 1.0  | 0.8     | 0.8  |
| S@10     | 0.8  | 0.8     | 0.8  |
| RR       | 1.0  | 1.0     | 1.0  |

#### gdb设置断点

| 评价指标 | 百度 | 360好搜 | 搜狗 |
| -------- | ---- | ------- | ---- |
| AP       | 0.99 | 0.93    | 0.98 |
| S@5      | 1.0  | 1.0     | 1.0  |
| S@10     | 0.9  | 0.8     | 0.9  |
| RR       | 1.0  | 1.0     | 1.0  |

#### word画表格

| 评价指标 | 百度 | 360好搜 | 搜狗 |
| -------- | ---- | ------- | ---- |
| AP       | 0.98 | 1.0     | 0.64 |
| S@5      | 1.0  | 1.0     | 0.8  |
| S@10     | 0.9  | 1.0     | 0.8  |
| RR       | 1.0  | 1.0     | 0.5  |

## 实验结论

从数据上来看，大体上百度优于360优于搜狗，少部分数据搜狗优于360但弱于百度。而搜索结果上，三家均会推荐自家产品，如百科等，而且同质化严重，内容基本一致。而三者无一例外都有大量广告夹杂在搜索结果中，甚至在某些搜索关键词中，广告严重影响了搜索结果。