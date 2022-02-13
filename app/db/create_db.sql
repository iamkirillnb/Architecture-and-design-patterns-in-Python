create table if not exists student (
    name varchar,
    phone varchar not null ,
    course_id varchar default ''
);

create table if not exists course (
    course_name varchar,
    category_id varchar default '',
    foreign key (course_name) references student(course_id)
);

create table if not exists category (
    category_name varchar,
    foreign key (category_name) references course(category_id)
);


