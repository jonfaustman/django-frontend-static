from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def djfrontendh5bp_css(v):
    """ Returns HTML5 Boilerplate CSS file.
    """
    return '<link rel="stylesheet" href="%sdjfrontendstatic/css/h5bp/%s/h5bp.css">' % (settings.STATIC_URL, v)


@register.simple_tag
def djfrontendnormalize(v):
    """ Returns Normalize CSS file.
    Included in HTML5 Boilerplate.
    """
    return '<link rel="stylesheet" href="%sdjfrontendstatic/css/normalize/%s/normalize.css">' % (settings.STATIC_URL, v)


@register.simple_tag
def djfrontendmodernizr(v):
    """ Returns Modernizr JavaScript file according to version number.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file.
    Included in HTML5 Boilerplate.
    """
    if getattr(settings, 'TEMPLATE_DEBUG',):
        return '<script src="%sdjfrontendstatic/js/modernizr/%s/modernizr.js"></script>' % (settings.STATIC_URL, v)
    else:
        if hasattr(settings, 'DJFRONTEND_STATIC_URL'):
            return '<script src="%sdjfrontendstatic/js/modernizr/%s/modernizr.min.js"></script>' % (settings.DJFRONTEND_STATIC_URL, v)
        else:
            return '<script src="%sdjfrontendstatic/js/modernizr/%s/modernizr.min.js"></script>' % (settings.STATIC_URL, v)


@register.simple_tag
def djfrontendjquery(v):
    """ Returns jQuery JavaScript file according to version number.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file from Google CDN with local fallback.
    Included in HTML5 Boilerplate.
    """
    if getattr(settings, 'TEMPLATE_DEBUG',):
        return '<script src="%sdjfrontendstatic/js/jquery/%s/jquery.js"></script>' % (settings.STATIC_URL, v)
    else:
        if hasattr(settings, 'DJFRONTEND_STATIC_URL'):
            output=[
                '<script src="//ajax.googleapis.com/ajax/libs/jquery/%s/jquery.min.js"></script>' % v,
                '<script>window.jQuery || document.write(\'<script src="%sdjfrontendstatic/js/jquery/%s/jquery.min.js"><\/script>\')</script>' % (settings.DJFRONTEND_STATIC_URL, v)
            ]
        else:
            output=[
                '<script src="//ajax.googleapis.com/ajax/libs/jquery/%s/jquery.min.js"></script>' % v,
                '<script>window.jQuery || document.write(\'<script src="%sdjfrontendstatic/js/jquery/%s/jquery.min.js"><\/script>\')</script>' % (settings.STATIC_URL, v)
            ]
        return '\n'.join(output)


@register.simple_tag
def djfrontendjquery_datatables(v):
    """ Returns the jQuery dataTables plugin file according to version number.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file.
    """
    if getattr(settings, 'TEMPLATE_DEBUG',):
        return '<script src="%sdjfrontendstatic/js/jquery/jquery.dataTables/%s/jquery.dataTables.js"></script>' % (settings.STATIC_URL, v)
    else:
        if hasattr(settings, 'DJFRONTEND_STATIC_URL'):
            return '<script src="%sdjfrontendstatic/js/jquery/jquery.dataTables/%s/jquery.dataTables.min.js"></script>' % (settings.DJFRONTEND_STATIC_URL, v)
        else:
            return '<script src="%sdjfrontendstatic/js/jquery/jquery.dataTables/%s/jquery.dataTables.min.js"></script>' % (settings.STATIC_URL, v)


@register.simple_tag
def djfrontendjquery_datatables_css(v):
    """ Returns the jQuery dataTables CSS file according to version number.
    """
    if getattr(settings, 'TEMPLATE_DEBUG',):
        return '<script src="%sdjfrontendstatic/css/jquery/jquery.dataTables/%s/jquery.dataTables.css"></script>' % (settings.STATIC_URL, v)
    else:
        if hasattr(settings, 'DJFRONTEND_STATIC_URL'):
            return '<script src="%sdjfrontendstatic/css/jquery/jquery.dataTables/%s/jquery.dataTables.css"></script>' % (settings.DJFRONTEND_STATIC_URL, v)


@register.simple_tag
def djfrontendjquery_formset(v):
    """ Returns the jQuery Formset plugin file according to version number.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file.
    """
    if getattr(settings, 'TEMPLATE_DEBUG',):
        return '<script src="%sdjfrontendstatic/js/jquery/jquery.formset/%s/jquery.formset.js"></script>' % (settings.STATIC_URL, v)
    else:
        if hasattr(settings, 'DJFRONTEND_STATIC_URL'):
            return '<script src="%sdjfrontendstatic/js/jquery/jquery.formset/%s/jquery.formset.min.js"></script>' % (settings.DJFRONTEND_STATIC_URL, v)
        else:
            return '<script src="%sdjfrontendstatic/js/jquery/jquery.dataTables/%s/jquery.formset.min.js"></script>' % (settings.STATIC_URL, v)


@register.simple_tag
def djfrontendjquery_smoothscroll(v):
    """ Returns the jQuery Smooth Scroll plugin file according to version number.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file.
    """
    if getattr(settings, 'TEMPLATE_DEBUG',):
        return '<script src="%sdjfrontendstatic/js/jquery/jquery.smooth-scroll/%s/jquery.smooth-scroll.js"></script>' % (settings.STATIC_URL, v)
    else:
        if hasattr(settings, 'DJFRONTEND_STATIC_URL'):
            return '<script src="%sdjfrontendstatic/js/jquery/jquery.smooth-scroll/%s/jquery.smooth-scroll.min.js"></script>' % (settings.DJFRONTEND_STATIC_URL, v)
        else:
            return '<script src="%sdjfrontendstatic/js/jquery/jquery.smooth-scroll/%s/jquery.smooth-scroll.min.js"></script>' % (settings.STATIC_URL, v)


@register.simple_tag
def djfrontendjqueryui(v):
    """ Returns the jQuery Smooth Scroll plugin file according to version number.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file.
    """
    if getattr(settings, 'TEMPLATE_DEBUG',):
        return '<script src="%sdjfrontendstatic/js/jquery/jqueryui/%s/jquery-ui.js"></script>' % (settings.STATIC_URL, v)
    else:
        if hasattr(settings, 'DJFRONTEND_STATIC_URL'):
            return '<script src="%sdjfrontendstatic/js/jquery/jquery-ui/%s/jquery-ui.min.js"></script>' % (settings.DJFRONTEND_STATIC_URL, v)
        else:
            return '<script src="%sdjfrontendstatic/js/jquery/jquery-ui/%s/jquery-ui.min.js"></script>' % (settings.STATIC_URL, v)


@register.simple_tag
def djfrontendtwbs_css():
    """ Returns Twitter Bootstrap CSS file.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file.
    """
    if getattr(settings, 'TEMPLATE_DEBUG',):
        return '<link rel="stylesheet" href="%sdjfrontendstatic/css/bootstrap/bootstrap.css">' % settings.STATIC_URL
    else:
        return '<link rel="stylesheet" href="%sdjfrontendstatic/css/bootstrap/bootstrap.min.css">' % settings.STATIC_URL


@register.simple_tag
def djfrontendtwbs_responsive_css():
    """ Returns Twitter Bootstrap responsive CSS file.
    TEMPLATE_DEBUG returns full file, otherwise returns minified file.
    """
    if getattr(settings, 'TEMPLATE_DEBUG',):
        return '<link rel="stylesheet" href="%sdjfrontendstatic/css/bootstrap/bootstrap-responsive.css">' % settings.STATIC_URL
    else:
        return '<link rel="stylesheet" href="%sdjfrontendstatic/css/bootstrap/bootstrap-responsive.min.css">' % settings.STATIC_URL


@register.simple_tag
def djfrontendga(ua):
    """ Returns Google Analytics asynchronous snippet.
    Use DJANGOFRONTEND_GA_SETDOMAINNAME to set domain for multiple, or cross-domain tracking.
    Set DJANGOFRONTEND_GA_SETALLOWLINKER to use _setAllowLinker method on target site for cross-domain tracking.
    Included in HTML5 Boilerplate.
    """
    if getattr(settings, 'TEMPLATE_DEBUG',):
        return ''
    else:
        if hasattr(settings, 'DJANGOFRONTEND_GA_SETDOMAINNAME',):
            if hasattr(settings, 'DJANGOFRONTEND_GA_SETALLOWLINKER',):
                return '<script>var _gaq=[["_setAccount","%s"],["_setDomainName","%s"],["_setAllowLinker", true],["_trackPageview"]];(function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];g.src="//www.google-analytics.com/ga.js";s.parentNode.insertBefore(g,s)}(document,"script"));</script>' % (ua, settings.DJANGOFRONTEND_GA_SETDOMAINNAME)
            else:
                return '<script>var _gaq=[["_setAccount","%s"],["_setDomainName","%s"],["_trackPageview"]];(function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];g.src="//www.google-analytics.com/ga.js";s.parentNode.insertBefore(g,s)}(document,"script"));</script>' % (ua, settings.DJANGOFRONTEND_GA_SETDOMAINNAME)
        else:
            return '<script>var _gaq=[["_setAccount","%s"],["_trackPageview"]];(function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];g.src="//www.google-analytics.com/ga.js";s.parentNode.insertBefore(g,s)}(document,"script"));</script>' % ua
@register.tag(name='djfrontendtwbs_js')
def do_djfrontendtwbs_js(parser, token):
    """ Returns Twitter Bootstrap (2.3.2) JavaScript file(s).
    all returns concatenated file; full file for TEMPLATE_DEBUG, minified otherwise.
    Other choice are:
        affix,
        alert,
        button,
        carousel,
        collapse,
        dropdown,
        modal,
        popover (adds tooltip if not included),
        scrollspy,
        tab,
        tooltip,
        transition,
        typeahead.
    Individual files are not minified.
    """
    return BootstrapJSNode(token.split_contents()[1:])


SCRIPT_TAG = '<script src="%sdjfrontendstatic/js/twbs/bootstrap-%s.js"></script>'

class BootstrapJSNode(template.Node):

    def __init__(self, args):
        self.args = set(args)

    def render(self, context):
        if 'all' in self.args:
            if getattr(settings, 'TEMPLATE_DEBUG', ):
                return '<script src="%sdjfrontendstatic/js/twbs/bootstrap.js"></script>' % settings.STATIC_URL
            else:
                if hasattr(settings, 'DJFRONTEND_STATIC_URL'):
                    return '<script src="%sdjfrontendstatic/js/twbs/bootstrap.min.js"></script>' % settings.DJFRONTEND_STATIC_URL
                else:
                    return '<script src="%sdjfrontendstatic/js/twbs/bootstrap.min.js"></script>' % settings.STATIC_URL
        else:
            # popover requires tooltip
            if 'popover' in self.args:
                self.args.add('tooltip')
            if hasattr(settings, 'DJFRONTEND_STATIC_URL'):
                tags = [SCRIPT_TAG % (settings.DJFRONTEND_STATIC_URL, tag) for tag in self.args]
            else:
                tags = [SCRIPT_TAG % (settings.STATIC_URL, tag) for tag in self.args]
            return '\n'.join(tags)


@register.simple_tag
def djfrontendios_fix():
    """ Returns the iOS-Orientationchange-Fix.
    """
    return '<script>/*! A fix for the iOS orientationchange zoom bug. Script by @scottjehl, rebound by @wilto.MIT / GPLv2 License.*/(function(a){function m(){d.setAttribute("content",g),h=!0}function n(){d.setAttribute("content",f),h=!1}function o(b){l=b.accelerationIncludingGravity,i=Math.abs(l.x),j=Math.abs(l.y),k=Math.abs(l.z),(!a.orientation||a.orientation===180)&&(i>7||(k>6&&j<8||k<8&&j>6)&&i>5)?h&&n():h||m()}var b=navigator.userAgent;if(!(/iPhone|iPad|iPod/.test(navigator.platform)&&/OS [1-5]_[0-9_]* like Mac OS X/i.test(b)&&b.indexOf("AppleWebKit")>-1))return;var c=a.document;if(!c.querySelector)return;var d=c.querySelector("meta[name=viewport]"),e=d&&d.getAttribute("content"),f=e+",maximum-scale=1",g=e+",maximum-scale=10",h=!0,i,j,k,l;if(!d)return;a.addEventListener("orientationchange",m,!1),a.addEventListener("devicemotion",o,!1)})(this);</script>'