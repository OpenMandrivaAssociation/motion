%define name	motion
%define version 3.2.11.1
%define release %mkrel 2 

Summary:      	Software motion detector
Name: 		%{name}
Version: 	%{version}
Release:	%{release}
Group:	        Video
License: 	GPL
URL: 		http://www.lavrsen.dk/twiki/bin/view/Motion/WebHome
Source: 	http://heanet.dl.sourceforge.net/motion/%{name}-%{version}.tar.gz
BuildRequires:	jpeg-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	mysql-devel
BuildRequires:	postgresql-libs-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
Motion is a software motion detector.
It grabs images from video4linux devices and/or from webcams (such as the 
axis network cameras). Motion is the perfect tool for keeping an eye on your
property keeping only those images that are interesting.

%prep
%setup -q

%build
%configure2_5x 
%make

%install
rm -rf %{buildroot}
%makeinstall_std
mv %{buildroot}%{_sysconfdir}/motion-dist.conf %{buildroot}%{_sysconfdir}/motion.conf
rm -Rf %{buildroot}/%_datadir/doc/
%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc CHANGELOG COPYING CREDITS FAQ README README.axis_2100 motion_guide.html
%config(noreplace) %{_sysconfdir}/motion.conf
%{_bindir}/motion
%{_mandir}/man1/motion.1*
%{_datadir}/%{name}-%{version}/examples/*


