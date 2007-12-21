%define  version	4.2
%define  release	 %mkrel 6

Summary:	A program to generate Web picture albums
Name:		cthumb
Version:	%version
Release:	%release
License:	GPL
Group:		Networking/WWW
Source:		http://cthumb.sourceforge.net/cthumb-%{version}.tar.bz2
BuildRoot:	%_tmppath/%name-%version-buildroot
URL:		http://cthumb.sourceforge.net/
BuildArch:	noarch
Requires:	perl-base
Requires:	perl-HTML-Parser
Requires:	perl-MIME-tools
Requires:	perl-URI
Requires:	libjpeg
Requires:	libnetpbm


%description
Cthumb allows you to create a web picture album, with an index and
several pages, each with thumbnails of your pictures. it optionally
generates pages in several languages simultaneously. it automatically
generates thumbnails of the pictures. it attempts to be nice in the
look of the pages it generates. it is geared towards people that have
ton of digital images that need to be labeled and classified. all you
need is the pictures and a text editor to put all the titles for every
picture in a simple "album" textfile.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --mandir=%{_mandir}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{_prefix} \
    mandir=$RPM_BUILD_ROOT%{_mandir} install
cp contrib/mkalbum $RPM_BUILD_ROOT%{_bindir}
cp contrib/tree2album $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README TO-DO INSTALL BUGS VERSION AUTHORS ChangeLog cthumbrc.sample
%doc contrib/*.readme
%attr(0755,root,root) %{_bindir}/*
%{_datadir}/man/*/*
%dir %{_datadir}/images/
%{_datadir}/images/*

