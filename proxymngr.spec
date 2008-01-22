Name: proxymngr
Version: 1.0.1
Release: %mkrel 4
Summary: Proxy manager service
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros	>= 1.1.5
BuildRequires: libx11-devel	>= 1.1.3
BuildRequires: lbxproxy		>= 1.0.1
BuildRequires: libice-devel	>= 1.0.4
BuildRequires: libxt-devel	>= 1.0.5

%description
The proxy manager (proxymngr) is responsible for resolving requests from
xfindproxy (and other similar clients), starting new proxies when appropriate,
and keeping track of all of the available proxy services. The proxy manager
strives to reuse existing proxies whenever possible.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/proxymngr
%{_libdir}/X11/proxymngr/pmconfig
%{_mandir}/man1/proxymngr.*


