%define realname Net-DAAP-Server-MythTV

Name:		perl-%{realname}
Version:	0.01
Release:	%mkrel 4
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Publish MythTV videos to DAAP clients like Apple's Front Row
Source0:	http://search.cpan.org/CPAN/authors/id/J/JA/JABLKO/%{realname}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	perl-Net-DMAP-Server

%description
MythTV is a homebrew PVR project. This module publishes MythTV videos,
including metadata, to DAAP clients like Apple's Front Row.

%prep
%setup -q -n %{realname}-%{version}

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
