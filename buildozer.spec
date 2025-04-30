[app]
title = LoginApp
package.name = loginapp
package.domain = org.alonso
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.3.0  # Versión específica de Kivy
orientation = portrait
fullscreen = 0

# Configuración Android (actualizada)
android.permissions = INTERNET  # Añade los permisos necesarios
android.api = 33
android.minapi = 21
android.ndk_version = 25b  # Usa ndk_version en lugar de ndk
android.build_tools_version = 34.0.0
android.gradle_plugin_version = 7.2.2

# Optimización de builds
android.allow_backup = false
android.adaptive_icon = false

# Assets
presplash.filename = %(source.dir)s/logo.png
icon.filename = %(source.dir)s/logo.png

[buildozer]
log_level = 2
warn_on_root = 1
