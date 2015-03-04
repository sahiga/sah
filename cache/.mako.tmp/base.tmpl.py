# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425427875.041953
_enable_loop = True
_template_filename = u'themes/lightning/templates/base.tmpl'
_template_uri = u'base.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'belowtitle']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'base', context._clean_inheritance_tokens(), templateuri=u'base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        def belowtitle():
            return render_belowtitle(context._locals(__M_locals))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        blog_url = _import_ns.get('blog_url', context.get('blog_url', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(unicode(set_locale(lang)))
        __M_writer(u'\n')
        __M_writer(unicode(base.html_headstart()))
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer(u'\n')
        __M_writer(unicode(template_hooks['extra_head']()))
        __M_writer(u'\n<link href=\'http://fonts.googleapis.com/css?family=Lato:400,700\' rel=\'stylesheet\' type=\'text/css\'>\n<link href=\'http://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic\' rel=\'stylesheet\' type=\'text/css\'>\n</head>\n<body>\n<div id="wrapper">\n  <div class="container">\n  <nav class="navigation">\n    <div class="clearfix">          \n      <h1 class="blog-title">\n          <a href="')
        __M_writer(unicode(blog_url))
        __M_writer(u'" title="')
        __M_writer(unicode(blog_title))
        __M_writer(u'">')
        __M_writer(unicode(blog_title))
        __M_writer(u'</a>\n      </h1>\n      <ul class="nav-list">\n')
        for url, text in navigation_links[lang]:
            __M_writer(u'          <li class="nav-list-item"><a href="')
            __M_writer(unicode(rel_link(permalink, url)))
            __M_writer(u'">')
            __M_writer(unicode(text))
            __M_writer(u'</a>\n            ')
            __M_writer(unicode(template_hooks['menu']()))
            __M_writer(u'\n            ')
            __M_writer(unicode(template_hooks['menu_alt']()))
            __M_writer(u'\n')
        __M_writer(u'      </ul>\n    </div>\n  </nav><!-- #primary .theme_sidebar -->\n        <div class="content">\n            <div id="header">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'belowtitle'):
            context['self'].belowtitle(**pageargs)
        

        __M_writer(u'\n            </div>\n        <div class="hfeed">\n            <!--Body content-->\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n            <!--End of body content-->\n        </div><!-- .hfeed -->\n    </div><!-- #content -->\n<footer class="footer">\n  <small>\n    ')
        __M_writer(unicode(content_footer))
        __M_writer(u'\n    ')
        __M_writer(unicode(template_hooks['page_footer']()))
        __M_writer(u'\n  </small>\n</footer><!-- #footer -->\n</div><!-- #container -->\n\n\n</div><!-- #wrapper -->\n    ')
        __M_writer(unicode(body_end))
        __M_writer(u'\n    ')
        __M_writer(unicode(template_hooks['body_end']()))
        __M_writer(u'\n    ')
        __M_writer(unicode(base.late_load_js()))
        __M_writer(u'\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_belowtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        def belowtitle():
            return render_belowtitle(context)
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        if len(translations) > 1:
            __M_writer(u'                <small>\n                    ')
            __M_writer(unicode(messages("Also available in:")))
            __M_writer(u'&nbsp;\n')
            for langname in translations.keys():
                if langname != lang:
                    __M_writer(u'                            <a href="')
                    __M_writer(unicode(_link("index", None, langname)))
                    __M_writer(u'">')
                    __M_writer(unicode(messages[langname]["LANGUAGE"]))
                    __M_writer(u'</a>\n')
            __M_writer(u'                </small>\n')
        __M_writer(u'                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 5, "150": 34, "134": 31, "147": 31, "148": 32, "149": 33, "22": 2, "151": 34, "152": 35, "25": 0, "154": 37, "155": 37, "156": 37, "157": 37, "158": 37, "159": 40, "160": 42, "166": 160, "53": 2, "54": 3, "55": 3, "56": 4, "57": 4, "62": 7, "63": 8, "64": 8, "65": 18, "66": 18, "67": 18, "68": 18, "69": 18, "70": 18, "71": 21, "72": 22, "73": 22, "74": 22, "75": 22, "76": 22, "77": 23, "78": 23, "79": 24, "80": 24, "81": 26, "86": 42, "153": 36, "91": 46, "92": 52, "93": 52, "94": 53, "95": 53, "96": 60, "97": 60, "98": 61, "99": 61, "100": 62, "101": 62, "107": 46, "120": 5}, "uri": "base.tmpl", "filename": "themes/lightning/templates/base.tmpl"}
__M_END_METADATA
"""
