# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1420346476.335857
_enable_loop = True
_template_filename = u'/usr/local/lib/python2.7/dist-packages/nikola/data/themes/bootstrap/templates/base.tmpl'
_template_uri = u'base.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'sourcelink', u'extra_js', u'belowtitle']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'notes', context._clean_inheritance_tokens(), templateuri=u'annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'notes')] = ns

    ns = runtime.TemplateNamespace(u'base', context._clean_inheritance_tokens(), templateuri=u'base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        momentjs_locales = _import_ns.get('momentjs_locales', context.get('momentjs_locales', UNDEFINED))
        date_fanciness = _import_ns.get('date_fanciness', context.get('date_fanciness', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        show_sourcelink = _import_ns.get('show_sourcelink', context.get('show_sourcelink', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        js_date_format = _import_ns.get('js_date_format', context.get('js_date_format', UNDEFINED))
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        annotations = _import_ns.get('annotations', context.get('annotations', UNDEFINED))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        def belowtitle():
            return render_belowtitle(context._locals(__M_locals))
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        notes = _mako_get_namespace(context, 'notes')
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(unicode(set_locale(lang)))
        __M_writer(u'\n')
        __M_writer(unicode(base.html_headstart()))
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer(u'\n')
        __M_writer(unicode(template_hooks['extra_head']()))
        __M_writer(u'\n</head>\n<body>\n<a href="#content" class="sr-only sr-only-focusable">')
        __M_writer(unicode(messages("Skip to main content")))
        __M_writer(u'</a>\n\n<!-- Menubar -->\n\n<div class="navbar navbar-fixed-top" id="navbar">\n    <div class="navbar-inner">\n        <div class="container">\n\n        <!-- .btn-navbar is used as the toggle for collapsed navbar content -->\n        <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n        </a>\n\n            <a class="brand" href="')
        __M_writer(unicode(abs_link('/')))
        __M_writer(u'">\n')
        if logo_url:
            __M_writer(u'                <img src="')
            __M_writer(unicode(logo_url))
            __M_writer(u'" alt="')
            __M_writer(unicode(blog_title))
            __M_writer(u'" id="logo">\n')
        __M_writer(u'\n')
        if show_blog_title:
            __M_writer(u'                <span id="blog-title">')
            __M_writer(unicode(blog_title))
            __M_writer(u'</span>\n')
        __M_writer(u'            </a>\n            <!-- Everything you want hidden at 940px or less, place within here -->\n            <div class="nav-collapse collapse">\n                <ul class="nav">\n                    ')
        __M_writer(unicode(base.html_navigation_links()))
        __M_writer(u'\n                    ')
        __M_writer(unicode(template_hooks['menu']()))
        __M_writer(u'\n                </ul>\n')
        if search_form:
            __M_writer(u'                    ')
            __M_writer(unicode(search_form))
            __M_writer(u'\n')
        __M_writer(u'                <ul class="nav pull-right">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'belowtitle'):
            context['self'].belowtitle(**pageargs)
        

        __M_writer(u'\n')
        if show_sourcelink:
            __M_writer(u'                    <li>')
            if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
                context['self'].sourcelink(**pageargs)
            

            __M_writer(u'</li>\n')
        __M_writer(u'                ')
        __M_writer(unicode(template_hooks['menu_alt']()))
        __M_writer(u'\n                </ul>\n            </div>\n        </div>\n    </div>\n</div>\n<!-- End of Menubar -->\n<div class="container-fluid" id="content">\n    <!--Body content-->\n    <div class="row-fluid">\n    <div class="span2"></div>\n    <div class="span8">\n    ')
        __M_writer(unicode(template_hooks['page_header']()))
        __M_writer(u'\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n    </div>\n    </div>\n    <!--End of body content-->\n</div>\n<div class="footerbox">\n    ')
        __M_writer(unicode(content_footer))
        __M_writer(u'\n    ')
        __M_writer(unicode(template_hooks['page_footer']()))
        __M_writer(u'\n</div>\n')
        __M_writer(unicode(base.late_load_js()))
        __M_writer(u'\n    <script>jQuery("a.image-reference").colorbox({rel:"gal",maxWidth:"100%",maxHeight:"100%",scalePhotos:true});</script>\n    <!-- fancy dates -->\n    <script>\n    moment.locale("')
        __M_writer(unicode(momentjs_locales[lang]))
        __M_writer(u'");\n    fancydates(')
        __M_writer(unicode(date_fanciness))
        __M_writer(u', ')
        __M_writer(unicode(js_date_format))
        __M_writer(u');\n    </script>\n    <!-- end fancy dates -->\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer(u'\n')
        if annotations and post and not post.meta('noannotations'):
            __M_writer(u'        ')
            __M_writer(unicode(notes.code()))
            __M_writer(u'\n')
        elif not annotations and post and post.meta('annotations'):
            __M_writer(u'        ')
            __M_writer(unicode(notes.code()))
            __M_writer(u'\n')
        __M_writer(unicode(body_end))
        __M_writer(u'\n')
        __M_writer(unicode(template_hooks['body_end']()))
        __M_writer(u'\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
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
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_belowtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        def belowtitle():
            return render_belowtitle(context)
        base = _mako_get_namespace(context, 'base')
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        if len(translations) > 1:
            __M_writer(u'                    <li>')
            __M_writer(unicode(base.html_translations()))
            __M_writer(u'</li>\n')
        __M_writer(u'                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 73, "129": 74, "130": 74, "131": 76, "132": 76, "133": 80, "134": 80, "135": 81, "136": 81, "137": 81, "138": 81, "190": 52, "143": 84, "144": 85, "145": 86, "146": 86, "147": 86, "148": 87, "149": 88, "22": 3, "151": 88, "152": 90, "25": 2, "154": 91, "155": 91, "28": 0, "218": 46, "150": 88, "230": 46, "161": 67, "241": 235, "175": 6, "184": 6, "153": 90, "67": 2, "68": 3, "69": 4, "70": 4, "71": 5, "72": 5, "204": 84, "77": 8, "78": 9, "79": 9, "80": 12, "81": 12, "82": 27, "83": 27, "84": 28, "85": 29, "86": 29, "87": 29, "88": 29, "89": 29, "90": 31, "91": 32, "92": 33, "93": 33, "94": 33, "95": 35, "96": 39, "97": 39, "98": 40, "99": 40, "100": 42, "101": 43, "102": 43, "103": 43, "104": 45, "233": 48, "234": 48, "231": 47, "235": 50, "109": 50, "110": 51, "111": 52, "232": 48, "116": 52, "117": 54, "118": 54, "119": 54, "120": 66, "121": 66, "126": 67, "127": 73}, "uri": "base.tmpl", "filename": "/usr/local/lib/python2.7/dist-packages/nikola/data/themes/bootstrap/templates/base.tmpl"}
__M_END_METADATA
"""
