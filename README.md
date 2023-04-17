```
Установка и запуск:
git clone git@github.com:Shibaev-am/SeaBattle.git
cd SeaBattle
pip install -r requirements.txt
python3 main.py
```


Морской бой: игра для двух участников, в которой игроки по очереди называют, сообщают иным способом, координаты на карте соперника. Если у врага с этими координатами имеется "корабль", то корабль или его палуба убивается, попавший делает еще один ход. Цель игрока: первым убить все игровые "корабли" врага. 

Игровое поле — квадрат 10×10 у каждого игрока, на котором размещается флот кораблей.

После запуска игры перед игроками открывается окно:
![Image alt](https://github.com/Shibaev-am/SeaBattle/blob/dev/gameProcessImgs/Welcome.png)
После нажатия на клавишу 'enter', первому игроку необходимо ввести свое имя и нажать 'enter':
![Image alt](https://github.com/Shibaev-am/SeaBattle/blob/dev/gameProcessImgs/FirstPlayerName.png)
![Image alt](https://github.com/Shibaev-am/SeaBattle/blob/dev/gameProcessImgs/FirstPlayerNameReady.png)
Затем второй игрок вводит свое имя и также нажимает 'enter'.
После этого игроки могут начать выставлять корабли, или, если нужно, изменить свои имена:
![Image alt](https://github.com/Shibaev-am/SeaBattle/blob/dev/gameProcessImgs/ReadyToSetFields.png)
Если нажать цифру 1 или 2, то игроки смогут ввести новые имена, если же нажать 'enter', то начинается следующий этап - расстановка кораблей. Первым это делает первый игрок:
![Image alt](https://github.com/Shibaev-am/SeaBattle/blob/dev/gameProcessImgs/EmptyField.png)
Сверху экрана написан размер корабля, который нужно поставить, установка корабля происходит несложным образом - нужно нажать на те клетки, на которые игрок хочет поставить новый корабль, если клетки выбраны некорректные, то корабль не выставится и нужно будет заново выбрать куда его установить.
![Image alt](https://github.com/Shibaev-am/SeaBattle/blob/dev/gameProcessImgs/FillField.png)
Серые клетки - это граничные клетки, на них ставить корабли нельзя, так же нельзя ставить на уже занятые клетки - можно только на белые. 
Всего нужно выставить 10 кораблей - 1 четырехпалубный (т.е. 4 подряд идущие клетки), 2 трехпалубных, 3 двухпалубных и 4 однопалубных(т.е. просто одиночные 4 клетки). При этом два корабля не могут стоять рядом, поэтмоу после выставления нового корабля, все клетки вокруг него становтяся серыми - на них ставить корабли нельзя.
После того, как первый игрок расставил все корабли, свое поле заполняет второй игрок. 
И вот, оба игрока готовы к игре, чтобы начать бой нужно нажать 'enter':
![Image alt](https://github.com/Shibaev-am/SeaBattle/blob/dev/gameProcessImgs/ReadyForGame.png)
Теперь игроку нужно подтвердить, что он готов ходить - т.к. игра происходит на одном устройстве, то другому игроку надо, например, отвернуться:
![Image alt](https://github.com/Shibaev-am/SeaBattle/blob/dev/gameProcessImgs/NextStep.png)
![Image alt](https://github.com/Shibaev-am/SeaBattle/blob/dev/gameProcessImgs/ChooseTarget.png)
После этого перед игроком открывается два поля - свое и чужое, чужое изначально полностью серое и на нем отображаются результаты выстрелов атакующего. Если игрок попал в корабль - на клетке появляется крестик, если промахнулся, то красная точка. 
![Image alt](https://github.com/Shibaev-am/SeaBattle/blob/dev/gameProcessImgs/GoodShot.png)
Игрок делает выстрелы до первого промаха, как только он промахивается, ход переходит другому игроку.
![Image alt](https://github.com/Shibaev-am/SeaBattle/blob/dev/gameProcessImgs/MiddleOfGame.png)
На поле игрока, который стреляет отображаются результаты выстрелов его противника по такой же схеме - попадание - крестик, промах - точка.
Как только один из игроков уничтожит все корабли противника, игра прекращатся и на экран выводятся "боевые" поля обоих игроков.
![Image alt](https://github.com/Shibaev-am/SeaBattle/blob/dev/gameProcessImgs/Finish.png)

