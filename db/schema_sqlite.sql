-- 产品信息表
create table at_product (
    id char(32) primary key, -- uuid
    ename varchar(10) not null, -- 产品英文名称
    cname varchar(50) not null, -- 产品中文名称
    description varchar(100) null, -- 产品描述
    creation_time timestamp default CURRENT_TIMESTAMP not null
);

insert into at_product(id, ename, cname, description)
values('2128f01e14d641d1bfb5173d653c0b85', 'etoh', '家校互联', '家校互联');
 
insert into at_product(id, ename, cname, description)
values('2128f01e14d641d1bfb5173d653c0b86', 'passport', 'Passport', '单点登录');

-- 自动化测试组件模板表
create table at_action (
    id char(32) primary key, -- uuid
    product_id char(32) not null, -- 所属产品ID，即 at_product.id
    serial integer not null, -- 组件编号
    name varchar(50) not null, -- 组件名称
    state integer default 1 not null, -- 组件状态：0废弃 | 1正常
    description varchar(100) null, -- 组件描述
    modify_time timestamp default CURRENT_TIMESTAMP not null,
    creation_time timestamp default CURRENT_TIMESTAMP not null
);

insert into at_action(id, product_id, serial, name, description)
values('593bab9787f445f7a8fdef7450601353', '2128f01e14d641d1bfb5173d653c0b85', 1, 'Login', '登录测试');

insert into at_action(id, product_id, serial, name, description)
values('9cbb964708f541cdafc5e5062d3abefc', '2128f01e14d641d1bfb5173d653c0b86', 2, 'Message', '短信箱测试');

-- 自动化测试功能表
create table at_function (
    id char(32) primary key, -- uuid
    action_id char(32) not null, -- 所属测试组件ID，即 at_action.id
    name varchar(50) not null, -- 功能名称
    state integer default 1 not null, -- 功能状态：0废弃 | 1正常
    description varchar(100) null, -- 功能描述
    modify_time timestamp default CURRENT_TIMESTAMP not null,
    creation_time timestamp default CURRENT_TIMESTAMP not null
);

insert into at_function(id, action_id, name, description)
values('ebb92cf0514c11dfbfa9000e35b49aba', '593bab9787f445f7a8fdef7450601353', 'SendMessage', '发送留言');

insert into at_function(id, action_id, name, description)
values('1ce58621514d11df8231000e35b49aba', '9cbb964708f541cdafc5e5062d3abefc', 'GetMessage', '检查留言');

-- 自动化测试控制文件表
create table at_control (
    id char(32) primary key, -- uuid
    product_id char(32) not null, -- 所属产品ID，即 at_product.id
    name varchar(50) not null, -- 控制文件名称
    is_enable integer default 1 not null, -- 是否启用：0否 | 1是
    description varchar(100) null, -- 文件描述
    modify_time timestamp default CURRENT_TIMESTAMP not null,
    creation_time timestamp default CURRENT_TIMESTAMP not null
);

insert into at_control(id, product_id, name)
values('c2ba5540514c11dfbead000e35b49aba', '2128f01e14d641d1bfb5173d653c0b85', '家校互联自动化测试控制文件');

-- 控制文件引用的测试组件表
create table at_action_ref (
    id char(32) primary key, -- uuid
    control_id char(32) not null, -- 控制文件ID
    action_id char(32) not null, -- 测试组件ID
    action_order integer not null, -- 排序编号
    is_enable integer default 1 not null -- 是否启用：0否 | 1是
);

insert into at_action_ref(id, control_id, action_id, action_order)
values('c2ba5540514c12dfbead000e35b49ab0', 'c2ba5540514c11dfbead000e35b49aba', '593bab9787f445f7a8fdef7450601353', 1);

insert into at_action_ref(id, control_id, action_id, action_order)
values('c2ba5540514c12dfbead000e35b49ab1', 'c2ba5540514c11dfbead000e35b49aba', '9cbb964708f541cdafc5e5062d3abefc', 2);

-- 控制文件引用的测试功能表
create table at_function_ref (
    id char(32) primary key, -- uuid
    action_ref_id char(32) not null, -- 测试组件引用记录ID，即 at_action_ref.id
    function_id char(32) not null, -- 测试组件功能ID
    function_order integer not null, -- 排序编号
    is_enable integer default 1 not null -- 是否启用：0否 | 1是
);

insert into at_function_ref(id, action_ref_id, function_id, function_order)
values('1d31a5b2259e4386865b886fdeaf3544', 'c2ba5540514c12dfbead000e35b49ab0', 'ebb92cf0514c11dfbfa9000e35b49aba', 1);

insert into at_function_ref(id, action_ref_id, function_id, function_order)
values('c20f88591a2c4dfe9311342a76d913ec', 'c2ba5540514c12dfbead000e35b49ab1', '1ce58621514d11df8231000e35b49aba', 2);
