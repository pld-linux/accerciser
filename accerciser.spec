Summary:	An interactive Python tool for querying accessibility information
Summary(pl.UTF-8):	Interaktywne narzędzie w Pythonie do pobierania informacji o dostępności
Name:		accerciser
Version:	1.1.91
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/accerciser/1.1/%{name}-%{version}.tar.bz2
# Source0-md5:	fbe7b09b9de936c466a049d3596aebd4
URL:		http://live.gnome.org/Accerciser
BuildRequires:	GConf2-devel >= 2.21.90
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils >= 0.12.0
BuildRequires:	intltool >= 0.37.0
BuildRequires:	python >= 1:2.4
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2
Requires:	python-pyatspi
Requires:	python-gnome
Requires:	python-gnome-desktop-libwnck
Requires:	python-ipython
Requires:	python-pygtk-gtk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An interactive Python accessibility explorer.

%description -l pl.UTF-8
Interaktywny eksplorator dostępności w Pythonie.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--without-pyreqs \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install accerciser.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall accerciser.schemas

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/accerciser
%{_datadir}/accerciser
%{_desktopdir}/accerciser.desktop
%{_mandir}/man1/accerciser.1*
%{_iconsdir}/hicolor/*/*/*
%{py_sitescriptdir}/accerciser
%{_sysconfdir}/gconf/schemas/accerciser.schemas
