$ErrorActionPreference = 'Stop'
Push-Location -LiteralPath $PSScriptRoot
try {
    & xelatex -interaction=nonstopmode -halt-on-error main.tex
    if ($LASTEXITCODE -ne 0) { throw 'XeLaTeX failed.' }
    & bibtex main
    if ($LASTEXITCODE -ne 0) { throw 'BibTeX failed.' }
    & xelatex -interaction=nonstopmode -halt-on-error main.tex
    if ($LASTEXITCODE -ne 0) { throw 'XeLaTeX failed.' }
    & xelatex -interaction=nonstopmode -halt-on-error main.tex
    if ($LASTEXITCODE -ne 0) { throw 'XeLaTeX failed.' }
    Copy-Item -LiteralPath 'main.pdf' -Destination '从笔记到论文_LaTeX数学排版实战指南_修订版.pdf' -Force
}
finally { Pop-Location }
