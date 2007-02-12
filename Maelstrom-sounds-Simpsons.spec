Summary:	Rockin' asteroids game - extra sounds
Summary(pl.UTF-8):   Gra, w której strzelasz do asteroidów - dodatkowe dźwięki
Name:		Maelstrom-sounds-Simpsons
Version:	1
Release:	1
License:	unknown
Group:		X11/Applications/Games
# Source0-md5:	74ddb0be0daa5aa7e546cb764a731c9a
Source0:	http://www.devolution.com/~slouken/projects/Maelstrom/add-ons/Extra_Sounds.zip
URL:		http://www.devolution.com/~slouken/projects/Maelstrom/add-ons.html
Requires:	Maelstrom
Obsoletes:	Maelstrom-sounds
Obsoletes:	Maelstrom-sounds-AoD
Obsoletes:	Maelstrom-sounds-BB
Obsoletes:	Maelstrom-sounds-Funky
Obsoletes:	Maelstrom-sounds-Martin
Obsoletes:	Maelstrom-sounds-Stooges
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_gamedir	%{_datadir}/Maelstrom

%description
Extra sounds for Maelstrom.

%description -l pl.UTF-8
Dźwięki dla Maelstroma.

%prep
%setup -q -n NewSounds

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_gamedir}

install Simpsons_Sounds $RPM_BUILD_ROOT%{_gamedir}/"%Maelstrom_Sounds"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_gamedir}/*
