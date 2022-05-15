%define gnome_online_accounts_version 3.25.3
%define glib2_version 2.56.0
%define gnome_desktop_version 3.35.4
%define gsd_version 3.35.0
%define gsettings_desktop_schemas_version 3.37.1
%define upower_version 0.99.8
%define gtk3_version 3.22.20
%define cheese_version 3.28.0
%define gnome_bluetooth_version 3.18.2
%define nm_version 1.24
%undefine _disable_source_fetch

%global commit 314132131a46b9ba57b68848c5b32a475034c917
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           budgie-control-center
Version:        1.0.2
Release:        1%{?dist}
Summary:        Utilities to configure the Budgie desktop

License:        GPLv2+ and CC-BY-SA
URL:            https://github.com/BuddiesOfBudgie/budgie-control-center
Source0:        https://github.com/BuddiesOfBudgie/budgie-control-center/archive/refs/tags/v%{version}.tar.gz
Source4:        https://gitlab.gnome.org/GNOME/libgnome-volume-control/-/archive/c5ab6037f460406ac9799b1e5765de3ce0097a8b/libgnome-volume-control-c5ab6037f460406ac9799b1e5765de3ce0097a8b.tar.gz
# https://gitlab.gnome.org/GNOME/budgie-control-center/-/merge_requests/965
#Patch0:         distro-logo.patch

BuildRequires:  chrpath
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl libxslt
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(cheese) >= %{cheese_version}
BuildRequires:  pkgconfig(cheese-gtk)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(colord-gtk)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-wayland-3.0)
BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= %{gnome_desktop_version}
BuildRequires:  pkgconfig(gnome-settings-daemon) >= %{gsd_version}
BuildRequires:  pkgconfig(goa-1.0) >= %{gnome_online_accounts_version}
BuildRequires:  pkgconfig(goa-backend-1.0)
BuildRequires:  pkgconfig(grilo-0.3)
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= %{gsettings_desktop_schemas_version}
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libnm) >= %{nm_version}
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
BuildRequires:  pkgconfig(upower-glib) >= %{upower_version}
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(udisks2)
%ifnarch s390 s390x
BuildRequires:  pkgconfig(gnome-bluetooth-1.0) >= %{gnome_bluetooth_version}
BuildRequires:  pkgconfig(libwacom)
%endif

# Versioned library deps
Requires: cheese-libs%{?_isa} >= %{cheese_version}
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gnome-desktop3%{?_isa} >= %{gnome_desktop_version}
Requires: gnome-online-accounts%{?_isa} >= %{gnome_online_accounts_version}
Requires: gnome-settings-daemon%{?_isa} >= %{gsd_version}
Requires: gsettings-desktop-schemas%{?_isa} >= %{gsettings_desktop_schemas_version}
Requires: gtk3%{?_isa} >= %{gtk3_version}
Requires: upower%{?_isa} >= %{upower_version}
%ifnarch s390 s390x
Requires: gnome-bluetooth%{?_isa} >= 1:%{gnome_bluetooth_version}
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
This package contains configuration utilities for the Budgie desktop, which
allow to configure accessibility options, desktop fonts, keyboard and mouse
properties, sound setup, desktop theme and background, user interface
properties, screen resolution, and other settings.

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
%autosetup -p1 -n budgie-control-center-%{version}

tar -xvzf %{SOURCE4} --strip-components=1 --no-same-owner -C subprojects/gvc

rm -rf subprojects/libhandy

%build
%meson \
  -Ddocumentation=true \
#%if 0%{?fedora}
#  -Ddistributor_logo=%{_datadir}/pixmaps/fedora_logo_med.png \
#  -Ddark_mode_distributor_logo=%{_datadir}/pixmaps/fedora_whitelogo_med.png \
#  -Dmalcontent=true \
#%endif
#%if 0%{?rhel}
#  -Ddistributor_logo=%{_datadir}/pixmaps/fedora-logo.png \
#  -Ddark_mode_distributor_logo=%{_datadir}/pixmaps/system-logo-white.png \
#%endif
  %{nil}
%meson_build

%install
%meson_install

# We do want this
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties

# We don't want these
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnome/autostart
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnome/cursor-fonts

# Remove rpath
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/budgie-control-center

%find_lang %{name} --all-name --with-gnome

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/budgie-control-center
%{_datadir}/applications/*.desktop
%{_datadir}/bash-completion/completions/budgie-control-center
#%{_datadir}/dbus-1/services/org.buddiesofbudgie.ControlCenter.SearchProvider.service
%{_datadir}/dbus-1/services/org.buddiesofbudgie.ControlCenter.service
#%{_datadir}/gettext/
%{_datadir}/glib-2.0/schemas/org.buddiesofbudgie.ControlCenter.gschema.xml
%{_datadir}/budgie-control-center/keybindings/*.xml
%{_datadir}/budgie-control-center/pixmaps
#%{_datadir}/gnome-shell/search-providers/org.buddiesofbudgie.ControlCenter.search-provider.ini
#%{_datadir}/icons/budgie-logo-text*.svg
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/man/man1/budgie-control-center.1*
%{_metainfodir}/budgie-control-center.appdata.xml
%{_datadir}/pixmaps/budgie-faces
%{_datadir}/pixmaps/budgie-logo.png
%{_datadir}/pkgconfig/budgie-keybindings.pc
%{_datadir}/polkit-1/actions/org.buddiesofbudgie.controlcenter.*.policy
%{_datadir}/polkit-1/rules.d/budgie-control-center.rules
%{_datadir}/sounds/budgie/default/*/*.ogg
%{_libexecdir}/budgie-cc-remote-login-helper
#%{_libexecdir}/budgie-control-center-goa-helper
#%{_libexecdir}/budgie-control-center-search-provider
%{_libexecdir}/budgie-control-center-print-renderer

%files filesystem
%dir %{_datadir}/budgie-control-center
%dir %{_datadir}/budgie-control-center/keybindings
%dir %{_datadir}/gnome/wm-properties

%changelog
* Tue Feb 22 2022 Cappy Ishihara <cappy@cappuchino.xyz> - 42~beta-1.um35
- Initial release