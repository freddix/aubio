Summary:	Library for audio labelling
Name:		aubio
Version:	0.4.1
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	http://aubio.org/pub/%{name}-%{version}.tar.bz2
# Source0-md5:	ffe7d24f6bd8e9053aeaba6c0231efb0
URL:		http://aubio.piem.org/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ffmpeg-devel
BuildRequires:	fftw3-single-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aubio is a library for audio labelling.

%package devel
Summary:	Header files for aubio library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for aubio library.

%package progs
Summary:	Example applications using aubio library
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description progs
A few examples of applications using aubio library.

%prep
%setup -q

%{__sed} -i 's|${PREFIX}/lib|%{_libdir}|' src/wscript_build

%build
export CC="%{__cc}"
export CXX="%{__cxx}"
export CFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcxxflags}"
export LDFLAGS="%{rpmldflags}"
./waf configure \
        --nocache \
	--libdir=%{_libdir} \
	--prefix=%{_prefix} \
	--enable-fftw3f
./waf -v build

%install
rm -rf $RPM_BUILD_ROOT

./waf -v install \
        --destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.md
%attr(755,root,root) %ghost %{_libdir}/libaubio.so.?
%attr(755,root,root) %{_libdir}/libaubio.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaubio.so
%{_includedir}/%{name}
%{_pkgconfigdir}/aubio.pc

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aubiomfcc
%attr(755,root,root) %{_bindir}/aubionotes
%attr(755,root,root) %{_bindir}/aubioonset
%attr(755,root,root) %{_bindir}/aubiopitch
%attr(755,root,root) %{_bindir}/aubioquiet
%attr(755,root,root) %{_bindir}/aubiotrack

