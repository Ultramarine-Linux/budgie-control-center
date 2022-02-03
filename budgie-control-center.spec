%undefine       _disable_source_fetch
Name:           budgie-control-center
Version:        0.3
Release:        1%{?dist}
Summary:        fork of GNOME Control Center for the Budgie 10 Series.

License:        GPLv2+
URL:            https://github.com/BuddiesOfBudgie/budgie-control-center
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        https://gitlab.gnome.org/GNOME/libgnome-volume-control/-/archive/7a621180b46421e356b33972e3446775a504139c/libgnome-volume-control-7a621180b46421e356b33972e3446775a504139c.tar.gz
Source2:        https://gitlab.gnome.org/GNOME/libhandy/-/archive/7b38a860ffcec6c2ad28153358cc3d037ddb618f/libhandy-7b38a860ffcec6c2ad28153358cc3d037ddb618f.tar.gz

BuildRequires:  chrpath
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl libxslt
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(cheese)
BuildRequires:  pkgconfig(cheese-gtk)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(colord-gtk)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-wayland-3.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gnome-settings-daemon)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(goa-backend-1.0)
BuildRequires:  pkgconfig(grilo-0.3)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnma)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(malcontent-0)
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(udisks2)
%ifnarch s390 s390x
BuildRequires:  pkgconfig(gnome-bluetooth-1.0)
BuildRequires:  pkgconfig(libwacom)
%endif

# Versioned library deps
Requires: cheese-libs%{?_isa}
Requires: glib2%{?_isa}
Requires: gnome-desktop3%{?_isa}
Requires: gnome-online-accounts%{?_isa}
Requires: gnome-settings-daemon%{?_isa}
Requires: gsettings-desktop-schemas%{?_isa}
Requires: gtk3%{?_isa}
Requires: upower%{?_isa}
%ifnarch s390 s390x
Requires: gnome-bluetooth%{?_isa}
%endif

Requires: %{name}-filesystem = %{version}-%{release}
# For user accounts
Requires: accountsservice
Requires: alsa-lib
# For the thunderbolt panel
Recommends: bolt
# For the color panel
Requires: colord
# For the printers panel
Requires: cups-pk-helper
Requires: dbus
# For the info/details panel
Requires: glx-utils
# For the user languages
Requires: iso-codes
# For parental controls support
Requires: malcontent
Requires: malcontent-control
# For the network panel
Recommends: NetworkManager-wifi
Recommends: nm-connection-editor
# For Show Details in the color panel
Recommends: gnome-color-manager
# For the sharing panel
Recommends: gnome-remote-desktop
%if 0%{?fedora}
Recommends: rygel
%endif
# For the info/details panel
Recommends: switcheroo-control
# For the keyboard panel
Requires: /usr/bin/gkbd-keyboard-display
%if 0%{?fedora} >= 35 || 0%{?rhel} >= 9
# For the power panel
Recommends: power-profiles-daemon
%endif

# Renamed in F28
Provides: control-center = 1:%{version}-%{release}
Provides: control-center%{?_isa} = 1:%{version}-%{release}
Obsoletes: control-center < 1:%{version}-%{release}


%description
Budgie Control Center is a fork of GNOME Settings / GNOME Control Center with the intent of providing a simplified list of settings that are applicable to the Budgie 10 series, along with any small quality-of-life settings.


%package filesystem
Summary: Budgie Control Center directories
# NOTE: this is an "inverse dep" subpackage. It gets pulled in
# NOTE: by the main package and MUST not depend on the main package
BuildArch: noarch
# Renamed in F28
Provides: control-center-filesystem = 1:%{version}-%{release}
Obsoletes: control-center-filesystem < 1:%{version}-%{release}

%description filesystem
The Budgie control-center provides a number of extension points
for applications. This package contains directories where applications
can install configuration files that are picked up by the control-center
utilities.



%prep
%autosetup
# install subprojects
tar -xf %{SOURCE1} -C subprojects/
mv subprojects/libgnome-volume-control-*/* subprojects/gvc
rm -rf subprojects/libgnome-volume-control-*
tar -xf %{SOURCE2} -C subprojects/
mv subprojects/libhandy-*/* subprojects/libhandy
rm -rf subprojects/libhandy-*


%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT
%meson_install


%files
%license LICENSE
%{_bindir}/budgie-control-center
%{_libexecdir}/budgie-cc-remote-login-helper
%{_libexecdir}/budgie-control-center-print-renderer
%{_datadir}/applications/budgie-applications-panel.desktop
%{_datadir}/applications/budgie-background-panel.desktop
%{_datadir}/applications/budgie-bluetooth-panel.desktop
%{_datadir}/applications/budgie-camera-panel.desktop
%{_datadir}/applications/budgie-color-panel.desktop
%{_datadir}/applications/budgie-control-center.desktop
%{_datadir}/applications/budgie-datetime-panel.desktop
%{_datadir}/applications/budgie-default-apps-panel.desktop
%{_datadir}/applications/budgie-diagnostics-panel.desktop
%{_datadir}/applications/budgie-display-panel.desktop
%{_datadir}/applications/budgie-info-overview-panel.desktop
%{_datadir}/applications/budgie-keyboard-panel.desktop
%{_datadir}/applications/budgie-location-panel.desktop
%{_datadir}/applications/budgie-microphone-panel.desktop
%{_datadir}/applications/budgie-mouse-panel.desktop
%{_datadir}/applications/budgie-multitasking-panel.desktop
%{_datadir}/applications/budgie-network-panel.desktop
%{_datadir}/applications/budgie-notifications-panel.desktop
%{_datadir}/applications/budgie-online-accounts-panel.desktop
%{_datadir}/applications/budgie-power-panel.desktop
%{_datadir}/applications/budgie-printers-panel.desktop
%{_datadir}/applications/budgie-region-panel.desktop
%{_datadir}/applications/budgie-removable-media-panel.desktop
%{_datadir}/applications/budgie-sharing-panel.desktop
%{_datadir}/applications/budgie-sound-panel.desktop
%{_datadir}/applications/budgie-thunderbolt-panel.desktop
%{_datadir}/applications/budgie-universal-access-panel.desktop
%{_datadir}/applications/budgie-usage-panel.desktop
%{_datadir}/applications/budgie-user-accounts-panel.desktop
%{_datadir}/applications/budgie-wacom-panel.desktop
%{_datadir}/applications/budgie-wifi-panel.desktop
%{_datadir}/applications/budgie-wwan-panel.desktop
%{_datadir}/bash-completion/completions/budgie-control-center
%{_datadir}/dbus-1/services/org.buddiesofbudgie.ControlCenter.service
%{_datadir}/glib-2.0/schemas/org.buddiesofbudgie.ControlCenter.gschema.xml
%{_datadir}/icons/hicolor/16x16/apps/boa-panel.png
%{_datadir}/icons/hicolor/16x16/apps/budgie-power-manager.png
%{_datadir}/icons/hicolor/16x16/apps/budgie-preferences-color.png
%{_datadir}/icons/hicolor/16x16/apps/budgie-preferences-desktop-display.png
%{_datadir}/icons/hicolor/16x16/apps/budgie-preferences-system-time.png
%{_datadir}/icons/hicolor/22x22/apps/boa-panel.png
%{_datadir}/icons/hicolor/22x22/apps/budgie-power-manager.png
%{_datadir}/icons/hicolor/22x22/apps/budgie-preferences-color.png
%{_datadir}/icons/hicolor/22x22/apps/budgie-preferences-desktop-display.png
%{_datadir}/icons/hicolor/22x22/apps/budgie-preferences-system-time.png
%{_datadir}/icons/hicolor/24x24/apps/boa-panel.png
%{_datadir}/icons/hicolor/24x24/apps/budgie-power-manager.png
%{_datadir}/icons/hicolor/24x24/apps/budgie-preferences-color.png
%{_datadir}/icons/hicolor/24x24/apps/budgie-preferences-desktop-display.png
%{_datadir}/icons/hicolor/256x256/apps/boa-panel.png
%{_datadir}/icons/hicolor/256x256/apps/budgie-power-manager.png
%{_datadir}/icons/hicolor/256x256/apps/budgie-preferences-color.png
%{_datadir}/icons/hicolor/256x256/apps/budgie-preferences-system-time.png
%{_datadir}/icons/hicolor/32x32/apps/boa-panel.png
%{_datadir}/icons/hicolor/32x32/apps/budgie-power-manager.png
%{_datadir}/icons/hicolor/32x32/apps/budgie-preferences-color.png
%{_datadir}/icons/hicolor/32x32/apps/budgie-preferences-desktop-display.png
%{_datadir}/icons/hicolor/32x32/apps/budgie-preferences-system-time.png
%{_datadir}/icons/hicolor/48x48/apps/boa-panel.png
%{_datadir}/icons/hicolor/48x48/apps/budgie-power-manager.png
%{_datadir}/icons/hicolor/48x48/apps/budgie-preferences-color.png
%{_datadir}/icons/hicolor/48x48/apps/budgie-preferences-system-time.png
%{_datadir}/icons/hicolor/64x64/apps/budgie-preferences-color.png
%{_datadir}/icons/hicolor/scalable/apps/budgie-preferences-color.svg
%{_datadir}/icons/hicolor/scalable/apps/budgie-preferences-desktop-display.svg
%{_datadir}/icons/hicolor/scalable/apps/budgie-preferences-system-time.svg
%{_datadir}/icons/hicolor/scalable/apps/org.buddiesofbudgie.Settings-multitasking-symbolic.svg
%{_datadir}/icons/hicolor/scalable/apps/org.buddiesofbudgie.Settings.Devel.svg
%{_datadir}/icons/hicolor/scalable/apps/org.buddiesofbudgie.Settings.svg
%{_datadir}/icons/hicolor/scalable/categories/budgie-slideshow-symbolic.svg
%{_datadir}/icons/hicolor/scalable/emblems/budgie-slideshow-emblem.svg
%{_datadir}/icons/hicolor/scalable/status/budgie-info-symbolic.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.buddiesofbudgie.Settings-symbolic.svg
%{_datadir}/locale/*/LC_MESSAGES/budgie-control-center*
%{_datadir}/metainfo/budgie-control-center.appdata.xml
%{_datadir}/pixmaps/budgie-logo.png
%{_datadir}/pkgconfig/budgie-keybindings.pc
%{_datadir}/polkit-1/actions/org.buddiesofbudgie.controlcenter.datetime.policy
%{_datadir}/polkit-1/actions/org.buddiesofbudgie.controlcenter.remote-login-helper.policy
%{_datadir}/polkit-1/actions/org.buddiesofbudgie.controlcenter.user-accounts.policy
%{_datadir}/polkit-1/rules.d/budgie-control-center.rules

%files filesystem
%{_datadir}/budgie-control-center/
%{_datadir}/sounds/budgie/
%{_datadir}/pixmaps/budgie-faces/

%changelog
* Thu Feb 03 2022 Cappy Ishihara <cappy@cappuchino.xyz>
- Initial Build
