%define upstream_name    Net-DAAP-Server-MythTV
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Publish MythTV videos to DAAP clients like Apple's Front Row
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/J/JA/JABLKO/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch
Requires:	perl(Net::DMAP::Server)

%description
MythTV is a homebrew PVR project. This module publishes MythTV videos,
including metadata, to DAAP clients like Apple's Front Row.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2010.0
+ Revision: 404069
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.01-4mdv2009.0
+ Revision: 258005
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.01-3mdv2009.0
+ Revision: 246059
- rebuild

* Sat Mar 22 2008 Stefan van der Eijk <stefan@mandriva.org> 0.01-1mdv2008.1
+ Revision: 189530
- import perl-Net-DAAP-Server-MythTV


