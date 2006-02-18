Summary: PHP extension and standalone application to do fast word-level diffs
Name: wikidiff2
Version: 0.0.2
Release: 1
Copyright: GPL
Group: Applications/Internet
Source: wikidiff2-0.0.2.tar.gz
BuildRoot: /var/tmp/%{name}-buildroot

%description
PHP extension and standalone application to do fast word-level diffs.
(Packaged for Wikimedia local use!)

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
INSTALL_TARGET="$RPM_BUILD_ROOT/usr/local/lib/php/extensions/no-debug-non-zts-20050922" make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir /usr/local/lib/php/extensions/no-debug-non-zts-20050922

/usr/local/lib/php/extensions/no-debug-non-zts-20050922/php_wikidiff2.so
