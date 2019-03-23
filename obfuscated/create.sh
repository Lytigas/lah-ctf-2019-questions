head -n 1 compacted.py | python3 execify.py exec chr | python3 execify.py exec chr > processed_1.py
tail -n +2 compacted.py >> processed_1.py

head -n 1 processed_1.py > processed_2.py # copy the first line
tail -n +2 processed_1.py | head -n 1 | python3 execify.py __JOSH A | python3 execify.py exec chr | python3 execify.py __JOSH A  >> processed_2.py
tail -n +3 processed_1.py >> processed_2.py


head -n 2 processed_2.py > processed_3.py # copy the first two lines
tail -n +3 processed_2.py | python3 execify.py __JOSH _JOSH 1337 | python3 execify.py __JOSH _JOSH 1337 >> processed_3.py
