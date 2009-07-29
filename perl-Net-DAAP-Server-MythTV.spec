%define upstream_name    Net-DAAP-Server-MythTV
%define upstream_version 0.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Publish MythTV videos to DAAP clients like Apple's Front Row
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/J/JA/JABLKO/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
Requires:	perl-Net-DMAP-Server

%description
MythTV is a homebrew PVR project. This module publishes MythTV videos,
including metadata, to DAAP clients like Apple's Front Row.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/%{perl_vendorarch}

mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp mythdaap $RPM_BUILD_ROOT/%{_bindir}
chmod 755 $RPM_BUILD_ROOT/%{_bindir}/mythdaap

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/mythdaap
%{perl_vendorlib}/*
%{_mandir}/man3/*
