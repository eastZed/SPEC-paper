# 定义变量
PYTHON_FILES := $(wildcard *.py)
PDF_FILES := $(wildcard *.pdf)

# 默认目标
all: run 

# 运行所有 Python 文件
run:
	@for file in $(PYTHON_FILES); do \
        echo "Running $$file..."; \
		python3	$$file; \
        echo "$$file finished."; \
    done

# 对所有 PDF 文件运行 pdfcrop
pdfcrop:
	@for file in $(PDF_FILES); do \
        echo "Cropping $$file..."; \
        pdfcrop	$$file $$file; \
        echo "$$file cropped."; \
    done

fig:
	# mv -f *.pdf ../../../fig/	
	mv -f *.pdf ../../	
clean: 
	rm -rf *.eps *.pdf