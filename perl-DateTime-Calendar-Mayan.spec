#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DateTime
%define		pnam	Calendar-Mayan
Summary:	DateTime::Calendar::Mayan - the Mayan Long Count, Haab, and Tzolkin calendars
Summary(pl):	DateTime::Calendar::Mayan - kalendarze Maj�w: D�ugi Kalendarz, Haab oraz Tzolkin
Name:		perl-DateTime-Calendar-Mayan
Version:	0.0601
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9ed964ceadee297770be4ef7778e090c
BuildRequires:	perl-DateTime
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An implementation of the Mayan Long Count, Haab, and Tzolkin
calendars as defined in "Calendrical Calculations The Millennium
Edition". Supplemented by "Frequently Asked Questions about Calendars".

%description -l pl
Implementacja kalendarzy Maj�w: D�ugiego, Haab i Tzolkin tak jak
opisano je w "Calendrical Calculations The Millennium Edition",
wraz z poprawkami wg "Frequently Asked Questions about Calendars".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README Todo
%{perl_vendorlib}/DateTime/Calendar/Mayan.pm
# not sure if that should be or should not be included..
# i rather would like to include it
#%{perl_vendorlib}/DateTime/Calendar/Mayan.pod
%{_mandir}/man3/*
