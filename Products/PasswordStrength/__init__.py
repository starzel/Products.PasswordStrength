# -*- coding: utf-8 -*-
from zope.i18nmessageid import MessageFactory

_ = MessageFactory("Products.PasswordStrength")

from AccessControl.Permissions import add_user_folders
from Products.PasswordStrength.plugin import manage_addPasswordStrength
from Products.PasswordStrength.plugin import manage_addPasswordStrengthForm
from Products.PasswordStrength.plugin import PasswordStrength
from Products.PluggableAuthService import registerMultiPlugin


def initialize(context):
    """Initialize the PasswordStrength plugin."""
    registerMultiPlugin(PasswordStrength.meta_type)

    context.registerClass(PasswordStrength,
                          permission=add_user_folders,
                          constructors=(manage_addPasswordStrengthForm,
                                        manage_addPasswordStrength),
                          # icon='www/noduplicatelogin.png',
                          visibility=None,
                          )

PROJECTNAME = "PasswordStrength"
