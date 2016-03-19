Summary:	Proxy manager service
Name:		proxymngr
Version:	1.0.4
Release:	3
Group:		Development/X11
License:	MIT
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:	lbxproxy >= 1.0.1
BuildRequires:	pkgconfig(ice) >= 1.0.0
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xt) >= 1.0.0

%description
The proxy manager (proxymngr) is responsible for resolving requests from
xfindproxy (and other similar clients), starting new proxies when appropriate,
and keeping track of all of the available proxy services. The proxy manager
strives to reuse existing proxies whenever possible.

%prep
%setup -q

%build
%configure \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/proxymngr
%{_mandir}/man1/proxymngr.*
%{_sysconfdir}/X11/proxymngr/pmconfig


