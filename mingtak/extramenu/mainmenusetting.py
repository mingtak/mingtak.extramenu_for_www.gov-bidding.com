from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from .mainmenu import IMainMenu
from plone.z3cform import layout
from z3c.form import form

class MainMenuSettingControlPanel(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = IMainMenu

MainMenuSettingControlPanelView = layout.wrap_form(MainMenuSettingControlPanel, ControlPanelFormWrapper)
MainMenuSettingControlPanelView.label = u"Main menu setting control panel"
