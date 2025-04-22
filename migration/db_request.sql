CREATE DATABASE IF NOT EXISTS db_request;
USE db_request;
CREATE TABLE IF NOT EXISTS tb_requests(pedido VARCHAR(1),tempo timestamp);
CREATE TABLE IF NOT EXISTS tb_room_lights(log VARCHAR(4),tempo timestamp);