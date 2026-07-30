%define upstream_name    Net-DAAP-Server-MythTV
%define upstream_version 0.01
Name:		perl-%{upstream_name}
Version:	0.01
Release:	1

Summary:	Publish MythTV videos to DAAP clients like Apple's Front Row
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	https://cpan.metacpan.org/authors/id/J/JA/JABLKO/Net-DAAP-Server-MythTV-0.01.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch
Requires:	perl(Net::DMAP::Server)

%description
MythTV is a homebrew PVR project. This module publishes MythTV videos,
including metadata, to DAAP clients like Apple's Front Row.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std
rm -rf %{buildroot}%{perl_vendorarch}

mkdir -p %{buildroot}%{_bindir}
install -m 755 mythdaap %{buildroot}%{_bindir}/mythdaap

%files
%doc README
%{_bindir}/mythdaap
%{perl_vendorlib}/*
%{_mandir}/man3/*

