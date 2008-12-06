%define name	motion
%define version 3.2.10.1
%define release %mkrel 3

Summary:      	Software motion detector
Name: 		%{name}
Version: 	%{version}
Release:	%{release}
Group:	        Video
License: 	GPL
Source: 	http://heanet.dl.sourceforge.net/motion/%{name}-%{version}.tar.gz
URL: 		http://www.lavrsen.dk/twiki/bin/view/Motion/WebHome
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	jpeg-devel ffmpeg-devel mysql-devel

%description
Motion is a software motion detector.
It grabs images from video4linux devices and/or from webcams (such as the 
axis network cameras). Motion is the perfect tool for keeping an eye on your
property keeping only those images that are interesting.

%prep
%setup -q

perl -pi -e 's!LDFLAGS="-Wl,-rpath,.*"!!g' configure

%build
export FFMPEG_CFLAGS_DEB="-I/usr/include/libavformat/ -I/usr/include/libavutil/"

%configure2_5x 
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
mv $RPM_BUILD_ROOT%{_sysconfdir}/motion-dist.conf $RPM_BUILD_ROOT%{_sysconfdir}/motion.conf
rm -Rf $RPM_BUILD_ROOT/%_datadir/doc/
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc CHANGELOG COPYING CREDITS FAQ README README.axis_2100 motion_guide.html
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/motion.conf
%{_bindir}/motion
%{_mandir}/man1/motion.1*


