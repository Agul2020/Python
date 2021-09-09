# Python 游戏编程快速上手

## 1. “猜数字”游戏

&emsp;&emsp;代码第 26 行 `guessesTaken = str(i+1)` 中 `i` 即第 11 行 `for i in range(6):` 中的 `i` , 且 `i` 的范围为 0~5 , 加上 1 之后才是玩家猜过的次数.

----

- 书中第 21 页 第 27 行中的 `i` 没有加 1 

- 第 31 页 第 27 行  `guessesTaken = str(guessesTaken)` 有错误 , `guessesTaken` 的值在定义为 0 后并没有发生变化。此处应该将 `range()` 函数的执行次数即 `i+1` 转化为字符串型并赋值给 `guessesTaken`

<br />
<br />

## 2.一个讲笑话程序

- 看不懂笑话ಠ_ಠ
<br />
<br />

## 3.Dragon Realm

&emsp;&emsp;程序只定义了三个函数，用了一个循环。在一开始将 `playAgain`的值设为 `yes`，在结尾由用户输入 `playAgain`的值，首尾衔接构成一个 while 循环。这样就能达成由到玩家决定是否继续游戏的效果。

---


- 当调用函数时，实参是复制到形参中的值
- 函数调用本身会把返回值作为结果