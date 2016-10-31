'''
Google+ SignIn
==============
'''


__all__ = ('GMap', 'GMapException', 'run_on_ui_thread')

from kivy.uix.widget import Widget
from kivy.clock import Clock
from android.runnable import run_on_ui_thread
from jnius import autoclass, cast, PythonJavaClass, java_method
from kivy.properties import ObjectProperty, BooleanProperty
from kivy.logger import Logger

Auth = autoclass('com.google.android.gms.auth.api.Auth')
GoogleSighInAccount = autoclass('com.google.android.gms.auth.api.signin.GoogleSignInAccount')
GoogleSignInOptions = autoclass('com.google.android.gms.auth.api.signin.GoogleSignInOptions')
GoogleSignInResult = autoclass('com.google.android.gms.auth.api.signin.GoogleSignInResult')
ConnectionResult = autoclass('com.google.android.gms.common.ConnectionResult')
SignInButton = autoclass('com.google.android.gms.common.SignInButton')
GoogleApiClient = autoclass('com.google.android.gms.common.api.GoogleApiClient')
OptionalPendingResult = autoclass('com.google.android.gms.common.api.OptionalPendingResult')
ResultCallback = autoclass('com.google.android.gms.common.api.ResultCallback')
Status = autoclass('com.google.android.gms.common.api.Status')

