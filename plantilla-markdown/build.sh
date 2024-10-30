# PARA EXPORTAR EN HORIZONTAL
pandoc doc1.md -o doc1.pdf --from markdown --template ../../plantilla-markdown/eisvogel --listings

# PARA EXPORTAR EN HORIZONTAL
# pandoc -V geometry:landscape doc1.md -o doc1.pdf --from markdown --template ../../plantilla-markdown/eisvogel --listings

# PARA COLORES EN TABLAS
# pandoc doc1.md -o doc1.pdf --from markdown --template ../../plantilla-markdown/eisvogel --pdf-engine=xelatex