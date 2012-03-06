Name:           gupnp
Version:        0.13.2
Release:        1%{?dist}
Summary:        A framework for creating UPnP devices & control points

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.gupnp.org/
Source0:        http://www.gupnp.org/sources/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gssdp-devel
BuildRequires: glib2-devel
BuildRequires: gtk-doc
BuildRequires: libsoup-devel
BuildRequires: libxml2-devel
BuildRequires: libuuid-devel

Requires: dbus

%description
GUPnP is an object-oriented open source framework for creating UPnP 
devices and control points, written in C using GObject and libsoup. 
The GUPnP API is intended to be easy to use, efficient and flexible. 

%package devel
Summary: Development package for gupnp
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: gssdp-devel
Requires: pkgconfig
Requires: libsoup-devel
Requires: libxml2-devel
Requires: libuuid-devel
Requires: glib2-devel

%description devel
Files for development with %{name}.

%package docs
Summary: Documentation files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: gtk-doc
BuildArch: noarch

%description docs
This package contains developer documentation for %{name}.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags} V=1

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_libdir}/libgupnp-1.0.so.*
%{_bindir}/gupnp-binding-tool

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/gupnp-1.0.pc
%{_libdir}/libgupnp-1.0.so
%{_includedir}/gupnp-1.0

%files docs
%defattr(-,root,root,-)
%doc %{_datadir}/gtk-doc/html/%{name}

%changelog
* Fri Dec  4 2009 Peter Robinson <pbrobinson@gmail.com> 0.13.2-1
- Update to 0.13.2

* Wed Oct  7 2009 Peter Robinson <pbrobinson@gmail.com> 0.13.1-1
- Update to 0.13.1

* Thu Sep 17 2009 Bastien Nocera <bnocera@redhat.com> 0.13.0-1
- Update to 0.13.0

* Mon Aug 31 2009 Peter Robinson <pbrobinson@gmail.com> 0.12.8-4
- some spec file cleanups, depend on libuuid instead of e2fsprogs-devel

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul  1 2009 Peter Robinson <pbrobinson@gmail.com> 0.12.8-2
- Rebuild with new libuuid build req

* Wed Jun  3 2009 Peter Robinson <pbrobinson@gmail.com> 0.12.8-1
- New upstream release

* Mon Apr 27 2009 Peter Robinson <pbrobinson@gmail.com> 0.12.7-1
- New upstream release

* Wed Mar  4 2009 Peter Robinson <pbrobinson@gmail.com> 0.12.6-4
- Move docs to noarch sub package

* Mon Mar  2 2009 Peter Robinson <pbrobinson@gmail.com> 0.12.6-3
- Add some extra -devel Requires packages

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Peter Robinson <pbrobinson@gmail.com> 0.12.6-1
- New upstream release

* Wed Jan 14 2009 Peter Robinson <pbrobinson@gmail.com> 0.12.5-1
- New upstream release

* Thu Dec 18 2008 Peter Robinson <pbrobinson@gmail.com> 0.12.4-3
- Add gtk-doc build req

* Sat Nov 22 2008 Peter Robinson <pbrobinson@gmail.com> 0.12.4-2
- Fix summary

* Mon Nov 17 2008 Peter Robinson <pbrobinson@gmail.com> 0.12.4-1
- New upstream release

* Mon Oct 27 2008 Peter Robinson <pbrobinson@gmail.com> 0.12.3-1
- New upstream release

* Mon Oct 20 2008 Colin Walters <walters@verbum.org> 0.12.2-2
- devel package requires gssdp-devel

* Sun Aug 31 2008 Peter Robinson <pbrobinson@gmail.com> 0.12.2-1
- New upstream release

* Thu Aug 28 2008 Peter Robinson <pbrobinson@gmail.com> 0.12.1-7
- Yet again. Interesting it builds fine in mock and not koji

* Thu Aug 28 2008 Peter Robinson <pbrobinson@gmail.com> 0.12.1-6
- Once more with feeling

* Thu Aug 28 2008 Peter Robinson <pbrobinson@gmail.com> 0.12.1-5
- Second go

* Thu Aug 28 2008 Peter Robinson <pbrobinson@gmail.com> 0.12.1-4
- Fix build on rawhide

* Wed Aug 13 2008 Peter Robinson <pbrobinson@gmail.com> 0.12.1-3
- Fix changelog entries

* Wed Aug 13 2008 Peter Robinson <pbrobinson@gmail.com> 0.12.1-2
- Fix a compile issue on rawhide

* Mon Jun 16 2008 Peter Robinson <pbrobinson@gmail.com> 0.12.1-1
- Initial release
