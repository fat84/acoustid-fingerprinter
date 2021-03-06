Name:           acoustid-fingerprinter
Version:        0.6
Release:        14%{?dist}
Summary:        Music AcoustID fingerprinting application

License:        GPLv2+
URL:            http://acoustid.org/fingerprinter
Source:         https://github.com/downloads/lalinsky/%{name}/%{name}-%{version}.tar.gz
Patch0:         01-Fix-build-with-upcoming-Libav-10-release.patch
Patch1:         02-CodecID.patch
Patch2:         03-pkg-config.patch
Patch3:         04-typo-warning.patch
Patch4:         05-g++-6-char-cast.patch
Patch5:         06-taglib.patch

BuildRequires:  cmake
BuildRequires:  qt4-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  taglib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libchromaprint-devel

Requires:       hicolor-icon-theme

%description
Acoustid fingerprinter is a cross-platform GUI application that uses
Chromaprint to submit audio fingerprints from your music collection 
to the Acoustid database. Only tagged audio files are submitted. 
Files tagged by MusicBrainz applications such as Picard are preferred,
but it will submit fingerprints for any files that have tags such as
track title, artist name, album name, etc.

%prep
%autosetup -p1

%build
%cmake -DCMAKE_BUILD_TYPE=Debug
# removing the -O3 optimization flag for the release building type
sed -i  "s/-O3 -DNDEBUG//g" CMakeCache.txt
%make_build

%install
%make_install

install -d -m755 %{buildroot}%{_datadir}/applications

desktop-file-install \
  --delete-original \
  --remove-key Encoding \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

install -p -D -m 0644 images/%{name}.svg  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%doc CHANGES.txt
%license COPYING.txt 
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg


%changelog
* Wed Jan 17 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.6-14
- Rebuilt for ffmpeg-3.5 git

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 18 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.6-12
- Fix build (patches from Debian)
- Update scriptlets
- Update spec fire

* Sat Mar 18 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 19 2014 Sérgio Basto <sergio@serjux.com> - 0.6-10
- Rebuilt for FFmpeg 2.4.3

* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.6-9
- Rebuilt for FFmpeg 2.4.x

* Thu Aug 07 2014 Sérgio Basto <sergio@serjux.com> - 0.6-8
- Rebuilt for ffmpeg-2.3

* Sat Mar 29 2014 Sérgio Basto <sergio@serjux.com> - 0.6-7
- Rebuilt for ffmpeg-2.2

* Wed Nov 27 2013 Leigh Scott <leigh123linux@googlemail.com> - 0.6-6
- Fix compile error

* Wed Oct 02 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.6-5
- Rebuilt

* Thu Aug 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.6-4
- Rebuilt for FFmpeg 2.0.x

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.6-3
- Rebuilt for x264/FFmpeg

* Sun Apr 28 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.6-2
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 24 2012 Ismael Olea <ismael@olea.org> - 0.6-1
- Update to 0.6

* Sat Nov 24 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.5.1-7
- Rebuilt for FFmpeg 1.0

* Tue Jun 26 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.5.1-6
- Rebuilt for FFmpeg

* Wed May 9 2012 Ismael Olea <ismael@olea.org> - 0.5.1-5
- bump

* Wed Apr 04 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.5.1-4
- Rebuilt

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.5.1-3
- Rebuilt for c++ ABI breakage

* Tue Feb 28 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.5.1-2
- Rebuilt for x264/FFmpeg

* Sat Jan 14 2012 Ismael Olea <ismael@olea.org> - 0.5.1-1
- updated to 0.5.1
- desktop svg icon now provided upstream
- fix-contenttypeheader.patch included in upstream
- Now CMAKE configured for Debug release -> better debuginfo
- added update-mime-database scriptlets

* Wed Jan 4 2012 Ismael Olea <ismael@olea.org> - 0.5-2
- upstream now includes desktop file
- patch0 fixes https://github.com/lalinsky/acoustid-fingerprinter/issues/3
- removing the -O3 optimization flag for the release building type
- more spec cleaning

* Sun Jan 1 2012 Ismael Olea <ismael@olea.org> - 0.5-1
- update to 0.5
- minor spec cleaning

* Thu Nov 18 2011 Ismael Olea <ismael@olea.org> - 0.4-1
- first version for Fedora

