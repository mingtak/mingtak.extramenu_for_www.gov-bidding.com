from zope.interface import Interface
from five import grok
"""
from plone.app.layout.viewlets.interfaces import *
 below viewlets manager can use.
IHTTPHeaders , IHtmlHead, IHtmlHeadLinks, IPortalTop,
IMainNavigation, IGlobalStatusMessage, IPortalHeader,
IToolbar, IAboveContent, IAboveContentTitle,
IDocumentActions,IBelowContentTitle, IAboveContentBody,
IBelowContentBody, IBelowContent, IPortalFooter, IScripts
"""
from mingtak.viewlets.viewlets.viewlets import IHomePage, IWebsiteTop

# Below define customized viewlet
grok.context(Interface)
grok.templatedir('templates')


class ExtraMainMenu(grok.Viewlet):
    grok.viewletmanager(IWebsiteTop)
