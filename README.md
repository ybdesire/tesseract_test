# tesseract_test
test tesseract at ubuntu

# steps

1. install tesseract

```
(base) root@zedou23khwxd3fj8Z:~# apt install tesseract-ocr
```

2. install chinese lang

```
(base) root@zedou23khwxd3fj8Z:~# apt-get install tesseract-ocr-chi-sim

```

3. check installed languages

```
(base) root@zedou23khwxd3fj8Z:/home/ocr/ocr_ing/tesseract_test# tesseract --list-langs
List of available languages (3):
osd
chi_sim
eng
```

4. image ocr

```
(base) root@zedou23khwxd3fj8Z:~# tesseract 07.jpg  out -l eng+chi_sim
```
