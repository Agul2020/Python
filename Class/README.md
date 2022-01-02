# Python 游戏编程快速上手

## 1. “猜数字”游戏

- 变量名区分大小写
- `import` 用于导入模块
- `randint()` 产生一个随机数字
- `for` 语句可以理解为：将如下的语句块中的代码执行一定的次数
- `语句块` Python 的函数语句块是和缩进相关的，这一点在写代码时要特别注意
- `str()` 函数返回和传递参数所对应的字符串版本
- `int()` 函数接收一个参数，并返回该参数的整数形式 
- `float()` 函数返回和传递参数所对应的浮点数版本
- `=` 是赋值号 
- `==` 是比较操作符，用于判断值是否相等，与 `!=` 相对
- 布尔数据类型只有两个值：`True` 或者 `False` 这两个值的首字母必须大写，值的剩余部分必须小写。
- `if` 语句：如果 `if` 语句的计算条件为 `True`, `if` 语句块后面的代码将会运行。如果该条件为 `False` 那么执行将会跳过 if 语句块中的代码。
- `break` 语句只会出现在循环语句中，用于跳出循环。   
    实例：

  ```python linenums="1"
  n = 5
  while n > 0:
      n -= 1
      if n == 2:
          break
      print(n)
  print('循环结束。')
  ```
  运行结果：
  ```
  4
  3
  循环结束。
  ```
- continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。   
  实例：

  ```PYTHON
  n = 5
  while n > 0:
      n -= 1
      if n == 2:
          break
      print(n)
  print('循环结束。')
  ```
    运行结果：
  ```
  4
  3
  循环结束。
  ```
  <br />
  <br />

## 2.一个讲笑话程序

- 传递给一个函数调用的值，叫做参数

- 转义字符(escape character) 使我们能够打印那些很难输入到源代码中的字符
- 常见转义字符表

    | 转义字符 | 实际打印的内容   | 
    | :---    |    :---:       |    
    | \\\     | 反斜杠 ( \\ )    | 
    | \\`     | 单引号 ( ` )     |
    |\\``     |   双引号 ( " )   |
    |\n       |     换行符       |
    | \t      |    tab           |


  (`/` 是斜杠，`\` 是反斜杠  )

- 单双引号: 在单引号字符串中，不需要转义双引号，但是需要转义单引号；双引号字符串中，不需要转义单引号，但是需要转义双引号。

- `print()` 的 `end` 关键字形参 ( keyworld parameter ) 
  通常 `print()`函数会在所打印的字符串的末尾添加一个换行符。为 `end` 传递一个空字符串。 `print()` 函数就不会在字符串的末尾添加一个换行符 。
  <br />
  <br />

## 3.Dragon Realm

&emsp;&emsp;程序只定义了三个函数，用了一个循环。在一开始将 `playAgain`的值设为 `yes`，在结尾由用户输入 `playAgain`的值，首尾衔接构成一个 while 循环。这样就能达成由到玩家决定是否继续游戏的效果。

---
- 当调用函数时，实参是复制到形参中的值
- 函数调用本身会把返回值作为结果
- 函数的 `def` 语句和 `def` 语句块必须放在该函数的调用之前
- 如果在一个字符串的开始和结尾使用了 3 个引号字符，那么，字符串就可以跨越多行了
- 一个局部变量的值不会在函数调用之间被记住
- 当程序终止时，全局作用域就销毁了，并且所有的变量也会被忘掉
- 局部变量和全局变量可以使用相同的名字，但是他们时不同变量，但是他们是不同变量， 因为他们在不同作用域之中

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



---

- 常量 (constant) 是在一次赋值之后其值就不再变化的变量
- Python 列表是基于 0 索引的 (zero-indexed)
- `in` 操作符可以告诉我们，一个值是否在一个列表中。使用 `in` 操作符的表达式会返回一个布尔值
- 在 `if-slif-else` 的语句中，**有且只有一个**语句块会执行
- **访问列表里的值**   
    实例：
  
  ```python
  list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
  print( list[0] )
  print( list[1] )
  print( list[2] )
  ```
  运行结果：
  ```
  red
  green
  blue
  ```
  
- 字符串方法

    |方法名         | 作用               |
    | :-----------  | :-----------:        | 
    | `reverse()`    |  相反            |
    | `append()`     | 增补             |
    | `split()`      | 分割             |
    | `lower()`      | 转换为小写        |
    | `upper()`      |转换为大写         |
    | `startswith()` | 检查开头的布尔函数 |
    | `endswith()`   | 检查结尾的布尔函数 |

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
- **访问字典里的值**  
  实例：  
  ```python
  dict = {'Name': 'Agul', 'Age': 7, 'Class': 'First'}
  print ("dict['Name']: ", dict['Name'])
  print ("dict['Age']: ", dict['Age'])
  ```
  运行结果：
  ```
  dict['Name']:  Agul
  dict['Age']:  7
  ```
- **字典键的特性**  
  1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
  ```python
  dict = {'Name': 'agul', 'Age': 7, 'Name': '阿古茹'}
  
  print ("dict['Name']: ", dict['Name'])
  ```
    以上代码的输出结果：
  ```
  dict['Name']:  阿古茹
  ```
   2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：
  ```python
  dict = {['Name']: 'agul', 'Age': 7}
   
  print ("dict['Name']: ", dict['Name'])
  ```
  以上实例输出结果：
  ```
  Traceback (most recent call last):
    File "test.py", line 2, in <module>
      dict = {['Name']: 'agul', 'Age': 7}
  TypeError: unhashable type: 'list'
  ```

<br />
<br />

## 6.Tic tac Toe

- 当我们把列表作为参数传递给函数时，我们实际上传递的是对这个列表的引用而不是列表本身。  

- `cheess = spam` 这个列表并没有被复制，复制的是对这个列表的引用。字典也已相同的方式工作。
- 如果想让 `spam` 和 `cheese` 存储两个不同的列表，就必须创建两个不同的列表，而不是复制一个引用。
- `return board[move] == ' '` 返回一个布尔值
- 短路求值——对于 `or` 和 `and` 操作符当左边的布尔值已经可以决定整体的布尔值时，右边的语句将不会执行。   
  实例：

  ```python
  def ReturnsTrue():
    print('ReturnsTrue() was called.')
    return True
  def ReturnsFalse():
      print('ReturnFalse() was called.')
      return False
  print('and 操作')
  ReturnsTrue() or ReturnsFalse()
  print('or 操作')
  ReturnsTrue() and ReturnsFalse()
  ```
  运行结果：
  ```
  and 操作
  ReturnsTrue() was called.
  or 操作
  ReturnsTrue() was called.
  ReturnFalse() was called.
  ```

<br />
<br />

## 7.推理游戏 Bagels

- `random.shufle()` 函数随机修改元素顺序。  
  实例：
  ```python
  import random
  number = list(range(12))
  print('打乱前'+str(number))
  random.shuffle(number)
  print('打乱后'+str(number))
  ```
  运行结果：
  ```
  打乱前[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
  打乱后[10, 3, 7, 8, 11, 9, 2, 0, 5, 6, 1, 4]
  ```
- `sort()` 是一个方法，它按照字母顺序或数字顺序重新排列列表中的元素。   
实例：
  ```python
  number = [9,1,2,5,4,7,0]
  number.sort()
  print(number)
  ```
  运行结果：
  ```
  [0, 1, 2, 4, 5, 7, 9]
  ```

- 以上两个都是“就地”修改 。    
- 字符串方法 `join()` 将字符串列表连接起来，作为一个单个的字符串返回。
- `join()` 就像是与 `split()` 相反的字符串方法。 `split()` 方法通过分割字符串而返回一个列表，而 `join()` 返回组合列表而得到一个字符串。
- 像 `%s` 这样的占位符叫做转换说明符（convertion specifiers）。一旦放入了转换说明符，我们就可以在字符串末尾放置所有的变量名称。 每个 `%s` 都会背代码行末尾的一个变量所替换。
- 变量数目必须和 `%s` 转换说明符的数目相同。
- 插值对于任意数据类型都是有效的，而不仅仅是对字符串有效。所有值都会自动转换为字符串数据类型。

- 字符串连接只能把两个字符串组合起来。
- 字符串插值也叫字符串格式化 （string formatting）
<br />
<br />

## 8.Sonar Treasure Hunt 游戏

-  `round( x [, n]  )`     
    x -- 数值表达式。   
    n -- 数值表达式，表示从小数点位数。     
     当参数 n 不存在时，round()函数的输出为整数   
     n的值可以是负数，表示在整数位部分四舍五入，但结果仍是**浮点数**。    
     实例：
     ```python
     print(round(123.45))
     print(round(123.45,0))
     print(round(123.45,-1))
     ```
    运行结果：
    ```
    123
    123.0
    120.0
    ```

- `sprt()` 用于求一个数字的平方根
- `exit()` 该函数立即终止程序执行
- `remove()` 是一个移除列表中与传入参数相匹配的第一个值的方法
- `isdigit()` 如果这个**字符串**只包含数字，字符串方法 `isdigit()` 将返回 `True` 否则，返回 `False`


<br />
<br />

## 9.凯撒密码

- `find()` 方法：在第一次出现后就停止查找. 如果没有找到所传递的字符串，`find()` 方法返回 `-1`  
  实例：
  ```python
  print('Hello world'.find('l'))
  print('Python is good!'.find('f'))
  ```
  运行结果：
  ```
  2
  -1
  ```

<br />
<br />

## 贪吃蛇小游戏
  -  [Python 贪吃蛇小游戏](https://hub.fastgit.org/Agul2020/Python/tree/main/snake)。



