# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1586749298.521284
_enable_loop = True
_template_filename = 'themes/lightning/templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'belowtitle', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def belowtitle():
            return render_belowtitle(context._locals(__M_locals))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(set_locale(lang)))
        __M_writer('\n')
        __M_writer(str(base.html_headstart()))
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        __M_writer(str(template_hooks['extra_head']()))
        __M_writer('\n\t<link href="https://fonts.googleapis.com/css?family=Lato:400,700" rel="stylesheet" type="text/css">\n\t<link href="https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic" rel="stylesheet" type="text/css">\n</head>\n<body>\n\t<a href="https://www.github.com/sahiga" class="github-corner" aria-label="View source on GitHub">\n\t\t<svg width="80" height="80" viewBox="0 0 250 250" class="github-corner-svg" aria-hidden="true">\n\t\t\t<path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"></path>\n\t\t\t<path\n\t\t\t\td="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2"\n\t\t\t\tfill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"></path>\n\t\t\t<path\n\t\t\t\td="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z"\n\t\t\t\tfill="currentColor" class="octo-body"></path>\n\t\t</svg>\n\t</a>\n<div id="wrapper">\n  <div class="container">\n  <nav class="navigation">\n    <div class="clearfix">          \n      <h1 class="blog-title">\n          <a href="/" title="')
        __M_writer(str(blog_title))
        __M_writer('">')
        __M_writer(str(blog_title))
        __M_writer('</a>\n      </h1>\n      <ul class="nav-list">\n')
        for url, text in navigation_links[lang]:
            __M_writer('          <li class="nav-list-item"><a href="')
            __M_writer(str(rel_link(permalink, url)))
            __M_writer('">')
            __M_writer(str(text))
            __M_writer('</a>\n            ')
            __M_writer(str(template_hooks['menu']()))
            __M_writer('\n            ')
            __M_writer(str(template_hooks['menu_alt']()))
            __M_writer('\n')
        __M_writer('      </ul>\n    </div>\n  </nav><!-- #primary .theme_sidebar -->\n        <div class="content">\n            <div id="header">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'belowtitle'):
            context['self'].belowtitle(**pageargs)
        

        __M_writer('\n            </div>\n        <div class="hfeed">\n            <!--Body content-->\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n            <!--End of body content-->\n        </div><!-- .hfeed -->\n    </div><!-- #content -->\n<footer class="footer">\n  <small>\n    ')
        __M_writer(str(content_footer))
        __M_writer('\n    ')
        __M_writer(str(template_hooks['page_footer']()))
        __M_writer('\n  </small>\n</footer><!-- #footer -->\n</div><!-- #container -->\n\n\n</div><!-- #wrapper -->\n    ')
        __M_writer(str(body_end))
        __M_writer('\n    ')
        __M_writer(str(template_hooks['body_end']()))
        __M_writer('\n    ')
        __M_writer(str(base.late_load_js()))
        __M_writer('\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_belowtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        def belowtitle():
            return render_belowtitle(context)
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            __M_writer('                <small>\n                    ')
            __M_writer(str(messages("Also available in:")))
            __M_writer('&nbsp;\n')
            for langname in translations.keys():
                if langname != lang:
                    __M_writer('                            <a href="')
                    __M_writer(str(_link("index", None, langname)))
                    __M_writer('">')
                    __M_writer(str(messages[langname]["LANGUAGE"]))
                    __M_writer('</a>\n')
            __M_writer('                </small>\n')
        __M_writer('                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/lightning/templates/base.tmpl", "uri": "base.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "53": 2, "54": 3, "55": 3, "56": 4, "57": 4, "62": 7, "63": 8, "64": 8, "65": 29, "66": 29, "67": 29, "68": 29, "69": 32, "70": 33, "71": 33, "72": 33, "73": 33, "74": 33, "75": 34, "76": 34, "77": 35, "78": 35, "79": 37, "84": 53, "89": 57, "90": 63, "91": 63, "92": 64, "93": 64, "94": 71, "95": 71, "96": 72, "97": 72, "98": 73, "99": 73, "105": 5, "113": 5, "119": 42, "132": 42, "133": 43, "134": 44, "135": 45, "136": 45, "137": 46, "138": 47, "139": 48, "140": 48, "141": 48, "142": 48, "143": 48, "144": 51, "145": 53, "151": 57, "164": 151}}
__M_END_METADATA
"""
