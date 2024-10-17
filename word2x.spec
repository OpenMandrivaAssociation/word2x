Summary:	A tool to convert Word 6 documents to text
Name:		word2x
Version:	0.005
Release:	%mkrel 12

Source0:	%name-%version.tar.bz2
Patch0:		word2x-make.patch.bz2
Patch1:		word2x-0.005-missing-includes.patch.bz2
Patch2:		word2x-0.005-c++fixes.patch.bz2
Patch3:		word2x-fix-gcc-3.4.patch.bz2

License:	GPL
Group:		Office
URL:		https://word2x.alcom.co.uk
BuildRoot:	%_tmppath/%name-%version-%release-root

%description 
Word2x is a GPLed program for converting Word 6 documents to text
without any Microsoft software to help you, including non-microsoft
operating systems (and therefore no OLE dll's, etc).

The currently supported output formats are plain text, LaTeX and
HTML. The program converts word to a central format and output modules
write the desired target format.

%prep
%setup -q
%patch0 -p1 -b .make
%patch1 -p1 -b .missing-includes
%patch2 -p1 -b .c++fixes
%patch3 -p1 -b .fix_gcc_3_4

%build
CFLAGS="%optflags" CXXFLAGS="%optflags" \
	./configure --prefix=%buildroot/%_prefix \
		    --mandir=%buildroot/%_mandir

%make

%install
install -d %buildroot/%_bindir
install -d %buildroot/%_mandir/man1

%makeinstall

%clean
rm -fr %buildroot

%files
%defattr(-,root,root)
%doc README
%_bindir/*
%_mandir/man1/*

