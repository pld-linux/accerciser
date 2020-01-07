Summary:	An interactive Python tool for querying accessibility information
Summary(pl.UTF-8):	Interaktywne narzędzie w Pythonie do pobierania informacji o dostępności
Name:		accerciser
Version:	3.34.3
Release:	1
License:	BSD
Group:		X11/Applications/Accessibility
Source0:	http://ftp.gnome.org/pub/GNOME/sources/accerciser/3.34/%{name}-%{version}.tar.xz
# Source0-md5:	8c383b765ed7fcd31648748479b32fee
URL:		https://wiki.gnome.org/Apps/Accerciser
BuildRequires:	at-spi2-core-devel >= 2.5.2
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	gtk+3-devel >= 3.1.13
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-pygobject3-devel >= 3.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.612
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	atk
Requires:	gdk-pixbuf2 >= 2.0
Requires:	gtk+3 >= 3.1.13
Requires:	librsvg >= 2.0
Requires:	libwnck >= 3.0
Requires:	pango
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

%prep
%setup -q

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	am_cv_python_pythondir=%{py3_sitescriptdir} \
%if "%{_host_cpu}" != "x32"
	--host=%{_host} \
	--build=%{_host}
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/accerciser
%{py3_sitescriptdir}/accerciser
%{_datadir}/accerciser
%{_datadir}/glib-2.0/schemas/org.a11y.Accerciser.gschema.xml
%{_datadir}/metainfo/accerciser.appdata.xml
%{_desktopdir}/accerciser.desktop
%{_iconsdir}/hicolor/*x*/apps/accerciser.png
%{_iconsdir}/hicolor/scalable/apps/accerciser.svg
%{_iconsdir}/hicolor/symbolic/apps/accerciser-symbolic.svg
%{_mandir}/man1/accerciser.1*
