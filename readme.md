
FizzBuzzというプログラムは、3の倍数が入力されると”Fizz”を出力し、5の倍数が入力されると”Buzz”を出力し、3の倍数でも5の倍数でもある数が入力されると”FizzBuzz”を出力します。

このプログラムはFizzBuzzの拡張として、複数の(整数i , 文字列s)のペアと一つの整数mが渡され、mがiの倍数ならsを出力するプログラムです。

- sはiの小さい順に出力してください(※iが小さい順に並んでいるとは限りません)
- どのsも出力されなければmを出力してください
- 入力は"input.txt"を読み込みます
- iとsのペアは"input.txt"に一行ずつ"i:s"形式で渡されます
- mは"input.txt"の下から２番目の行で渡されます
- "input.txt"の最終行は空行です

## 入力例と出力例

### 例1

入力 ("sample1.txt")

```txt
5:buzz
3:fizz
8:hoge
2:huga
24

```

出力

hugafizzhoge

### 例2

入力 ("sample2.txt")

```txt
3:yoshida
5:takuma
2

```

出力

2
