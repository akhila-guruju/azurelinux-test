%define distro mariner
%define polyinstatiate n
%define monolithic n
%define policy_name targeted
%define refpolicy_major 2
%define refpolicy_minor 20240226
%define POLICYCOREUTILSVER 3.2
%define CHECKPOLICYVER 3.2
Summary:        SELinux policy
Name:           selinux-policy
Version:        %{refpolicy_major}.%{refpolicy_minor}
Release:        11%{?dist}
License:        GPLv2
Vendor:         Microsoft Corporation
Distribution:   Azure Linux
URL:            https://github.com/SELinuxProject/refpolicy
Source0:        %{url}/releases/download/RELEASE_%{refpolicy_major}_%{refpolicy_minor}/refpolicy-%{version}.tar.bz2
Source1:        Makefile.devel
Source2:        booleans_targeted.conf
Source3:        modules_targeted.conf
Source4:        macros.selinux-policy
Patch1:         0001-Add-dac_read_search-perms.patch
Patch2:         0002-systemd-systemd-logind-reads-cloud-init-state.patch
Patch3:         0003-Set-default-login-to-unconfined_u.patch
Patch4:         0004-Add-compatibility-for-container-selinux.patch
Patch5:         0005-Temp-kubernetes-fix.patch
Patch6:         0006-container-docker-Fixes-for-containerd-and-kubernetes.patch
Patch7:         0007-Port-tomcat-module-from-Fedora-policy.patch
Patch8:         0008-Port-PKI-module-from-Fedora-policy.patch
Patch9:         0009-domain-Unconfined-can-transition-to-other-domains.patch
Patch10:        0010-modutils-Handle-running-dracut-during-rpm-postinst.patch
Patch11:        0011-iptables-Support-Mariner-non-standard-config-locatio.patch
Patch12:        0012-systemd-Fix-run-systemd-shutdown-handling.patch
Patch13:        0013-modutils-Temporary-fix-for-mkinitrd-dracut.patch
Patch14:        0014-Add-additional-Fedora-policy-compatibility.patch
Patch15:        0015-various-Add-new-pidfd-uses.patch
Patch16:        0016-various-Add-use-of-pressure-stall-information-in-sys.patch
Patch17:        0017-various-Add-additional-logging-access-for-domains-ru.patch
Patch18:        0018-unconfined-Add-user-namespace-creation.patch
Patch19:        0019-sysnet-The-ip-command-reads-various-files-in-usr-sha.patch
Patch20:        0020-rpm-Minor-fixes.patch
Patch21:        0021-systemd-Minor-fixes.patch
Patch22:        0022-irqbalance-Dontaudit-net_admin.patch
Patch23:        0023-systemd-tmpfiles-loadkeys-Read-var_t-symlinks.patch
Patch24:        0024-systemd-tmpfiles-create-root-and-root-.ssh.patch
Patch25:        0025-kernel-Exec-systemctl.patch
Patch26:        0026-getty-grant-checkpoint_restore.patch
Patch27:        0027-systemd-Add-basic-systemd-analyze-rules.patch
Patch28:        0028-cloudinit-Add-support-for-cloud-init-growpart.patch
Patch29:        0029-filesystem-systemd-memory.pressure-fixes.patch
Patch30:        0030-init-Add-homectl-dbus-access.patch
Patch31:        0031-Temporary-workaround-for-memory.pressure-labeling-is.patch
Patch32:        0032-rpm-Fixes-from-various-post-scripts.patch
Patch33:        0033-kmod-fix-for-run-modprobe.d.patch
Patch34:        0034-systemd-Fix-dac_override-use-in-systemd-machine-id-s.patch
Patch35:        0035-rpm-Run-systemd-sysctl-from-post.patch
Patch36:        0036-fstools-Add-additional-perms-for-cloud-utils-growpar.patch
Patch37:        0037-docker-Fix-dockerc-typo-in-container_engine_executab.patch
Patch38:        0038-enable-liveos-iso-flow.patch
Patch41:        0041-rpm-Allow-gpg-agent-run-in-rpm-scripts-to-watch-secr.patch
BuildRequires:  bzip2
BuildRequires:  checkpolicy >= %{CHECKPOLICYVER}
BuildRequires:  m4
BuildRequires:  policycoreutils-devel >= %{POLICYCOREUTILSVER}
BuildRequires:  python3
BuildRequires:  python3-xml
Requires(pre):  coreutils
Requires(pre):  policycoreutils >= %{POLICYCOREUTILSVER}
Provides:       selinux-policy-base
Provides:       selinux-policy-targeted
BuildArch:      noarch

%description
SELinux policy describes security properties of system components, to be
enforced by the kernel when running with SELinux enabled.

%files
%license COPYING
%dir %{_usr}/share/selinux
%dir %{_usr}/share/selinux/packages
%dir %{_sysconfdir}/selinux
%ghost %config(noreplace) %{_sysconfdir}/selinux/config
%ghost %{_sysconfdir}/sysconfig/selinux
%{_datadir}/selinux/%{policy_name}
%dir %{_sysconfdir}/selinux/%{policy_name}
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/selinux/%{policy_name}/seusers
%dir %{_sysconfdir}/selinux/%{policy_name}/logins
%dir %{_sharedstatedir}/selinux/%{policy_name}/active
%verify(not md5 size mtime) %{_sharedstatedir}/selinux/%{policy_name}/semanage.read.LOCK
%verify(not md5 size mtime) %{_sharedstatedir}/selinux/%{policy_name}/semanage.trans.LOCK
%dir %attr(700,root,root) %dir %{_sharedstatedir}/selinux/%{policy_name}/active/modules
%verify(not md5 size mtime) %{_sharedstatedir}/selinux/%{policy_name}/active/modules/100/base
%dir %{_sysconfdir}/selinux/%{policy_name}/policy/
%verify(not md5 size mtime) %{_sysconfdir}/selinux/%{policy_name}/policy/policy.*
%dir %{_sysconfdir}/selinux/%{policy_name}/contexts
%config %{_sysconfdir}/selinux/%{policy_name}/contexts/customizable_types
%config(noreplace) %{_sysconfdir}/selinux/%{policy_name}/contexts/securetty_types
%config(noreplace) %{_sysconfdir}/selinux/%{policy_name}/contexts/dbus_contexts
%config %{_sysconfdir}/selinux/%{policy_name}/contexts/x_contexts
%config %{_sysconfdir}/selinux/%{policy_name}/contexts/default_contexts
%config %{_sysconfdir}/selinux/%{policy_name}/contexts/virtual_domain_context
%config %{_sysconfdir}/selinux/%{policy_name}/contexts/virtual_image_context
%config %{_sysconfdir}/selinux/%{policy_name}/contexts/lxc_contexts
%config %{_sysconfdir}/selinux/%{policy_name}/contexts/sepgsql_contexts
%config %{_sysconfdir}/selinux/%{policy_name}/contexts/openrc_contexts
%config(noreplace) %{_sysconfdir}/selinux/%{policy_name}/contexts/default_type
%config(noreplace) %{_sysconfdir}/selinux/%{policy_name}/contexts/failsafe_context
%config(noreplace) %{_sysconfdir}/selinux/%{policy_name}/contexts/initrc_context
%config(noreplace) %{_sysconfdir}/selinux/%{policy_name}/contexts/removable_context
%config(noreplace) %{_sysconfdir}/selinux/%{policy_name}/contexts/userhelper_context
%dir %{_sysconfdir}/selinux/%{policy_name}/contexts/files
%verify(not md5 size mtime) %{_sysconfdir}/selinux/%{policy_name}/contexts/files/file_contexts
%ghost %{_sysconfdir}/selinux/%{policy_name}/contexts/files/file_contexts.bin
%verify(not md5 size mtime) %{_sysconfdir}/selinux/%{policy_name}/contexts/files/file_contexts.homedirs
%ghost %{_sysconfdir}/selinux/%{policy_name}/contexts/files/file_contexts.homedirs.bin
%config(noreplace) %{_sysconfdir}/selinux/%{policy_name}/contexts/files/file_contexts.local
%ghost %{_sysconfdir}/selinux/%{policy_name}/contexts/files/file_contexts.local.bin
%config(noreplace) %{_sysconfdir}/selinux/%{policy_name}/contexts/files/file_contexts.subs
%{_sysconfdir}/selinux/%{policy_name}/contexts/files/file_contexts.subs_dist
%config %{_sysconfdir}/selinux/%{policy_name}/contexts/files/media
%dir %{_sysconfdir}/selinux/%{policy_name}/contexts/users
%config(noreplace) %{_sysconfdir}/selinux/%{policy_name}/contexts/users/root
%config(noreplace) %{_sysconfdir}/selinux/%{policy_name}/contexts/users/guest_u
%config(noreplace) %{_sysconfdir}/selinux/%{policy_name}/contexts/users/xguest_u
%config(noreplace) %{_sysconfdir}/selinux/%{policy_name}/contexts/users/user_u
%config(noreplace) %{_sysconfdir}/selinux/%{policy_name}/contexts/users/staff_u
%config(noreplace) %{_sysconfdir}/selinux/%{policy_name}/contexts/users/unconfined_u
%config(noreplace) %{_sysconfdir}/selinux/%{policy_name}/contexts/users/xdm
%{_sharedstatedir}/selinux/%{policy_name}/active/commit_num
%{_sharedstatedir}/selinux/%{policy_name}/active/users_extra
%{_sharedstatedir}/selinux/%{policy_name}/active/homedir_template
%{_sharedstatedir}/selinux/%{policy_name}/active/seusers
%{_sharedstatedir}/selinux/%{policy_name}/active/file_contexts
%{_sharedstatedir}/selinux/%{policy_name}/active/modules_checksum
%exclude %{_sharedstatedir}/selinux/%{policy_name}/active/policy.kern
%verify(not md5 size mtime) %{_sharedstatedir}/selinux/%{policy_name}/active/file_contexts.homedirs
%{_sharedstatedir}/selinux/%{policy_name}/active/modules/100/*

%package modules
Summary:        SELinux policy modules
Requires:       selinux-policy = %{version}-%{release}
Requires(pre):  selinux-policy = %{version}-%{release}

%description modules
Additional SELinux policy modules -- deprecated: all policy modules are now
in selinux-policy.  This package will be removed in Azure Linux 4.0.

%files modules

%package devel
Summary:        SELinux policy devel
Requires:       %{_bindir}/make
Requires:       checkpolicy >= %{CHECKPOLICYVER}
Requires:       m4
Requires:       selinux-policy = %{version}-%{release}
Requires(post): policycoreutils-devel >= %{POLICYCOREUTILSVER}

%description devel
SELinux policy development and man page package

%files devel
%dir %{_usr}/share/selinux/devel
%dir %{_usr}/share/selinux/devel/include
%{_rpmconfigdir}/macros.d/macros.selinux-policy
%{_usr}/share/selinux/devel/include/*
%{_usr}/share/selinux/devel/Makefile
%{_usr}/share/selinux/devel/example.*
%{_usr}/share/selinux/devel/policy.*
%ghost %{_sharedstatedir}/sepolgen/interface_info

%post devel
selinuxenabled && %{_bindir}/sepolgen-ifgen 2>/dev/null
exit 0

%package doc
Summary:        SELinux policy documentation
Requires:       selinux-policy = %{version}-%{release}
Requires(pre):  selinux-policy = %{version}-%{release}

%description doc
SELinux policy documentation package

%files doc
%{_mandir}/man*/*
%{_mandir}/ru/*/*
%doc %{_usr}/share/doc/%{name}

%define common_makeopts DISTRO=%{distro} MONOLITHIC=%{monolithic} DESTDIR=%{buildroot} SYSTEMD=y DIRECT_INITRC=n MLS_CATS=1024 MCS_CATS=1024

%define makeCmds() \
%make_build UNK_PERMS=%{4} NAME=%{1} TYPE=%{2} UBAC=%{3} %{common_makeopts} bare \
install -m0644 %{_sourcedir}/modules_%{1}.conf policy/modules.conf \
%make_build UNK_PERMS=%{4} NAME=%{1} TYPE=%{2} UBAC=%{3} %{common_makeopts} conf \
install -m0644 %{_sourcedir}/booleans_%{1}.conf policy/booleans.conf

%define installCmds() \
%make_build UNK_PERMS=%{4} NAME=%{1} TYPE=%{2} UBAC=%{3} %{common_makeopts} base.pp \
%make_build validate UNK_PERMS=%{4} NAME=%{1} TYPE=%{2} UBAC=%{3} %{common_makeopts} modules \
make UNK_PERMS=%{4} NAME=%{1} TYPE=%{2} UBAC=%{3} %{common_makeopts} install \
make UNK_PERMS=%{4} NAME=%{1} TYPE=%{2} UBAC=%{3} %{common_makeopts} install-appconfig \
make UNK_PERMS=%{4} NAME=%{1} TYPE=%{2} UBAC=%{3} SEMODULE="semodule -p %{buildroot} -X 100 " load \
mkdir -p %{buildroot}/%{_sysconfdir}/selinux/%{1}/logins \
touch %{buildroot}%{_sysconfdir}/selinux/%{1}/contexts/files/file_contexts.subs \
install -m0644 config/appconfig-%{2}/securetty_types %{buildroot}%{_sysconfdir}/selinux/%{1}/contexts/securetty_types \
install -m0644 config/file_contexts.subs_dist %{buildroot}%{_sysconfdir}/selinux/%{1}/contexts/files \
touch %{buildroot}%{_sysconfdir}/selinux/%{1}/contexts/files/file_contexts.bin \
touch %{buildroot}%{_sysconfdir}/selinux/%{1}/contexts/files/file_contexts.local \
touch %{buildroot}%{_sysconfdir}/selinux/%{1}/contexts/files/file_contexts.local.bin \
rm -f %{buildroot}/%{_usr}/share/selinux/%{1}/*pp*  \
rm -rf %{buildroot}%{_sysconfdir}/selinux/%{1}/contexts/netfilter_contexts  \
rm -rf %{buildroot}%{_sysconfdir}/selinux/%{1}/modules/active/policy.kern \
rm -f %{buildroot}%{_sharedstatedir}/selinux/%{1}/active/*.linked \
%{nil}
%define relabel() \
. %{_sysconfdir}/selinux/config; \
FILE_CONTEXT=%{_sysconfdir}/selinux/%{1}/contexts/files/file_contexts; \
%{_sbindir}/selinuxenabled; \
if [ $? = 0  -a "${SELINUXTYPE}" = %{1} -a -f ${FILE_CONTEXT}.pre ]; then \
     /sbin/fixfiles -C ${FILE_CONTEXT}.pre restore; \
     rm -f ${FILE_CONTEXT}.pre; \
fi; \
if /sbin/restorecon -e /run/media -R /root %{_var}/log %{_var}/run %{_sysconfdir}/passwd* %{_sysconfdir}/group* %{_sysconfdir}/*shadow* ;then \
    continue; \
fi;
%define preInstall() \
if [ -s %{_sysconfdir}/selinux/config ]; then \
     . %{_sysconfdir}/selinux/config; \
     FILE_CONTEXT=%{_sysconfdir}/selinux/%{1}/contexts/files/file_contexts; \
     if [ "${SELINUXTYPE}" = %{1} -a -f ${FILE_CONTEXT} ]; then \
        [ -f ${FILE_CONTEXT}.pre ] || cp -f ${FILE_CONTEXT} ${FILE_CONTEXT}.pre; \
     fi; \
     if [ -d %{_sysconfdir}/selinux/%{1} ]; then \
        touch %{_sysconfdir}/selinux/%{1}/.rebuild; \
     fi; \
fi;
%define postInstall() \
. %{_sysconfdir}/selinux/config; \
if [ -e %{_sysconfdir}/selinux/%{2}/.rebuild ]; then \
   rm %{_sysconfdir}/selinux/%{2}/.rebuild; \
   %{_sbindir}/semodule -B -n -s %{2}; \
fi; \
[ "${SELINUXTYPE}" == "%{2}" ] && selinuxenabled && load_policy; \
if [ %{1} -eq 1 ]; then \
   /sbin/restorecon -R /root %{_var}/log /run %{_sysconfdir}/passwd* %{_sysconfdir}/group* %{_sysconfdir}/*shadow* ; \
else \
%relabel %{2} \
fi;

%prep
%autosetup -p1 -n refpolicy

%install
# Build policy
mkdir -p %{buildroot}%{_sysconfdir}/selinux
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
touch %{buildroot}%{_sysconfdir}/selinux/config
touch %{buildroot}%{_sysconfdir}/sysconfig/selinux
mkdir -p %{buildroot}%{_usr}/lib/tmpfiles.d/
mkdir -p %{buildroot}%{_bindir}

# Always create policy module package directories
mkdir -p %{buildroot}%{_usr}/share/selinux/%{policy_name}
mkdir -p %{buildroot}%{_sharedstatedir}/selinux/{%{policy_name},modules}/

mkdir -p %{buildroot}%{_usr}/share/selinux/packages

mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
install -m 644 %{SOURCE4} %{buildroot}%{_rpmconfigdir}/macros.d/macros.selinux-policy
sed -i 's/SELINUXPOLICYVERSION/%{version}-%{release}/' %{buildroot}%{_rpmconfigdir}/macros.d/macros.selinux-policy
sed -i 's@SELINUXSTOREPATH@%{_sharedstatedir}/selinux@' %{buildroot}%{_rpmconfigdir}/macros.d/macros.selinux-policy

# Install devel
make clean
%makeCmds targeted mcs n allow
%installCmds targeted mcs n allow

# remove leftovers when save-previous=true (semanage.conf) is used
rm -rf %{buildroot}%{_sharedstatedir}/selinux/%{policy_name}/previous

mkdir -p %{buildroot}%{_mandir}
cp -R  man/* %{buildroot}%{_mandir}
make UNK_PERMS=allow NAME=%{policy_name} TYPE=mcs UBAC=%{3} PKGNAME=%{name} %{common_makeopts} install-docs
make UNK_PERMS=allow NAME=%{policy_name} TYPE=mcs UBAC=%{3} PKGNAME=%{name} %{common_makeopts} install-headers
mkdir %{buildroot}%{_usr}/share/selinux/devel/
mv %{buildroot}%{_usr}/share/selinux/%{policy_name}/include %{buildroot}%{_usr}/share/selinux/devel/include
install -m 644 %{SOURCE1} %{buildroot}%{_usr}/share/selinux/devel/Makefile
install -m 644 doc/example.* %{buildroot}%{_usr}/share/selinux/devel/
install -m 644 doc/policy.* %{buildroot}%{_usr}/share/selinux/devel/

%post
if [ ! -s %{_sysconfdir}/selinux/config ]; then
# Permissive by default.  Enforcing support will be added in a later phase
echo "
# This file controls the state of SELinux on the system.
# SELINUX= can take one of these three values:
#     enforcing - SELinux security policy is enforced.
#     permissive - SELinux prints warnings instead of enforcing.
#     disabled - No SELinux policy is loaded.
SELINUX=permissive
# SELINUXTYPE= defines the policy to load
#     Currently the only supported option is %{policy_name}
SELINUXTYPE=%{policy_name}

" > %{_sysconfdir}/selinux/config

     ln -sf ../selinux/config %{_sysconfdir}/sysconfig/selinux
     restorecon %{_sysconfdir}/selinux/config || :
else
     . %{_sysconfdir}/selinux/config
fi
%postInstall $1 %{policy_name}
exit 0

%postun
if [ $1 = 0 ]; then
     setenforce 0 2> /dev/null
     if [ ! -s %{_sysconfdir}/selinux/config ]; then
          echo "SELINUX=disabled" > %{_sysconfdir}/selinux/config
     else
          sed -i 's/^SELINUX=.*/SELINUX=disabled/g' %{_sysconfdir}/selinux/config
     fi
fi
exit 0

%pre
%preInstall %{policy_name}

%triggerin -- pcre
selinuxenabled && semodule -nB
exit 0
%changelog
* Fri Apr 04 2025 Chris PeBenito <chpebeni@microsoft.com> - 2.20240226-11
- Add fix for gpg-agent use in rpm scripts for watching root's secrets dir.

* Thu Mar 06 2025 Chris PeBenito <chpebeni@microsoft.com> - 2.20240226-10
- Add tmpfs fix for cloud-utils-growpart.

* Wed Nov 20 2024 George Mileka <gmileka@microsoft.com> - 2.20240226-9
- Enable SELinux for LiveOS ISO.

* Wed Sep 11 2024 Chris PeBenito <chpebeni@microsoft.com> - 2.20240226-8
- Add additional required permissions for cloud-utils-growpart.
- Cherry-pick upstream fix for typo in docker module.

* Tue Aug 13 2024 Chris PeBenito <chpebeni@microsoft.com> - 2.20240226-7
- Change policy composition so the base module only consits of policy modules
  that must be in the base.  This will allow dowstream users to disable or
  override the individual policy modules.

* Thu Jul 18 2024 Chris PeBenito <chpebeni@microsoft.com> - 2.20240226-6
- Drop rules that are specific to AzureLinux testing systems.
- Add fix for systemd-machine-id-setup CAP_DAC_OVERRIDE use.
- Run systemd-sysctl from RPM scripts.

* Tue Jul 16 2024 Chris PeBenito <chpebeni@microsoft.com> - 2.20240226-5
- Change unconfined to a separate module so it can be disabled.

* Mon Jul 01 2024 Chris PeBenito <chpebeni@microsoft.com> - 2.20240226-4
- Add cloud-init and kmod fixes.

* Tue May 14 2024 Chris PeBenito <chpebeni@microsoft.com> - 2.20240226-3
- Fix systemd-analyze issues.
- Add selinux-policy-modules to selinux.json package list since it has rules for cloud-init
- Add fixes and new systemd access to memory.pressure
- Remove redirections in %post to make it easier to debug issues

* Mon Mar 25 2024 Chris PeBenito <chpebeni@microsoft.com> - 2.20240226-2
- Add fixes from BVTs
- Add new systemd pidfd uses
- Add new pressure stall information in systemd
- Fixes for systemd-tmpfiles and loadkeys

* Tue Mar 12 2024 Chris PeBenito <chpebeni@microsoft.com> - 2.20240226-1
- Rebase to upstream release 2.20240226.

* Fri Dec 15 2023 Aditya Dubey <adityadubey@microsoft.com> - 2.20221101-6
- Adding modules_checksum file
- removed exclude for policy.linked, seusers.linked, and users_extra.linked files

* Tue Oct 17 2023 Chris PeBenito <chpebeni@microsoft.com> - 2.20221101-5
- Silence noise in containerd io.containerd.internal.v1.opt plugin.

* Thu Sep 28 2023 Chris PeBenito <chpebeni@microsoft.com> - 2.20221101-4
- Cherry pick systemd-hostnamed fix for handling /run/systemd/default-hostname.

* Tue May 16 2023 Chris PeBenito <chpebeni@microsoft.com> - 2.20221101-3
- Fix missing role associations in cloud-init patch.
- Fix missing require in mkinitrd patch.

* Tue Apr 11 2023 Chris PeBenito <chpebeni@microsoft.com> - 2.20221101-2
- Handle non-standard location for iptables rules configuration.
- Add further cloud-init permissions to handle a wider variety of use cases
  without requiring policy changes.
- Fix scheduled shutdown/reboot.
- Add temporary fix for mkinitrd issues until final implementation is ready.

* Wed Mar 01 2023 Chris PeBenito <chpebeni@microsoft.com> - 2.20221101-1
- Update to new upstream release.
- Fix iscsid access to initiatorname.iscsi.
- Add file context for /etc/multipath/*
- Handle /media and /srv symlinks.
- Add cloud-init support for installing RPMs and setting passwords.
- Port tomcat and pki modules from the Fedora policy.
- Fix running dracut in RPM scripts.

* Fri Nov 11 2022 Pawel Winogrodzki <pawelwi@microsoft.com> - 2.20220106-12
- Added 'selinux-policy' RPM macros.

* Wed Sep 14 2022 Chris PeBenito <chpebeni@microsoft.com> - 2.20220106-11
- Fix issue with preinst on systems that do not have selinux-policy.

* Tue Jul 19 2022 Chris PeBenito <chpebeni@microsoft.com> - 2.20220106-10
- Fixed denials during coredump.
- Allow NoNewPerms transition from init scripts/systemd unit commands.
- Minor fixes in semanage, ifconfig, rpm, and useradd.
- Fix incorrect label for kubernetes runtime dir when created by initrc_t.

* Tue Jul 19 2022 Chris PeBenito <chpebeni@microsoft.com> - 2.20220106-9
- Fixes for interactive container use.

* Thu Jul 07 2022 Chris PeBenito <chpebeni@microsoft.com> - 2.20220106-8
- Add sysctl access for groupadd and systemd-cgroups
- Allow access for hv_utils shutdown sequence access to poweroff.target.

* Wed Jun 15 2022 Chris PeBenito <chpebeni@microsoft.com> - 2.20220106-7
- Unconfined domains can manipulate thier own fds.

* Mon May 23 2022 Chris PeBenito <chpebeni@microsoft.com> - 2.20220106-6
- Fix previous multipath LVM changes.
- Add types for devices.
- Cherry pick upstream commit for container fds.
- Allow container engines to connect to http cache ports.
- Allow container engines to stat() generic (device_t) devices.

* Mon May 02 2022 Chris PeBenito <chpebeni@microsoft.com> - 2.20220106-5
- Additional compatibility for Fedora container-selinux.
- Remove unneeded systemd_run_t domain
- Updates for multipath LVM
- Fix for console logins
- New type for SAS management devices

* Fri Apr 29 2022 Pawel Winogrodzki <pawelwi@microsoft.com> - 2.20220106-4
- Fixing source URL.

* Mon Mar 14 2022 Chris PeBenito <chpebeni@microsoft.com> - 2.20220106-3
- Additional policy fixes for enforcing core images.

* Tue Mar 08 2022 Chris PeBenito <chpebeni@microsoft.com> - 2.20220106-2
- Split policy modules to a subpackage. Keep core images supported by
  base module.
- Update systemd-homed and systemd-userdbd patch to upstreamed version.
- Backport containers policy.

* Mon Jan 10 2022 Chris PeBenito <chpebeni@microsoft.com> - 2.20220106-1
- Update to version 2.20220106.
- Fix setup process to apply patches.
- Correct files listing to include the module store files.
- Create a booleans.conf for the build process, to override upstream Boolean
  default values.
- Fix build to include systemd rules.

* Tue Sep 07 2021 Chris PeBenito <chpebeni@microsoft.com> - 2.20210203-1
- Update to newest refpolicy release.  Add policy changes to boot the system
  in enforcing.  Change policy name to targeted.  Remove unrelated changelog
  entries from selinux-policy. The spec file uses the Fedora spec file as
  guidance, but does not use the Fedora's policy. The Fedora policy is a hard
  fork Reference Policy, so the changes are not related and the version numbers
  are incomparable.

* Fri Aug 13 2021 Thomas Crain <thcrain@microsoft.com> - 2.20200818-2
- Update versions on checkpolicy, policycoreutils dependencies

* Mon Aug 31 2020 Daniel Burgener <daburgen@microsoft.com> - 2.20200818-1
- Initial CBL-Mariner import from Fedora 31 (license: MIT)
- Heavy modifications to build from upstream reference policy rather than from fedora selinux policy.
  Fedora's policy and versioning tracks their policy fork specificially, whereas this tracks the upstream
  policy that Fedora's policy is based on.
- License verified
