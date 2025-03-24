/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 80032 (8.0.32)
 Source Host           : localhost:3306
 Source Schema         : fsray

 Target Server Type    : MySQL
 Target Server Version : 80032 (8.0.32)
 File Encoding         : 65001

 Date: 24/03/2025 19:37:35
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for access
-- ----------------------------
DROP TABLE IF EXISTS `access`;
CREATE TABLE `access`  (
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `access_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `access_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `access_desc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `access_scopes` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `access_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `parent_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `is_menu` tinyint(1) NOT NULL,
  `is_verify` tinyint(1) NOT NULL,
  PRIMARY KEY (`access_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of access
-- ----------------------------
INSERT INTO `access` VALUES ('2024-11-23 23:48:56', '2024-11-23 23:48:59', '1', '用户管理', '管理用户的菜单项', '', 'user', '0', 1, 1);
INSERT INTO `access` VALUES ('2024-11-25 18:59:33', '2024-11-25 18:59:35', '10', '主页', NULL, NULL, 'home', '0', 1, 0);
INSERT INTO `access` VALUES ('2024-12-02 14:06:06', '2024-12-02 14:06:09', '11', '查询用户', '查询用户的权限', NULL, 'userlist', '1', 0, 1);
INSERT INTO `access` VALUES ('2024-12-02 23:01:53', '2024-12-02 23:01:56', '12', '查询角色列表', '查询角色的权限', NULL, 'get_role_list', '4', 0, 1);
INSERT INTO `access` VALUES ('2024-12-02 23:55:24', '2024-12-02 23:55:26', '13', '更改用户的角色', '更改用户的角色', NULL, 'update_user_role', '1', 0, 1);
INSERT INTO `access` VALUES ('2024-12-05 13:47:46', '2024-12-05 13:47:48', '14', '查询电动车列表权限', '查询电动车列表权限', NULL, 'machine_list', '2', 0, 1);
INSERT INTO `access` VALUES ('2024-12-09 15:48:21', '2024-12-09 15:48:23', '15', '添加电动车', '添加电动车的权限', NULL, 'machine_add', '2', 0, 1);
INSERT INTO `access` VALUES ('2024-12-14 19:44:37', '2024-12-14 19:44:40', '16', '查询区域列表', '查询区域列表的权限', NULL, 'area_list', '7', 0, 1);
INSERT INTO `access` VALUES ('2024-12-14 22:10:02', '2024-12-14 22:10:03', '17', '获取角色需验证权限', '获取角色需验证权限', NULL, 'get_role_menu_access', '4', 0, 1);
INSERT INTO `access` VALUES ('2024-12-15 16:29:45', '2024-12-15 16:29:47', '18', '权限赋予', '权限变更', NULL, 'update_role_access', '4', 0, 1);
INSERT INTO `access` VALUES ('2024-12-17 13:26:40', '2024-12-17 13:26:44', '19', '电动车骑行', '电动车模拟或真实骑行的权限', NULL, 'start_ride', '2', 0, 1);
INSERT INTO `access` VALUES ('2024-11-23 23:49:56', '2024-11-23 23:49:58', '2', '电动车管理', '管理电动车的菜单项', NULL, 'machine', '0', 1, 1);
INSERT INTO `access` VALUES ('2024-12-17 14:45:46', '2024-12-17 14:45:48', '20', '查询订单记录', '查询订单记录', NULL, 'get_record_list', '6', 0, 0);
INSERT INTO `access` VALUES ('2024-12-19 14:06:59', '2024-12-19 14:07:02', '21', '统计数据', '统计数据', NULL, 'get_anaylze', '3', 0, 1);
INSERT INTO `access` VALUES ('2024-12-24 10:02:18', '2024-12-24 10:02:21', '22', '删除电动车', '删除电动车', NULL, 'machine_delete', '2', 0, 1);
INSERT INTO `access` VALUES ('2024-11-23 23:50:50', '2024-11-23 23:50:53', '3', '仪表盘', '对数据进行统计', NULL, 'analyze', '0', 1, 1);
INSERT INTO `access` VALUES ('2024-11-23 23:53:07', '2024-11-23 23:53:10', '4', '角色权限管理', '管理权限的菜单项', NULL, 'access', '0', 1, 1);
INSERT INTO `access` VALUES ('2024-11-23 23:54:08', '2024-11-23 23:54:10', '5', '地图管理', '显示地图的权限', NULL, 'map', '0', 1, 0);
INSERT INTO `access` VALUES ('2024-11-23 23:54:54', '2024-11-23 23:54:56', '6', '订单管理', '管理订单的菜单', NULL, 'orders', '0', 1, 1);
INSERT INTO `access` VALUES ('2024-11-23 23:55:39', '2024-11-23 23:55:41', '7', '区域管理', '管理区域的菜单', NULL, 'area', '0', 1, 1);
INSERT INTO `access` VALUES ('2024-11-25 14:37:59', '2024-11-25 14:38:03', '8', '用户添加', '添加用户的权限', NULL, 'adduser', '1', 0, 1);
INSERT INTO `access` VALUES ('2024-11-25 14:40:06', '2024-11-25 14:40:09', '9', '用户状态变更', '启用禁用用户的权限', NULL, 'update_user_status', '1', 0, 1);

-- ----------------------------
-- Table structure for area
-- ----------------------------
DROP TABLE IF EXISTS `area`;
CREATE TABLE `area`  (
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `area_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `area_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `area_desc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`area_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of area
-- ----------------------------
INSERT INTO `area` VALUES ('2024-12-17 16:36:37', '2024-12-17 16:36:40', '0', '违规区域', NULL);
INSERT INTO `area` VALUES ('2024-12-05 13:37:48', '2024-12-05 13:37:51', '1', '江夏中央公园区', '[(114.320506,30.396504),(114.282176,30.376638),(114.347709,30.376105),(114.320506,30.396504)]');
INSERT INTO `area` VALUES ('2024-12-09 13:02:14', '2024-12-09 13:02:12', '2', '国家检察官学院区', '[(114.371974,30.386238),(114.424833,30.383638),(114.409223,30.370504),(114.371974,30.386238)]');
INSERT INTO `area` VALUES ('2024-12-24 17:03:16', '2024-12-24 17:03:19', '3', '湖北经济学院区', '[(114.437397,30.425653),(114.42523,30.414526),(114.430866,30.40997),(114.440567,30.414305),(114.444601,30.421015),(114.437397,30.425653)]');
INSERT INTO `area` VALUES ('2024-12-24 17:15:20', '2024-12-24 17:15:22', '4', '藏龙东街区', '[(114.428282,30.43645),(114.434595,30.437945),(114.435501,30.435111),(114.429162,30.433505),(114.428282,30.43645)]');
INSERT INTO `area` VALUES ('2024-12-24 17:21:07', '2024-12-24 17:21:09', '5', '武汉软件工程学院区', '[(114.433413,30.442536),(114.431411,30.448739),(114.425462,30.447876),(114.425764,30.443936),(114.427482,30.44208),(114.433413,30.442536)]');
INSERT INTO `area` VALUES ('2024-12-24 17:24:27', '2024-12-24 17:24:29', '6', '当代国际城区', '[(114.433776,30.442372),(114.438079,30.444095),(114.439224,30.439448),(114.434716,30.438331),(114.433776,30.442372)]');

-- ----------------------------
-- Table structure for feedback
-- ----------------------------
DROP TABLE IF EXISTS `feedback`;
CREATE TABLE `feedback`  (
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `feedback_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `feedback_msg` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_solve` tinyint(1) NOT NULL,
  `user_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `machine_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`feedback_id`) USING BTREE,
  INDEX `user_id`(`user_id` ASC) USING BTREE,
  INDEX `machine_id`(`machine_id` ASC) USING BTREE,
  CONSTRAINT `feedback_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `feedback_ibfk_2` FOREIGN KEY (`machine_id`) REFERENCES `machine` (`machine_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of feedback
-- ----------------------------

-- ----------------------------
-- Table structure for machine
-- ----------------------------
DROP TABLE IF EXISTS `machine`;
CREATE TABLE `machine`  (
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `machine_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `machine_point` json NULL,
  `machine_battery` int NOT NULL,
  `status` int NOT NULL,
  `area_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`machine_id`) USING BTREE,
  INDEX `area_id`(`area_id` ASC) USING BTREE,
  CONSTRAINT `machine_ibfk_1` FOREIGN KEY (`area_id`) REFERENCES `area` (`area_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of machine
-- ----------------------------
INSERT INTO `machine` VALUES ('2024-12-24 08:50:04', '2024-12-24 12:13:12', '0cd042b0-7350-4c56-87ea-0c68de84783d', '{\"latitude\": 30.380091, \"longitude\": 114.400773}', 89, 1, '2');
INSERT INTO `machine` VALUES ('2024-12-24 08:50:04', '2024-12-24 13:26:25', '1c162ced-da1f-4bf0-8f1c-698623770194', '{\"latitude\": 30.441784, \"longitude\": 114.436833}', 90, 1, '6');
INSERT INTO `machine` VALUES ('2024-12-24 08:50:04', '2024-12-25 07:27:39', '24e8d012-222e-466d-b650-a61807270121', '{\"latitude\": 30.382137, \"longitude\": 114.315651}', 94, 1, '1');
INSERT INTO `machine` VALUES ('2024-12-24 08:50:04', '2024-12-24 12:59:54', '26a91f80-9d86-486e-a517-ed1b2247900a', '{\"latitude\": 30.421078, \"longitude\": 114.437128}', 94, 1, '3');
INSERT INTO `machine` VALUES ('2024-12-24 08:50:04', '2024-12-25 07:31:09', '4b1284a4-272d-4481-99f3-faf8a558d702', '{\"latitude\": 30.383715, \"longitude\": 114.314798}', 87, 1, '1');
INSERT INTO `machine` VALUES ('2024-12-24 08:50:04', '2024-12-25 07:29:09', '5748574b-0f27-4bc6-97db-396f066d65fa', '{\"latitude\": 30.379551, \"longitude\": 114.312358}', 91, 1, '1');
INSERT INTO `machine` VALUES ('2024-12-24 08:50:04', '2024-12-24 13:02:19', '754f5b5d-bc95-41fc-990f-7440f64744e0', '{\"latitude\": 30.420825, \"longitude\": 114.432906}', 93, 1, '3');
INSERT INTO `machine` VALUES ('2024-12-24 08:50:04', '2024-12-25 07:31:09', '75901d22-4e69-44d2-a6d6-5c97e4aaed04', '{\"latitude\": 30.377862, \"longitude\": 114.317936}', 87, 1, '1');
INSERT INTO `machine` VALUES ('2024-12-24 08:50:04', '2024-12-24 08:50:04', '773d1345-c7d4-485b-ab23-c0c6ae0e5f5c', '{\"latitude\": \"30.446583\", \"longitude\": \"114.429565\"}', 100, 1, '5');
INSERT INTO `machine` VALUES ('2024-12-24 08:50:04', '2024-12-24 13:26:26', '7ac58eeb-b3f9-4265-9f99-5fb620fa6ffe', '{\"latitude\": 30.442267, \"longitude\": 114.43664}', 93, 1, '6');
INSERT INTO `machine` VALUES ('2024-12-24 08:50:04', '2024-12-24 13:40:27', '8970b0cd-2542-4dc9-b8e2-ffb9c070409a', '{\"latitude\": 30.435588, \"longitude\": 114.430643}', 97, 1, '4');
INSERT INTO `machine` VALUES ('2024-12-24 08:50:04', '2024-12-24 12:13:38', '94230331-59c2-486e-bec1-7e999fddc843', '{\"latitude\": 30.380332, \"longitude\": 114.398753}', 93, 1, '2');
INSERT INTO `machine` VALUES ('2024-12-24 08:50:04', '2024-12-24 12:13:41', '9b9b81dc-6800-4d10-91ca-cd895163f663', '{\"latitude\": 30.37982, \"longitude\": 114.397829}', 97, 1, '2');
INSERT INTO `machine` VALUES ('2024-12-24 08:50:04', '2024-12-24 08:50:04', '9f699a58-a387-416a-98d1-07a0c089464f', '{\"latitude\": \"30.444894\", \"longitude\": \"114.429441\"}', 100, 1, '5');
INSERT INTO `machine` VALUES ('2024-12-24 08:50:04', '2024-12-24 08:50:04', 'a76bf28d-9885-4e30-9bd0-f027daf080fe', '{\"latitude\": \"30.444532\", \"longitude\": \"114.42927\"}', 100, 1, '5');
INSERT INTO `machine` VALUES ('2024-12-24 08:50:04', '2024-12-24 13:40:30', 'ac91cf08-132b-4366-8df2-936d83fbd42b', '{\"latitude\": 30.43624, \"longitude\": 114.431328}', 99, 1, '4');
INSERT INTO `machine` VALUES ('2024-12-24 08:50:04', '2024-12-26 05:23:56', 'b73c0757-d676-44eb-8414-c4e9c6abdf7b', '{\"latitude\": 30.413712, \"longitude\": 114.435653}', 66, 1, '3');
INSERT INTO `machine` VALUES ('2024-12-17 08:19:27', '2024-12-24 08:35:44', 'cec802b1-dc99-49a1-985f-e47eb0c87163', '{\"latitude\": 30.422901, \"longitude\": 114.440637}', 88, 1, '0');
INSERT INTO `machine` VALUES ('2024-12-24 08:50:04', '2024-12-24 13:26:50', 'd33985a9-654b-4f1c-b1ed-4d20909905c3', '{\"latitude\": 30.4404, \"longitude\": 114.437456}', 91, 1, '6');
INSERT INTO `machine` VALUES ('2024-12-24 08:50:04', '2024-12-24 08:50:04', 'dc48c7b3-4767-4231-bc0c-074590265ec3', '{\"latitude\": \"30.442166\", \"longitude\": \"114.435528\"}', 100, 1, '6');
INSERT INTO `machine` VALUES ('2024-12-24 08:50:04', '2024-12-24 13:00:25', 'dd9215a1-a68d-4100-bea3-eaa10388ce73', '{\"latitude\": 30.421142, \"longitude\": 114.44039}', 98, 1, '3');
INSERT INTO `machine` VALUES ('2024-12-24 08:50:04', '2024-12-24 08:50:04', 'ddec1d97-1a5c-409b-b131-dd3bc24dab45', '{\"latitude\": \"30.440697\", \"longitude\": \"114.436995\"}', 100, 1, '6');
INSERT INTO `machine` VALUES ('2024-12-09 07:28:22', '2024-12-09 07:28:22', 'e193dc82-842b-40a8-b524-0f404ffeaf8a', '{\"latitude\": \"30.381705\", \"longitude\": \"114.397322\"}', 100, 1, '2');
INSERT INTO `machine` VALUES ('2024-12-24 08:50:04', '2024-12-24 13:40:56', 'e6f42f73-a857-4994-9a85-9992469d3e56', '{\"latitude\": 30.436313, \"longitude\": 114.431179}', 96, 1, '4');
INSERT INTO `machine` VALUES ('2024-12-24 08:50:04', '2024-12-24 13:41:29', 'f13da857-1903-4769-8e3b-d539fe30d9b3', '{\"latitude\": 30.434027, \"longitude\": 114.430144}', 93, 1, '4');
INSERT INTO `machine` VALUES ('2024-12-24 08:50:04', '2024-12-24 08:50:04', 'fac4b7bf-44fa-450c-a750-74bdf32d6a9c', '{\"latitude\": \"30.378439\", \"longitude\": \"114.397189\"}', 100, 1, '2');

-- ----------------------------
-- Table structure for record
-- ----------------------------
DROP TABLE IF EXISTS `record`;
CREATE TABLE `record`  (
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `record_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `start_time` datetime NULL DEFAULT NULL,
  `end_time` datetime NULL DEFAULT NULL,
  `stop_time` int NOT NULL,
  `consume_battery` int NOT NULL,
  `tracejectory` json NULL,
  `user_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `machine_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`record_id`) USING BTREE,
  INDEX `user_id`(`user_id` ASC) USING BTREE,
  INDEX `machine_id`(`machine_id` ASC) USING BTREE,
  CONSTRAINT `record_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `record_ibfk_2` FOREIGN KEY (`machine_id`) REFERENCES `machine` (`machine_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of record
-- ----------------------------
INSERT INTO `record` VALUES ('2024-12-24 12:15:54', '2024-12-24 12:15:54', '03c4045c-472c-4a6e-8176-3b8204aa6405', '2024-12-24 13:00:00', '2024-12-24 13:01:01', 0, 12, '[[114.434825, 30.423493], [114.437144, 30.425605], [114.437992, 30.425412], [114.440572, 30.423481], [114.438679, 30.422392], [114.437413, 30.422665], [114.435798, 30.421727], [114.434805, 30.421201], [114.433572, 30.421126], [114.432193, 30.420203], [114.433025, 30.4195], [114.433148, 30.418846]]', '3f343dda-16ce-4b1d-b513-528bc2c2095e', 'b73c0757-d676-44eb-8414-c4e9c6abdf7b');
INSERT INTO `record` VALUES ('2024-12-17 08:34:42', '2024-12-17 08:34:42', '06d92bcb-e726-4897-be0d-c4db580e4809', '2024-12-24 12:13:03', '2024-12-24 12:13:38', 0, 15, '[[114.400243, 30.380026], [114.400425, 30.380587], [114.399368, 30.381215], [114.397517, 30.380753], [114.397587, 30.379815], [114.398, 30.38011], [114.398753, 30.380332]]', '8e9ff3f4-91af-4211-ad2b-ac47ad25942c', '94230331-59c2-486e-bec1-7e999fddc843');
INSERT INTO `record` VALUES ('2024-12-16 12:15:54', '2024-12-16 12:15:54', '4c0370bd-cad2-4019-a74c-817de0951280', '2024-12-24 13:02:04', '2024-12-24 13:02:19', 0, 3, '[[114.435078, 30.421254], [114.433641, 30.421142], [114.432906, 30.420825]]', '3f343dda-16ce-4b1d-b513-528bc2c2095e', '754f5b5d-bc95-41fc-990f-7440f64744e0');
INSERT INTO `record` VALUES ('2024-12-24 12:15:54', '2024-12-24 12:15:54', '5be032db-d25d-46c4-bc7c-a492b9644941', '2024-12-24 12:59:24', '2024-12-24 12:59:54', 0, 6, '[[114.431231, 30.419398], [114.433116, 30.420954], [114.433878, 30.421185], [114.435261, 30.421319], [114.436758, 30.421711], [114.437128, 30.421078]]', '7dae4d84-7fe6-4fbe-b678-d89b4df04639', '26a91f80-9d86-486e-a517-ed1b2247900a');
INSERT INTO `record` VALUES ('2024-12-25 07:24:37', '2024-12-25 07:24:37', '5c80f779-51a4-4993-9a5c-4ca7097bba0b', '2024-12-25 07:24:39', '2024-12-25 07:29:09', 0, 9, '[[114.320329, 30.380024], [114.320753, 30.380319], [114.321407, 30.379289], [114.320613, 30.377953], [114.318285, 30.377749], [114.315791, 30.378151], [114.314873, 30.37864], [114.312341, 30.378924], [114.312358, 30.379551]]', '135b6c88-b6c8-4303-80b9-72b3bfca9f07', '5748574b-0f27-4bc6-97db-396f066d65fa');
INSERT INTO `record` VALUES ('2024-12-26 05:19:24', '2024-12-26 05:19:24', '64a072c5-a6e8-4a64-8aad-973cf8615977', '2024-12-26 05:19:26', '2024-12-26 05:23:56', 0, 9, '[[114.440846, 30.420708], [114.441178, 30.42008], [114.44113, 30.419109], [114.440449, 30.418197], [114.439371, 30.416947], [114.438657, 30.415697], [114.437053, 30.415241], [114.436173, 30.414721], [114.435653, 30.413712]]', '3f343dda-16ce-4b1d-b513-528bc2c2095e', 'b73c0757-d676-44eb-8414-c4e9c6abdf7b');
INSERT INTO `record` VALUES ('2024-12-18 08:34:42', '2024-12-18 08:34:42', '67c4d6b6-55b4-4b94-ad0b-d28f00ceb04c', '2024-12-24 12:12:37', '2024-12-24 12:13:12', 0, 4, '[[114.397436, 30.379943], [114.396986, 30.379165], [114.397512, 30.378806], [114.398322, 30.37886], [114.399475, 30.378731], [114.400039, 30.379418], [114.400773, 30.380091]]', '3f343dda-16ce-4b1d-b513-528bc2c2095e', '0cd042b0-7350-4c56-87ea-0c68de84783d');
INSERT INTO `record` VALUES ('2024-12-20 12:15:54', '2024-12-20 12:15:54', '719c8a67-5baa-49b7-bcd4-fd9354b6d7e0', '2024-12-24 13:40:12', '2024-12-24 13:40:27', 0, 3, '[[114.430179, 30.436438], [114.430375, 30.43613], [114.430643, 30.435588]]', '3f343dda-16ce-4b1d-b513-528bc2c2095e', '8970b0cd-2542-4dc9-b8e2-ffb9c070409a');
INSERT INTO `record` VALUES ('2024-12-20 12:15:54', '2024-12-20 12:15:54', '73d0c2af-a156-4b8c-b90f-f7e3e2e98a87', '2024-12-24 13:26:05', '2024-12-24 13:26:50', 0, 9, '[[114.43475, 30.441965], [114.434559, 30.441484], [114.435551, 30.441355], [114.43627, 30.441897], [114.43664, 30.442267], [114.436297, 30.443115], [114.436275, 30.443356], [114.436613, 30.442787], [114.437456, 30.4404]]', '3f343dda-16ce-4b1d-b513-528bc2c2095e', 'd33985a9-654b-4f1c-b1ed-4d20909905c3');
INSERT INTO `record` VALUES ('2024-12-24 12:15:54', '2024-12-24 12:15:54', '813eb4c1-e74f-4ddd-815d-b9aa1d3ac3b4', '2024-12-24 13:40:54', '2024-12-24 13:41:29', 0, 7, '[[114.432547, 30.435446], [114.433405, 30.436023], [114.433792, 30.434623], [114.432005, 30.434118], [114.431716, 30.434553], [114.429972, 30.434473], [114.430144, 30.434027]]', '3f343dda-16ce-4b1d-b513-528bc2c2095e', 'f13da857-1903-4769-8e3b-d539fe30d9b3');
INSERT INTO `record` VALUES ('2024-12-28 12:15:54', '2024-12-28 12:15:54', '88f3f315-fc2f-4759-bf4f-7a09b7b76904', '2024-12-24 13:25:35', '2024-12-24 13:26:25', 0, 10, '[[114.437396, 30.442218], [114.43841, 30.442568], [114.438485, 30.442911], [114.439236, 30.441264], [114.43922, 30.439349], [114.438351, 30.439054], [114.43671, 30.439601], [114.436613, 30.440105], [114.437316, 30.440411], [114.436833, 30.441784]]', '3f343dda-16ce-4b1d-b513-528bc2c2095e', '1c162ced-da1f-4bf0-8f1c-698623770194');
INSERT INTO `record` VALUES ('2024-12-29 08:34:42', '2024-12-29 08:34:42', '950c2aa2-709b-4dfc-a6e9-374d0678e068', '2024-12-24 12:13:26', '2024-12-24 12:13:41', 0, 3, '[[114.397006, 30.379084], [114.397383, 30.3799], [114.397829, 30.37982]]', '3f343dda-16ce-4b1d-b513-528bc2c2095e', '9b9b81dc-6800-4d10-91ca-cd895163f663');
INSERT INTO `record` VALUES ('2024-12-23 08:34:42', '2024-12-23 08:34:42', '9eb17a28-ebb3-4202-94a0-44af815e3555', '2024-12-24 08:34:43', '2024-12-24 08:35:44', 0, 7, '[[114.441075, 30.418964], [114.440626, 30.418347], [114.439494, 30.417269], [114.438818, 30.415853], [114.438426, 30.415531], [114.439167, 30.416437], [114.440041, 30.417918], [114.441076, 30.418964], [114.441205, 30.419924], [114.440846, 30.420708], [114.440025, 30.421437], [114.440637, 30.422901]]', '135b6c88-b6c8-4303-80b9-72b3bfca9f07', 'cec802b1-dc99-49a1-985f-e47eb0c87163');
INSERT INTO `record` VALUES ('2024-12-25 12:15:54', '2024-12-25 12:15:54', '9f52e401-51e9-46c5-891a-e4c5f1604f05', '2024-12-24 13:40:25', '2024-12-24 13:40:30', 0, 1, '[[114.431328, 30.43624]]', '3f343dda-16ce-4b1d-b513-528bc2c2095e', 'ac91cf08-132b-4366-8df2-936d83fbd42b');
INSERT INTO `record` VALUES ('2024-12-25 12:15:54', '2024-12-25 12:15:54', 'a0879977-cd25-4551-817a-213e7c5dbee9', '2024-12-24 13:40:36', '2024-12-24 13:40:56', 0, 4, '[[114.430637, 30.434705], [114.430906, 30.434859], [114.431506, 30.435111], [114.431179, 30.436313]]', '3f343dda-16ce-4b1d-b513-528bc2c2095e', 'e6f42f73-a857-4994-9a85-9992469d3e56');
INSERT INTO `record` VALUES ('2024-12-25 07:24:37', '2024-12-25 07:24:37', 'adf87bf7-c51b-4003-bad4-c70275658799', '2024-12-25 07:24:39', '2024-12-25 07:27:39', 0, 6, '[[114.312725, 30.380493], [114.313081, 30.381241], [114.312953, 30.381805], [114.313779, 30.382014], [114.314905, 30.381756], [114.315651, 30.382137]]', '135b6c88-b6c8-4303-80b9-72b3bfca9f07', '24e8d012-222e-466d-b650-a61807270121');
INSERT INTO `record` VALUES ('2024-12-18 08:34:42', '2024-12-18 08:34:42', 'afec849f-1042-469c-88da-ed247c7aef30', '2024-12-24 11:10:49', '2024-12-24 11:11:09', 0, 7, '[[114.400578, 30.381027], [114.399894, 30.38107], [114.397915, 30.381129], [114.397437, 30.379943]]', '135b6c88-b6c8-4303-80b9-72b3bfca9f07', '0cd042b0-7350-4c56-87ea-0c68de84783d');
INSERT INTO `record` VALUES ('2024-12-19 12:15:54', '2024-12-19 12:15:54', 'cca12324-f867-4c81-8d20-723850bda918', '2024-12-24 13:00:15', '2024-12-24 13:00:25', 0, 2, '[[114.441447, 30.421255], [114.44039, 30.421142]]', '141023d1-7c37-485d-beaf-6f931f484417', 'dd9215a1-a68d-4100-bea3-eaa10388ce73');
INSERT INTO `record` VALUES ('2024-12-25 07:24:37', '2024-12-25 07:24:37', 'cf59fe06-62b5-42a3-af51-06eb027822e5', '2024-12-25 07:24:39', '2024-12-25 07:31:09', 0, 13, '[[114.317421, 30.378017], [114.318736, 30.377567], [114.321326, 30.37879], [114.321203, 30.379975], [114.32094, 30.381424], [114.321402, 30.382363], [114.321418, 30.383795], [114.320012, 30.384648], [114.319438, 30.38453], [114.317555, 30.383741], [114.316402, 30.38409], [114.315453, 30.383838], [114.314798, 30.383715]]', '135b6c88-b6c8-4303-80b9-72b3bfca9f07', '4b1284a4-272d-4481-99f3-faf8a558d702');
INSERT INTO `record` VALUES ('2024-12-14 12:15:54', '2024-12-14 12:15:54', 'e448ceeb-b468-4207-a410-2aee3cc8b32b', '2024-12-24 12:59:45', '2024-12-24 13:00:06', 0, 4, '[[114.430268, 30.418484], [114.432906, 30.420825], [114.433641, 30.421142], [114.435079, 30.421255]]', '141023d1-7c37-485d-beaf-6f931f484417', '754f5b5d-bc95-41fc-990f-7440f64744e0');
INSERT INTO `record` VALUES ('2024-12-27 12:15:54', '2024-12-27 12:15:54', 'e8ae956b-810f-4d34-8560-a6c4af68fe44', '2024-12-24 13:25:51', '2024-12-24 13:26:26', 0, 7, '[[114.435329, 30.439722], [114.434779, 30.438657], [114.436865, 30.439054], [114.436613, 30.440105], [114.437289, 30.440357], [114.437016, 30.441291], [114.43664, 30.442267]]', '425efd64-c568-469f-83dd-4b3078a6c9d2', '7ac58eeb-b3f9-4265-9f99-5fb620fa6ffe');
INSERT INTO `record` VALUES ('2024-12-15 12:15:54', '2024-12-15 12:15:54', 'f76e5e5f-7a0b-402c-a259-fb75d232f052', '2024-12-24 13:01:49', '2024-12-24 13:02:54', 0, 13, '[[114.433147, 30.418846], [114.433255, 30.418594], [114.434881, 30.418159], [114.433303, 30.418556], [114.433164, 30.419125], [114.432333, 30.420069], [114.433116, 30.420954], [114.433878, 30.421185], [114.435261, 30.421319], [114.436925, 30.422548], [114.438233, 30.42258], [114.440025, 30.421437], [114.440846, 30.420708]]', 'bfce4a82-c3f3-4e8c-b88b-ea81f84404ad', 'b73c0757-d676-44eb-8414-c4e9c6abdf7b');
INSERT INTO `record` VALUES ('2024-12-25 07:24:37', '2024-12-25 07:24:37', 'f8fb7aae-37c9-42b8-a380-16d58d8e03b8', '2024-12-25 07:24:39', '2024-12-25 07:31:09', 0, 13, '[[114.315986, 30.38282], [114.315404, 30.383607], [114.315721, 30.383827], [114.31681, 30.383966], [114.318231, 30.383848], [114.319615, 30.384643], [114.321214, 30.384181], [114.321203, 30.383044], [114.321386, 30.382239], [114.321332, 30.380737], [114.321412, 30.379192], [114.320468, 30.377878], [114.317936, 30.377862]]', '135b6c88-b6c8-4303-80b9-72b3bfca9f07', '75901d22-4e69-44d2-a6d6-5c97e4aaed04');

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role`  (
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `role_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `role_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `role_desc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`role_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of role
-- ----------------------------
INSERT INTO `role` VALUES ('2024-11-23 23:59:53', '2024-11-23 23:59:55', '0', '管理员', '所有权限');
INSERT INTO `role` VALUES ('2024-11-24 00:00:26', '2024-11-24 00:00:28', '1', '客服', '除了权限管理，用户管理');
INSERT INTO `role` VALUES ('2024-11-24 00:01:25', '2024-11-24 00:01:27', '2', '用户', NULL);

-- ----------------------------
-- Table structure for roleaccesslink
-- ----------------------------
DROP TABLE IF EXISTS `roleaccesslink`;
CREATE TABLE `roleaccesslink`  (
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `role_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `access_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`role_id`, `access_id`) USING BTREE,
  INDEX `access_id`(`access_id` ASC) USING BTREE,
  CONSTRAINT `roleaccesslink_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`role_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `roleaccesslink_ibfk_2` FOREIGN KEY (`access_id`) REFERENCES `access` (`access_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of roleaccesslink
-- ----------------------------
INSERT INTO `roleaccesslink` VALUES ('2024-11-24 00:01:48', '2024-11-24 00:01:51', '0', '1');
INSERT INTO `roleaccesslink` VALUES ('2024-11-25 19:00:22', '2024-11-25 19:00:24', '0', '10');
INSERT INTO `roleaccesslink` VALUES ('2024-12-02 14:07:05', '2024-12-02 14:07:09', '0', '11');
INSERT INTO `roleaccesslink` VALUES ('2024-12-02 23:03:27', '2024-12-02 23:03:29', '0', '12');
INSERT INTO `roleaccesslink` VALUES ('2024-12-03 00:02:49', '2024-12-03 00:02:51', '0', '13');
INSERT INTO `roleaccesslink` VALUES ('2024-12-05 13:50:04', '2024-12-05 13:50:06', '0', '14');
INSERT INTO `roleaccesslink` VALUES ('2024-12-09 15:49:05', '2024-12-09 15:49:07', '0', '15');
INSERT INTO `roleaccesslink` VALUES ('2024-12-14 19:45:27', '2024-12-14 19:45:29', '0', '16');
INSERT INTO `roleaccesslink` VALUES ('2024-12-15 16:30:32', '2024-12-15 16:30:35', '0', '18');
INSERT INTO `roleaccesslink` VALUES ('2024-12-17 13:28:15', '2024-12-17 13:28:18', '0', '19');
INSERT INTO `roleaccesslink` VALUES ('2024-11-24 00:02:39', '2024-11-24 00:02:41', '0', '2');
INSERT INTO `roleaccesslink` VALUES ('2024-12-17 14:46:24', '2024-12-17 14:46:26', '0', '20');
INSERT INTO `roleaccesslink` VALUES ('2024-12-19 14:07:49', '2024-12-19 14:07:52', '0', '21');
INSERT INTO `roleaccesslink` VALUES ('2024-12-24 10:03:10', '2024-12-24 10:03:12', '0', '22');
INSERT INTO `roleaccesslink` VALUES ('2024-11-24 00:02:52', '2024-11-24 00:02:54', '0', '3');
INSERT INTO `roleaccesslink` VALUES ('2024-11-24 00:03:03', '2024-11-24 00:03:06', '0', '4');
INSERT INTO `roleaccesslink` VALUES ('2024-11-24 00:03:17', '2024-11-24 00:03:20', '0', '5');
INSERT INTO `roleaccesslink` VALUES ('2024-11-24 00:03:30', '2024-11-24 00:03:32', '0', '6');
INSERT INTO `roleaccesslink` VALUES ('2024-11-24 00:03:41', '2024-11-24 00:03:43', '0', '7');
INSERT INTO `roleaccesslink` VALUES ('2024-12-02 15:10:36', '2024-12-02 15:10:38', '0', '8');
INSERT INTO `roleaccesslink` VALUES ('2024-12-02 23:32:51', '2024-12-02 23:32:54', '0', '9');
INSERT INTO `roleaccesslink` VALUES ('2024-12-15 08:44:02', '2024-12-15 08:44:02', '1', '1');
INSERT INTO `roleaccesslink` VALUES ('2024-12-24 17:00:41', '2024-12-24 17:00:43', '1', '10');
INSERT INTO `roleaccesslink` VALUES ('2024-12-15 08:44:02', '2024-12-15 08:44:02', '1', '11');
INSERT INTO `roleaccesslink` VALUES ('2024-12-15 08:44:02', '2024-12-15 08:44:02', '1', '13');
INSERT INTO `roleaccesslink` VALUES ('2024-12-15 08:19:34', '2024-12-15 08:19:34', '1', '14');
INSERT INTO `roleaccesslink` VALUES ('2024-12-15 08:19:34', '2024-12-15 08:19:34', '1', '15');
INSERT INTO `roleaccesslink` VALUES ('2024-12-24 08:50:04', '2024-12-24 08:50:04', '1', '16');
INSERT INTO `roleaccesslink` VALUES ('2024-12-17 13:28:35', '2024-12-17 13:28:37', '1', '19');
INSERT INTO `roleaccesslink` VALUES ('2024-12-15 08:19:34', '2024-12-15 08:19:34', '1', '2');
INSERT INTO `roleaccesslink` VALUES ('2024-12-17 14:47:19', '2024-12-17 14:47:21', '1', '20');
INSERT INTO `roleaccesslink` VALUES ('2024-12-24 08:50:04', '2024-12-24 08:50:04', '1', '21');
INSERT INTO `roleaccesslink` VALUES ('2024-12-24 08:50:04', '2024-12-24 08:50:04', '1', '3');
INSERT INTO `roleaccesslink` VALUES ('2024-12-24 17:09:03', '2024-12-24 17:09:05', '1', '5');
INSERT INTO `roleaccesslink` VALUES ('2024-12-24 08:50:04', '2024-12-24 08:50:04', '1', '6');
INSERT INTO `roleaccesslink` VALUES ('2024-12-24 08:50:04', '2024-12-24 08:50:04', '1', '7');
INSERT INTO `roleaccesslink` VALUES ('2024-12-15 08:44:02', '2024-12-15 08:44:02', '1', '8');
INSERT INTO `roleaccesslink` VALUES ('2024-12-15 08:44:02', '2024-12-15 08:44:02', '1', '9');
INSERT INTO `roleaccesslink` VALUES ('2024-11-25 19:00:08', '2024-11-25 19:00:10', '2', '10');
INSERT INTO `roleaccesslink` VALUES ('2024-12-17 13:28:49', '2024-12-17 13:28:50', '2', '19');
INSERT INTO `roleaccesslink` VALUES ('2024-12-17 14:47:29', '2024-12-17 14:47:32', '2', '20');
INSERT INTO `roleaccesslink` VALUES ('2024-11-25 00:00:21', '2024-11-25 00:00:23', '2', '6');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `user_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `user_status` int NOT NULL,
  PRIMARY KEY (`user_id`) USING BTREE,
  INDEX `ix_user_username`(`username` ASC) USING BTREE,
  INDEX `ix_user_user_status`(`user_status` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('2024-12-02 07:53:21', '2024-12-02 07:53:21', '135b6c88-b6c8-4303-80b9-72b3bfca9f07', '15824267253', '$pbkdf2-sha256$29000$3zvnPMcYY8xZaw0BIOQ8Zw$rstXHXKAHoP2yR5Z/kmv3ktuiPKzFlOi0a/FakKcuH8', 2);
INSERT INTO `user` VALUES ('2024-12-02 07:53:21', '2024-12-02 07:53:21', '141023d1-7c37-485d-beaf-6f931f484417', '13593493649', '$pbkdf2-sha256$29000$FoIQ4vy/NyYkJASAcA4BQA$P2c9v.8evUBKLoq/0FWFzVpvWOgeL9ixkRpdADDi4zM', 1);
INSERT INTO `user` VALUES ('2024-12-02 07:53:21', '2024-12-02 07:53:21', '16f7856b-dd3d-4604-a9d6-3a73ed857198', '13976548299', '$pbkdf2-sha256$29000$3TsnJITQ.r/X2lvrHSOEcA$9oyEHyRz3yiNvhKyS0yaUHUcuzdeLOVLk1nkxiR/luc', 1);
INSERT INTO `user` VALUES ('2024-12-02 07:53:21', '2024-12-02 07:53:21', '3f343dda-16ce-4b1d-b513-528bc2c2095e', '18234272075', '$pbkdf2-sha256$29000$QOgdIyRE6H2PcS4FwDjnvA$sYPDiZZTvzcyl3w5IKoTVdfn0TyUFpHVUOBH/QhkrjE', 2);
INSERT INTO `user` VALUES ('2024-12-02 07:53:21', '2024-12-02 07:53:21', '425efd64-c568-469f-83dd-4b3078a6c9d2', '15791332840', '$pbkdf2-sha256$29000$JySkFKIUQohRyplzLmXsvQ$ckDu9j7ZAHYCT9gsuFH1kTqdeJ5ioiKTF5jsihU6tGk', 1);
INSERT INTO `user` VALUES ('2024-12-02 07:53:21', '2024-12-02 07:53:21', '5ad3b30d-110c-454d-a54d-cb2c32584db1', '13258746298', '$pbkdf2-sha256$29000$SAlBqBXinNOac44xBqAUIg$c1em6FXC89nYq/06744Nbr9XAE/krIBfoMznDhpONYk', 1);
INSERT INTO `user` VALUES ('2024-12-02 07:53:21', '2024-12-02 07:53:21', '7dae4d84-7fe6-4fbe-b678-d89b4df04639', '13509729054', '$pbkdf2-sha256$29000$4jzH2Ns7p3ROSYlR6p2Tkg$KRgoAKdwI0F2JK/t/fZZsefW0wj.x/8zMETnuS4UqS4', 1);
INSERT INTO `user` VALUES ('2024-12-02 07:53:21', '2024-12-02 07:53:21', '8e9ff3f4-91af-4211-ad2b-ac47ad25942c', '18671329845', '$pbkdf2-sha256$29000$7x0jhLBWSskZ4/w/B8BYiw$WP2rfBAHqLVmlS4ACob5C1z3VN1g3nJmXDr.iTXzLLs', 1);
INSERT INTO `user` VALUES ('2024-12-02 07:53:21', '2024-12-02 07:53:21', '922cbf5e-36cb-483c-8c9e-4c1fb991a978', '15198623512', '$pbkdf2-sha256$29000$h5CSkjKG0JqTUqo1htA6Zw$RcB1hV0cBfz7URPr7DvG2UNhc/nAoENBqNtMecPkz7Y', 1);
INSERT INTO `user` VALUES ('2024-12-13 09:47:42', '2024-12-13 09:47:42', 'b9dfb253-39e4-4e83-8f08-414170ee9cbb', '15534393649', '$pbkdf2-sha256$29000$xxjDeG8tZYzR.l9rbU2JMQ$BSh9fFHOrDRxPCVPuLgQrc/nZkvKjgvk9R.9qn5hM.Q', 1);
INSERT INTO `user` VALUES ('2024-12-02 07:53:21', '2024-12-02 07:53:21', 'bfce4a82-c3f3-4e8c-b88b-ea81f84404ad', '13834291876', '$pbkdf2-sha256$29000$9D6ndC5l7N2bsxbiHINwTg$dPyy2Dugr2kYXeDU6sdpgP9LvG5K5L2YAqUzttT9dUY', 1);
INSERT INTO `user` VALUES ('2024-12-02 07:53:21', '2024-12-02 07:53:21', 'e5ad3be4-65bb-4e7d-9eaa-999452d1d20f', '15534293649', '$pbkdf2-sha256$29000$JgRASEnpnTMmJCRkDOH83w$BHDPzBvsdgc7MFfzq627dQGuwt.buFLhdMGbBJ8Y7H8', 1);

-- ----------------------------
-- Table structure for userrolelink
-- ----------------------------
DROP TABLE IF EXISTS `userrolelink`;
CREATE TABLE `userrolelink`  (
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `user_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `role_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`user_id`, `role_id`) USING BTREE,
  INDEX `role_id`(`role_id` ASC) USING BTREE,
  CONSTRAINT `userrolelink_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `userrolelink_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `role` (`role_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of userrolelink
-- ----------------------------
INSERT INTO `userrolelink` VALUES ('2024-12-02 07:53:21', '2024-12-02 07:53:21', '135b6c88-b6c8-4303-80b9-72b3bfca9f07', '1');
INSERT INTO `userrolelink` VALUES ('2024-12-02 07:53:21', '2024-12-02 07:53:21', '141023d1-7c37-485d-beaf-6f931f484417', '1');
INSERT INTO `userrolelink` VALUES ('2024-12-02 07:53:21', '2024-12-02 07:53:21', '16f7856b-dd3d-4604-a9d6-3a73ed857198', '1');
INSERT INTO `userrolelink` VALUES ('2024-12-02 07:53:21', '2024-12-02 07:53:21', '3f343dda-16ce-4b1d-b513-528bc2c2095e', '0');
INSERT INTO `userrolelink` VALUES ('2024-12-02 07:53:21', '2024-12-02 07:53:21', '425efd64-c568-469f-83dd-4b3078a6c9d2', '2');
INSERT INTO `userrolelink` VALUES ('2024-12-02 07:53:21', '2024-12-02 07:53:21', '5ad3b30d-110c-454d-a54d-cb2c32584db1', '2');
INSERT INTO `userrolelink` VALUES ('2024-12-02 07:53:21', '2024-12-02 07:53:21', '7dae4d84-7fe6-4fbe-b678-d89b4df04639', '2');
INSERT INTO `userrolelink` VALUES ('2024-12-02 07:53:21', '2024-12-02 07:53:21', '8e9ff3f4-91af-4211-ad2b-ac47ad25942c', '2');
INSERT INTO `userrolelink` VALUES ('2024-12-02 07:53:21', '2024-12-02 07:53:21', '922cbf5e-36cb-483c-8c9e-4c1fb991a978', '2');
INSERT INTO `userrolelink` VALUES ('2024-12-13 09:47:42', '2024-12-13 09:47:42', 'b9dfb253-39e4-4e83-8f08-414170ee9cbb', '2');
INSERT INTO `userrolelink` VALUES ('2024-12-02 07:53:21', '2024-12-02 07:53:21', 'bfce4a82-c3f3-4e8c-b88b-ea81f84404ad', '2');
INSERT INTO `userrolelink` VALUES ('2024-12-02 07:53:21', '2024-12-02 07:53:21', 'e5ad3be4-65bb-4e7d-9eaa-999452d1d20f', '2');

SET FOREIGN_KEY_CHECKS = 1;
