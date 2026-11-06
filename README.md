# 从笔记到论文 · LaTeX 数学排版实战指南

雪落长安无声｜修订版

一本 60 页的中文 LaTeX 实战教程，写给想整理数学复习笔记、准备数学建模竞赛，或第一次用 LaTeX 写论文的同学。

**[下载修订版 PDF](https://github.com/qkl12041016s/latex-math-typesetting-guide/releases/latest)**

## 书里有什么

- **数学笔记**：从中文导言区开始，排公式、矩阵、分段函数、三线表和自定义知识框。
- **一章完整实战**：把微积分基本定理、最小二乘和概率计算编进同一份笔记，沿着公式和条件复核推导。
- **数模论文排版**：练习摘要页、对比子图、带行号的算法和中文参考文献。正式参赛时请核对当届主办方的格式要求。
- **可以自己改的示例**：原有 14 段源码及本次新增的 3 个独立示例都在仓库里，也附在对应的 PDF 清单旁。支持附件的 PDF 阅读器可以直接提取原始文件。

## 2026-11-07 内容修订 · v1.1.0

书名保持不变，新增内容包括：

- 第8章增加独立的BibLaTeX/Biber国标样式小样，与整书原有gbt7714/BibTeX流程分别说明。
- 第9章增加Beamer数学答辩模板与主题、覆盖层、fragile帧的说明。
- 补充minted/Pygments、ctex行距单一入口与常见宏包冲突排查。

[examples/revision](examples/revision)下的Biber、Beamer、minted三个示例均实际编译。整书不依赖minted或shell escape。详见[修订记录](docs/revision-20261107.md)。

## 从哪里开始

| 目的 | 入口 |
| --- | --- |
| 编译整书 | [main.tex](main.tex) 和 [preamble.tex](preamble.tex) |
| 试一份完整中文模板 | [第一章模板](examples/ch01/01_example.tex) |
| 看一章如何组合公式、图表和知识框 | [第六章独立示例](clean_chapters/ch06.tex) |
| 练习中文文献与编译排错 | [第八章独立示例](clean_chapters/ch08.tex) |
| 查其余示例 | [examples](examples) 和 [clean_chapters](clean_chapters) |

## 本地编译

已在 TeX Live 2024 下验证。请安装 CTeX、Fandol 和源码中加载的宏包。整书使用 **XeLaTeX + BibTeX**，在仓库根目录依次运行：

    xelatex -interaction=nonstopmode -halt-on-error main.tex
    bibtex main
    xelatex -interaction=nonstopmode -halt-on-error main.tex
    xelatex -interaction=nonstopmode -halt-on-error main.tex

Windows 也可以直接运行 [build.ps1](build.ps1)。整书和第八章示例使用 TeX Live 2024 随附的 gbt7714 样式名 gbt7714-numerical。使用 gbt7714 3.1.1 时，可按宏包说明改为 gbt7714-numeric。

独立示例在各自的目录里运行 XeLaTeX。交叉引用通常需要编译两遍，第八章独立示例需要上面的四步流程，并将 BibTeX 的作业名换成 ch08。

## 许可

书稿、示例文档、原创插图和 PDF 按 CC BY-NC 4.0 发布。独立的构建与绘图脚本按 MIT 发布。详见 [LICENSE](LICENSE)。
