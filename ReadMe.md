# このソフトウェアについて

Python音楽理論ライブラリの細かい点を修正した。

## 修正点

* PitchClass.py
    * `_PitchClass`を`__PitchClass`に修正した
* Accidental.py
    * `Accidentals`のキー`None`, `''`を削除した
* Degree.py
    * `_Pattern`を`__Pattern`に修正した
    * `r'[1-9][0-9]*'`を`r'[0-9]{1,}'`に修正した
        * degreeが`0`のときのエラーが`引数nameに有効な数字が含まれていません。`だったのを`degreeは1〜14までの自然数のみ有効です。`になるようになった（エラーがわかりやすい）
* Interval.py
    * `_PatternFormat`を`__PatternFormat`に修正した
    * `_Pattern`を`__Pattern`に修正した
    * `r'(?P<prefix>[P|M|m|a|d])(?P<degree>[1-9][0-9]?)'`を`r'(?P<prefix>[P|M|m|a|d])(?P<degree>[0-9]{1,})'`に修正した
        * degreeが`0`のときのエラーが`引数nameが有効な書式ではありません。`だったのを`degreeは1〜14までの自然数にしてください。`になるようになった（エラーがわかりやすい）

## 前回まで

* https://github.com/ytyaru/Python.MusicTheory.Chord.Triad.201709071957
* https://github.com/ytyaru/Python.MusicTheory.Pitch.201709131752
* https://github.com/ytyaru/Python.MusicTheory.Pitch.201709131811
* https://github.com/ytyaru/Python.MusicTheory.Pitch.201709132015
* https://github.com/ytyaru/Python.MusicTheory.Pitch.201709132015
* https://github.com/ytyaru/Python.MusicTheory.Pitch.201709141450
* https://github.com/ytyaru/Python.MusicTheory.Pitch.201709141657

# 実行

```sh
$ cd ./src/
$ python TestPitchClass.py
$ python TestAccidental.py
$ python TestDegree.py
$ python TestInterval.py
```

テストコード|項目数
------------|------
TestPitchClass.py|9
TestAccidental.py|9
TestDegree.py|13
TestInterval.py|16

計47項目。

# 課題

* メッセージに統一性を持たせたい
* メッセージを国際化したい

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [libav](http://ytyaru.hatenablog.com/entry/2018/08/24/000000)
    * [各コーデック](http://ytyaru.hatenablog.com/entry/2018/08/23/000000)
* [pyenv](https://github.com/pylangstudy/201705/blob/master/27/Python%E5%AD%A6%E7%BF%92%E7%92%B0%E5%A2%83%E3%82%92%E7%94%A8%E6%84%8F%E3%81%99%E3%82%8B.md) 1.0.10
    * Python 3.6.1
        * [pydub](http://ytyaru.hatenablog.com/entry/2018/08/25/000000)
        * [PyAudio](http://ytyaru.hatenablog.com/entry/2018/07/27/000000) 0.2.11
            * [ALSA lib pcm_dmix.c:1022:(snd_pcm_dmix_open) unable to open slave](http://ytyaru.hatenablog.com/entry/2018/07/29/000000)
        * [matplotlib](http://ytyaru.hatenablog.com/entry/2018/07/22/000000)
            * [matplotlibでのグラフ表示を諦めた](http://ytyaru.hatenablog.com/entry/2018/08/05/000000)

# 参考

感謝。

## Python

### 定数

* http://fakatatuku.hatenablog.com/entry/2015/03/26/233024

### サイン波のスピーカ再生

* http://www.non-fiction.jp/2015/08/17/sin_wave/
* http://aidiary.hatenablog.com/entry/20110607/1307449007
* http://ism1000ch.hatenablog.com/entry/2013/11/15/182442

## 音楽理論

### 和音

* https://ja.wikipedia.org/wiki/%E5%92%8C%E9%9F%B3
* http://www.piano-c.com/
* https://pf-j.sakura.ne.jp/music/chord.htm

### 音程

* https://ja.wikipedia.org/wiki/%E9%9F%B3%E7%A8%8B
* https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q1365320628
* https://okwave.jp/qa/q6858420.html

### 440Hz, 432Hz

* http://tabi-labo.com/156689/music-a432

### 和音の生成

* http://ism1000ch.hatenablog.com/entry/2013/11/15/182442
* https://ja.wikipedia.org/wiki/%E4%B8%89%E5%92%8C%E9%9F%B3
* https://ja.wikipedia.org/wiki/%E3%83%91%E3%83%AF%E3%83%BC%E3%82%B3%E3%83%BC%E3%83%89

### 音名

* https://ja.wikipedia.org/wiki/%E9%9F%B3%E5%90%8D%E3%83%BB%E9%9A%8E%E5%90%8D%E8%A1%A8%E8%A8%98

### 音階

* https://ja.wikipedia.org/wiki/%E9%9F%B3%E9%9A%8E

#### 五度圏

* http://dn-voice.info/music-theory/godoken/

### 音高の算出

* http://www.asahi-net.or.jp/~HB9T-KTD/music/Japan/Research/DTM/freq_map.html
* http://www.nihongo.com/aaa/chigaku/suugaku/pythagoras.htm

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

Library|License|Copyright
-------|-------|---------
[pydub](https://github.com/jiaaro/pydub)|[MIT](https://github.com/jiaaro/pydub/blob/master/LICENSE)|[Copyright (c) 2011 James Robert, http://jiaaro.com](https://github.com/jiaaro/pydub/blob/master/LICENSE)
[pygame](http://www.pygame.org/)|[LGPL](https://www.pygame.org/docs/)|[pygame](http://www.pygame.org/)

