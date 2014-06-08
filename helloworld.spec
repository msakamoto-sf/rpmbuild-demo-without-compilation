# Original Version and Article, Special-Thanx to :
# http://momijiame.tumblr.com/post/32458077768/spec-rpm

Name:      helloworld
Version:   1.0
Release:   1
Group:     Security Tools
Vendor:    Example Company Inc.
URL:       http://www.example.com/
License:   Custom License
Summary:   Example RPM Plain File Packaging.
BuildArch: noarch
# use build-time generated tar ball.
Source0:   %{name}.tar.gz
# (only create temporary directory name, for RHEL5 compat environment)
# see : http://fedoraproject.org/wiki/Packaging:Guidelines#BuildRoot_tag
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%define INSTALLDIR %{buildroot}/etc/helloworld

%description
%{summary}

%prep
%setup -q -n %{name}

%build

%install
rm -rf %{INSTALLDIR}
mkdir -p %{INSTALLDIR}
cp -Rp * %{INSTALLDIR}

%clean
#rm -rf %{buildroot}
# Avoid Disastarous Damage : http://dev.tapweb.co.jp/2010/12/273
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/etc/helloworld/regular.txt

# auto include child files under the directory
/etc/helloworld/auto_include_child

%config %attr(0600,root,root) /etc/helloworld/greet.conf
%config(noreplace) /etc/helloworld/greet-noreplace.conf

%attr(0700,root,root) /etc/helloworld/greet.sh
%attr(0600,root,root) /etc/helloworld/p0600.txt
%attr(0705,root,root) /etc/helloworld/p0705.txt

# directory only
%dir %attr(0770,-,-) /etc/helloworld/dir_only
%exclude /etc/helloworld/dir_only/ignored.txt

%pre
if [ "$1" = "1" ]; then
  echo "pre-install script : Initial installation."
elif [ "$1" = "2" ]; then
  echo "pre-install script : Upgrade installation."
fi

%post
if [ "$1" = "1" ]; then
  echo "post-install script : Initial installation."
elif [ "$1" = "2" ]; then
  echo "post-install script : Upgrade installation."
fi

%preun
if [ "$1" = "0" ] ; then
  echo "pre-uninstall script : Uninstall operation."
elif [ "$1" = "1" ]; then
  echo "pre-uninstall script : Upgrade uninstallation process."
fi

%postun
if [ "$1" = "0" ] ; then
  echo "post-uninstall script : Uninstall operation."
elif [ "$1" = "1" ]; then
  echo "post-uninstall script : Upgrade uninstallation process."
fi

%changelog

