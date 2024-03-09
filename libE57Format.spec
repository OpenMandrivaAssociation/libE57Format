%define major %(echo %{version} |cut -d\. -f1)
%define libname %mklibname E57Format
%define devname %mklibname E57Format -d

Summary:	Library for reading and writing the E57 file format
Name:		libE57Format
Version:	3.1.1
Release:	1
License:	GPL
Group:		System/Libraries
URL:		https://github.com/asmaloney/libE57Format
Source0:	https://github.com/asmaloney/libE57Format/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		libE57Format-3.1.1-set_soname.patch
Patch1:		libE57Format-3.1.1-fix_cmake_path.patch
BuildRequires: cmake ninja
BuildRequires: ccache
BuildRequires: pkgconfig(xerces-c)

%description
libE57Format is a C++ library which provides read & write support for the
ASTM-standard E57 file format. E57 files store 3D point cloud data (produced
by 3D imaging systems such as laser scanners), attributes associated with
3D point data (color & intensity), and 2D images (photos taken using a 3D
imaging system).

#----------------------------------------------------------------------

%package -n %{libname}
Summary:	Library for reading and writing the E57 file format
Group:		System/Libraries

%description -n %{libname}
libE57Format is a C++ library which provides read & write support for the
ASTM-standard E57 file format. E57 files store 3D point cloud data (produced
by 3D imaging systems such as laser scanners), attributes associated with
3D point data (color & intensity), and 2D images (photos taken using a 3D
imaging system).

%files -n %{libname}
%{_libdir}/*.so.%{major}*

#----------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	e57format-devel
Provides:	E57Format-devel

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_datadir}/cmake/E57Format/*
#{_libdir}/pkgconfig/*

#----------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake -Wno-dev \
	-DE57_BUILD_SHARED:BOOL=ON \
	-DE57_BUILD_TEST:BOOL=OFF \
	-G Ninja
%ninja_build

%install
%ninja_install -C build

