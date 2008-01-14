#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DateTime
%define		pnam	Calendar-Mayan
Summary:	DateTime::Calendar::Mayan - the Mayan Long Count, Haab, and Tzolkin calendars
Summary(pl.UTF-8):	DateTime::Calendar::Mayan - kalendarze Majów: Długi Kalendarz, Haab oraz Tzolkin
Name:		perl-DateTime-Calendar-Mayan
Version:	0.0601
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9ed964ceadee297770be4ef7778e090c
URL:		http://search.cpan.org/dist/DateTime-Calendar-Mayan/
BuildRequires:	perl-DateTime
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An implementation of the Mayan Long Count, Haab, and Tzolkin calendars
as defined in "Calendrical Calculations The Millennium Edition".
Supplemented by "Frequently Asked Questions about Calendars".

%description -l pl.UTF-8
Implementacja kalendarzy Majów: Długiego, Haab i Tzolkin tak jak
opisano je w "Calendrical Calculations The Millennium Edition", wraz z
poprawkami wg "Frequently Asked Questions about Calendars".

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

rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/DateTime/Calendar/Mayan.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README Todo
%dir %{perl_vendorlib}/DateTime/Calendar
%{perl_vendorlib}/DateTime/Calendar/Mayan.pm
%{_mandir}/man3/*
