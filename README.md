# Python 游戏编程快速上手
## 1. “猜数字”游戏

&emsp;&emsp;代码第 26 行 `guessesTaken = str(i+1)` 中 `i` 即第 11 行 `for i in range(6):` 中的 `i` , 且 `i` 的范围为 0~5 , 加上 1 之后才是玩家猜过的次数.

----

- 书中第 21 页 第 27 行中的 `i` 没有加 1 

- 第 31 页 第 27 行  `guessesTaken = str(guessesTaken)` 有错误 , `guessesTaken` 的值在定义为 0 后并没有发生变化。此处应该将 `range()` 函数的执行次数即 `i+1` 转化为字符串型并赋值给 `guessesTaken`
