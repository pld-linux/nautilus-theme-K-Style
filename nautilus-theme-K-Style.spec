Summary:	Original KDE look and feel
Summary(pl):	Temat oparty na KDE
Name:		nautilus-theme-K-Style
Version:	1.0
Release:	1
License:	Free
Group:		X11/Amusements
Source0:	nautilus-k-style.tar.gz
URL:		http://sunshineinabag.co.uk/
Requires:	nautilus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%define		_prefix		/usr/X11R6

%description
Original KDE look and feel.

%description -l pl
Temat oparty na KDE.

%prep
%setup -q -n K-Style

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}/nautilus/K-Style

mv * $RPM_BUILD_ROOT%{_pixmapsdir}/nautilus/K-Style

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_pixmapsdir}/nautilus/K-Style
