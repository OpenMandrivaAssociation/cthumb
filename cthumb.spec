%define  version	4.2
%define release	13

Summary:	A program to generate Web picture albums
Name:		cthumb
Version:	%version
Release:	%release
License:	GPL
Group:		Networking/WWW
Source0:	http://cthumb.sourceforge.net/cthumb-%{version}.tar.bz2
URL:		https://cthumb.sourceforge.net/
BuildArch:	noarch
Requires:	perl-base
Requires:	perl-HTML-Parser
Requires:	perl-MIME-tools
Requires:	perl-URI
Requires:	netpbm


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
mkdir -p %{buildroot}

make prefix=%{buildroot}%{_prefix} \
    mandir=%{buildroot}%{_mandir} install
cp contrib/mkalbum %{buildroot}%{_bindir}
cp contrib/tree2album %{buildroot}%{_bindir}

%files
%doc README TO-DO INSTALL BUGS VERSION AUTHORS ChangeLog cthumbrc.sample
%doc contrib/*.readme
%attr(0755,root,root) %{_bindir}/*
%{_datadir}/man/*/*
%dir %{_datadir}/images/
%{_datadir}/images/*
