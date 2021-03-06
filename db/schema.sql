create table at_control (
    id char(32) not null primary key,
    name varchar(50) not null,
    encoding varchar(10) default 'UTF-8' null,
    is_enable integer default 1 not null,
    description varchar(100) null,
    modify_time timestamp default CURRENT_TIMESTAMP not null,
    creation_time timestamp default CURRENT_TIMESTAMP not null
);

insert into at_control(id, name)
values('c2ba5540514c11dfbead000e35b49aba', '家校互联 Control file');

create table at_action (
    id integer primary key,
    name varchar(50) not null,
    is_enable integer default 1 not null,
    description varchar(100) null,
    modify_time timestamp default CURRENT_TIMESTAMP not null,
    creation_time timestamp default CURRENT_TIMESTAMP not null
);

create table at_control_action (
    id char(32) not null primary key,
    control_id char(32) not null,
    action_id integer not null,
    action_order integer not null
);

insert into at_action(name, description)
values('Login', '登录测试');

insert into at_action(name, description)
values('Message', '短信箱测试');

insert into at_control_action(id, control_id, action_id, action_order)
values('c2ba5540514c12dfbead000e35b49ab0', 'c2ba5540514c11dfbead000e35b49aba', 1, 1);

insert into at_control_action(id, control_id, action_id, action_order)
values('c2ba5540514c12dfbead000e35b49ab1', 'c2ba5540514c11dfbead000e35b49aba', 2, 2);

create table at_function (
    id char(32) not null primary key,
    action_id integer not null,
    name varchar(50) not null,
    is_enable integer default 1 not null,
    description varchar(100) null,
    modify_time timestamp default CURRENT_TIMESTAMP not null,
    creation_time timestamp default CURRENT_TIMESTAMP not null
);

insert into at_function(id, action_id, name, description)
values('ebb92cf0514c11dfbfa9000e35b49aba', 1, 'SendMessage', '发送留言');

insert into at_function(id, action_id, name, description)
values('1ce58621514d11df8231000e35b49aba', 1, 'GetMessage', '检查留言');
