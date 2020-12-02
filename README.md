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


5. image ocr with box output

```
(base) root@zedou23khwxd3fj8Z:~# tesseract 07.jpg  out2 makebox -l eng+chi_sim
```

**issue:** cannot recognize chinese character by cmd above.


run `main.py` to get output with box for each word.


6. other ocr cmd

```
(ocr_word_detect_py36) root@zedou23khwxd3fj8Z:/home/ocr/ocr_ing/tesseract_test# tesseract -l chi_sim test_data.png out_test_data
```

