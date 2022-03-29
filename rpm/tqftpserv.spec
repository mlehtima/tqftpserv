Name:          tqftpserv
Version:       1.0
Release:       1
Summary:       Trivial File Transfer Protocol server over AF_QIPCRTR 
URL:           https://github.com/andersson/tqftpserv
Source0:       %{name}-%{version}.tar.gz
License:       BSD-3-Clause
BuildRequires: pkgconfig(systemd)
BuildRequires: qrtr-devel

%description
Trivial File Transfer Protocol server over AF_QIPCRTR.

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
%make_build

%install
make prefix=%{_prefix} libdir=%{_libdir} install DESTDIR=%{buildroot}

mkdir -p %{buildroot}/%{_unitdir}/multi-user.target.wants
ln -s ../%{name}.service %{buildroot}/%{_unitdir}/multi-user.target.wants/%{name}.service

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_unitdir}/multi-user.target.wants/%{name}.service
%{_unitdir}/%{name}.service
