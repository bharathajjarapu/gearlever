Name:           gearlever
Version:        %{_version}
Release:        1%{?dist}
Summary:        A utility to manage AppImages
License:        GPL-3.0-or-later
URL:            https://github.com/mijorus/gearlever
BuildArch:      x86_64

Requires:       python3, python3-gobject, gtk4, libadwaita

%description
Gear Lever is a GTK4/libadwaita application to manage AppImages on Linux.

%install
cp -a %{_builddir}/installroot/. %{buildroot}/

%files
%{_bindir}/gearlever
%{_datadir}/gearlever/
%{_datadir}/applications/it.mijorus.gearlever.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/glib-2.0/schemas/it.mijorus.gearlever.gschema.xml
%{_datadir}/metainfo/it.mijorus.gearlever.metainfo.xml
%{_datadir}/locale/*/LC_MESSAGES/gearlever.mo

%changelog
* Mon Jan 01 2024 Gear Lever Contributors <noreply@github.com>
- Automated build
