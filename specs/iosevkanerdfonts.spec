%global debug_package %{nil}

Name:           iosevka-nerd-fonts
Version:       3.4.0 
Release:        1%{?dist}
Summary:   nerd fonts      

License:  MIT
URL:    https://github.com/ryanoasis/nerd-fonts      
Source0:  https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}/Iosevka.tar.xz 

%define name iosevka-nerd-fonts
%define fontdir /fonts/%{name}

%description
Nerd Fonts is a project that patches developer targeted fonts with a high number of glyphs (icons).
Specifically to add a high number of extra glyphs from popular 'iconic fonts' such as Font Awesome, Devicons, Octicons, and others.


%prep
%autosetup -c


%install
#mkdir -p %{buildroot}%{_datadir}%{fontdir}
install -m 0644 -D -t %{buildroot}%{_datadir}%{fontdir} *.ttf
# %fontinstall -a


%files
%{_datadir}/%{fontdir}


%changelog
%autochangelog
