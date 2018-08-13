# -*- coding: utf-8 -*-

from pyhanlp import HanLP


def convertToSimplifiedChinese(traditionalChineseString):
    """
     * 繁转简
     *
     * @param traditionalChineseString 繁体中文
     * @return 简体中文
    """
    return HanLP.convertToSimplifiedChinese(traditionalChineseString)


def convertToTraditionalChinese(simplifiedChineseString):
    """
     * 简转繁
     *
     * @param simplifiedChineseString 简体中文
     * @return 繁体中文

    """
    return HanLP.convertToTraditionalChinese(simplifiedChineseString)


def convertToPinyinString(text, separator, remainNone):
    """
     * 转化为拼音
     *
     * @param text       文本
     * @param separator  分隔符
     * @param remainNone 有些字没有拼音（如标点），是否保留它们的拼音（true用none表示，false用原字符表示）
     * @return 一个字符串，由[拼音][分隔符][拼音]构成

    """
    return HanLP.convertToPinyinString(text, separator, remainNone)


def convertToPinyinList(text):
    """
     * 转化为拼音
     *
     * @param text 待解析的文本
     * @return 一个拼音列表

    """
    return HanLP.convertToPinyinList(text)


def convertToPinyinFirstCharString(text, separator, remainNone):
    """
     * 转化为拼音（首字母）
     *
     * @param text       文本
     * @param separator  分隔符
     * @param remainNone 有些字没有拼音（如标点），是否保留它们（用none表示）
     * @return 一个字符串，由[首字母][分隔符][首字母]构成

    """
    return HanLP.convertToPinyinFirstCharString(text, separator, remainNone)


def newSegment(algorithm="viterbi"):
    """
    * 创建一个分词器，
     * 这是一个工厂方法<br>
     *
     * @param algorithm 分词算法，传入算法的中英文名都可以，可选列表：<br>
     *                  <ul>
     *                  <li>维特比 (viterbi)：效率和效果的最佳平衡</li>
     *                  <li>双数组trie树 (dat)：极速词典分词，千万字符每秒</li>
     *                  <li>条件随机场 (crf)：分词、词性标注与命名实体识别精度都较高，适合要求较高的NLP任务</li>
     *                  <li>感知机 (perceptron)：分词、词性标注与命名实体识别，支持在线学习</li>
     *                  <li>N最短路 (nshort)：命名实体识别稍微好一些，牺牲了速度</li>
     *                  <li>2阶隐马 (hmm2)：训练速度较CRF快</li>
     *                  </ul>
     * @return 一个分词器

    """
    return HanLP.newSegment(algorithm)


def segment(text, algorithm=None):
    if algorithm is None:
        return HanLP.segment(text)

    return newSegment(algorithm).seg(text)


def parseDependency(sentence):
    """
     * 依存文法分析
     *
     * @param sentence 待分析的句子
     * @return CoNLL格式的依存关系树

    """
    return HanLP.parseDependency(sentence)


def extractPhrase(text, size):
    """
     * 提取短语
     * @param text 文本
     * @param size 需要多少个短语
     * @return 一个短语列表，大小 <= size

    """
    return HanLP.extractPhrase(text, size)


def extractWords(text, size, newWordsOnly=False):
    """
     * 提取词语
     *
     * @param reader 从reader获取文本
     * @param size   需要提取词语的数量
     * @param newWordsOnly 是否只提取词典中没有的词语
     * @return 一个词语列表

    """
    return HanLP.extractWords(text, size, newWordsOnly)


def extractKeyword(document, size):
    """
    * 提取关键词
     *
     * @param document 文档内容
     * @param size     希望提取几个关键词
     * @return 一个列表
    """
    return HanLP.extractKeyword(document, size)


def extractSummary(document, size, sentence_separator=None):
    """
      * 自动摘要
     *
     * @param document           目标文档
     * @param size               需要的关键句的个数
     * @param sentence_separator 分割目标文档时的句子分割符，正则格式， 如：[。？?！!；;]
     * @return 关键句列表
    """
    if sentence_separator:
        return HanLP.extractSummary(document, size, sentence_separator)
    else:
        return HanLP.extractSummary(document, size)


def getSummary(document, max_length, sentence_separator=None):
    """
     * 自动摘要
     *
     * @param document           目标文档
     * @param max_length         需要摘要的长度
     * @param sentence_separator 分割目标文档时的句子分割符，正则格式， 如：[。？?！!；;]
     * @return 摘要文本

    """
    if sentence_separator:
        return HanLP.getSummary(document, max_length, sentence_separator)
    else:
        return HanLP.getSummary(document, max_length)

