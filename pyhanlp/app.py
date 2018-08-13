# -*- coding: utf-8 -*-


from flask import Flask
from flask_admin import Admin, AdminIndexView
from flask_admin import BaseView, expose
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

import urllib.request as urllib2
import api
import logging
import traceback

# views
class Tokenizer(BaseView):
    category = "词法分析"

    @expose("/")
    def index(self):
        content = request.args.get("content", "")
        content = urllib2.unquote(content)
        content = str(content).strip()
        algorithm = request.args.get("algorithm")
        sentence = api.segment(content, algorithm)

        sentence = "  ".join([i.word for i in sentence])
        ret = self.render('tokenizer.html',
                          algorithm=algorithm,
                          content=content,
                          sentence=sentence)

        return ret


class TextTransformer(BaseView):
    category = "文本转换"

    @expose("/")
    def index(self):
        content = request.args.get("content", "")
        content = urllib2.unquote(content)
        content = str(content).strip()
        algorithm = request.args.get("algorithm")
        sentence = ""
        if algorithm == "chinese2pingyin":
            sentence = api.convertToPinyinList(content)
        elif algorithm == "tradictional2chinese":
            sentence = api.convertToSimplifiedChinese(content)
        elif algorithm == "chinese2tradictional":
            sentence = api.convertToTraditionalChinese(content)

        ret = self.render('texttransform.html',
                          algorithm=algorithm,
                          content=content,
                          sentence=sentence)

        return ret


class SyTextView(BaseView):
    category = "文本语义分析"

    @expose("/")
    def index(self):
        content = request.args.get("content", "")
        content = urllib2.unquote(content)
        content = str(content).strip()
        algorithm = request.args.get("algorithm", "getSummary")
        size = int(request.args.get("size", "10"))
        sentence = ""

        try:
            if algorithm == "parseDependency":
                sentence = api.parseDependency(content)
            elif algorithm == "extractPhrase":
                sentence = api.extractPhrase(content, size)
            elif algorithm == "extractWords":
                sentence = api.extractWords(content, size)
            elif algorithm == "extractKeyword":
                sentence = api.extractKeyword(content, size)
            elif algorithm == "extractSummary":
                sentence = api.extractSummary(content, size)
            elif algorithm == "getSummary":
                sentence = api.getSummary(content, size)
        except:
            logging.error(traceback.format_exc())
            logging.error("content, size: %s, %d", content, size)

        ret = self.render('sytext.html',
                          algorithm=algorithm,
                          size=size,
                          content=content,
                          sentence=sentence)

        return ret


app = Flask(__name__)
app.debug = False


# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">goto adminview!</a>'


def init():
    admin = Admin(app, name="HanLP 演示",
                  index_view=AdminIndexView(name='Home',
                                            template='admin/index.html',
                                            url='/admin'),
                  base_template='layout.html',
                  template_mode="bootstrap3")
    admin.add_view(Tokenizer(name=u"词法分析", endpoint="tokenizer"))
    admin.add_view(TextTransformer(name=u"文本转换", endpoint="TextTransformer"))
    admin.add_view(SyTextView(name=u"语义分析", endpoint="SyTextView"))


init()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=False)

