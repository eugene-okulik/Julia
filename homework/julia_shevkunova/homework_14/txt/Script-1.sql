-- добавляем студента
INSERT INTO students (name, second_name) VALUES ('Fname', 'Sname')

-- добавляем группу
INSERT INTO `groups` (title, start_date, end_date) VALUES ('Testgrp', 'mar 12', 'apr 13')

-- добавляем группу студенту
UPDATE students SET group_id = 2487 where id = 3929

-- добавляем книги
INSERT INTO books (title, taken_by_student_id) VALUES ('One intresting book', 3929)

INSERT INTO books (title, taken_by_student_id) VALUES ('Second intresting book', 3929)

-- добавляем учебные предметы
INSERT INTO subjets (title) VALUES ('Basics of programming')

INSERT INTO subjets (title) VALUES ('Architecture')

-- добавляем занятия по предметам
INSERT INTO lessons  (title, subject_id) VALUES ('Variables', 3806)
INSERT INTO lessons  (title, subject_id) VALUES ('Operators', 3806)
INSERT INTO lessons  (title, subject_id) VALUES ('Components of Web application', 3805)
INSERT INTO lessons  (title, subject_id) VALUES ('Building Application', 3805)

-- добавляем оценки по занятиям
INSERT INTO marks  (value, lesson_id, student_id) VALUES (5 , 7404, 3929)
INSERT INTO marks  (value, lesson_id, student_id) VALUES (5 , 7405, 3929)
INSERT INTO marks  (value, lesson_id, student_id) VALUES (8 , 7406, 3929)
INSERT INTO marks  (value, lesson_id, student_id) VALUES (10 , 7407, 3929)

-- выводим все оценки студента
SELECT * FROM marks where student_id = 3929

 -- выводим все книги, которые находятся у студента
SELECT * FROM books WHERE taken_by_student_id = 3929

-- выводим группу студента, книги, оценки с названиями занятий и предметов
SELECT s.name as 'имя студента', g.title as 'группа', b.title as 'название книги', m.value as 'оценка',  l.title as 'название занятия', s2.title as 'предмет' FROM students s
JOIN books b
on s.id =b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN `groups` g ON g.id = s.group_id
JOIN lessons l ON l.id  = m.lesson_id
JOIN subjets s2 ON s2.id = l.subject_id
where s.id = 3929
