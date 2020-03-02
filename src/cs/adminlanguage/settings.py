# -*- coding: utf-8 -*-
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from zope import schema
from zope.interface import Interface
from cs.adminlanguage import _


class ISettings(Interface):
    """ Define settings data structure """

    adminLanguage = schema.TextLine(
        title=_(u"Editor language"),
        description=_(
            u"Type two letter language code and admins always use this language"
        ),
        required=False,
    )


class SettingsControlPanelForm(RegistryEditForm):
    schema = ISettings
    schema_prefix = "admin_language"
    label = _(u"Language Admin Settings")


SettingsPanelView = layout.wrap_form(SettingsControlPanelForm, ControlPanelFormWrapper)
