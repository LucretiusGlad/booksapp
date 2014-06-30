DROP TABLE IF EXISTS "authors_author";
CREATE TABLE authors_author (
	id INTEGER NOT NULL, 
	name VARCHAR(255), 
	PRIMARY KEY (id)
);
INSERT INTO "authors_author" VALUES(1,'Грегори Дэвид Робертс');
INSERT INTO "authors_author" VALUES(2,'Джордж Рэймонд Ричард Мартин');
INSERT INTO "authors_author" VALUES(3,'Мартин Д.');
INSERT INTO "authors_author" VALUES(4,'Габриэль Гарсиа Маркес');
INSERT INTO "authors_author" VALUES(5,'Стив Харви');
INSERT INTO "authors_author" VALUES(6,'Джоджо Мойес');
INSERT INTO "authors_author" VALUES(7,'Джеймс Э. Л.');
INSERT INTO "authors_author" VALUES(8,'Антуан де Сент-Экзюпери');
INSERT INTO "authors_author" VALUES(9,'Брэдбери Р.');
INSERT INTO "authors_author" VALUES(10,'Ирэне Као');
INSERT INTO "authors_author" VALUES(11,'Диана Сеттерфилд');
INSERT INTO "authors_author" VALUES(12,'Элизабет Рудник');
INSERT INTO "authors_author" VALUES(13,'Евгений Комаровский');
INSERT INTO "authors_author" VALUES(14,'Стивен Чбоски');
INSERT INTO "authors_author" VALUES(15,'Александр Мясников');
INSERT INTO "authors_author" VALUES(16,'Элис Манро');
INSERT INTO "authors_author" VALUES(17,'Розамунд Лаптон');
INSERT INTO "authors_author" VALUES(18,'Александр Волков');
INSERT INTO "authors_author" VALUES(19,'Джанни Родари');
DROP TABLE IF EXISTS "authors_books";
CREATE TABLE authors_books (
	author_id INTEGER, 
	book_id INTEGER, 
	FOREIGN KEY(author_id) REFERENCES authors_author (id), 
	FOREIGN KEY(book_id) REFERENCES books_book (id)
);
INSERT INTO "authors_books" VALUES(1,1);
INSERT INTO "authors_books" VALUES(2,2);
INSERT INTO "authors_books" VALUES(3,2);
INSERT INTO "authors_books" VALUES(4,3);
INSERT INTO "authors_books" VALUES(5,4);
INSERT INTO "authors_books" VALUES(6,5);
INSERT INTO "authors_books" VALUES(8,7);
INSERT INTO "authors_books" VALUES(9,8);
INSERT INTO "authors_books" VALUES(10,9);
INSERT INTO "authors_books" VALUES(7,10);
INSERT INTO "authors_books" VALUES(7,6);
INSERT INTO "authors_books" VALUES(7,11);
INSERT INTO "authors_books" VALUES(12,12);
INSERT INTO "authors_books" VALUES(1,13);
INSERT INTO "authors_books" VALUES(11,14);
INSERT INTO "authors_books" VALUES(13,15);
INSERT INTO "authors_books" VALUES(14,16);
INSERT INTO "authors_books" VALUES(15,17);
INSERT INTO "authors_books" VALUES(10,20);
INSERT INTO "authors_books" VALUES(19,22);
DROP TABLE IF EXISTS "books_book";
CREATE TABLE books_book (
	id INTEGER NOT NULL, 
	name VARCHAR(255), 
	PRIMARY KEY (id)
);
INSERT INTO "books_book" VALUES(1,'Шантарам');
INSERT INTO "books_book" VALUES(2,'Игра престолов');
INSERT INTO "books_book" VALUES(3,'Сто лет одиночества');
INSERT INTO "books_book" VALUES(4,'Поступай как женщина, думай как мужчина');
INSERT INTO "books_book" VALUES(5,'До встречи с тобой');
INSERT INTO "books_book" VALUES(6,'Пятьдесят оттенков серого');
INSERT INTO "books_book" VALUES(7,'Маленький принц');
INSERT INTO "books_book" VALUES(8,'Вино из одуванчиков');
INSERT INTO "books_book" VALUES(9,'Я смотрю на тебя');
INSERT INTO "books_book" VALUES(10,'Беллмен и Блэк, или Незнакомец в черном');
INSERT INTO "books_book" VALUES(11,'Пятьдесят оттенков свободы');
INSERT INTO "books_book" VALUES(12,'Малефисента. История истинной любви');
INSERT INTO "books_book" VALUES(13,'Шантарам (в 2-х книгах) (комплект)');
INSERT INTO "books_book" VALUES(14,'Тринадцатая сказка. Роман');
INSERT INTO "books_book" VALUES(15,'Здоровье ребенка и здравый смысл его родственников: Настольная книга для мам и пап');
INSERT INTO "books_book" VALUES(16,'Хорошо быть тихоней');
INSERT INTO "books_book" VALUES(17,'Русская рулетка: Как выжить в борьбе за собственное здоровье');
INSERT INTO "books_book" VALUES(18,'Беглянка');
INSERT INTO "books_book" VALUES(19,'Разгадай мою смерть');
INSERT INTO "books_book" VALUES(20,'Я чувствую тебя');
INSERT INTO "books_book" VALUES(21,'Я чувствую тебя');
INSERT INTO "books_book" VALUES(22,'Большая книга сказок');
DROP TABLE IF EXISTS "role";
CREATE TABLE role (
	id INTEGER NOT NULL, 
	name VARCHAR(80), 
	description VARCHAR(255), 
	PRIMARY KEY (id), 
	UNIQUE (name)
);
INSERT INTO "role" VALUES(1,'editor','can edit');
DROP TABLE IF EXISTS "roles_users";
CREATE TABLE roles_users (
	user_id INTEGER, 
	role_id INTEGER, 
	FOREIGN KEY(user_id) REFERENCES user (id), 
	FOREIGN KEY(role_id) REFERENCES role (id)
);
INSERT INTO "roles_users" VALUES(1,1);
DROP TABLE IF EXISTS "user";
CREATE TABLE user (
	id INTEGER NOT NULL, 
	email VARCHAR(255), 
	password VARCHAR(255), 
	active BOOLEAN, 
	confirmed_at DATETIME, "username" VARCHAR(255), 
	PRIMARY KEY (id), 
	UNIQUE (email), 
	CHECK (active IN (0, 1))
);
INSERT INTO "user" VALUES(1,'editor@test.com','$2a$12$o3pTQPVn/QLbVVwF0VIxG.mbhluzc3ymeYwWXQmC79d4OLmyuwDFq',1,NULL,'Editor');
