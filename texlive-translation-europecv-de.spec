# revision 23840
# category Package
# catalog-ctan /info/translations/europecv/de
# catalog-date 2011-09-05 11:34:40 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-translation-europecv-de
Version:	20110905
Release:	6
Summary:	German version of europecv
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/europecv/de
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-europecv-de.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-europecv-de.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110905-2
+ Revision: 757083
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110905-1
+ Revision: 719798
- texlive-translation-europecv-de
- texlive-translation-europecv-de
- texlive-translation-europecv-de

