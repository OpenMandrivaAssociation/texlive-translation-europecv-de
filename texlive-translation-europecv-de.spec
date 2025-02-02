Name:		texlive-translation-europecv-de
Version:	23840
Release:	2
Summary:	German version of europecv
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/translations/europecv/de
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-europecv-de.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-europecv-de.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This is a "translation" of the europecv documentation.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/translation-europecv-de/Beispiele/at.pdf
%doc %{_texmfdistdir}/doc/latex/translation-europecv-de/Beispiele/bulgarian-koi8-r.tex
%doc %{_texmfdistdir}/doc/latex/translation-europecv-de/Beispiele/bulgarian-utf8.tex
%doc %{_texmfdistdir}/doc/latex/translation-europecv-de/Beispiele/greek-utf8.pdf
%doc %{_texmfdistdir}/doc/latex/translation-europecv-de/Beispiele/greek-utf8.tex
%doc %{_texmfdistdir}/doc/latex/translation-europecv-de/Beispiele/maltese-maltese.tex
%doc %{_texmfdistdir}/doc/latex/translation-europecv-de/Beispiele/maltese-utf8.tex
%doc %{_texmfdistdir}/doc/latex/translation-europecv-de/Beispiele/minimal.pdf
%doc %{_texmfdistdir}/doc/latex/translation-europecv-de/Beispiele/minimal.tex
%doc %{_texmfdistdir}/doc/latex/translation-europecv-de/europecv-de.pdf
%doc %{_texmfdistdir}/doc/latex/translation-europecv-de/europecv-de.tex
%doc %{_texmfdistdir}/doc/latex/translation-europecv-de/templates/cv_template_de.pdf
%doc %{_texmfdistdir}/doc/latex/translation-europecv-de/templates/cv_template_de.tex
%doc %{_texmfdistdir}/doc/latex/translation-europecv-de/templates/cv_template_en.pdf
%doc %{_texmfdistdir}/doc/latex/translation-europecv-de/templates/cv_template_en.tex
%doc %{_texmfdistdir}/doc/latex/translation-europecv-de/templates/cv_template_it.pdf
%doc %{_texmfdistdir}/doc/latex/translation-europecv-de/templates/cv_template_it.tex
%doc %{_texmfdistdir}/doc/latex/translation-europecv-de/templates/cv_template_pl.pdf
%doc %{_texmfdistdir}/doc/latex/translation-europecv-de/templates/cv_template_pl.tex
%doc %{_texmfdistdir}/doc/latex/translation-europecv-de/templates/publications.bib

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
