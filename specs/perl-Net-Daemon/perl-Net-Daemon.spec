# $Id$

# Authority: dries
# Upstream: Jochen Wiedmann <jwied$cpan,org>


%define real_name Net-Daemon
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Perl extension for portable daemons
Name: perl-Net-Daemon
Version: 0.43
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Daemon/

Source: http://www.cpan.org/modules/by-module/Net/Net-Daemon-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This package contains a perl extension for portable daemons.

%prep
%setup -n %{real_name}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%{_mandir}/man3/*
%{perl_vendorlib}/Net/Daemon.pm
%{perl_vendorlib}/Net/Daemon/*

%changelog
* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.43-1
- Updated to release 0.43.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.39-1
- Updated to release 0.39.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.38-1.2
- Rebuild for Fedora Core 5.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.38-1
- Initial package.
