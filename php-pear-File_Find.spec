%define		_class		File
%define		_subclass	Find
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.3.1
Release:	6
Summary:	A class that facillitates the search of filesystems
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/File_Find/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
File_Find, created as a replacement for its Perl counterpart, also
named File_Find, is a directory searcher, which handles globbing,
recursive directory searching, as well as a slew of other cool
features.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-3mdv2012.0
+ Revision: 741967
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-2
+ Revision: 679318
- mass rebuild

* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.1-1mdv2011.0
+ Revision: 587640
- update to new version 1.3.1

* Mon Dec 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.0-4mdv2010.1
+ Revision: 478665
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.3.0-3mdv2010.0
+ Revision: 441031
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-2mdv2009.0
+ Revision: 236836
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.3.0-1mdv2008.1
+ Revision: 136404
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-1mdv2008.0
+ Revision: 15655
- 1.3.0


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-1mdv2007.0
+ Revision: 81576
- Import php-pear-File_Find

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-1mdk
- 1.2.2

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-1mdk
- 1.2.1
- new group (Development/PHP)

* Thu Sep 22 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-1mdk
- 1.1.0

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-7mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-6mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-5mdk
- fix deps

* Fri Jul 22 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-4mdk
- fix the package.xml file so it will register

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-1mdk
- initial Mandriva package (PLD import)

