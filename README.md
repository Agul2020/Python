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
<br />
<br />

## 4.Hangman
  ```
   +---+
   O   |
/|\  |
/ \  |
===
  ```
   &emsp;&emsp;火柴人？？吊死在路灯上的资本家？~~🐶🐶 ~~ 

   &emsp;&emsp;课本 97 页 100-105 和 106-108 行代码的缩进有问题。。。。 搞得头大~


---
 

- Python 列表是基于 0 索引的
- reverse() 相反
- append() 增补
- split() 分割
- lower() 转换为小写
- upper() 转换为大写
- startswith() 检查开头的布尔函数 
- endswith()  检查结尾的布尔函数

<br />
<br />

## 5.Hangman 扩展

- 字典是无序的，列表是有序的。
- 字典可拥有任意数据类型的键，而不仅仅是字符串类型的键。
- `choice()` 接受一个列表作为参数，并从列表中返回一个随机值。
- ` wordKey = random.choice(list(wordDict.keys()))`  
 &emsp;&emsp;将字典的 `keys` 返回为一个列表，通过 `random.choice()` 得到一个随机的 `key` 赋值给`wordKey`。这就实现了在多组单词中随机选择一组的功能。
- `wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)`  
  &emsp;&emsp;`wordDict[wordKey]` 返回字典中 `wordKey` 所对应的值，即返回一组单词。因为一组单词就是一个列表，用 `len()` 返回该列表的长度。然后，`random.randint()` 返回一个随机数赋值给 `wordIndex`

- `return [wordDict[wordKey][wordIndex], wordKey]`  
&emsp;&emsp;最后返回的是字典中一个 `key` 所对应的 `value` 中的一个 `值`和 `key`组成的列表。也就是所有单词中的一组词汇中的一个`单词` 和 `这组单词的名称`这两个结果。  

## 6.Tic tac Toe

- 当我们把列表作为参数传递给函数时，我们实际上传递的是对这个列表的引用而不是列表本身。  

- `cheess = spam` 这个列表并没有被复制，复制的是对这个列表的引用。字典也已相同的方式工作。
- 如果想让 `spam` 和 `cheese` 存储两个不同的列表，就必须创建两个不同的列表，而不是复制一个引用。
- `return board[move] == ' '` 返回一个布尔值
- 短路求值——对于 `or` 和 `and` 操作符当左边的布尔值已经可以决定整体的布尔值时，右边的语句将不会执行。

## 7.推理游戏 Bagels

- `random.shufle()` 函数随机修改元素顺序。
- `sort()` 是一个方法，它按照字母顺序或数字顺序重新排列列表中的元素。
- 以上两个都是“就地”修改 。

- 字符串方法 `join()` 将字符串列表连接起来，作为一个单个的字符串返回。
- `join()` 就像是与 `split()` 相反的字符串方法。 `split()` 方法通过分割字符串而返回一个列表，而 `join()` 返回组合列表而得到一个字符串。
- 像 `%s` 这样的占位符叫做转换说明符（convertion specifiers）。一旦放入了转换说明符，我们就可以在字符串末尾放置所有的变量名称。 每个 `%s` 都会背代码行末尾的一个变量所替换。
- 变量数目必须和 `%s` 转换说明符的数目相同。
- 插值对于任意数据类型都是有效的，而不仅仅是对字符串有效。所有值都会自动转换为字符串数据类型。
- 字符串连接只能把两个字符串组合起来。
- 字符串插值也叫字符串格式化 （string formatting）