Summary:	Standalone libvisual port which supports ALSA input only
Summary(pl.UTF-8):	Samodzielny port libvisual obsługujący tylko wejście ALSA
Name:		projectM-libvisual-alsa
Version:	2.0.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/projectm/%{name}-%{version}-Source.tar.gz
# Source0-md5:	0daf5da7a729d9a274f8b8c22a405610
URL:		http://projectm.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	cmake >= 2.4.0
BuildRequires:	libprojectM-devel >= 1:2.0.1
BuildRequires:	libstdc++-devel
BuildRequires:	libvisual-devel = 0.4.0
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the experimental libvisual standalone port which allows ALSA
input only.

%description -l pl.UTF-8
Ten pakiet zawiera eksperymentalny, samodzielny port libvisual
obsługujący tylko wejście ALSA.

%prep
%setup -q -n %{name}-%{version}-Source

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc DESIGN README
%attr(755,root,root) %{_bindir}/projectM-libvisual-alsa
%{_desktopdir}/projectM-libvisual-alsa.desktop
