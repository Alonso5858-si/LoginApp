[app]
title = LoginApp
package.name = loginapp
package.domain = org.alonso
source.dir = .
version = 1.0
requirements = python3,kivy==2.3.0
orientation = portrait

[android]
api = 33
minapi = 21
ndk_version = 25b
build_tools_version = 34.0.0
skip_assets = 1  # Acelera el build

[buildozer]
log_level = 1
warn_on_root = 0
