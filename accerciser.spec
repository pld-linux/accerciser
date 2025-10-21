Summary:	An interactive Python tool for querying accessibility information
Summary(pl.UTF-8):	Interaktywne narzędzie w Pythonie do pobierania informacji o dostępności
Name:		accerciser
Version:	3.48.0
Release:	1
License:	BSD
Group:		X11/Applications/Accessibility
Source0:	https://download.gnome.org/sources/accerciser/3.48/%{name}-%{version}.tar.xz
# Source0-md5:	11a4eb370315436701bf4bff47e127e8
URL:		https://wiki.gnome.org/Apps/Accerciser
BuildRequires:	AppStream
BuildRequires:	at-spi2-core-devel >= 2.5.2
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	gtk+3-devel >= 3.24
BuildRequires:	meson >= 1.0.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-pygobject3-devel >= 3.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	atk
Requires:	gdk-pixbuf2 >= 2.0
Requires:	gtk+3 >= 3.24
Requires:	librsvg >= 2.0
Requires:	libwnck >= 3.0
Requires:	pango
Requires:	python3-Xlib
Requires:	python3-ipython
Requires:	python3-modules >= 1:3.2
Requires:	python3-pyatspi
Requires:	python3-pycairo
Requires:	python3-pygobject3 >= 3.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An interactive Python accessibility explorer.

%description -l pl.UTF-8
Interaktywny eksplorator dostępności w Pythonie.

%package -n gnome-shell-extension-%{name}
Summary:	GNOME Shell extension for Accerciser
Summary(pl.UTF-8):	Rozszerzenie powłoki GNOME (GNOME Shell) dla Accercisera
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-shell >= 3

%description -n gnome-shell-extension-%{name}
GNOME Shell extension for Accerciser.

%description -n gnome-shell-extension-%{name} -l pl.UTF-8
Rozszerzenie powłoki GNOME (GNOME Shell) dla Accercisera.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog MAINTAINERS NEWS NOTICE README.md
%attr(755,root,root) %{_bindir}/accerciser
%{py3_sitescriptdir}/accerciser
%{_datadir}/accerciser
%{_datadir}/glib-2.0/schemas/org.a11y.Accerciser.gschema.xml
%{_datadir}/metainfo/org.gtk.accerciser.metainfo.xml
%{_desktopdir}/accerciser.desktop
%{_iconsdir}/hicolor/*x*/apps/accerciser.png
%{_iconsdir}/hicolor/scalable/apps/accerciser.svg
%{_iconsdir}/hicolor/symbolic/apps/accerciser-symbolic.svg
%{_mandir}/man1/accerciser.1*

%files -n gnome-shell-extension-%{name}
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/extensions/accerciser@accerciser.gnome.org
