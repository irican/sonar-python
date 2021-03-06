############################################
###                Django                ###
############################################

from django.conf import settings, mysettings

settings.configure(DEBUG=True)  # Noncompliant
settings.configure(DEBUG_PROPAGATE_EXCEPTIONS=True)  # Noncompliant {{Make sure this debug feature is deactivated before delivering the code in production.}}
#                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
mysettings.configure(DEBUG=True)  # OK
settings.otherFn(DEBUG=True)  # OK

configure(DEBUG=True) # OK

def custom_config(config):
    settings.configure(default_settings=config, DEBUG=True)  # Noncompliant

settings.configure(DEBUG=False) # OK
settings.configure(OTHER=False) # OK