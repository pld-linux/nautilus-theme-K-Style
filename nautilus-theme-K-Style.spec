Summary:	Original KDE look and feel
Summary(pl):	Motyw oparty na KDE
Name:		nautilus-theme-K-Style
Version:	1.0
Release:	1
License:	Free
Group:		X11/Amusements
#http://www.lucidus.uklinux.net/index.php?theme=nautilus&get=k-style.tar.gz
Source0:	nautilus-k-style.tar.gz
URL:		http://sunshineinabag.co.uk/
Requires:	nautilus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch


%description
Original KDE look and feel.

%description -l pl
Motyw oparty na KDE.

%prep
%setup -q -n K-Style

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}/nautilus/K-Style

mv * $RPM_BUILD_ROOT%{_pixmapsdir}/nautilus/K-Style

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_pixmapsdir}/nautilus/K-Style
