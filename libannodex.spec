Summary:	A library for reading and writing annodexed media
Summary(pl.UTF-8):	Biblioteka do odczytu i zapisu mediów w formacie Annodex
Name:		libannodex
Version:	0.7.3
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://annodex.net/software/libannodex/download/%{name}-%{version}.tar.gz
# Source0-md5:	504cf036cf04512260006a986926177f
Patch0:		%{name}-libcmml.patch
Patch1:		%{name}-no-ltdl.patch
Patch2:		%{name}-export.patch
URL:		http://annodex.net/software/libannodex/index.html
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	libcmml-devel >= 0.9.2
BuildRequires:	liboggz-devel >= 0.9.1
BuildRequires:	libsndfile-devel >= 1.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	libcmml >= 0.9.2
Requires:	liboggz >= 0.9.1
Requires:	libsndfile >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libannodex is a library to provide reading and writing of Annodex
files and streams.

%description -l pl.UTF-8
libannodex to biblioteka pozwalająca na odczyt i zapis plików i
strumieni w formacie Annodex.

%package devel
Summary:	Header files for libannodex library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libannodex
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcmml-devel >= 0.9.2
Requires:	liboggz-devel >= 0.9.1
Requires:	libsndfile-devel >= 1.0.0

%description devel
Header files for libannodex library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libannodex.

%package static
Summary:	Static libannodex library
Summary(pl.UTF-8):	Statyczna biblioteka libannodex
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libannodex library.

%description static -l pl.UTF-8
Statyczna biblioteka libannodex.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/annodex/importers/*.{la,a}
rm -rf $RPM_BUILD_ROOT%{_docdir}/libannodex

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(755,root,root) %{_bindir}/anx*
%attr(755,root,root) %{_libdir}/libannodex.so.*.*.*
%dir %{_libdir}/annodex
%dir %{_libdir}/annodex/importers
%attr(755,root,root) %{_libdir}/annodex/importers/libanx_import_*.so*
%{_mandir}/man1/anx*.1*

%files devel
%defattr(644,root,root,755)
%doc doc/libannodex/html/*
%attr(755,root,root) %{_libdir}/libannodex.so
%{_libdir}/libannodex.la
%{_includedir}/annodex
%{_pkgconfigdir}/annodex.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libannodex.a
