#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/PROTO/elsa elsa; \
#cd elsa; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#VERSION=$(cat configure.ac | grep "elsa" | grep INIT | sed 's@\[@@g' | sed 's@\]@@g' | sed 's@)@@g' | cut -d, -f 2 | sed "s@ @@"); \
#PKG_VERSION=$VERSION.$SVNREV; \
#cd ..; \
#tar -Jcf elsa-$PKG_VERSION.tar.xz elsa/ --exclude .svn --exclude .*ignore

%define svnrev  66786

Summary:	Open Enlightenmet session with pam
Name:		elsa
Version:	0.0.4
Release:	0.%{svnrev}.1
License:	GPLv3
Group:		System/Configuration/Other
URL:		http://enlightenment.org/
Source0:	%{name}-%{version}.%{svnrev}.tar.xz

BuildRequires:	edje
BuildRequires:	embryo
BuildRequires:	pam-devel
BuildRequires:	pkgconfig(elementary)

%description
Elsa allows you to open a Enlightenment session with pam.
It also integrates with the rc scripts.

%prep
%setup -qn %{name}

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%files 
%config(noreplace) %{_sysconfdir}/pam.d/elsa
%config(noreplace) %{_sysconfdir}/elsa.conf
%{_datadir}/elsa/themes/*.edj
%{_datadir}/elsa/themes/old/*.edj
%{_sbindir}/elsa
%{_libdir}/elsa/elsa_wait
%{_libdir}/elsa/elsa_client

