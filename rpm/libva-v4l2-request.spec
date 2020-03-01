Name:          libva-v4l2-request
Version:       2020.03
Release:       1
Summary:       v4l2-request backend for libVA video acceleration
License:       LGPLv2.1 & MIT
URL:           https://github.com/bootlin/libva-v4l2-request
Source:        %{name}-%{version}.tar.gz
BuildRequires: meson
BuildRequires: pkgconfig(libva) >= 1.1.0
BuildRequires: pkgconfig(libdrm)
BuildRequires: kernel-headers

%description
This libVA backend is designed to work with the Linux Video4Linux2 Request API
that is used by a number of video codecs drivers, including the Video Engine 
found in most Allwinner SoCs.

%prep
%setup -q -n %{name}-%{version}/upstream

%build
%meson 

%meson_build

%install
rm -rf $RPM_BUILD_ROOT
%meson_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, -)
%license COPYING.LGPL
%{_libdir}/dri/v4l2_request_drv_video.so
