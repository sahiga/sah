# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1597524543.958326
_enable_loop = True
_template_filename = 'themes/lightning/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('pheader', context._clean_inheritance_tokens(), templateuri='post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pheader')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        pheader = _mako_get_namespace(context, 'pheader')
        title = context.get('title', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        permalink = context.get('permalink', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        messages = context.get('messages', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        post = context.get('post', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        post = context.get('post', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\n')
        if post.meta('keywords'):
            __M_writer('    <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(post.meta('keywords'))))
            __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        pheader = _mako_get_namespace(context, 'pheader')
        date_format = context.get('date_format', UNDEFINED)
        post = context.get('post', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context)
        permalink = context.get('permalink', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        def content():
            return render_content(context)
        comments = _mako_get_namespace(context, 'comments')
        title = context.get('title', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        __M_writer('\n  <div id="post-')
        __M_writer(str(post.meta('slug')))
        __M_writer('" class="post hfeed">\n    <h2 class="entry-title"><a href=\'')
        __M_writer(str(permalink))
        __M_writer("'>")
        __M_writer(str(title))
        __M_writer('</a></h2>\n    <div class="entry-content">\n        ')
        __M_writer(str(post.text()))
        __M_writer('\n    </div>\n    <div class="archive-meta">\n        ')
        __M_writer(str(messages("Posted:")))
        __M_writer(' <time class="published" datetime="')
        __M_writer(str(post.date.isoformat()))
        __M_writer('">')
        __M_writer(str(post.formatted_date(date_format)))
        __M_writer('</time>\n        ')
        __M_writer(str(pheader.html_translations(post)))
        __M_writer('\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\n            ')
        __M_writer(str(helper.html_tags(post)))
        __M_writer('\n        <span class="entry-tags">\n        </span>\n      <hr />\n    </div>\n  </div>\n  ')
        __M_writer(str(helper.html_pager(post)))
        __M_writer('\n')
        if not post.meta('nocomments'):
            __M_writer('      ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post.base_path)))
            __M_writer('\n')
        __M_writer('  ')
        __M_writer(str(helper.mathjax_script(post)))
        __M_writer('\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def sourcelink():
            return render_sourcelink(context)
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if not post.meta('password'):
            __M_writer('            <a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a>\n')
        __M_writer('        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/lightning/templates/post.tmpl", "uri": "post.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "35": 0, "54": 2, "55": 3, "56": 4, "57": 5, "62": 11, "72": 6, "80": 6, "81": 7, "82": 7, "83": 8, "84": 9, "85": 9, "86": 9, "92": 12, "108": 12, "109": 13, "110": 13, "111": 14, "112": 14, "113": 14, "114": 14, "115": 16, "116": 16, "117": 19, "118": 19, "119": 19, "120": 19, "121": 19, "122": 19, "123": 20, "124": 20, "129": 25, "130": 26, "131": 26, "132": 32, "133": 32, "134": 33, "135": 34, "136": 34, "137": 34, "138": 36, "139": 36, "140": 36, "146": 21, "154": 21, "155": 22, "156": 23, "157": 23, "158": 23, "159": 23, "160": 23, "161": 25, "167": 161}}
__M_END_METADATA
"""
