[app]

title = LoginApp
package.name = loginapp
package.domain = org.alonso
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

android.permissions = 
android.api = 33
android.build_tools_version = 34.0.0
android.ndk = 25b
android.gradle_dependencies = 
android.gradle_plugin_version = 7.2.2


# Archivos incluidos
presplash.filename = %(source.dir)s/logo.png
icon.filename = %(source.dir)s/logo.png

[buildozer]

log_level = 2
warn_on_root = 1
