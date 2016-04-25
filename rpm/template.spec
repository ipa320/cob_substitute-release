Name:           ros-indigo-cob-safety-controller
Version:        0.6.4
Release:        0%{?dist}
Summary:        ROS cob_safety_controller package

Group:          Development/Libraries
License:        LGPL
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ros-indigo-catkin

%description
This package is a substitute for the private implementation of
cob_safety_controller package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Apr 25 2016 Matthias Luedtke <mdl@ipa.fhg.de> - 0.6.4-0
- Autogenerated by Bloom

* Fri Apr 01 2016 Matthias Luedtke <mdl@ipa.fhg.de> - 0.6.3-0
- Autogenerated by Bloom

* Tue Aug 25 2015 Matthias Luedtke <mdl@ipa.fhg.de> - 0.6.2-0
- Autogenerated by Bloom

* Wed Jun 17 2015 Matthias Luedtke <mdl@ipa.fhg.de> - 0.6.1-0
- Autogenerated by Bloom

* Wed Sep 17 2014 Matthias Luedtke <mdl@ipa.fhg.de> - 0.6.0-0
- Autogenerated by Bloom

* Mon Aug 25 2014 Matthias Luedtke <mdl@ipa.fhg.de> - 0.5.2-0
- Autogenerated by Bloom

