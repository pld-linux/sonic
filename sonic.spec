Summary:	Sonic Library for speeding up and slowing speach
Summary(pl.UTF-8):	Biblioteka Sonic do przyspieszania i spowalniania mowy
Name:		sonic
Version:	0.2.0
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://github.com/waywardgeek/sonic/releases
Source0:	https://github.com/waywardgeek/sonic/archive/release-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9c3024a5485e66558ffb621c81385d75
Patch0:		%{name}-libdir.patch
URL:		https://github.com/waywardgeek/sonic
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sonic is a simple algorithm for speeding up or slowing down speech.
However, it's optimized for speed ups of over 2X, unlike previous
algorithms for changing speech rate. The Sonic library is a very
simple ANSI C library that is designed to easily be integrated into
streaming voice applications, like TTS back ends.

%description -l pl.UTF-8
Sonic to prosty algorytm do przyspieszania i spowalniania mowy. W
porównaniu do wcześniejszych algorytmów tego typu, jest
zoptymalizowany pod kątem przyspieszania ponad dwukrotnego. Biblioteka
Sonic to bardzo prosta biblioteka ANSI C, zaprojektowana do łatwej
integracji w aplikacjach przetwarzających strumienie głosu, takich jak
backendy syntezatorów mowy.

%package devel
Summary:	Header files for Sonic library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Sonic
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Sonic library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Sonic.

%package static
Summary:	Static Sonic library
Summary(pl.UTF-8):	Statyczna biblioteka Sonic
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Sonic library.

%description static -l pl.UTF-8
Statyczna biblioteka Sonic.

%prep
%setup -q -n %{name}-release-%{version}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -Wall -fPIC -pthread"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX="%{_prefix}" \
	LIBDIR="%{_libdir}"

install -Dp sonic.1 $RPM_BUILD_ROOT%{_mandir}/man1/sonic.1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README doc/index.md
%attr(755,root,root) %{_bindir}/sonic
%attr(755,root,root) %{_libdir}/libsonic.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsonic.so.0
%{_mandir}/man1/sonic.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsonic.so
%{_includedir}/sonic.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libsonic.a
